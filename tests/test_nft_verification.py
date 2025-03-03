#This file tests the NFT ownership verification by calling OpenSea API.
import unittest
from src.asset_verification import verify_nft_ownership

class TestNFTVerification(unittest.TestCase):

    def test_valid_nft_ownership(self):
        """Test with a wallet that owns relevant NFTs."""
        wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Example wallet
        virtual_world = "Decentraland"
        score = verify_nft_ownership(wallet, virtual_world)
        self.assertGreater(score, 0)  # User should have NFTs

    def test_no_nft_ownership(self):
        """Test with a wallet that does not own relevant NFTs."""
        wallet = "0x0000000000000000000000000000000000000000"  # Example empty wallet
        virtual_world = "Decentraland"
        score = verify_nft_ownership(wallet, virtual_world)
        self.assertEqual(score, 0)  # No NFTs should return a 0 score

if __name__ == "__main__":
    unittest.main()
