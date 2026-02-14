import pandas as pd
from src.config import TEAM_NAME


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column names to lowercase and remove spaces.
    """
    df.columns = df.columns.str.strip().str.lower()
    return df


def select_essential_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only columns needed for performance analysis.
    """
    required_columns = [
        "date",
        "hometeam",
        "awayteam",
        "fthg",
        "ftag",
        "ftr",
        "season"
    ]

    return df[required_columns]


def filter_barcelona_matches(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only matches where Barcelona played.
    """
    return df[
        (df["hometeam"] == TEAM_NAME) |
        (df["awayteam"] == TEAM_NAME)
    ].copy()


def create_match_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create performance-related features.
    """

    # Identify home/away
    df["is_home"] = df["hometeam"] == TEAM_NAME

    # Goals scored
    df["goals_scored"] = df.apply(
        lambda row: row["fthg"] if row["is_home"] else row["ftag"],
        axis=1
    )

    # Goals conceded
    df["goals_conceded"] = df.apply(
        lambda row: row["ftag"] if row["is_home"] else row["fthg"],
        axis=1
    )

    # Goal difference
    df["goal_difference"] = df["goals_scored"] - df["goals_conceded"]

    # Result mapping
    def get_result(row):
        if row["goals_scored"] > row["goals_conceded"]:
            return "Win"
        elif row["goals_scored"] < row["goals_conceded"]:
            return "Loss"
        else:
            return "Draw"

    df["result"] = df.apply(get_result, axis=1)

    # Points
    df["points"] = df["result"].map({
        "Win": 3,
        "Draw": 1,
        "Loss": 0
    })

    return df
