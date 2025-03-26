
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="Hover-Insights for Tables", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("hover_data.csv")

@st.cache_data
def load_column_descriptions():
    return {
        "Base Name": "Name of the base — mostly fictional, used for demonstration.",
        "Readiness Score": "Readiness ranges from ~50 to 95, with most values clustering around 75–85.",
        "Equipment Availability": "Most values are between 70–95%, indicating solid equipment support across bases.",
        "Cyber Resilience": "Cyber strength scores mostly fall between 60–90, with a few bases needing attention.",
        "Training Level": "Training values typically range from 60–100, with most bases above 80%, suggesting well-prepared personnel."
    }

df = load_data()
descriptions = load_column_descriptions()

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

    full_html = f'''
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 6px;
            text-align: left;
            color: black;
        }}
        th {{
            background-color: #f2f2f2;
            cursor: help;
        }}
        tr:hover {{ background-color: #f5f5f5; }}
    </style>
    <table>{header_html}{body_html}</table>
    '''
    return full_html

st.title("🧠 STRIDE: Hover-Insights for Tables")
st.markdown("Hover over the column headers below to understand the **distribution and meaning of the data**, not just the field names.")

components.html(create_hover_table(df, descriptions), height=500, scrolling=True)

st.subheader("📊 Descriptive Statistics")
st.dataframe(df.describe().round(2))

