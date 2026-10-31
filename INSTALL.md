# Server integration

Create ModuleScripts named `GachaManager` and `Config` in ServerScriptService and paste the corresponding Luau sources. A server Script can then use:

```lua
local ServerScriptService = game:GetService("ServerScriptService")
local GachaManager = require(ServerScriptService.GachaManager)
local Config = require(ServerScriptService.Config)
local manager = GachaManager.new()
-- After validating a real player and the cost of the roll:
-- local item = manager:Roll(player.UserId, Config.SampleBanner)
```

Pity is stored only in memory and currently hard-coded to 80 in the manager. Config.PityThreshold is illustrative, not consumed by the module.
Supply a non-empty pool with positive integer weights and at least one Legendary item. Invalid pools are not currently validated.
No RemoteFunction, UI, persistence, currency charging or inventory awarding is supplied. Implement these server-side and test in Studio before deployment.
The Python suite checks source structure only; it does not execute this snippet or the Luau module.
