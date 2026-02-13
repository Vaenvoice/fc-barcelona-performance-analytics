# FC Barcelona Performance Analytics: A Data Science Project

## Overview

This project is an end-to-end data science analysis of FC Barcelona’s competitive performance from 2008 to 2025.

The objective of this project is to design a modular analytical system that processes match-level data, derives performance metrics, applies rolling statistical analysis, and visualizes long-term trends through an interactive dashboard.

This project demonstrates applied data analysis, feature engineering, time-series reasoning, and structured software design.

---

## Problem Statement

How has FC Barcelona’s performance evolved over time, and how can short-term form fluctuations and long-term structural trends be quantified using data?

This project addresses:

- Short-term performance volatility using rolling metrics  
- Long-term season trends using aggregated features  
- Era-based structural performance differences  
- Quantitative comparison across competitive phases  

---

## Data Pipeline

The project follows a structured data workflow:

1. Raw match data ingestion  
2. Data cleaning and preprocessing  
3. Feature engineering (points, goal difference, rolling averages)  
4. Aggregation to season-level metrics  
5. Analytical modeling and visualization  

The modular design ensures separation between data engineering, analysis, and presentation layers.

---

## Key Analytical Components

### 1. Feature Engineering

Derived structured features including:

- Points per match  
- Goal difference  
- Cumulative season statistics  
- Rolling averages (form indicators)  

These engineered features enable quantitative performance comparison across time.

---

### 2. Rolling Time-Series Analysis

Implemented moving window calculations to model short-term form trends.

Techniques used:

- Rolling mean  
- Window-based aggregation  
- Time-indexed analysis  

This enables detection of momentum shifts and performance instability periods.

---

### 3. Era-Based Comparative Analysis

Defined temporal segments representing different competitive phases and compared:

- Average points  
- Average goals scored  
- Goal differential trends  

This enables structural performance comparison beyond isolated season-level evaluation.

---

### 4. Interactive Analytical Dashboard

Developed an interactive dashboard using Streamlit to:

- Visualize long-term trends  
- Explore rolling performance dynamics  
- Compare metrics across eras  

The dashboard separates analytical computation from presentation logic.

---

## Technology Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Streamlit  

---

## Project Structure

```
fc-barcelona-performance-analytics/
│
├── app/                 # Streamlit application layer
│   └── streamlit_app.py
│
├── data/                # Raw and processed datasets
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data/            # Data ingestion and cleaning
│   ├── analysis/        # Analytical computations
│   └── report/          # Report generation
│
├── reports/             # Generated figures and reports
│
├── requirements.txt
└── README.md
```

The architecture emphasizes modularity, maintainability, and scalability.

---

## Skills Demonstrated

- Data preprocessing and cleaning  
- Feature engineering  
- Rolling time-series analysis  
- Statistical aggregation  
- Data visualization  
- Modular Python project design  
- Reproducible environment management  
- Analytical storytelling through dashboards  

---

## How to Run Locally

Clone the repository:

```bash
git clone <repository-url>
cd fc-barcelona-performance-analytics
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app/streamlit_app.py
```

---

## Future Improvements

- Predictive modeling for match outcomes  
- Expected goals (xG) efficiency comparison  
- Elo-based team strength modeling  
- Performance volatility index  
- Model evaluation using cross-validation  

---

## Author

Pragyan  
Undergraduate student focused on data science, statistical modeling, and applied analytics.
