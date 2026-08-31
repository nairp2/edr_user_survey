import streamlit as st
import pandas as pd
import plotly.express as px
import colorsys
 
from questions import QUESTIONS
from db import init_db, save_response, get_all_responses, check_admin_login
 
st.set_page_config(page_title="EDR Data Call User Survey", page_icon="", layout="wide")
init_db()
 
def shades_of(hex_color: str, n: int) -> list[str]:
    """Generate n shades of a single hue (light to dark) for a monochrome pie chart."""
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i + 2], 16) / 255 for i in (0, 2, 4))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    shades = []
    for i in range(max(n, 1)):
        lightness = 0.82 - (0.82 - 0.25) * (i / max(n - 1, 1))
        r2, g2, b2 = colorsys.hls_to_rgb(h, lightness, s)
        shades.append("#{:02x}{:02x}{:02x}".format(int(r2 * 255), int(g2 * 255), int(b2 * 255)))
    return shades

# ----------------------------------------------------------------------
# Light styling
# ----------------------------------------------------------------------
st.markdown(
    """
    <style>
    .main .block-container { max-width: 850px; padding-top: 1.5rem; }
    h1 { color: #1F3864; font-weight: 700; }
    h3 { color: #1F3864; margin-top: 1.2rem; }
    div[data-testid="stForm"] {
        background-color: #FAFBFC;
        border: 1px solid #E3E8EF;
        border-radius: 12px;
        padding: 1.75rem 2rem;
    }
    div.stButton > button, button[kind="formSubmit"] {
        background-color: #1F3864;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
    }
    div.stButton > button:hover, button[kind="formSubmit"]:hover {
        background-color: #2E4E8F;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
 
 
# ----------------------------------------------------------------------
# Admin login (sidebar)
# ----------------------------------------------------------------------
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
 
st.sidebar.divider()
st.sidebar.subheader("Admin")
 
if st.session_state.is_admin:
    st.sidebar.success("Logged in as admin")
    if st.sidebar.button("Log out"):
        st.session_state.is_admin = False
        st.rerun()
else:
    with st.sidebar.form("admin_login", clear_on_submit=True):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_clicked = st.form_submit_button("Log in")
    if login_clicked:
        if check_admin_login(username, password):
            st.session_state.is_admin = True
            st.rerun()
        else:
            st.sidebar.error("Invalid username or password.")
 
st.sidebar.divider()
 
nav_options = ["📝 Take Survey"]
if st.session_state.is_admin:
    nav_options.append("📊 Results")
    st.sidebar.subheader("Chart style")
    chart_style = st.sidebar.radio("Chart style", ["Bar", "Pie"], label_visibility="collapsed")
else:
    chart_style = "Bar"
 
page = st.sidebar.radio("Navigate", nav_options)
 
 
# ----------------------------------------------------------------------
# Logo + title
# ----------------------------------------------------------------------
import os
col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
        logo_left, logo_right = st.columns([1, 3])
        with logo_right:
            if os.path.exists("logo.png"):
                st.image("logo.png", width=275) 
# ----------------------------------------------------------------------
# Survey form
# ----------------------------------------------------------------------
if page == "📝 Take Survey":
    st.markdown("<h1 style='text-align:center;'> EDR Data Call User Survey</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; color:#595959;'>This survey is anonymous — no names, emails, "
        "or other identifying information are collected. Only your answers are stored.</p>",
        unsafe_allow_html=True,
    )
    st.write("")
 
    with st.form("survey_form", clear_on_submit=True):
        answers = {}
        for i, q in enumerate(QUESTIONS):
            qid, qtype, label = q["id"], q["type"], q["label"]
            st.markdown(f"**{i + 1}. {label}**" + (" \\*" if q.get("required") else ""))
 
            if qtype == "dropdown":
                answers[qid] = st.selectbox(label, q["options"], index=None, placeholder="Choose an option", label_visibility="collapsed")
            elif qtype == "radio":
                answers[qid] = st.radio(label, q["options"], index=None, label_visibility="collapsed")
            elif qtype == "multiselect":
                n_opts = len(q["options"])
                help_text = f"Start typing to filter — {n_opts} options available." if n_opts > 15 else None
                answers[qid] = st.multiselect(label, q["options"], label_visibility="collapsed", help=help_text)
            elif qtype == "slider":
                answers[qid] = st.slider(label, q.get("min", 0), q.get("max", 10), label_visibility="collapsed")
            elif qtype == "number":
                answers[qid] = st.number_input(label, min_value=q.get("min", 0), max_value=q.get("max", 100), label_visibility="collapsed")
            elif qtype == "text_input":
                answers[qid] = st.text_input(label, label_visibility="collapsed")
            elif qtype == "text_area":
                answers[qid] = st.text_area(label, label_visibility="collapsed")
            else:
                raise ValueError(f"Unknown question type: {qtype!r} for question {qid!r}")
 
            st.write("")
 
        submitted = st.form_submit_button("Submit Survey")
 
    if submitted:
        missing = [
            q["label"] for q in QUESTIONS
            if q.get("required") and (not answers.get(q["id"]) and answers.get(q["id"]) != 0)
        ]
        if missing:
            st.error("Please answer the required question(s): " + "; ".join(missing))
        else:
            save_response(answers)
            st.cache_data.clear()
            st.success("Thanks — your response has been submitted successfully.")
            st.balloons()
 
 
# ----------------------------------------------------------------------
# Results dashboard
# ----------------------------------------------------------------------
elif page == "📊 Results" and st.session_state.is_admin:
    st.markdown("<h1 style='text-align:center;'>📊 Survey Results</h1>", unsafe_allow_html=True)
    st.caption("Aggregated, anonymous — individual responses can't be traced back to anyone.")
 
    @st.cache_data(ttl=30, show_spinner=False)
    def load_responses_df():
        return pd.DataFrame(get_all_responses())
 
    df = load_responses_df()
    if df.empty:
        st.info("No responses yet. Check back once people start filling out the survey.")
        st.stop()
 
    st.metric("Total responses", len(df))
    st.divider()
 
    for q in QUESTIONS:
        qid, qtype, label = q["id"], q["type"], q["label"]
        if qid not in df.columns:
            continue
 
        st.subheader(label)
 
        if qtype in ("dropdown", "radio"):
            counts = df[qid].dropna().value_counts().reindex(q["options"]).fillna(0)
            if chart_style == "Pie":
                fig = px.pie(names=counts.index, values=counts.values, color_discrete_sequence=shades_of("#1F3864", len(counts)), hole=0.15)
                fig.update_traces(textposition="inside", textinfo="percent+label", marker=dict(line=dict(color="white", width=2)))
                fig.update_layout(showlegend=True, margin=dict(l=20, r=20, t=20, b=20))
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.bar_chart(counts)
 
        elif qtype == "multiselect":
            exploded = df[qid].explode().dropna()
            if exploded.empty:
                st.write("No responses yet.")
            else:
                counts = exploded.value_counts()
                if chart_style == "Pie":
                    fig = px.pie(names=counts.index, values=counts.values, color_discrete_sequence=shades_of("#1F3864", len(counts)), hole=0.15)
                    fig.update_traces(textposition="inside", textinfo="percent+label", marker=dict(line=dict(color="white", width=2)))
                    fig.update_layout(showlegend=True, margin=dict(l=20, r=20, t=20, b=20))
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.bar_chart(counts)
 
        elif qtype in ("slider", "number"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.bar_chart(df[qid].dropna().value_counts().sort_index())
            with col2:
                st.metric("Average", f"{df[qid].mean():.1f}")
                st.metric("Median", f"{df[qid].median():.1f}")
 
        elif qtype in ("text_input", "text_area"):
            responses = [t for t in df[qid].dropna() if str(t).strip()]
            st.write(f"{len(responses)} written response(s)")
            with st.expander("View all responses"):
                for t in responses:
                    st.write(f"- {t}")
 
        st.divider()
 
    st.download_button(
        "⬇️ Download raw data (CSV)",
        df.to_csv(index=False).encode("utf-8"),
        file_name="survey_results.csv",
        mime="text/csv",
    )
 