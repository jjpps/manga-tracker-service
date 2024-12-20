from urllib.parse import urlparse

def extract_id_from_url(url):
    parsed = urlparse(url)
    path_parts = parsed.path.rstrip('/').split('/')
    if "title" in path_parts:
        return path_parts[-2]  # Extract and return the manga ID
    return None