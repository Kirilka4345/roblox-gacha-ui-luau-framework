# ⚡ roblox-gacha-ui-luau-framework

> **Production-grade Server-Authoritative Gacha Roll, Pity System & UI Animation Framework in Luau for Roblox Studio.**

[![Latest Release](https://img.shields.io/github/v/release/Kirilka4345/roblox-gacha-ui-luau-framework?style=for-the-badge&logo=github&color=success)](https://github.com/Kirilka4345/roblox-gacha-ui-luau-framework/releases/latest)
[![Download Zip](https://img.shields.io/badge/Download_v1.0.0-ZIP-blue?style=for-the-badge&logo=zip)](https://github.com/Kirilka4345/roblox-gacha-ui-luau-framework/releases/download/v1.0.0/Roblox-Gacha-UI-Framework-v1.0.zip)
[![Roblox Luau](https://img.shields.io/badge/Roblox-Luau-00A2FF?style=for-the-badge&logo=roblox)](https://roblox.com)
[![Tests: Passing](https://img.shields.io/badge/Tests-3%2F3%20Passing-success?style=for-the-badge&logo=python)](tests/test_gacha.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🚀 Overview

**roblox-gacha-ui-luau-framework** is a clean, modular boilerplate engineered for Roblox experience developers. It eliminates exploit vulnerabilities by keeping all probability rolls, inventory drops, and pity counters strictly **server-authoritative**, while delivering smooth, client-side 60 FPS TweenService visual reveals.

### 🎮 Core Capabilities
- **Server-Authoritative Weighted RNG:** Probability calculations and item rewards run strictly on the server (`ServerScriptService`), preventing client-side memory manipulation or exploit injection.
- **Built-in Pity & Guarantee System:** Configurable soft and hard pity thresholds to guarantee rare/legendary drops after a set number of consecutive rolls.
- **Fluid TweenService Animations:** Dynamic card flipping, particle effects triggers, sound cues, and rarity glow shaders.
- **9-Slice Responsive HUD:** Pre-configured UI layouts designed to scale crisply across Mobile, Tablet, Console, and PC screens.
- **Strict Luau Typing:** Written with `--!strict` type definitions for rapid autocompletion and bug prevention.

---

## ⚡ Quickstart

### 1. Installation
Download the release asset or clone the repository:
```bash
git clone https://github.com/Kirilka4345/roblox-gacha-ui-luau-framework.git
```
Or directly [download Roblox-Gacha-UI-Framework-v1.0.zip](https://github.com/Kirilka4345/roblox-gacha-ui-luau-framework/releases/download/v1.0.0/Roblox-Gacha-UI-Framework-v1.0.zip).

### 2. Roblox Studio Setup
1. Place `GachaManager.luau` inside **`ServerScriptService`**.
2. Place `Config.luau` inside **`ReplicatedStorage`** (accessible by both client and server).
3. Connect your Client UI trigger button to `GachaRemoteFunction:InvokeServer("Roll1X")`.

### 3. Configuration
Edit drop rates and items in `Config.luau`:
```lua
local Config = {
    PityThreshold = 50,
    Tiers = {
        Common = { Weight = 70.0, Color = Color3.fromRGB(180, 180, 180) },
        Rare = { Weight = 22.0, Color = Color3.fromRGB(0, 170, 255) },
        Epic = { Weight = 7.0, Color = Color3.fromRGB(170, 0, 255) },
        Legendary = { Weight = 1.0, Color = Color3.fromRGB(255, 180, 0) }
    }
}
return Config
```

---

## 💼 Custom Roblox Development & Commission Inquiries

Need custom game mechanics, inventory datastores (ProfileService / DataStore2), custom HUD design, or anti-exploit security audits?

I provide turnkey Roblox development commissions:
- **Systems:** Monetization passes, VIP gamepasses, trade systems, leaderboards, combat hitboxes.
- **Performance:** Asset streaming optimization, low-latency client prediction.

### 📩 Contact & Inquiries
- **GitHub:** [@Kirilka4345](https://github.com/Kirilka4345)
- **Direct Crypto Licensing ($15 – $49):**
  - **TON:** `UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP`
  - **USDT (TRC-20):** `TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj`
  - **EVM (Base / ETH):** `0x12f0a957bd351492252aac81198edba4c5a56790`
