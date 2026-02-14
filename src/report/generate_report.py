import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from src.config import PROCESSED_DATA_DIR


def generate_report():

    # Create reports folder
    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)

    # Load season summary
    season_df = pd.read_csv(PROCESSED_DATA_DIR / "season_summary.csv")
    season_df = season_df.sort_values("season")

    # -----------------------------
    # Chart 1: Total Points
    # -----------------------------
    plt.figure()
    plt.plot(season_df["season"], season_df["total_points"])
    plt.xticks(rotation=45)
    plt.title("Barcelona Total Points Per Season")
    plt.xlabel("Season")
    plt.ylabel("Total Points")
    plt.tight_layout()
    plt.savefig(report_dir / "total_points_trend.png")
    plt.close()

    # -----------------------------
    # Chart 2: Goals Trend
    # -----------------------------
    plt.figure()
    plt.plot(season_df["season"], season_df["goals_scored"])
    plt.plot(season_df["season"], season_df["goals_conceded"])
    plt.xticks(rotation=45)
    plt.title("Goals Scored vs Conceded")
    plt.xlabel("Season")
    plt.ylabel("Goals")
    plt.tight_layout()
    plt.savefig(report_dir / "goals_trend.png")
    plt.close()

    # -----------------------------
    # Chart 3: Goal Difference
    # -----------------------------
    plt.figure()
    plt.plot(season_df["season"], season_df["goal_difference"])
    plt.xticks(rotation=45)
    plt.title("Goal Difference Trend")
    plt.xlabel("Season")
    plt.ylabel("Goal Difference")
    plt.tight_layout()
    plt.savefig(report_dir / "goal_difference_trend.png")
    plt.close()

    # Save summary table
    season_df.to_csv(report_dir / "season_summary_report.csv", index=False)
        # -----------------------------
    # Automated Performance Summary
    # -----------------------------

    peak_season = season_df.loc[season_df["total_points"].idxmax()]
    worst_season = season_df.loc[season_df["total_points"].idxmin()]

    peak_points = peak_season["total_points"]
    worst_points = worst_season["total_points"]

    percent_decline = round(
        ((peak_points - worst_points) / peak_points) * 100, 2
    )

    print("\n===== PERFORMANCE SUMMARY =====")
    print(f"Peak Season: {peak_season['season']} ({peak_points} points)")
    print(f"Lowest Season: {worst_season['season']} ({worst_points} points)")
    print(f"Performance decline from peak: {percent_decline}%")

    print("Report generated successfully.")
    print("Saved files:")
    print("- total_points_trend.png")
    print("- goals_trend.png")
    print("- goal_difference_trend.png")
    print("- season_summary_report.csv")


if __name__ == "__main__":
    generate_report()
