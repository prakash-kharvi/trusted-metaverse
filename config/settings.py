#This configuration is for illustration and MUST be used as part of instantiation of the design science research. The database configuration mentioned depends on the platform infrastructure
import os

# General App Configuration
APP_NAME = "Trust Score Evaluation System"
APP_VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:password@localhost:5432/trustdb")

# Redis Cache Configuration
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Blockchain Provider (Infura, Alchemy, QuickNode, etc.)
BLOCKCHAIN_PROVIDER = os.getenv("BLOCKCHAIN_PROVIDER", "https://mainnet.infura.io/v3/2b550ef047814ff68ebf0b9ecd4c1f91")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Allowed Virtual Worlds for Migration
ALLOWED_VIRTUAL_WORLDS = ["Decentraland", "The Sandbox", "Somnium Space"]

# Trust Score Thresholds
TRUST_SCORE_PASS = 80  # Users above this score are verified
TRUST_SCORE_MFA = 70   # Users between 70-80% require Multi-Factor Authentication (MFA)
TRUST_SCORE_FAIL = 60  # Users below this score fail verification
