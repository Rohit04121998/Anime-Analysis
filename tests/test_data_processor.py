from src.data_processor import process_metadata


def test_process_metadata():
    entries = (
        {"mediaId": 1, "score": 10, "irrelevant_key": 0},
        {"mediaId": 2, "score": 9, "irrelevant_key": 0, "invalid_key": None},
    )
    metadata_df = process_metadata(entries)
    assert metadata_df.columns.tolist() == ["media_id", "score"]
    assert metadata_df.shape == (2, 2)
    assert metadata_df["media_id"].tolist() == [1, 2]
    assert metadata_df["score"].tolist() == [10, 9]
