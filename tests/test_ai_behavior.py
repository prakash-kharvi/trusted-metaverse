#This file tests the AI model for detecting behavioral anomalies.
import unittest
from src.behavior_analysis import analyze_behavior

class TestAIBehavior(unittest.TestCase):

    def test_normal_behavior(self):
        """Test with a normal user behavior pattern."""
        wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
        score = analyze_behavior(wallet)
        self.assertGreaterEqual(score, 50)  # Normal users should have a behavior score >= 50

    def test_anomalous_behavior(self):
        """Test for an anomalous behavior scenario."""
        wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
        score = analyze_behavior(wallet)
        self.assertLessEqual(score, 50)  # Anomalous behavior should be detected

if __name__ == "__main__":
    unittest.main()
