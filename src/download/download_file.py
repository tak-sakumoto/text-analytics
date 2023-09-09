"""
download_file.py
"""
import requests

def download_file(url, save_path):
    """
    Download a file from the specified URL and save it to the specified path

    Args:
        url (str): URL of the file to be downloaded
        save_path (Path): Path where the downloaded file will be saved
    """
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        # Raise an exception if the request was not successful
        response.raise_for_status()

        # Save the content of the response to the specified file path
        with open(save_path, "wb") as file:
            file.write(response.content)

        print(f"Downloaded successfully: {save_path}")

    except requests.exceptions.RequestException as exception:
        print(f"Error downloading the file: {exception}")
