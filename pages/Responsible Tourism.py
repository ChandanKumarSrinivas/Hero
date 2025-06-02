import streamlit as st

st.set_page_config(page_title="Untouched Places in Indian Tourism", layout="wide")

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
        font-size: 23px;
        text-align: justify;
        }
    .font {
        font-family: 'Times New Roman', Times, serif;
        font-size: 50px;
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

st.markdown('<p class="font">Responsible tourism.</p>', unsafe_allow_html=True)

st.markdown('<p class="main">Tales of Heriatage.</p>', unsafe_allow_html=True)


st.markdown('<h2 class="ttl">Responsible Tourism Overview</h2>', unsafe_allow_html=True)
st.markdown('<p class="para">Increase in responsible tourism practices: 35% in India over last 5 years.<br>'
            'Local community income rise in responsible tourism areas: 20%.<br>'
            'Reduction in waste generation at eco-friendly destinations: 40%.</p>', unsafe_allow_html=True)

st.markdown('<h2 class="ttl">Community-Based Tourism</h2>', unsafe_allow_html=True)
st.markdown('<p class="para">Number of villages implementing community-based tourism: 150+.<br>'
            'Employment generated in local communities: ~50,000 jobs.<br>'
            'Average household income increase in these communities: 25%.</p>', unsafe_allow_html=True)

st.markdown('<h2 class="ttl">Ecotourism</h2>', unsafe_allow_html=True)
st.markdown('<p class="para">Percentage of eco-tourism sites inside protected areas: 75%.<br>'
            'Annual visitor increase at eco-tourism sites since 2018: 18%.<br>'
            'Operators with waste reduction programs: 60%.</p>', unsafe_allow_html=True)

st.markdown('<h2 class="ttl">Cultural Tourism with Preservation</h2>', unsafe_allow_html=True)
st.markdown('<p class="para">Heritage sites following responsible tourism guidelines: 120.<br>'
            'Tourists receiving information on local customs: 70%.<br>'
            'Economic contribution from responsible cultural tourism in 2023: ₹250 crore.</p>', unsafe_allow_html=True)

st.markdown('<h2 class="ttl">Sustainable Transport Initiatives</h2>', unsafe_allow_html=True)
st.markdown('<p class="para">Increase in electric vehicle deployment in tourist hotspots: 30%.<br>'
            'Heritage cities improving public transport access in last 3 years: 40%.<br>'
            'Estimated reduction in tourist-related carbon emissions: 15%.</p>', unsafe_allow_html=True)