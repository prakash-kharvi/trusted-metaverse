#Implements the Trust Score equation.
def compute_trust_score(identity, assets, behavior, context):
    """
    Computes the trust score using weighted metrics.
    Parameters:
        identity (float): Identity Verification Score (0-100)
        assets (float): Asset Ownership Score (0-100)
        behavior (float): Behavioral Consistency Score (0-100)
        context (float): Contextual Verification Score (0-100)
    Returns:
        trust_score (float): Final Trust Score
        status (str): Verification Status
    """
    # Define Weights
    w1, w2, w3, w4 = 0.4, 0.3, 0.2, 0.1

    # Compute Final Trust Score
    trust_score = (w1 * identity) + (w2 * assets) + (w3 * behavior) + (w4 * context)

    # Define Status Levels
    if trust_score >= 80:
        status = "Verified"
    elif 70 <= trust_score < 80:
        status = "Needs MFA"
    else:
        status = "Failed"

    return round(trust_score, 2), status
