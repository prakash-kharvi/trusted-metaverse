#This file initializes the FastAPI server and routes.
from fastapi import FastAPI
from src.compute_trust import compute_trust_score
from src.identity_verification import verify_identity
from src.asset_verification import verify_nft_ownership
from src.behavior_analysis import analyze_behavior
from src.context_verification import check_context

app = FastAPI(title="Trust Score Evaluation API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Trust Score Evaluation API is running"}


@app.get("/compute-trust/")
def compute_trust(user_wallet: str, virtual_world: str):
    """Computes the trust score for a user moving between metaverse worlds."""

    identity_score = verify_identity(user_wallet)
    asset_score = verify_nft_ownership(user_wallet, virtual_world)
    behavior_score = analyze_behavior(user_wallet)
    context_score = check_context(user_wallet)

    identity_score = 90
    asset_score = 80
    behavior_score = 50
    context_score = 95
    trust_score, status = compute_trust_score(identity_score, asset_score, behavior_score, context_score)

    return {
        "user_wallet": user_wallet,
        #"virtual_world": virtual_world,
        "Identity verification (I) score": identity_score,
        "Asset Ownership (A) score": asset_score,
        "behavioral consistency (B) score": behavior_score,
        "contextual verification (C) score": context_score,
        "Total Trust Score (%)": trust_score,
        #"status": status
    }
