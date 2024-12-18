import os
import requests
import hashlib


def get_file_hash(filepath):
    """Calculate the SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


def download_file(url, dest):
    """Download a file and save it to the destination."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)


def check_for_updates(dir, files_to_download):
    os.makedirs(dir, exist_ok=True)

    for filename, url in files_to_download.items():
        local_path = os.path.join(dir, filename)

        # Download the file to a temporary location
        temp_path = f"{local_path}.tmp"
        download_file(url, temp_path)

        # Check if the file exists locally
        if os.path.exists(local_path):
            # Compare hashes to detect updates
            local_hash = get_file_hash(local_path)
            remote_hash = get_file_hash(temp_path)

            if local_hash == remote_hash:
                print(f"{filename} is up-to-date.")
                os.remove(temp_path)  # Remove temporary file
            else:
                print(f"{filename} has been updated. Overwriting with the new version.")
                os.replace(temp_path, local_path)  # Replace the old file
        else:
            print(f"{filename} is not found locally. Downloading for the first time.")
            os.rename(temp_path, local_path)


if __name__ == "__main__":
    check_for_updates(
        "ref",
        {
            "AnalogueKeyboard.cpp": "https://raw.githubusercontent.com/calamity-inc/Soup/senpai/soup/AnalogueKeyboard.cpp",
            "wooting-analog-midi-core": "https://raw.githubusercontent.com/WootingKb/wooting-analog-midi/develop/wooting-analog-midi-core/src/lib.rs",
        },
    )
