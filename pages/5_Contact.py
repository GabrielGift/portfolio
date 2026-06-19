import streamlit as st
from style import inject, term_bar, eyebrow, prompt_title

st.set_page_config(page_title="Contact — Gabriel Gift", page_icon="▣", layout="wide")
inject()
term_bar("contact")

eyebrow("GET IN TOUCH")
prompt_title("Contact")
st.write("")

col1, col2 = st.columns([2, 3], gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
        <p class="eyebrow">DIRECT</p>
        <p style="font-size:16px; margin:4px 0;">📞 506-349-8478</p>
        <p style="font-size:16px; margin:4px 0;">
            ✉️ <a href="mailto:gabrielasagift@gmail.com">gabrielasagift@gmail.com</a>
        </p>
        <p style="color:#777; font-size:13px; margin-top:18px;">
            Open to internships, research collaborations, and project work.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown('<p class="eyebrow">SEND A MESSAGE</p>', unsafe_allow_html=True)
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message", height=140)
        submitted = st.form_submit_button("Send")
        if submitted:
            if name and email and message:
                st.success("Message captured. (Hook this form up to an email service — e.g. Formspree or SMTP — to receive it for real.)")
            else:
                st.error("Fill in all fields before sending.")

st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown(
    '<p style="color:#555; font-size:12px;">Built with Streamlit · black & white, on purpose.</p>',
    unsafe_allow_html=True,
)
