#This API handles user authentication using Web3 wallets and ENS (Ethereum Name Service).
from fastapi import APIRouter, HTTPException
from src.identity_verification import verify_identity
import logging

# Initialize Logger
logger = logging.getLogger("user_api")

# Initialize Router
router = APIRouter()


@router.post("/verify-user/")
def verify_user(user_wallet: str):
    """
    Verifies the user identity based on their Web3 wallet.
    Returns:
        - Identity Score (0-100)
    """
    try:
        identity_score = verify_identity(user_wallet)

        if identity_score > 0:
            logger.info(f"User verified: {user_wallet} (Score: {identity_score})")
            return {"user_wallet": user_wallet, "identity_score": identity_score, "status": "Verified"}
        else:
            logger.warning(f"User verification failed: {user_wallet}")
            raise HTTPException(status_code=400, detail="Invalid Wallet Address")

    except Exception as e:
        logger.error(f"Error verifying user: {e}")
        raise HTTPException(status_code=500, detail="Error verifying user")
