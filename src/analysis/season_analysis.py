import pandas as pd
import numpy as np


def calculate_dominance_index(summary: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate composite dominance score for each season.
    Expects season-level aggregated dataframe.
    """

    summary = summary.copy()

    # Per-game advanced metrics
    summary["gd_per_game"] = summary["goal_difference"] / summary["matches"]
    summary["goals_per_game"] = summary["goals_scored"] / summary["matches"]
    summary["goals_conceded_per_game"] = (
        summary["goals_conceded"] / summary["matches"]
    )

    # ---- Normalization (Z-Score) ----
    metrics = [
        "points_per_game",
        "gd_per_game",
        "goals_per_game",
        "goals_conceded_per_game",
    ]

    for col in metrics:
        summary[f"{col}_z"] = (
            summary[col] - summary[col].mean()
        ) / summary[col].std()

    # Invert defensive metric (lower conceded = better)
    summary["goals_conceded_per_game_z"] *= -1

    # ---- Weighted Composite Score ----
    summary["dominance_index"] = (
        0.35 * summary["points_per_game_z"]
        + 0.30 * summary["gd_per_game_z"]
        + 0.20 * summary["goals_per_game_z"]
        + 0.15 * summary["goals_conceded_per_game_z"]
    )

    summary["dominance_rank"] = (
        summary["dominance_index"]
        .rank(method="first", ascending=False)
        .astype(int)
    )

    return summary


def build_season_summary(match_df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates match-level dataset into season summary
    and computes dominance index.
    """

    summary = (
        match_df.groupby("season")
        .agg(
            matches=("season", "count"),
            wins=("result", lambda x: (x == "Win").sum()),
            draws=("result", lambda x: (x == "Draw").sum()),
            losses=("result", lambda x: (x == "Loss").sum()),
            goals_scored=("goals_scored", "sum"),
            goals_conceded=("goals_conceded", "sum"),
            total_points=("points", "sum"),
        )
        .reset_index()
    )

    # Goal difference
    summary["goal_difference"] = (
        summary["goals_scored"] - summary["goals_conceded"]
    )

    # Points per game
    summary["points_per_game"] = (
        summary["total_points"] / summary["matches"]
    ).round(3)

    summary = summary.sort_values("season")

    # Add dominance index
    summary = calculate_dominance_index(summary)

    return summary



