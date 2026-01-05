# Liquidity Pools

This page explains how conditional assets are combined into **liquidity pools** to form tradable markets in Futarchy Labs.

It focuses on pool structure and mechanics. Asset creation and accounting are documented separately.

---

## Overview

In Futarchy Labs, what users experience as “markets” are implemented as **liquidity pools** over conditional assets.

Each pool allows participants to trade conditional exposure using standard automated market maker (AMM) mechanics, while remaining fully conditional until the underlying governance outcome is known.

---

## Pool Structure

For each futarchy condition, exactly **two liquidity pools** are created:

- **YES Pool**  
  Pair: `YES_TOKEN / YES_CURRENCY`

- **NO Pool**  
  Pair: `NO_TOKEN / NO_CURRENCY`

Each pool is scoped to a single outcome of the condition.

This structure ensures that:
- all assets in a pool correspond to the same outcome,
- trades do not mix exposure across outcomes,
- all market activity remains conditional until resolution.

---

## Why Two Pools (Not One)

Futarchy uses two separate pools rather than a single multi-asset pool because each outcome represents a **distinct counterfactual world**.

The YES pool represents the world in which the proposal is approved.  
The NO pool represents the world in which the proposal is rejected.

Keeping these worlds separate allows prices in each pool to independently reflect the market’s assessment of token value under each outcome.

Futarchy signals are derived by **comparing prices across these pools**, not by estimating outcome probabilities.

---

## Assets in a Pool

Each pool contains exactly two ERC-20 assets:

- one conditional token asset (`YES_TOKEN` or `NO_TOKEN`),
- one conditional currency asset (`YES_CURRENCY` or `NO_CURRENCY`).

No unconditional assets appear in the pools.

As a result:
- all liquidity remains conditional,
- all positions are outcome-scoped,
- settlement logic remains simple and global.

---

## Trading Against a Pool

When a participant trades against a pool:

- they exchange conditional currency for conditional token exposure, or vice versa,
- using standard AMM swap logic,
- without interacting directly with ERC-1155 positions.

From the pool’s perspective:
- prices adjust based on supply and demand,
- liquidity remains locked until resolution,
- no special handling is required before the outcome is known.

---

## Liquidity Provision

Liquidity providers (LPs) supply conditional asset pairs to pools:

- YES pool LPs provide `YES_TOKEN` and `YES_CURRENCY`,
- NO pool LPs provide `NO_TOKEN` and `NO_CURRENCY`.

In return, LPs receive pool shares and earn trading fees, subject to the same conditional structure as traders.

LP positions remain conditional until resolution.

---

## Effect of Resolution on Pools

When the underlying condition is resolved:

- only one of the two pools corresponds to the winning outcome,
- assets in the winning pool become redeemable,
- assets in the losing pool become worthless.

At that point:
- pool balances collapse to the winning assets,
- LP and trader positions resolve mechanically via redemption,
- no further trading is required.

No price comparison or oracle intervention is needed at the pool level.

---

## Relationship to Futarchy Signals

Liquidity pools provide the price signals used in futarchy.

Specifically:
- the YES pool price reflects token value *if the proposal is approved*,
- the NO pool price reflects token value *if the proposal is rejected*.

Comparing these prices yields the futarchy signal used to evaluate governance decisions.

Importantly:
- these prices emerge from real trading activity,
- they do not depend on prediction-market probability estimates,
- they remain meaningful even if one pool is thinly traded.

---

## Navigation

- ⬆️ **[Protocol Overview](./README.md)**  
  Return to the top-level protocol documentation.

- ⬅️ **[Conditional Assets](./conditional-assets.md)**  
  How conditional ERC-20 assets are created and redeemed.

- ➡️ **[Proposal Lifecycle](./proposal-lifecycle.md)**  
  How proposals are created, markets are initialized, and outcomes are resolved.
