import streamlit as st
from style import inject, term_bar, eyebrow, prompt_title, skill_row

st.set_page_config(page_title="Skills — Gabriel Gift", page_icon="▣", layout="wide")
inject()
term_bar("skills")

eyebrow("TECHNICAL TOOLKIT")
prompt_title("Skills")
st.write("")

DEVICON = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/{slug}/{slug}-original.svg"
SIMPLEICON = "https://cdn.simpleicons.org/{slug}/{color}"

# (label, icon_url, emoji_fallback)
LANGUAGES = [
    ("SQL", SIMPLEICON.format(slug="mysql", color="4479A1"), "🗄️"),
    ("Python", DEVICON.format(slug="python"), "🐍"),
    ("R", DEVICON.format(slug="r"), "📊"),
    ("Java", DEVICON.format(slug="java"), "☕"),
    ("C", DEVICON.format(slug="c"), "🔤"),
    ("C++", DEVICON.format(slug="cplusplus"), "➕"),
    ("LaTeX", SIMPLEICON.format(slug="latex", color="008080"), "📄"),
]

LIBRARIES = [
    ("NumPy", DEVICON.format(slug="numpy"), "🔢"),
    ("Pandas", DEVICON.format(slug="pandas"), "🐼"),
    ("Matplotlib", DEVICON.format(slug="matplotlib"), "📈"),
    ("Seaborn", SIMPLEICON.format(slug="python", color="4C72B0"), "📉"),
]

TOOLS = [
    ("Tableau", DEVICON.format(slug="tableau"), "📊"),
    ("Power BI", SIMPLEICON.format(slug="powerbi", color="F2C811"), "📶"),
    ("Power Query", SIMPLEICON.format(slug="powerbi", color="767676"), "🔎"),
    ("Excel", SIMPLEICON.format(slug="microsoftexcel", color="207245"), "🟩"),
    ("RStudio", SIMPLEICON.format(slug="rstudio", color="75AADB"), "📐"),
    ("Jupyter Notebook", DEVICON.format(slug="jupyter"), "📓"),
    ("R Markdown", DEVICON.format(slug="r"), "📝"),
    ("VS Code", DEVICON.format(slug="vscode"), "🖥️"),
    ("Anaconda", DEVICON.format(slug="anaconda"), "🐍"),
    ("IntelliJ IDEA", DEVICON.format(slug="intellij"), "🧠"),
]

st.markdown("**Languages**")
st.markdown(skill_row(LANGUAGES), unsafe_allow_html=True)

st.markdown("**Libraries**")
st.markdown(skill_row(LIBRARIES), unsafe_allow_html=True)

st.markdown("**Tools & Software**")
st.markdown(skill_row(TOOLS), unsafe_allow_html=True)

# Professional / soft skills don't have logos — keep these as plain text tags
PROFESSIONAL = ["Data Cleaning", "ETL Processes", "Relational Databases", "Data Visualization",
                 "Data Modeling", "Strategic Analysis", "Stakeholder Collaboration"]
SOFT = ["Data Storytelling", "Collaborative Problem Solving", "Adaptability", "Strategic Communication"]

st.markdown("**Professional**")
st.markdown(
    '<div style="margin-bottom:24px;">' + "".join(f'<span class="tag">{i}</span>' for i in PROFESSIONAL) + "</div>",
    unsafe_allow_html=True,
)

st.markdown("**Soft Skills**")
st.markdown(
    '<div style="margin-bottom:24px;">' + "".join(f'<span class="tag">{i}</span>' for i in SOFT) + "</div>",
    unsafe_allow_html=True,
)

st.markdown("<hr/>", unsafe_allow_html=True)

eyebrow("PROFICIENCY SNAPSHOT")
st.write("")

prof = [
    ("SQL", 91, "#4479A1"), ("Python", 93, "#3776AB"), ("R", 97, "#276DC3"),
    ("Tableau", 99, "#E97627"), ("Power BI", 70, "#F2C811"), ("Java / C++", 65, "#F89820"),
]
for name, val, color in prof:
    c1, c2 = st.columns([1, 5])
    with c1:
        st.markdown(f'<div style="padding-top:4px;">{name}</div>', unsafe_allow_html=True)
    with c2:
        st.markdown(
            f"""
            <div style="border:1px solid #2A2A2A; height:14px; width:100%; margin-top:8px;">
                <div style="background:{color}; height:100%; width:{val}%;"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    '<p style="color:#555; font-size:12px; margin-top:18px;">Self-assessed, based on coursework depth and hackathon application.</p>',
    unsafe_allow_html=True,
)
