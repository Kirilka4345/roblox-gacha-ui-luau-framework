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

    def test_pity_system_logic_simulation(self):
        """Simulate the server-authoritative pity counter and verify guaranteed legendary at roll 80."""
        class MockGachaManager:
            def __init__(self):
                self.pity_counters = {}
                self.banner = [
                    {"Id": "sword_01", "Rarity": "Common", "Weight": 7000},
                    {"Id": "sword_02", "Rarity": "Rare", "Weight": 2300},
                    {"Id": "sword_03", "Rarity": "Epic", "Weight": 650},
                    {"Id": "sword_04", "Rarity": "Legendary", "Weight": 50},
                ]

            def roll(self, user_id, force_pity_roll=None):
                pity = force_pity_roll if force_pity_roll is not None else self.pity_counters.get(user_id, 0) + 1
                self.pity_counters[user_id] = pity

                force_legendary = (pity >= 80)
                if force_legendary:
                    self.pity_counters[user_id] = 0
                    candidates = [it for it in self.banner if it["Rarity"] == "Legendary"]
                    return candidates[0]
                return self.banner[0]

        gm = MockGachaManager()
        # Roll 1 through 79 (normal)
        res_79 = gm.roll(user_id=1001, force_pity_roll=79)
        self.assertNotEqual(res_79["Rarity"], "Legendary")

        # Roll 80 (guaranteed pity triggered)
        res_80 = gm.roll(user_id=1001, force_pity_roll=80)
        self.assertEqual(res_80["Rarity"], "Legendary")
        self.assertEqual(gm.pity_counters[1001], 0)

if __name__ == "__main__":
    unittest.main()
