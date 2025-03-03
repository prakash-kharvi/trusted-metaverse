# Blockchain Configuration. This configuration is for illustration and MUST be used as part of instantiation of the design science research
BLOCKCHAIN_NETWORK = "Ethereum"  # Supported: Ethereum, Polygon, Solana
BLOCKCHAIN_RPC_URL = os.getenv("BLOCKCHAIN_RPC_URL", "https://mainnet.infura.io/v3/2b550ef047814ff68ebf0b9ecd4c1f91")

# Smart Contract Addresses for NFT Verification
NFT_CONTRACTS = {
    "Decentraland": "0x123456789abcdef",
    "The Sandbox": "0xabcdef123456789",
    "Somnium Space": "0x987654321abcdef"
}

# Web3 Wallet Authentication
ENS_PROVIDER = "https://mainnet.infura.io/v3/2b550ef047814ff68ebf0b9ecd4c1f91"

# Token Standards for Asset Ownership Verification
TOKEN_STANDARDS = ["ERC-721", "ERC-1155"]

# Ethereum Gas Fees Optimization
GAS_LIMIT = 3000000
GAS_PRICE = "fast"

# Security Settings
ENABLE_SMART_CONTRACT_VALIDATION = True  # Ensures NFT ownership is verified via smart contract calls
