# Market Implementation

This section documents how Futarchy Labs markets are implemented on-chain.

It covers the concrete mechanics behind collateral custody, oracle resolution, conditional tokens, and liquidity pools. These pages are intended for readers who want to understand the protocol’s trust assumptions and execution details.

You do not need this level of detail to trade or participate in governance.

---

## Overview

Futarchy Labs builds on existing, battle-tested infrastructure rather than introducing new custody or oracle mechanisms.

At a high level:

- All collateral is held by the **Gnosis Conditional Token Framework (CTF)**.
- Governance decisions are represented as **binary conditions** (YES / NO).
- Conditions are resolved via **reality.eth**, with disputes handled by **Kleros**.
- Conditional claims are represented internally as **ERC-1155 positions** and exposed to users as **ERC-20 wrapper tokens**.
- Markets are implemented as **liquidity pools** over these conditional ERC-20 assets.

Each of these components is documented in detail in the pages below.

---

## Architecture Components

- **Collateral custody and oracle resolution**  
  Where funds are held, who is authorized to resolve outcomes, and how disputes are handled.

- **Conditions and outcomes**  
  How governance decisions are modeled as CTF conditions, including outcome indexing and payout vectors.

- **Conditional assets**  
  How unconditional assets are split into YES / NO claims, how ERC-1155 positions are wrapped as ERC-20 tokens, and how splitting and merging work.

- **Liquidity pools**  
  How conditional assets are paired into pools, how trades are executed, and how markets remain conditional until resolution.

---

## Documentation Map

- **[Custody and Oracles](./custody-and-oracles.md)**  
  Collateral custody, oracle requirements, Seer integration, reality.eth, and Kleros.

- **[Conditions and Outcomes](./conditions-and-outcomes.md)**  
  Condition definitions, outcome structure, and resolution semantics.

- **[Conditional Assets](./conditional-assets.md)**  
  ERC-1155 positions, ERC-20 wrappers, splitting, merging, and redemption.

- **[Liquidity Pools](./liquidity-pools.md)**  
  Market construction and trade execution mechanics.

---

## How to Read This Section

- **Protocol engineers and auditors** should read all pages in order.
- **Advanced traders and liquidity providers** may want to focus on *Conditional Assets* and *Liquidity Pools*.
- **Governance designers** may only need *Custody and Oracles* to understand trust boundaries.

For conceptual background and economic intuition, see:
- **[How Futarchy Works](../how-futarchy-works.md)**
- **[Trading in Futarchy Markets](../trading-in-futarchy.md)**

For governance usage patterns, see:
- **[Using Futarchy in Practice](../using-futarchy-in-practice.md)**

