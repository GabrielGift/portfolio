import streamlit as st
from style import inject, term_bar, eyebrow, prompt_title

st.set_page_config(page_title="Gabriel Gift — Data Science", page_icon="▣", layout="wide")
inject()
term_bar("home")

col1, col2 = st.columns([3, 2], gap="large")

with col1:
    eyebrow("DATA SCIENCE · SFU · 2024–2028")
    prompt_title("Gabriel Gift")
    st.markdown(
        """
        <p style="font-size:18px; color:#CFCFCF; max-width:560px; line-height:1.65; margin-top:18px;">
        I turn messy, multi-table datasets into decisions. Currently studying Data Science
        at Simon Fraser University, with hands-on work spanning Tableau dashboards,
        statistical modeling in R, and applied SQL/Python pipelines, tested under
        hackathon time pressure, not just in the classroom.
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="bignum">2nd</div><div class="metric-label">RBC × BCCAI × SFU Beedie Hackathon</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="bignum">FIN</div><div class="metric-label">SFU Sports Analytics Baseball Hackathon</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="bignum">9</div><div class="metric-label">Relational datasets, one dashboard</div>', unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown(
        '<span class="tag">SQL</span><span class="tag">Python</span><span class="tag">R</span>'
        '<span class="tag">Tableau</span><span class="tag">Power BI</span><span class="tag">Java</span>'
        '<span class="tag">C++</span>',
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card" style="margin-top:64px;">
        <pre style="color:#9FEF9F; margin:0; white-space:pre-wrap; font-size:13px; line-height:1.5;">
$ whoami
gabriel_gift

$ cat status.txt
> Data Science @ SFU, year 2
> Building: hackathon dashboards,
  regression models, ML fundamentals
> Open to: internships, research,
  collaborative projects

$ ls skills/
sql/  python/  r/  tableau/
power_bi/  java/  cpp/  latex/
        </pre>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown(
    '<p style="color:#666; font-size:13px;">Use the sidebar to navigate — Skills · Projects · Education · About · Contact</p>',
    unsafe_allow_html=True,
)
