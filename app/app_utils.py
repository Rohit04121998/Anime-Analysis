import logging

from src.data_processor import process_data, process_metadata
from src.queries import data_query_template, metadata_query_template
from src.save_data import save_csv, save_json
from src.utils import extract_entries, make_request


def fetch_and_save_data(anilist_user):
    """
    Fetches and saves data from AniList for a given user.

    This function retrieves metadata and data for the specified AniList user
    across different statuses ("COMPLETED", "PLANNING", "CURRENT"). It then
    processes and saves the data in JSON and CSV formats.

    Args:
        anilist_user (str): The AniList username for which to fetch data.

    Returns:
        bool: True if data fetching and saving were successful, False otherwise.

    Raises:
        Exception: If an error occurs during the data fetching or processing.
    """
    statuses = ["COMPLETED", "PLANNING", "CURRENT"]
    csv_files = []  # List to store CSV file paths
    try:
        for status in statuses:
            logging.info(f"Fetching data for status: {status}")

            metadata_query = metadata_query_template.format(anilist_user=anilist_user, status=status)
            data_query = data_query_template.format(anilist_user=anilist_user, status=status)

            metadata_response = make_request(metadata_query)
            data_response = make_request(data_query)

            metadata_entries = extract_entries(metadata_response)
            data_entries = extract_entries(data_response)

            save_json(metadata_entries, f"anilist_metadata_{status}.json")
            save_json(data_entries, f"anilist_data_{status}.json")

            metadata_df = process_metadata(metadata_entries)
            data_df = process_data(data_entries)

            merged_df = metadata_df.merge(data_df, on="media_id")
            csv_file_path = f"anilist_merged_{status}.csv"
            save_csv(merged_df, csv_file_path)
            csv_files.append(csv_file_path)  # Add CSV file path to the list

        return csv_files  # Return the list of CSV file paths
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
