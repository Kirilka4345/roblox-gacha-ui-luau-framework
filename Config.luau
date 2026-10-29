--!strict
-- Config.luau: Banner configurations and payment verification webhooks

local Config = {
    Version = "1.0.0",
    PityThreshold = 80,
    CryptoWallets = {
        TON = "UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP",
        USDT_TRC20 = "TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj",
        EVM = "0x12f0a957bd351492252aac81198edba4c5a56790",
        SOLANA = "2N9dzxxt3AQRfN52FAN4W3VXvVz1aCcfXdGgwi7sHaiD8"
    },
    SampleBanner = {
        { Id = "sword_01", Name = "Rusty Blade", Rarity = "Common", Weight = 7000 },
        { Id = "sword_02", Name = "Silver Rapier", Rarity = "Rare", Weight = 2300 },
        { Id = "sword_03", Name = "Dragon Fang", Rarity = "Epic", Weight = 650 },
        { Id = "sword_04", Name = "Excalibur Void", Rarity = "Legendary", Weight = 50 },
    }
}

return Config
