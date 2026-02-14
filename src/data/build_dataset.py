from src.data.load_data import load_all_seasons
from src.data.clean_data import (
    standardize_columns,
    select_essential_columns,
    filter_barcelona_matches,
    create_match_features
)
from src.config import PROCESSED_DATA_DIR


def build_dataset():
    df = load_all_seasons()
    df = standardize_columns(df)
    df = select_essential_columns(df)
    df = filter_barcelona_matches(df)
    df = create_match_features(df)

    output_path = PROCESSED_DATA_DIR / "barcelona_2008_2025.csv"
    df.to_csv(output_path, index=False)

    print("Processed dataset created successfully.")
    print("Final shape:", df.shape)


if __name__ == "__main__":
    build_dataset()
