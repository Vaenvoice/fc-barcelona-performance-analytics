import pandas as pd


def get_rolling_metrics(df: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    """
    Computes rolling match-level performance metrics.

    Expected columns:
    - date
    - season
    - points
    - goal_difference
    """

    df = df.copy()

    # Ensure proper datetime format
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    df = df.sort_values("date")

    # Rolling averages
    df[f"rolling_points_{window}"] = (
        df["points"]
        .rolling(window=window)
        .mean()
    )

    df[f"rolling_goal_difference_{window}"] = (
        df["goal_difference"]
        .rolling(window=window)
        .mean()
    )

    return df


def get_season_consistency(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates season consistency index using
    standard deviation of match points.
    Lower std = more consistent season.
    """

    consistency = (
        df.groupby("season")
        .agg(points_std=("points", "std"))
        .round(3)
        .reset_index()
        .sort_values("season")
    )

    return consistency

