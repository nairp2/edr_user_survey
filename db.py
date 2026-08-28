import datetime
import hashlib
import uuid

import streamlit as st
from sqlalchemy import create_engine, text

@st.cache_resource(show_spinner=False)
def get_engine():
    db_url = st.secrets["DATABASE_URL"]
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "posgresql://", 1)
    return create_engine(db_url, pool_pre_ping=True)

def init_db() -> None:
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS survey_responses (
                response_id   UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                submitted_at  TIMESTAMP NOT NULL DEFAULT now(),
                answers       JSONB NOT NULL
            )              
        """))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS admin_users (
                username       TEXT PRIMARY KEY,
                password_hash  TEXT NOT NULL,
                created_at     TIMESTAMP NOT NULL DEFAULT now()
            )           
        """))

def save_response(answers: dict) -> None:
    import json
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO survey_responses (answers) VALUES (:answers)"),
            {"answers": json.dumps(answers)},
        )

def get_all_responses() -> list[dict]:
    engine = get_engine()
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT submitted_at, answers FROM survey_responses ORDER BY submitted_at")
        ).fetchall()
    return [{"submitted_at": r[0], **r[1]} for r in rows]

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def check_admin_login(username: str, password: str) -> bool:
    if not username or not password:
        return False
    engine = get_engine()
    with engine.connect() as conn:
        row = conn.execute(
            text("SELECT password_hash FROM admin_users WHERE username = :u"),
            {"u": username}
        ).fetchone()
    if not row:
        return False
    return row[0] == _hash_password(password)

def create_admin_user(username: str, password: str) -> None:
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO admin_users (username, password_hash)
                VALUES (:u, :h)
                ON CONFLICT (username) DO UPDATE SET password_hash = EXCLUDED.password_hash
            """),
            {"u": username, "h": _hash_password(password)},
        )