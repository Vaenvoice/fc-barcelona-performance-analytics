import pandas as pd
from pathlib import Path
from src.config import RAW_DATA_DIR


def get_csv_files():
    """
    Returns all CSV files inside data/raw directory.
    """
    return sorted(Path(RAW_DATA_DIR).glob("*.csv"))


def load_single_season(file_path: Path) -> pd.DataFrame:
    """
    Loads a single season file and adds a season column.
    """
    df = pd.read_csv(file_path)

    # Extract season from filename
    season_name = file_path.stem
    df["season"] = season_name

    return df


def load_all_seasons() -> pd.DataFrame:
    """
    Loads and combines all season files into one dataframe.
    """
    files = get_csv_files()

    if not files:
        raise FileNotFoundError("No CSV files found in data/raw/")

    all_dfs = []

    for file in files:
        print(f"Loading {file.name}")
        df = load_single_season(file)
        all_dfs.append(df)

    combined_df = pd.concat(all_dfs, ignore_index=True)

    return combined_df


if __name__ == "__main__":
    df = load_all_seasons()
    print("Combined shape:", df.shape)
    print(df.head())
