import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="NBA Cup Prediction Dashboard", layout="wide")

st.title("🏀 2024 NBA Cup Prediction Dashboard")
st.markdown("### A Cloud Computing Approach to Score Prediction (INFO-516)")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predictions", "Group Standings", "Methodology"])

if page == "Home":
    st.header("Welcome to the NBA Cup Analytics Hub")
    st.image("https://upload.wikimedia.org/wikipedia/en/b/b5/2023_NBA_In-Season_Tournament_logo.svg", width=200)
    st.write("""
    This application hosts the predictive model results for the NBA Cup. 
    Our model uses 9+ seasons of historical data to predict team scores and determine game winners.
    """)
    
    st.subheader("Key Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Training Accuracy", "62.3%")
    col2.metric("Group Play Accuracy", "68.33%")
    col3.metric("Projected Final", "Knicks vs. Thunder")

elif page == "Predictions":
    st.header("Game by Game Predictions")
    
    # Mock data based on Figure 1 in report
    date = st.date_input("Select Date", value=pd.to_datetime("2024-12-03"))
    
    if str(date) == "2024-12-03":
        predictions = pd.DataFrame({
            "Matchup": [
                "Philadelphia @ Charlotte", "Orlando @ New York", "Washington @ Cleveland", 
                "Utah @ Okla City", "Indiana @ Toronto", "Golden State @ Denver"
            ],
            "Predicted Score": [
                "106.25 - 109.89", "105.25 - 116.06", "107.27 - 123.47", 
                "108.64 - 114.02", "114.37 - 115.76", "114.68 - 119.82"
            ],
            "Correct?": ["❌", "✅", "✅", "✅", "✅", "✅"]
        })
        st.table(predictions)
    else:
        st.info("Showing mock data for 2024-12-03 only.")

elif page == "Group Standings":
    st.header("NBA Cup Group Play: West C (Actual vs Predicted)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Actual Standings")
        actual = pd.DataFrame({
            "Team": ["Golden State", "Dallas", "Denver", "Memphis", "New Orleans"],
            "W": [3, 3, 2, 1, 1], "L": [1, 1, 2, 3, 3], "Pts Diff": [+8, +46, +6, -11, -49]
        })
        st.dataframe(actual)
        
    with col2:
        st.subheader("Predicted Standings")
        predicted = pd.DataFrame({
            "Team": ["Denver", "Golden State", "Dallas", "Memphis", "New Orleans"],
            "W": [4, 3, 2, 1, 0], "L": [0, 1, 2, 3, 4], "Pts Diff": [+12.9, +11.7, +6.5, -4.8, -26.2]
        })
        st.dataframe(predicted)

elif page == "Methodology":
    st.header("How the Model Works")
    st.write("""
    1. **Data Ingestion**: Scraped daily team stats and game scores using pySpark.
    2. **Feature Engineering**: Normalized stats like eFG%, Turnover Rate, and Pace.
    3. **Training**: Evaluated Linear Regression, Ridge, Lasso, and GBT.
    4. **Selection**: Linear Regression was chosen for its superior winner-prediction accuracy.
    """)
    st.latex(r"Score_{Team} = \beta_0 + \beta_1(Location) + \beta_2(eFG\%) + \dots + \epsilon")

st.sidebar.markdown("---")
st.sidebar.info("Developed by: Chin-yu Wu")
