# Conditional Assets

This page explains how unconditional assets are transformed into **conditional assets** in Futarchy Labs, and how those assets behave before and after resolution.

It focuses on asset representation and accounting. Market structure and trade execution are documented separately.

---

## Overview

Once a condition is defined, the Gnosis Conditional Token Framework (CTF) allows unconditional assets to be **split** into conditional claims tied to the outcomes of that condition.

In Futarchy Labs, both:
- the project’s governance token, and
- the trading currency (e.g. a stablecoin)

are split into conditional assets.

These conditional assets are the building blocks used to construct markets.

---

## Conditional Claims in CTF and ERC-20 Wrapper Tokens

At the lowest level, the Conditional Token Framework represents conditional claims using the **ERC-1155** token standard.

Each ERC-1155 position corresponds to:
- a specific condition,
- a specific outcome index,
- and a quantity of collateral locked in the CTF contract.

These ERC-1155 tokens are currently not directly composable into most existing DeFi protocols, so instead of exposing ERC-1155 positions directly, conditional positions on Futarchy are wrapped into **ERC-20 tokens**, which provide:

- standard fungible token semantics,
- compatibility with AMMs and liquidity pools,
- a familiar interface for traders and integrators.

When this documentation refers to **YES_TOKEN**, **NO_TOKEN**, **YES_CURRENCY**, or **NO_CURRENCY**, it is referring to these **ERC-20 wrapper tokens**, not the underlying ERC-1155 positions.

---

## Outcome-Based Asset Types

For futarchy conditions with two outcomes (YES and NO), splitting produces the following assets:

### Token Assets

Splitting the project’s token produces:

- **YES_TOKEN** — claim on the token if the outcome is YES  
- **NO_TOKEN** — claim on the token if the outcome is NO  

### Currency Assets

Splitting the trading currency produces:

- **YES_CURRENCY** — claim on the currency if the outcome is YES  
- **NO_CURRENCY** — claim on the currency if the outcome is NO  

Each ERC-20 conditional asset wraps an ERC-1155 position corresponding to a specific outcome index.

---

## Outcome Indexing

Conditional assets are mapped directly to outcome indices of the underlying condition:

- **Outcome 0 (YES)**  
  - YES_TOKEN  
  - YES_CURRENCY  

- **Outcome 1 (NO)**  
  - NO_TOKEN  
  - NO_CURRENCY  

This mapping is fixed at condition creation time and is consistent across all futarchy markets.

---

## Splitting Assets

Splitting is the process by which unconditional ERC-20 assets are converted into conditional ERC-20 assets.

Splitting is handled by the Seer **FutarchyRouter**, which abstracts the underlying CTF operations.

When splitting:

1. An unconditional ERC-20 asset is transferred to the router.
2. The router interacts with the CTF contract to lock the collateral and mint ERC-1155 outcome positions.
3. The router mints corresponding ERC-20 wrapper tokens (YES and NO) to the user.

For example, splitting 1 unit of TOKEN results in:
- 1 YES_TOKEN
- 1 NO_TOKEN

Both claims exist simultaneously until resolution.

> At no point does the FutarchyRouter take custody of collateral outside of the Conditional Token Framework. However, it is necessary to provide allowances to the FutarchyRouter for the split to happen.

---

## Merging Assets

Merging is the inverse of splitting.

When merging:

1. A user supplies matching quantities of YES and NO ERC-20 tokens.
2. The router unwraps these into ERC-1155 positions.
3. The CTF contract merges the positions back into the original unconditional collateral.
4. The unconditional ERC-20 asset is returned to the user.

Merging is only possible when both outcome positions are provided in equal amounts, and is also performed by the FutarchyRouter.

---

## Supply and Accounting Invariants

The following invariants always hold:

- All unconditional collateral backing conditional assets is held by the CTF contract.
- For each unit of collateral split, exactly one unit of conditional claim exists per outcome.
- The sum of conditional claims equals the locked collateral.
- At most one outcome’s conditional assets will be redeemable after resolution.

These invariants are enforced mechanically by the Conditional Token Framework.

---

## Redemption After Resolution

Once a condition is resolved:

- Conditional assets corresponding to the winning outcome become redeemable for the underlying asset.
- Conditional assets corresponding to the losing outcome become worthless.

Specifically:

- If the outcome is **YES**:
  - YES_TOKEN and YES_CURRENCY are redeemable.
  - NO_TOKEN and NO_CURRENCY have zero value.

- If the outcome is **NO**:
  - NO_TOKEN and NO_CURRENCY are redeemable.
  - YES_TOKEN and YES_CURRENCY have zero value.

Redemption is handled by the FutarchyRouter contract. It unwraps the ERC-20 tokens into the underlying ERC-1155 positions and then redeems those positions directly on the CTF contract using the payout vector reported at resolution.

---

## Relationship to Futarchy Markets

In Futarchy, conditional assets are not meant to be traded directly against unconditional assets.

Instead:
- YES_TOKEN is traded against YES_CURRENCY in the YES market.
- NO_TOKEN is traded against NO_CURRENCY in the NO market.

This ensures that all trading activity remains conditional until the outcome is known.

The next section explains how these conditional assets are paired into liquidity pools to form markets.

---

## Relationship to Prediction Markets

Although Futarchy uses conditional assets primarily to compare counterfactual token prices, the same conditional assets can also be used to construct traditional prediction markets.

For example, a prediction market on proposal approval can be formed by trading **YES_CURRENCY** directly against the unconditional **CURRENCY**, where prices reflect beliefs about whether the proposal will be approved.

Importantly, futarchy does not rely on prediction markets to function. Deep liquidity in prediction-style trades is not required for futarchy signals to emerge, since futarchy compares relative prices between conditional worlds rather than estimating probabilities directly.

Because conditional assets are standard ERC-20 tokens wrapping Conditional Token Framework positions, they are **composable primitives** across applications that use the same framework.

In practice, this means that conditional assets created elsewhere — for example, prediction-market positions created on Polymarket on Polygon, or markets created via Seer on Gnosis Chain — could potentially be reused directly by a Futarchy deployment on the same chain.

In this sense, futarchy markets do not need to be the sole origin of conditional assets. Instead, futarchy can consume existing CTF-based positions as inputs, using them to evaluate governance decisions via counterfactual price comparisons.

From this perspective, futarchy can be viewed as a governance layer that operates over an existing ecosystem of conditional assets, rather than a standalone market silo.

---

## Navigation

- ⬅️ **[Protocol Overview](./README.md)**  
  Return to the top-level protocol documentation.

- ⬅️ **[Conditions and Outcomes](./conditions-and-outcomes.md)**  
  How governance decisions are represented and resolved.

- ➡️ **[Liquidity Pools](./liquidity-pools.md)**  
  How conditional assets are combined into markets and traded.
