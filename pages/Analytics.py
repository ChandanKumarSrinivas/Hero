import streamlit as st
import pandas as pd
import plotly.express as px
import json
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib.cm import get_cmap
import numpy as np

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
        background-color: #000000;  /* 🎨 Your custom background color */
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

# st.sidebar.button("Home")
# st.sidebar.button("Analytics")
# st.sidebar.button("Lookup")
# st.sidebar.button("Untouched")



# Use HTML inside markdown for the title
st.markdown('<p class="font">Analytics page.</p>', unsafe_allow_html=True)

# st.markdown('<p class="para">Tales of Heriatage.</p>', unsafe_allow_html=True)
# st.markdown('<p class="main">Tales of Heriatage.</p>', unsafe_allow_html=True)

st.text("")
st.text("")

st.markdown('<p class="main">📊 Monthly Tourist Arrivals in 2024 (in lakhs)</p>', unsafe_allow_html=True)

st.text("")
st.text("")

import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", 
          "September", "October", "November", "December"]

visitors_2023 = [8.91, 8.93, 8.25, 6.26, 6.18, 6.68, 7.86, 6.64, 6.67, 8.32, 9.49, 11.02]
visitors_2024 = [9.59, 10.03, 8.6, 6.51, 6, 7.06, 7.76, 6.36, 0, 0, 0, 0]

# Plasma colors for lines
color_2023 = '#d01c8b'  # plasma magenta
color_2024 = '#fdb863'  # plasma orange

# Set page config for dark background
# st.set_page_config(page_title="Tourist Visitors Plot", layout="wide", initial_sidebar_state="auto")

# Title
# st.title("Monthly Foreign Tourist Visitors in India")

# Create figure with black background
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('black')      # Figure background
ax.set_facecolor('black')              # Plot background

# Plot lines
ax.plot(months, visitors_2023, marker='o', color=color_2023, label='2023')
ax.plot(months, visitors_2024, marker='o', color=color_2024, label='2024')

# Text colors to white
# ax.set_title("Monthly Foreign Tourist Visitors in India (Millions)", color='white', fontsize=16)
ax.set_xlabel("Month", color='white', fontsize=14)
ax.set_ylabel("Visitors (Millions)", color='white', fontsize=14)

ax.tick_params(axis='x', colors='white', rotation=45)
ax.tick_params(axis='y', colors='white')

ax.legend(facecolor='black', edgecolor='white', fontsize=12)

ax.grid(True, color='gray', linestyle='--', alpha=0.3)

# Show plot in Streamlit
st.pyplot(fig)

#########################################################################################################

with open('swdfvc.json', 'r') as f:
    data_json = json.load(f)

df = pd.DataFrame(data_json)
df = df[df["State/ UT Name"] != "Total"]

plt.style.use('dark_background')  # Sets plot background to black and grid/dark style

def plot_visitors(visitor_type):
    fig, ax = plt.subplots(figsize=(14, 6))
    states = df["State/ UT Name"]
    n = len(states)

    # Use plasma colormap for bars, 2 colors (for 2014 and 2015)
    cmap = get_cmap('plasma')
    color_2014 = cmap(0.6)  # Bright plasma color for 2014
    color_2015 = cmap(0.9)  # Another bright plasma color for 2015

    bar_width = 0.35
    indices = np.arange(n)

    ax.bar(indices, df[f"2014 - {visitor_type}"], width=bar_width, label='2014', color=color_2014)
    ax.bar(indices + bar_width, df[f"2015 - {visitor_type}"], width=bar_width, label='2015', color=color_2015)

    ax.set_xticks(indices + bar_width / 2)
    ax.set_xticklabels(states, rotation=90, fontsize=8, color='white')
    ax.set_ylabel('Visitor Count', color='white')
    ax.set_title(f'{visitor_type} Visitors in 2014 and 2015 by State/UT', color='white')

    # Set tick params color to white
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='x', colors='white')

    # Legend text color to white
    legend = ax.legend()
    for text in legend.get_texts():
        text.set_color('white')

    # Set figure background and axes background to pitch black
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    plt.tight_layout()
    st.pyplot(fig)

st.title("Tourist Visitors in India by State/UT (2014 vs 2015)")

st.header("Domestic Visitors")
plot_visitors("Domestic")

st.header("Foreign Visitors")
plot_visitors("Foreign")

############################################################################################################

with open('swdfvc.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

# Remove the "Total" row
df = df[df['State/ UT Name'] != 'Total']

def plot_growth_rate(vis_type):
    # Choose column based on visitor type
    col_name = f"Growth Rate - {vis_type}"

    states = df['State/ UT Name']
    growth_rates = df[col_name].astype(float)

    # Select colormap 'plasma', focusing on magenta range (0.6 to 0.9)
    cmap = get_cmap('plasma')
    # magenta_pink_color = cmap(0.8)
    # cmap = get_cmap('plasma')
    colors = [cmap(0.9) for _ in growth_rates]  # fixed magenta-ish color

    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    bars = ax.bar(states, growth_rates, color=colors)

    ax.set_title(f'{vis_type} Growth Rate by State (2014-2015)', color='white', fontsize=16)
    ax.set_xlabel('State / UT Name', color='white', fontsize=12)
    ax.set_ylabel('Growth Rate (%)', color='white', fontsize=12)
    ax.tick_params(axis='x', rotation=90, colors='white')
    ax.tick_params(axis='y', colors='white')

    # Grid lines with subtle white color
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.3)

    st.pyplot(fig)

st.title("Tourism Growth Rates by State/UT")
st.markdown("<hr>", unsafe_allow_html=True)

plot_growth_rate("Domestic")
plot_growth_rate("Foreign")