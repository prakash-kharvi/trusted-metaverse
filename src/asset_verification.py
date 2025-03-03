#Checks NFT ownership in the user's wallet.
import requests
import os

NFT_API_URL = "https://api.opensea.io/api/v1/assets"


def verify_nft_ownership(user_wallet, virtual_world):
    """
    Checks if the user owns relevant NFTs for a given metaverse world.
    Returns an asset ownership score (0-100).
    """
    # Fetch NFTs from OpenSea API
    params = {"owner": user_wallet, "limit": 50}
    headers = {"X-API-KEY": os.getenv("OPENSEA_API_KEY")}

    response = requests.get(NFT_API_URL, params=params, headers=headers)

    if response.status_code != 200:
        return 0  # API failure

    nft_data = response.json().get("assets", [])

    # Check if user owns relevant NFTs
    relevant_nfts = [nft for nft in nft_data if virtual_world.lower() in nft["collection"]["name"].lower()]

    # Score Calculation
    asset_score = min(100, len(relevant_nfts) * 10)  # Example logic: More NFTs, higher score

    return asset_score
