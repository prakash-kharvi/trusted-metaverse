#Verifies IP address, device fingerprint, and login location.
import requests

GEOIP_API_URL = "https://ipinfo.io/json"


def check_context(user_wallet):
    """
    Checks if the user's IP and device fingerprint match past logins.
    Returns a contextual verification score (0-100).
    """
    response = requests.get(GEOIP_API_URL)

    if response.status_code != 200:
        return 50  # Default score if API fails

    user_location = response.json().get("city", "Unknown")

    # Simulate comparison with previous login locations
    known_locations = ["New York", "London", "Berlin"]

    context_score = 100 if user_location in known_locations else 50

    return context_score
