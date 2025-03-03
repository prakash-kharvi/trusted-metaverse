#This API calculates and returns the trust score for a given user migrating between virtual worlds.

from fastapi import APIRouter, HTTPException
from src.compute_trust import compute_trust_score
from src.identity_verification import verify_identity
from src.asset_verification import verify_nft_ownership
from src.behavior_analysis import analyze_behavior
from src.context_verification import check_context
import logging

# Initialize Logger
logger = logging.getLogger("trust_api")

# Initialize Router
router = APIRouter()

@router.post("/compute-trust/")
def compute_trust(user_wallet: str, virtual_world: str):
    """
    Computes the trust score for a user migrating to a new metaverse world.
    Returns:
        - Trust Score (0-100)
        - Status (Verified, Needs MFA, Failed)
    """

    try:
        identity_score = verify_identity(user_wallet)
        asset_score = verify_nft_ownership(user_wallet, virtual_world)
        behavior_score = analyze_behavior(user_wallet)
        context_score = check_context(user_wallet)

        trust_score, status = compute_trust_score(identity_score, asset_score, behavior_score, context_score)

        logger.info(f"Trust score computed for {user_wallet}: {trust_score} ({status})")

        return {
            "user_wallet": user_wallet,
            "virtual_world": virtual_world,
            "Identity verification (I) score": identity_score,
            "Asset Ownership (A) score": asset_score,
            "behavioral consistency (B) score": behavior_score,
            "contextual verfication (C) score": context_score,
            "Total Trust Score (%)": trust_score,
            "status": status
        }
    except Exception as e:
        logger.error(f"Error computing trust score: {e}")
        raise HTTPException(status_code=500, detail="Error computing trust score")
