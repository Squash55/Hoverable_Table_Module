
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="STRIDE Hover-Insight Table", layout="wide")

@st.cache_data
def load_data():
    return pd.DataFrame({
        "Base Name": ["Alpha", "Bravo", "Charlie"],
        "Readiness Score": [82.5, 74.3, 90.1],
        "Equipment Availability": [88, 76, 95],
        "Cyber Resilience": [79, 68, 91],
        "Training Level": [85, 70, 92]
    })

@st.cache_data
def load_column_descriptions():
    return {
        "Base Name": "Identifier for each Air Force base.",
        "Readiness Score": "Composite score representing overall mission readiness (0–100).",
        "Equipment Availability": "Percentage of mission-critical equipment operational and ready.",
        "Cyber Resilience": "System hardening and response strength to cyber threats.",
        "Training Level": "Percent of personnel meeting operational training requirements."
    }

# Load
df = load_data()
descriptions = load_column_descriptions()

# HTML table with hover-enabled header row
def create_hover_table(dataframe, tooltips):
    header_html = "<thead><tr>"
    for col in dataframe.columns:
        desc = tooltips.get(col, "")
        header_html += f'<th title="{desc}">{col}</th>'
    header_html += "</tr></thead>"

    body_html = "<tbody>"
    for _, row in dataframe.iterrows():
        body_html += "<tr>" + "".join([f"<td>{val}</td>" for val in row]) + "</tr>"
    body_html += "</tbody>"

    table_html = f'''
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            cursor: help;
        }}
        tr:hover {{ background-color: #f5f5f5; }}
    </style>
    <table>{header_html}{body_html}</table>
    '''
    return table_html

# Render
st.title("🧠 STRIDE: Hover-Insight Demo Table")
st.markdown("This is a sample of how STRIDE integrates **data explanations directly into the experience.** Hover over any column header to see its meaning.")

components.html(create_hover_table(df, descriptions), height=300, scrolling=True)
