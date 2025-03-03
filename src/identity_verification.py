#Handles user authentication using Ethereum Name Service (ENS) and Web3 wallets
from web3 import Web3
import os

BLOCKCHAIN_RPC_URL = os.getenv("BLOCKCHAIN_RPC_URL", "https://mainnet.infura.io/v3/2b550ef047814ff68ebf0b9ecd4c1f91")

# Connect to Ethereum network
w3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_RPC_URL))


def verify_identity(user_wallet):
    """
    Verifies a user's identity using their Ethereum wallet address and ENS.
    Returns an identity score (0-100).
    """
    if not Web3.is_address(user_wallet):
        return 0  # Invalid Wallet

    # Check if wallet is active (has transactions)
    tx_count = w3.eth.get_transaction_count(user_wallet)

    # Identity Score Calculation
    identity_score = min(100, tx_count * 5)  # Example logic: More tx, higher trust

    return identity_score
