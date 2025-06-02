import streamlit as st

st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Butterfly+Kids&family=Cabin:ital,wght@0,400..700;1,400..700&family=Mona+Sans:ital,wght@0,200..900;1,200..900&family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <style>
    *{
        border-radius: 0px;
        # background: #000000;
        font-family: 'Mona sans', arial;
    }
    h{
        font-family: 'Times New Roman', Times, serif;
        }
    p{
        font-family: 'Mona sans', arial;
        font-size: 23px !important;
        text-align: justify;
        }
    .font {
        font-family: 'Times New Roman', Times, serif;
        font-size: 50px !important;
        line-height: 1.6;
    }
    .para{
        font-family: 'Mona sans', arial;
        font-size: 16px;
    }
    .main{
        margin: 0px;
        padding: 0px;
        # padding: 0.5em;
        font-family: 'Mona sans' arial;
        # font-size: 16px;
        # display:flex;
        # flex-direction: column;
        background: #000000;
    }
    [data-testid="stSidebar"] {
        min-width: 20%;
        width: 20%;
        height: 100vh;
        position: sticky;
        top: 0;
        background-color: #000000;
        padding: 0px;
        color: white;
        # display: none;
        gap: 5px;
        *{
        border-radius: 0px;
        # margin: 0px;
        font-weight: normal;
        font-size: 23px;
        }
        border-right: 1px solid #555555;
        margin: 0px;
    }
    [data-testid="collapsedControl"] {
        visibility: hidden !important;
        display: none !important;
        color: #000000
        height: 0px;
        width: 0px;
        # border-radius: 0px;
    }
    .main-container {
        top: 0px;
        display: flex;
        flex-direction: row;
        # background: #000000;
    }
    #collapsedControl{
        visibility: hidden !important;
        display: none !important;
    }
    #MainMenu{
        visibility: hidden;
        }
    .stDeployButton {display:none;}
    header{visibility: hidden;}
    footer {visibility: hidden;}
    #stDecoration {display:none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="font">Govt. Schemes to preserve culture and heritage.</p>', unsafe_allow_html=True)

st.markdown("""
---

### 1. National Heritage City Development and Augmentation Yojana (HRIDAY)

The HRIDAY scheme was launched in 2015 with the objective of preserving and revitalizing the cultural heritage of selected cities. It integrates heritage conservation with urban development, focusing on infrastructure upgradation around heritage sites to enhance the overall heritage experience.

- **Coverage:** 12 cities across India including Amritsar, Varanasi, and Gwalior.
- **Funding:** ₹500 crore allocated over 5 years.
- **Impact:** Over 150 heritage structures restored; urban infrastructure improved benefiting more than 10 million residents and tourists.
""")

st.markdown("""
---

### 2. National Culture Fund (NCF)

Established in 1996, the National Culture Fund mobilizes resources for the conservation of heritage and culture from private sectors, individuals, and philanthropists.

- **Financial Assistance:** Over ₹300 crore sanctioned for more than 200 projects.
- **Focus Areas:** Restoration of monuments, promotion of folk and tribal arts, and safeguarding intangible cultural heritage.
- **Outcomes:** Restoration of 50+ monuments and preservation of over 100 traditional art forms.
""")

st.markdown("""
---

### 3. Scheme for Financial Assistance for Preservation of Cultural Heritage

Under the Ministry of Culture, this scheme provides financial aid to State Governments, NGOs, and other agencies for conserving tangible and intangible cultural heritage.

- **Budget Allocation:** ₹100 crore annually.
- **Projects Supported:** Conservation of temples, forts, museums, traditional crafts, and performing arts.
- **Statistics:** Funded over 400 projects nationwide, benefitting nearly 1.5 million artisans and cultural practitioners.
""")

st.markdown("""
---

### 4. National Mission on Monuments and Antiquities (NMMA)

NMMA aims to create a comprehensive database and documentation of India's monuments and antiquities for their effective conservation.

- **Database Size:** Documented over 370,000 heritage sites and monuments.
- **Collaboration:** Works with ASI, State Archaeology Departments, and Universities.
- **Achievements:** Enabled better monitoring and preventive conservation measures on 70% of surveyed sites.
""")

st.markdown("""
---

### 5. INTACH (Indian National Trust for Art and Cultural Heritage) Grants

Though INTACH is a non-governmental body, it receives government support to implement conservation projects.

- **Projects:** Over 250 heritage buildings restored since inception.
- **Geographical Reach:** Works across 20 states.
- **Financial Support:** Government grants totaling ₹50 crore over recent 5 years.
""")
