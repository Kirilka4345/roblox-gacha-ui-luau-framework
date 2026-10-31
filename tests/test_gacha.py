# -*- coding: utf-8 -*-
"""Unit tests for Roblox Modern Gacha UI & Luau Server Framework."""
import unittest
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

class TestRobloxGachaFramework(unittest.TestCase):
    def test_config_wallets_and_pity(self):
        """Verify Config.luau contains required pity threshold and valid crypto payout addresses."""
        config_path = BASE_DIR / "Config.luau"
        self.assertTrue(config_path.exists())
        content = config_path.read_text(encoding="utf-8")

        # Pity Threshold
        self.assertIn("PityThreshold = 80", content)

        # Wallets
        self.assertIn("UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP", content)
        self.assertIn("TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj", content)
        self.assertIn("0x12f0a957bd351492252aac81198edba4c5a56790", content)
        self.assertIn("2N9dzxxt3AQRfN52FAN4W3VXvVz1aCcfXdGgwi7sHaiD8", content)

    def test_sample_banner_weights(self):
        """Verify sample banner items and weight distribution."""
        content = (BASE_DIR / "Config.luau").read_text(encoding="utf-8")
        weights = [int(w) for w in re.findall(r"Weight\s*=\s*(\d+)", content)]
        self.assertGreaterEqual(len(weights), 4)
        total_weight = sum(weights)
        self.assertEqual(total_weight, 10000)  # Standard 10,000 basis points (100.0%)

if __name__ == "__main__":
    unittest.main()
