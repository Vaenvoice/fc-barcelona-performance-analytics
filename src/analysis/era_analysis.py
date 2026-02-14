import pandas as pd


def assign_era(season: str) -> str:
    """
    Assign managerial era based on season.
    """

    if season in ["2008_2009", "2009_2010", "2010_2011", "2011_2012"]:
        return "Guardiola Era"

    elif season == "2012_2013":
        return "Tito Era"

    elif season in ["2014_2015", "2015_2016", "2016_2017"]:
        return "Luis Enrique Era"

    elif season in ["2017_2018", "2018_2019", "2019_2020"]:
        return "Valverde Era"

    elif season in ["2020_2021", "2021_2022"]:
        return "Post-Messi Decline"

    elif season in ["2022_2023", "2023_2024", "2024_2025"]:
        return "Xavi Era"

    else:
        return "Other"


def get_era_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns aggregated performance metrics grouped by era.
    Expects dataframe with:
    - season
    - total_points
    - goal_difference
    - dominance_index
    """

    df = df.copy()

    df["era"] = df["season"].apply(assign_era)

    era_summary = (
        df.groupby("era")
        .agg(
            avg_points=("total_points", "mean"),
            avg_goal_difference=("goal_difference", "mean"),
            avg_dominance=("dominance_index", "mean"),
        )
        .round(2)
        .reset_index()
    )

    return era_summary


