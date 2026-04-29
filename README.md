# Projecting the 2024 NBA Cup: A Cloud Computing Approach to Score Prediction

## Overview
This project, developed for the **INFO-516 Cloud Computing** course, aims to create a predictive model for NBA team scores and simulate the 2024 NBA Cup (In-Season Tournament). By leveraging large-scale data and cloud computing tools, I simulated matchups from the group phase through the knockout rounds to predict the tournament winner.

## Author
*   **Chin-yu Wu**: Developed the end-to-end pipeline, including data scraping, cleaning, model training, and dashboard development.

## Key Features
*   **Massive Data Scraping**: Collected over 9 seasons of NBA data (from 2015-16 onwards) from ESPN and TeamRankings.
*   **High-Performance Processing**: Utilized **pySpark** to handle and process over 12,000 individual site scrapes efficiently.
*   **Predictive Modeling**: Tested Linear Regression, Ridge, Lasso, and Gradient Boosted Trees (GBT).
*   **Best Model**: Linear Regression provided the highest accuracy for winner prediction.
*   **Web Dashboard**: A **Streamlit** application hosting pre-game predictions and real-time result tracking.

## Dataset Variables
The model uses the following variables to predict a team's score:
*   `team_location` (Home/Away)
*   `team_efg%` (Effective Field Goal Percentage)
*   `team_tov%` (Turnover Rate)
*   `team_fta_rate` (Free Throw Attempt Rate)
*   `team_oreb%` (Offensive Rebounding Percentage)
*   `team_pace` (Possessions per game)
*   `opponent_efg%`, `opponent_tov%`, `opponent_fta_rate`, `opponent_oreb%`, `opponent_pace`

## Results
*   **Training Accuracy**: 62.3% winner prediction accuracy.
*   **NBA Cup Group Play Accuracy**: 68.33% accuracy.
*   **Predicted Championship**: New York Knicks vs. Oklahoma City Thunder.

## Discussion & Limitations
*   **Evolution of Play**: Only the last 10 seasons were used as the NBA's style of play has evolved significantly (increased offensive efficiency).
*   **Missing Context**: Factors such as player injuries, team schedules, and individual personalities were not included in the model.
*   **Future Work**: Incorporating season trends, injury reports, and trade data.

## Setup & Usage
1.  **Dependencies**: Install required packages using `pip install -r requirements.txt`.
2.  **Scraping**: Run `scraper.py` to collect latest data using pySpark.
3.  **Training**: Run `train_model.py` to train the Linear Regression model.
4.  **Dashboard**: Launch the dashboard using `streamlit run app.py`.
