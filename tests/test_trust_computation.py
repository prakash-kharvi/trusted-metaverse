#This file tests the trust score computation logic.
import unittest
from src.compute_trust import compute_trust_score


class TestTrustComputation(unittest.TestCase):

    def test_high_trust_score(self):
        """Test case for a high trust score scenario."""
        identity, assets, behavior, context = 95, 85, 80, 75
        trust_score, status = compute_trust_score(identity, assets, behavior, context)
        self.assertEqual(status, "Verified")
        self.assertGreaterEqual(trust_score, 80)

    def test_mfa_required(self):
        """Test case where the user requires multi-factor authentication."""
        identity, assets, behavior, context = 75, 70, 65, 60
        trust_score, status = compute_trust_score(identity, assets, behavior, context)
        self.assertEqual(status, "Needs MFA")
        self.assertTrue(70 <= trust_score < 80)

    def test_failed_verification(self):
        """Test case for low trust score leading to verification failure."""
        identity, assets, behavior, context = 50, 45, 40, 35
        trust_score, status = compute_trust_score(identity, assets, behavior, context)
        self.assertEqual(status, "Failed")
        self.assertLess(trust_score, 70)


if __name__ == "__main__":
    unittest.main()
