import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700;800&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'JetBrains Mono', monospace;
}

#MainMenu, footer {visibility: hidden;}

header {
    background-color: transparent !important;
    box-shadow: none !important;
}
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"] {
    color: #F5F5F5 !important;
}
[data-testid="collapsedControl"] svg,
[data-testid="stSidebarCollapsedControl"] svg {
    fill: #F5F5F5 !important;
    color: #F5F5F5 !important;
}
.stApp {
    background-color: #0A0A0A;
    color: #F5F5F5;
}

/* sidebar */
section[data-testid="stSidebar"] {
    background-color: #000000;
    border-right: 1px solid #2A2A2A;
}
section[data-testid="stSidebar"] * {
    font-family: 'JetBrains Mono', monospace;
}

/* hide default page nav label spacing weirdness, keep clean */
section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p {
    color: #888;
}

/* headings */
h1, h2, h3 {
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: -0.5px;
    color: #FFFFFF;
}

/* hairline divider */
hr {
    border: none;
    border-top: 1px solid #2A2A2A;
    margin: 1.6rem 0;
}

/* buttons */
.stButton > button {
    background-color: transparent;
    color: #F5F5F5;
    border: 1px solid #F5F5F5;
    border-radius: 0px;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 1px;
    padding: 0.45rem 1.1rem;
    transition: all 0.15s ease;
}
.stButton > button:hover {
    background-color: #F5F5F5;
    color: #0A0A0A;
    border: 1px solid #F5F5F5;
}

/* links */
a { color: #F5F5F5 !important; text-decoration: underline; text-decoration-color: #555; }
a:hover { text-decoration-color: #F5F5F5; }

/* terminal prompt bar */
.term-bar {
    border: 1px solid #2A2A2A;
    background: #0F0F0F;
    padding: 10px 16px;
    font-size: 13px;
    color: #888;
    margin-bottom: 28px;
    display: flex;
    justify-content: space-between;
    letter-spacing: 0.5px;
}
.term-dots span {
    display: inline-block;
    width: 9px; height: 9px;
    border-radius: 50%;
    background: #444;
    margin-right: 6px;
}

.blink-cursor {
    display: inline-block;
    width: 9px; height: 18px;
    background: #F5F5F5;
    margin-left: 6px;
    animation: blink 1s step-end infinite;
    vertical-align: middle;
}
@keyframes blink { 50% { opacity: 0; } }

/* eyebrow tag */
.eyebrow {
    color: #777;
    font-size: 12.5px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

/* card */
.card {
    border: 1px solid #2A2A2A;
    padding: 22px 24px;
    margin-bottom: 18px;
    background: #0D0D0D;
    transition: border-color 0.2s ease;
}
.card:hover { border-color: #777; }

.tag {
    display: inline-block;
    border: 1px solid #3A3A3A;
    color: #C9C9C9;
    font-size: 12px;
    padding: 3px 9px;
    margin: 3px 4px 3px 0;
    letter-spacing: 0.5px;
}

.metric-num {
    font-size: 30px;
    font-weight: 800;
    color: #FFFFFF;
}
.metric-label {
    font-size: 12px;
    color: #888;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.bignum {
    font-size: 64px;
    font-weight: 800;
    line-height: 1;
    color: #FFFFFF;
}

/* image frame */
.imgframe img {
    border: 1px solid #2A2A2A;
}

/* dataframe / table tweak */
[data-testid="stDataFrame"] { border: 1px solid #2A2A2A; }

/* skill item — squircle icon box + label to the right, fixed 4-column grid */
.skill-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 28px 24px;
    margin-bottom: 36px;
}
.skill-item {
    display: flex;
    align-items: center;
    gap: 14px;
    min-width: 0;
}
.skill-box {
    width: 60px;
    height: 60px;
    min-width: 60px;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #161616;
    transition: background 0.18s ease, transform 0.18s ease;
}
.skill-item:hover .skill-box {
    background: #222;
    transform: translateY(-2px);
}
.skill-box img {
    width: 32px;
    height: 32px;
    object-fit: contain;
}
.skill-box .emoji {
    font-size: 26px;
    line-height: 1;
}
.skill-name {
    font-size: 17px;
    color: #F0F0F0;
    letter-spacing: 0.3px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
/* ---- Mobile responsiveness ---- */
@media (max-width: 768px) {
    /* skills grid: 4 cols -> 2 cols */
    .skill-row {
        grid-template-columns: repeat(2, 1fr);
        gap: 22px 16px;
    }
    .skill-box {
        width: 52px;
        height: 52px;
        min-width: 52px;
    }
    .skill-box img { width: 28px; height: 28px; }
    .skill-name { font-size: 15px; }

    /* terminal bar: drop the right-hand "zsh — 80x24" label, shrink padding */
    .term-bar {
        font-size: 11px;
        padding: 8px 12px;
    }
    .term-bar div:last-child { display: none; }

    /* big numbers on Home don't need to be huge on a phone */
    .bignum { font-size: 42px; }

    /* cards get tighter padding so text isn't cramped */
    .card { padding: 16px 18px; }

    /* tags wrap more compactly */
    .tag { font-size: 11px; padding: 2px 7px; }

    /* prompt_title heading scales down */
    h1 { font-size: 28px !important; }
}

@media (max-width: 480px) {
    /* very small phones: skills go to single column */
    .skill-row {
        grid-template-columns: 1fr;
    }
}
</style>
"""

def inject():
    st.markdown(CSS, unsafe_allow_html=True)

def term_bar(path: str):
    st.markdown(
        f"""<div class="term-bar">
        <div class="term-dots"><span></span><span></span><span></span>&nbsp; gabriel@sfu&nbsp;:&nbsp;~/{path}</div>
        <div>zsh — 80x24</div>
        </div>""",
        unsafe_allow_html=True,
    )

def eyebrow(text: str):
    st.markdown(f'<div class="eyebrow">{text}</div>', unsafe_allow_html=True)

def skill_row(items):
    """items: list of (label, icon_url, emoji_fallback) tuples. Renders squircle icon box + label."""
    cells = []
    for label, icon_url, emoji in items:
        img_html = (
            f'<img src="{icon_url}" '
            f'onerror="this.outerHTML=\'<span class=&quot;emoji&quot;>{emoji}</span>\'" />'
        )
        cells.append(
            f'<div class="skill-item">'
            f'<div class="skill-box">{img_html}</div>'
            f'<span class="skill-name">{label}</span>'
            f'</div>'
        )
    return '<div class="skill-row">' + "".join(cells) + "</div>"


def prompt_title(text: str):
    st.markdown(
        f'<h1 style="margin-bottom:0;">&gt; {text}<span class="blink-cursor"></span></h1>',
        unsafe_allow_html=True,
    )
