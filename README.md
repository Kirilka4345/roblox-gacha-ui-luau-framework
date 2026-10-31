# Luau Weighted Loot & Pity Starter

A compact Luau module for weighted item selection and in-memory pity counters.

**Status: development starter / prototype.** Read the scope before integrating.

## Included

- Selects from a weighted item pool.
- Tracks per-user pity and forces a Legendary candidate at roll 80.

## Scope and limitations

- No client UI, animations, RemoteFunction handlers, persistence or payment integration.
- Call only from a server script; validate requests, ownership, currency and rate limits in your game.
- Python checks inspect files and simulate logic; they do not execute Luau. Studio runtime validation remains required.

## Quick start

See [INSTALL.md](INSTALL.md) for server-side ModuleScript setup.

## Validation

```sh
python -m unittest discover -s tests -v
```

Python structural checks are not runtime tests of GachaManager.luau.

## Repository map

- `GachaManager.luau` — implementation.
- `tests/` — current checks and regression tests.
- [CHANGELOG.md](CHANGELOG.md) — changes and verification limits.
- [CONTRIBUTING.md](CONTRIBUTING.md) — issue and change guidelines.

## Visual assets

For corresponding 2D icons, rarity slots and 3D loot models, see the asset pack on [itch.io](https://kirilka4345.itch.io/gacha-ui-kit-complete-roblox-slots-buttons-icons-vfx-luau-roll-system) (free sampler available at [gacha-loot-free-sampler](https://kirilka4345.itch.io/gacha-loot-free-sampler-6-icons-3-slots-2-vfx-for-roblox)).

## Downloads and usage terms

[Repository releases](https://github.com/Kirilka4345/roblox-gacha-ui-luau-framework/releases) contain historical snapshots; use the current source for the documented fixes.
No LICENSE file is present. Earlier MIT badges and commercial-license claims did not establish usable license terms. License terms require clarification before redistribution.

## Questions

For reproducible technical issues, use [GitHub Issues](https://github.com/Kirilka4345/roblox-gacha-ui-luau-framework/issues). Include the commit, runtime version, expected result and minimal reproduction. Never include tokens, cookies or customer data.
