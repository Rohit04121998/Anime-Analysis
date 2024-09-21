import pandas as pd

from src.utils import extract_values, item_generator


def process_metadata(entries):
    """
    Processes metadata into a Pandas DataFrame (mediaId, score).
    """
    metadata_list = []
    for entry in entries:
        metadata_list.append(pd.DataFrame({"media_id": [entry["mediaId"]], "score": [entry["score"]]}))
    metadata_df = pd.concat(metadata_list, ignore_index=True)
    return metadata_df


def process_data(entries):
    """
    Processes the main data into a Pandas DataFrame (media details).
    """
    data_df = pd.DataFrame(
        columns=[
            "media_id",
            "title_in_romaji",
            "title_in_english",
            "episodes",
            "source",
            "genres",
            "mean_score",
            "description",
            "duration",
            "year_released",
        ]
    )
    # Extract values for data fields (media details)
    data_df["media_id"] = extract_values(entries, "id")
    data_df["title_in_romaji"] = extract_values(entries, "romaji")
    data_df["title_in_english"] = extract_values(entries, "english")
    data_df["episodes"] = extract_values(entries, "episodes")
    data_df["source"] = extract_values(entries, "source")
    data_df["mean_score"] = extract_values(entries, "meanScore")
    data_df["description"] = extract_values(entries, "description")
    data_df["duration"] = extract_values(entries, "duration")
    data_df["genres"] = list(item_generator(entries, "genres"))
    data_df["year_released"] = extract_values(entries, "seasonYear")

    # Extraction logic similar to earlier
    return data_df
