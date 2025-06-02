import json
import streamlit as st
import pydeck as pdk
import pandas as pd

st.set_page_config(layout="wide")

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
        font-size: 21px !important;
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
        font-size: 21px;
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

st.markdown('<p class="font">Tales of Heriatage.</p>', unsafe_allow_html=True)
st.text("")
st.markdown('<p class="main">In 2023, India received 18.89 million international tourists. This included 9.52 million foreign tourists, exceeding pre-pandemic levels by 87.09%, according to the Ministry of Tourism. Additionally, 9.38 million Non-Resident Indian (NRI) arrivals were recorded, also exceeding pre-pandemic levels.<br></p>', unsafe_allow_html=True)
st.text("")
st.text("")
st.text("")

with open("./Resource/places_with_coordinates.json", "r", encoding="utf-8") as f:
    data = json.load(f)

filtered = [d for d in data if d.get("latitude") and d.get("longitude")]

df = pd.DataFrame(filtered)

df["elevation"] = df["Counts"] * 0.1  

def get_color(count):
    if count == 0:
        return [220, 220, 220]
    elif count < 100000:
        return [100, 255, 200]
    elif count < 1000000:
        return [100, 180, 255]
    elif count < 5000000:
        return [255, 165, 0]
    else:
        return [255, 0, 0]

df["color"] = df["Counts"].apply(get_color)


layer = pdk.Layer(
    "ColumnLayer",
    data=df,
    get_position='[longitude, latitude]',
    get_elevation="elevation",
    elevation_scale=1,
    radius=20000,  
    get_fill_color="color",
    pickable=True,
    auto_highlight=True,
)


view_state = pdk.ViewState(
    longitude=78.9629,
    latitude=22.5937,
    zoom=4,
    pitch=50,
    bearing=-10
)

st.title("🗺️ 3D Interactive Bar Map of Indian Landmarks by Visitor Count")

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    map_style='mapbox://styles/mapbox/dark-v10',  
    tooltip={"text": "{Name}\nVisitors: {Counts}"}
))

#######################################################################################3


st.text("")
st.text("")
st.markdown("""
<p class="para">
Medical tourism in India has emerged as a significant contributor to the country's foreign exchange earnings, positioning India as one of the leading global destinations for affordable and quality healthcare services. In 2023, India attracted over 1.4 million foreign patients, generating approximately USD 9 billion in revenue, which significantly bolstered the nation’s foreign exchange reserves. The cost-effectiveness of treatments, combined with the availability of highly skilled medical professionals and advanced technology, makes India an attractive option for medical travelers from countries like the US, UK, Africa, and the Middle East. Cities such as Chennai have become hubs for medical tourism due to their extensive network of multi-specialty hospitals offering services ranging from cardiac surgery to orthopedic treatments and cosmetic procedures. Chennai alone accounts for nearly 45 percent of India’s total medical tourists, supported by robust healthcare infrastructure and proximity to international airports facilitating easy access.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p class="para">
Beyond medical tourism, India’s overall tourism sector comprising both foreign and domestic travelers plays a pivotal role in its economy. In the fiscal year 2023-24, India received around 18 million foreign tourists, generating approximately USD 30 billion in foreign exchange, while domestic tourism accounted for over 2 billion visits, contributing substantially to internal economic growth. The city of Delhi remains the most visited destination by foreign tourists due to its rich cultural heritage, historical monuments, and status as the national capital, drawing an estimated 16 million foreign visitors annually. Technical aspects such as visa facilitation through e-tourist visas and improvements in transport connectivity have further fueled tourism growth. The government’s focused promotion of niche tourism segments including wellness and heritage tourism alongside sustained investments in infrastructure have enhanced India’s competitive edge in attracting tourists globally, fostering significant socioeconomic benefits.
</p>
""", unsafe_allow_html=True)