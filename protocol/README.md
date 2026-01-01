# Futarchy Protocol

This section documents the **on-chain protocol architecture** used by Futarchy Labs.

It describes how futarchy proposals are represented, how conditions are resolved, how conditional assets are created, and how markets are formed and settled. These pages are intended for readers who want to understand the protocol’s mechanics and trust assumptions.

You do not need to read this section to trade or participate in governance, but it is essential for auditors, integrators, and DAO operators.

---

## Overview

At a high level, the Futarchy protocol consists of:

- custody of collateral via the Gnosis Conditional Token Framework (CTF),
- resolution of governance outcomes via oracles,
- creation of conditional assets representing counterfactual outcomes,
- formation of markets over those assets using AMMs,
- and an explicit lifecycle that ties proposals, markets, and settlement together.

Each of these components is documented in detail below.

---

## Documentation Map

### Core Protocol Components

- **[Custody and Oracles](./custody-and-oracles.md)**  
  Collateral custody, oracle requirements, Seer integration, reality.eth, and Kleros.

- **[Conditions and Outcomes](./conditions-and-outcomes.md)**  
  How governance decisions are represented as resolvable conditions.

- **[Conditional Assets](./conditional-assets.md)**  
  ERC-1155 positions, ERC-20 wrappers, splitting, merging, and redemption.

- **[Liquidity Pools](./liquidity-pools.md)**  
  Market construction and trade execution mechanics.

---

### Protocol Flows and Operations

- **[Proposal Lifecycle](./proposal-lifecycle.md)**  
  The end-to-end protocol flow from proposal creation through resolution and settlement.

- **[Liquidity Management](./liquidity-management.md)**  
  How liquidity is provided and managed for futarchy markets, including current operational practices and planned mechanisms.

---

## How to Read This Section

- **Protocol engineers and auditors** should read all pages in order.
- **Advanced traders and liquidity providers** may focus on Conditional Assets and Liquidity Pools.
- **DAO operators** may want to read Proposal Lifecycle alongside Custody and Oracles to understand trust boundaries.

For conceptual background, see:
- **[How Futarchy Works](../how-futarchy-works.md)**

For trading behavior, see:
- **[Trading in Futarchy Markets](../trading-in-futarchy.md)**

For governance norms and interpretation of signals, see:
- **[Using Futarchy in Practice](../using-futarchy-in-practice.md)**
