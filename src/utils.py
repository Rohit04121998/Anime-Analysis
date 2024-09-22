import logging

import requests


def make_request(query):
    """
    Sends a GraphQL request to Anilist API and returns the JSON response.
    Includes error handling for 'User not found'.
    """
    url = "https://graphql.anilist.co"
    try:
        response = requests.post(url, json={"query": query})
        response.raise_for_status()
        data = response.json()

        if "errors" in data:
            error_message = data["errors"][0]["message"]
            if "User not found" in error_message:
                logging.error(f"Anilist API error: {error_message}")
                return {"error": "User not found"}

        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return {"error": str(e)}  # Ensure it returns a dict with error message


def extract_entries(data):
    """
    Extracts entries from multiple lists in the JSON response.
    """
    entries = []
    for lst in data.get("data", {}).get("MediaListCollection", {}).get("lists", []):
        entries.extend(lst["entries"])
    return entries


def extract_values(obj, key):
    """
    Recursively extracts values associated with a specific key from a nested JSON object.

    Args:
    obj (dict or list): The JSON object to search.
    key (str): The key whose values we want to extract.

    Returns:
    list: List of values for the specified key.
    """
    arr = []

    def recursive_extract(obj, arr, key):
        """Helper function for recursive key extraction."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    recursive_extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                recursive_extract(item, arr, key)
        return arr

    return recursive_extract(obj, arr, key)


def item_generator(json_input, lookup_key):
    """
    Generates values for a specific key from a nested JSON object.

    Args:
    json_input (dict or list): The JSON input to search through.
    lookup_key (str): The key to look for.

    Yields:
    Generator of values matching the lookup_key.
    """
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)
