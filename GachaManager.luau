--!strict
-- GachaManager.luau: Server-authoritative drop-rates, pity counter and secure roll logic

local GachaManager = {}
GachaManager.__index = GachaManager

export type DropItem = {
    Id: string,
    Name: string,
    Rarity: "Common" | "Rare" | "Epic" | "Legendary",
    Weight: number,
}

local BASE_WEIGHTS = {
    Common = 7000,   -- 70.0%
    Rare = 2300,     -- 23.0%
    Epic = 650,      -- 6.5%
    Legendary = 50,  -- 0.5%
}

function GachaManager.new()
    local self = setmetatable({}, GachaManager)
    self.PityCounters = {}
    return self
end

function GachaManager:Roll(playerUserId: number, bannerPool: {DropItem}): DropItem
    local pity = self.PityCounters[playerUserId] or 0
    pity += 1
    self.PityCounters[playerUserId] = pity

    -- Guaranteed Legendary at 80 pity
    local forceLegendary = (pity >= 80)
    if forceLegendary then
        self.PityCounters[playerUserId] = 0
    end

    local candidatePool = {}
    for _, item in ipairs(bannerPool) do
        if forceLegendary then
            if item.Rarity == "Legendary" then
                table.insert(candidatePool, item)
            end
        else
            table.insert(candidatePool, item)
        end
    end

    local totalWeight = 0
    for _, item in ipairs(candidatePool) do
        totalWeight += item.Weight or BASE_WEIGHTS[item.Rarity] or 100
    end

    local rng = math.random(1, totalWeight)
    local current = 0
    for _, item in ipairs(candidatePool) do
        current += item.Weight or BASE_WEIGHTS[item.Rarity] or 100
        if rng <= current then
            if item.Rarity == "Legendary" then
                self.PityCounters[playerUserId] = 0
            end
            return item
        end
    end

    return candidatePool[1]
end

return GachaManager
