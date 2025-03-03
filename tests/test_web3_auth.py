#This file tests the Web3 authentication and Ethereum wallet verification.
import unittest
from src.identity_verification import verify_identity

class TestWeb3Auth(unittest.TestCase):

    def test_valid_wallet(self):
        """Test with a valid Ethereum wallet address."""
        valid_wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Example wallet
        score = verify_identity(valid_wallet)
        self.assertGreater(score, 0)  # Score should be non-zero for valid wallets

    def test_invalid_wallet(self):
        """Test with an invalid Ethereum wallet address."""
        invalid_wallet = "0x123InvalidWalletAddress"
        score = verify_identity(invalid_wallet)
        self.assertEqual(score, 0)  # Invalid wallets should return 0 trust score

if __name__ == "__main__":
    unittest.main()
