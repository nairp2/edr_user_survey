from docx import Document
from dotenv import load_dotenv
import os
import pandas as pd
import streamlit as st

load_dotenv()
WORD_PATH = os.getenv("WORD_PATH")
CSV_PATH = os.getenv("CSV_PATH")
csv_path = os.path.join(CSV_PATH, "survey_results.csv")
word_path = os.path.join(WORD_PATH, "survey_report.docx")


st.title("🌍 EDR Data Call User Survey")

# Dropdown menu
dropdown_list = [f"Placeholder {i}" for i in range(1, 225)]
selected_value = st.selectbox("Select your dropdown option", dropdown_list)

# Checkboxes for values
st.markdown("**Interests**")
checkbox_list = st.multiselect(
    "Pick your interests:",
    ["AI", "Machine Learning", "Web Development", "Data Science", "Gaming", "Music", "Art"]
)

# Textarea for feedback
user_input = st.text_area("Any suggestions or feedback?")
    
def generate_word_report(csv_path=csv_path, output_path=os.path.join(WORD_PATH, "survey_report.docx")):
    df = pd.read_csv(csv_path)
    doc = Document()

    doc.add_heading("🌍 Survey Summary Report", 0)

    for i, row in df.iterrows():
        doc.add_heading(f"Response #{i+1}", level=1)
        #doc.add_paragraph(f"Name: {row['Name']}")
        doc.add_paragraph(f"Dropdown: {row['Country']}")
        doc.add_paragraph(f"Interests: {row['Interests']}")
        doc.add_paragraph(f"Feedback: {row['Feedback']}")
        doc.add_paragraph("\n" + "-"*40 + "\n")

    # Aggregated Metrics Section
    doc.add_page_break()
    doc.add_heading("📊 Aggregated Metrics", level=0)

    doc.add_paragraph(f"Total Responses: {len(df)}")

    doc.add_heading("Top Dropdown Selections", level=1)
    dropdown_counts = df['Country'].value_counts().head(10)
    for country, count in dropdown_counts.items():
        doc.add_paragraph(f"{country}: {count}")

    doc.add_heading("Interest Popularity", level=1)
    interest_series = df['Interests'].dropna().str.split(', ').explode()
    interest_counts = interest_series.value_counts()
    for interest, count in interest_counts.items():
        doc.add_paragraph(f"{interest}: {count}")

    doc.save(output_path)

if st.button("Submit"):
    st.success("🎉 Thank you for your submission!")
    st.write("Here’s what you submitted:")
    #st.write(f"**Name:** {name}")
    st.write(f"**Country:** {selected_value}")
    st.write(f"**Interests:** {', '.join(checkbox_list)}")
    st.write(f"**Feedback:** {user_input}")

    response = {
        #"Name": name,
        "Country": selected_value,
        "Interests": ", ".join(checkbox_list),
        "Feedback": user_input
    }

    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        df = pd.DataFrame(columns=response.keys())

    df = pd.concat([df, pd.DataFrame([response])], ignore_index=True)
    df.to_csv(csv_path, index=False)

    generate_word_report(csv_path=csv_path, output_path=word_path)
    st.success("✅ Your response has been recorded!")