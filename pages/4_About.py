import streamlit as st
from style import inject, term_bar, eyebrow, prompt_title

st.set_page_config(page_title="About — Gabriel Gift", page_icon="▣", layout="wide")
inject()
term_bar("about")

eyebrow("THE LONG VERSION")
prompt_title("About")
st.write("")

col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.markdown(
        """
        <p style="color:#CFCFCF; font-size:16px; line-height:1.75;">
        I'm a Data Science student at Simon Fraser University with a track record in
        competitive analytics — placing 2nd in division at the RBC × BCCAI × SFU Beedie
        Agribusiness Hackathon and reaching finalist standing at the SFU Sports Analytics
        Baseball Hackathon. I combine a strong foundation in statistical modeling, SQL,
        Python, R, and Tableau with interdisciplinary coursework in mathematics, computing
        science, and business to deliver data-driven insights across complex domains.
        </p>
        <p style="color:#CFCFCF; font-size:16px; line-height:1.75;">
        Before SFU, I worked as an Insurance Representative at American Income Life,
        where I ran data-driven gap analyses on client portfolios and built a standardized
        assessment framework to speed up financial reviews — early reps for the same
        instinct I now bring to dashboards and datasets: find the gap, quantify it, fix it.
        </p>
        <p style="color:#CFCFCF; font-size:16px; line-height:1.75;">
        Outside coursework, I volunteer with Civic Tech Saint John, collaborating with
        developers and designers on technology-driven solutions to local social challenges
        through weekly hackathon nights.
        </p>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
        <p class="eyebrow">EXPERIENCE</p>
        <h4 style="margin-top:0;">Insurance Representative</h4>
        <p style="color:#888; font-size:13px; margin-top:-8px;">American Income Life Insurance · Nov 2023 – Apr 2024</p>
        <ul style="color:#AEAEAE; font-size:14px; line-height:1.6;">
            <li>Strategic insurance consulting for labor and credit unions, exceeding client retention targets.</li>
            <li>Data-driven gap analyses on client portfolios, increasing adoption of supplemental plans.</li>
            <li>Built a standardized data assessment framework for faster, more accurate reviews.</li>
        </ul>
        </div>

        <div class="card">
        <p class="eyebrow">VOLUNTEERING</p>
        <h4 style="margin-top:0;">Civic Tech Saint John</h4>
        <p style="color:#888; font-size:13px; margin-top:-8px;">Technology & Community Collaboration · 2024</p>
        <ul style="color:#AEAEAE; font-size:14px; line-height:1.6;">
            <li>Worked with a multidisciplinary team on tech-driven solutions to local social challenges.</li>
            <li>Weekly hackathon nights maintaining open-source tools for regional social services.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
