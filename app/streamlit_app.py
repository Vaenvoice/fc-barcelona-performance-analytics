import streamlit as st
import pandas as pd
import sys
import os

# Allow src imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.analysis.era_analysis import get_era_summary
from src.analysis.rolling_analysis import get_rolling_metrics, get_season_consistency
from src.analysis.trend_analysis import get_season_trends

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="FC Barcelona Performance Dashboard",
    layout="wide"
)

st.title("FC Barcelona Performance Analysis (2008–2025)")
st.markdown("Comprehensive performance and dominance evaluation.")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
SEASON_PATH = "data/processed/season_summary.csv"
MATCH_PATH = "data/processed/barcelona_2008_2025.csv"

season_df = pd.read_csv(SEASON_PATH)
match_df = pd.read_csv(MATCH_PATH)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.header("Dashboard Controls")

rolling_window = st.sidebar.slider(
    "Rolling Window (Matches)",
    min_value=3,
    max_value=10,
    value=5
)

# --------------------------------------------------
# 1️⃣ Executive KPI Section
# --------------------------------------------------
st.header("Executive Overview")

col1, col2, col3 = st.columns(3)

best_season = season_df.loc[season_df["total_points"].idxmax()]
worst_season = season_df.loc[season_df["total_points"].idxmin()]
highest_dom = season_df.loc[season_df["dominance_index"].idxmax()]

with col1:
    st.metric(
        "Best Season",
        best_season["season"],
        f"{best_season['total_points']} pts"
    )

with col2:
    st.metric(
        "Worst Season",
        worst_season["season"],
        f"{worst_season['total_points']} pts"
    )

with col3:
    st.metric(
        "Highest Dominance",
        highest_dom["season"],
        round(highest_dom["dominance_index"], 2)
    )

st.divider()

# --------------------------------------------------
# 2️⃣ Season Trends
# --------------------------------------------------
st.header("Season Performance Trends")

trend_df = get_season_trends(season_df)

st.subheader("Total Points per Season")
st.line_chart(trend_df.set_index("season")["total_points"])

st.subheader("Goal Difference Trend")
st.line_chart(trend_df.set_index("season")["goal_difference"])

st.subheader("Dominance Index Trend")
st.line_chart(trend_df.set_index("season")["dominance_index"])

st.divider()

# --------------------------------------------------
# 3️⃣ Dominance Ranking Table
# --------------------------------------------------
st.header("Season Dominance Ranking")

ranking_df = season_df.sort_values(
    "dominance_index", ascending=False
)[["season", "dominance_index", "dominance_rank"]]

st.dataframe(ranking_df, use_container_width=True)

st.divider()

# --------------------------------------------------
# 4️⃣ Era Comparison
# --------------------------------------------------
st.header("Era Comparison")

era_summary = get_era_summary(season_df)

st.dataframe(era_summary, use_container_width=True)

st.bar_chart(
    era_summary.set_index("era")[
        ["avg_points", "avg_goal_difference", "avg_dominance"]
    ]
)

st.divider()

# --------------------------------------------------
# 5️⃣ Rolling Match Analysis
# --------------------------------------------------
st.header("Rolling Match Analysis")

rolling_df = get_rolling_metrics(match_df, window=rolling_window)

st.subheader(f"{rolling_window}-Match Rolling Points")
st.line_chart(
    rolling_df.set_index("date")[f"rolling_points_{rolling_window}"]
)

st.subheader(f"{rolling_window}-Match Rolling Goal Difference")
st.line_chart(
    rolling_df.set_index("date")[f"rolling_goal_difference_{rolling_window}"]
)

st.subheader("Season Consistency (Points STD)")
consistency_df = get_season_consistency(match_df)
st.line_chart(consistency_df.set_index("season")["points_std"])
