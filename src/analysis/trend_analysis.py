import pandas as pd


def get_season_trends(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns season-level trend data sorted chronologically.

    Expected columns:
    - season
    - total_points
    - goals_scored
    - goals_conceded
    - goal_difference
    - dominance_index
    """

    df = df.copy()
    df = df.sort_values("season")

    return df[
        [
            "season",
            "total_points",
            "goals_scored",
            "goals_conceded",
            "goal_difference",
            "dominance_index",
        ]
    ]

