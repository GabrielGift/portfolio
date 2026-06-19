import streamlit as st
from style import inject, term_bar, eyebrow, prompt_title

st.set_page_config(page_title="Education — Gabriel Gift", page_icon="▣", layout="wide")
inject()
term_bar("education")

eyebrow("ACADEMIC BACKGROUND")
prompt_title("Education")
st.write("")

st.markdown(
    """
    <div class="card">
    <div style="display:flex; justify-content:space-between; flex-wrap:wrap;">
        <div>
            <h3 style="margin-bottom:2px;">Simon Fraser University</h3>
            <p style="color:#888; margin-top:0;">Bachelor of Science in Data Science</p>
        </div>
        <div style="text-align:right; color:#888;">Burnaby, BC<br/>2024 – 2028</div>
    </div>
    <ul style="color:#CFCFCF; line-height:1.7;">
        <li>Interdisciplinary coursework spanning computational mathematics, statistical modeling, business intelligence, and cognitive science.</li>
        <li>Active participant in the SFU Sports Analytics Club and university-led data hackathons, applying classroom theory to real-world datasets.</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
eyebrow("RELEVANT COURSEWORK")
st.write("")

coursework = [
    ("Data Analysis & Statistics", "Applied full data science workflows in R — ingestion, cleaning, visualization, regression modeling, probability distributions, and frequentist inference."),
    ("Computing Science & IT Systems", "Engineered efficient algorithms in C++ and Java; applied NumPy and Pandas for high-performance numerical analysis; studied OOP, memory management, and computational complexity."),
    ("Mathematics", "Mastered linear algebra and discrete mathematics as foundations for machine learning algorithms, relational database theory, and computational problem-solving; applied these frameworks directly in project and hackathon work."),
    ("Business Administration", "Explored organizational structures, financial reporting, and the strategic role of data analytics in corporate decision-making."),
]

cols = st.columns(2, gap="large")
for i, (title, desc) in enumerate(coursework):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class="card">
                <p class="eyebrow" style="margin-bottom:8px;">COURSE AREA</p>
                <h4 style="margin-top:0;">{title}</h4>
                <p style="color:#AEAEAE; font-size:14px; line-height:1.6;">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
eyebrow("CERTIFICATIONS")
st.markdown(
    """
    <div class="card">
        <strong>Harmonized Life License Qualification Program (HLLQP)</strong>
        <span style="color:#888;"> — 2024</span>
    </div>
    """,
    unsafe_allow_html=True,
)
