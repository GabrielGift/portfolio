import streamlit as st
from style import inject, term_bar, eyebrow, prompt_title

st.set_page_config(page_title="Projects — Gabriel Gift", page_icon="▣", layout="wide")
inject()
term_bar("projects")

eyebrow("ACADEMIC PROJECTS & HACKATHONS")
prompt_title("Projects")
st.write("")

PROJECTS = [
    {
        "key": "greenleaf",
        "title": "RBC × BCCAI × SFU Beedie Agribusiness Analytics Hackathon",
        "date": "May 2026",
        "result": "2nd place — division",
        "tags": ["Tableau", "Excel", "Data Modeling", "ETL"],
        "images": ["assets/greenleaf_1.png", "assets/greenleaf_2.png", "assets/greenleaf_3.png"],
        "bullets": [
            "Engineered a multi-dashboard for a hypothetical Controlled Environment Agriculture operator, integrating 9 relational datasets spanning 25,200+ sensor readings across 120 experimental microplots.",
            "Designed a relationship-based data model to eliminate fan-out aggregation errors, enabling accurate cross-table KPI calculations — a 2.52x precision payback ratio and $28,387 net precision value.",
            "Delivered a three-act data narrative quantifying crop-stress cost, precision-technology ROI, and optimal crop-treatment combinations to a panel of judges from RBC and BCCAI.",
        ],
    },
    {
        "key": "baseball",
        "title": "Baseball Data Hackathon — SFU Sports Analytics Club",
        "date": "Mar 2025",
        "result": "Finalist",
        "tags": ["SQL", "Python", "R", "Power BI", "Tableau"],
        "images": ["assets/baseball_1.png", "assets/baseball_2.png", "assets/baseball_3.png"],
        "bullets": [
            "Optimized team performance metrics by analyzing pitch-by-pitch simulation data, identifying top KPIs correlated with a 15% increase in projected win probability.",
            "Automated delivery of statistical models through interactive Power BI and Tableau dashboards, reducing data-interpretation time for non-technical stakeholders.",
            "Recognized as a finalist for technical insight quality and a formal presentation delivered to a panel of industry professionals.",
        ],
    },
    {
        "key": "rubik",
        "title": "Rubik's Cube Solver — Java, OOP, IDA* Search",
        "date": "Dec 2025",
        "result": "100% success rate",
        "tags": ["Java", "Algorithms", "OOP", "Search"],
        "images": ["assets/rubik_1.png", "assets/rubik_2.png", "assets/rubik_3.png"],
        "bullets": [
            "Engineered an optimal solver navigating a 4.3×10^19 state space, achieving a 100% success rate on 16-move scrambles in under 5 seconds.",
            "Implemented a two-phase heuristic and memory-efficient recursive search, cutting search time by 40% versus standard BFS.",
            "Built robust OOP abstractions and a file-based I/O system for deterministic, reliable solver output.",
        ],
    },
]

for p in PROJECTS:
    idx_key = f"idx_{p['key']}"
    if idx_key not in st.session_state:
        st.session_state[idx_key] = 0

    st.markdown('<div class="card">', unsafe_allow_html=True)
    img_col, text_col = st.columns([3, 4], gap="large")

    with img_col:
        i = st.session_state[idx_key]
        st.markdown('<div class="imgframe">', unsafe_allow_html=True)
        st.image(p["images"][i], use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        b1, b2, b3 = st.columns([1, 2, 1])
        with b1:
            if st.button("◀", key=f"prev_{p['key']}"):
                st.session_state[idx_key] = (i - 1) % len(p["images"])
                st.rerun()
        with b2:
            st.markdown(
                f'<p style="text-align:center; color:#777; font-size:12px; padding-top:8px;">'
                f'{i+1} / {len(p["images"])}</p>',
                unsafe_allow_html=True,
            )
        with b3:
            if st.button("▶", key=f"next_{p['key']}"):
                st.session_state[idx_key] = (i + 1) % len(p["images"])
                st.rerun()

    with text_col:
        st.markdown(f"### {p['title']}")
        st.markdown(
            f'<p style="color:#888; font-size:13px; margin-top:-10px;">{p["date"]} &nbsp;·&nbsp; <span style="color:#F5F5F5;">{p["result"]}</span></p>',
            unsafe_allow_html=True,
        )
        tag_html = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
        st.markdown(f'<div style="margin:8px 0 14px 0;">{tag_html}</div>', unsafe_allow_html=True)
        for b in p["bullets"]:
            st.markdown(f"- {b}")

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")
