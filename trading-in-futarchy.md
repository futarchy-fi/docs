# Trading in Futarchy Markets

This page explains how trading works in Futarchy Labs from a trader’s perspective.

It focuses on **what positions you can take**, **what assets you are trading**, and **how those positions behave** when a governance decision is made.

For a deeper explanation of the on-chain implementation, see the **[Futarchy Protocol](./protocol/README.md)**.

---

## Overview

Futarchy Labs uses **conditional token markets** built on the
[Gnosis Conditional Token Framework (CTF)](https://conditional-tokens.readthedocs.io/en/latest/index.html), the battle tested framework used by Polymarket and others.

Rather than trading a token unconditionally, participants trade **conditional exposure** to the token, depending on whether a proposal is approved or rejected.

For each proposal, trading is organized around two markets:

- the **YES market** — exposure conditional on approval
- the **NO market** — exposure conditional on rejection

In practice these two markets are implemented by **liquidity pools** composed of conditional tokens.

---

## The Assets You Trade

For each proposal, trading involves four conditional assets:

- **YES_TOKEN** — the project’s token, conditional on proposal approval. This can be redeemed back to the token if the proposal is approved.
- **NO_TOKEN** — the project’s token, conditional on proposal rejection. This can be redeemed back to the token if the proposal is rejected.

- **YES_CURRENCY** — the trading currency, conditional on proposal approval. This can be redeemed back to currency if the proposal is approved.
- **NO_CURRENCY** — the trading currency, conditional on proposal rejection. This can be redeemed back to currency if the proposal is rejected.

These assets are created using the Conditional Token Framework.

You do not need to interact with these tokens directly — the trading interface handles this — but understanding them helps clarify what positions you are taking.

---

## Markets as Liquidity Pools

Each proposal has two liquidity pools:

- **YES pool**: `YES_TOKEN / YES_CURRENCY`
- **NO pool**: `NO_TOKEN / NO_CURRENCY`

Trading in a pool corresponds to taking a position in the associated conditional world.

When you trade:
- you exchange conditional currency for conditional token exposure (or vice versa),
- using standard AMM-style mechanics,
- with all positions remaining conditional until the proposal outcome is known.

## What Happens Under the Hood

Suppose you have some currency (e.g. USDC) and want to buy tokens, but only if a proposal is approved.

Under the hood, your currency is first split into **YES_CURRENCY** and **NO_CURRENCY**, representing collateral in each of the two possible worlds.

You then use the **YES_CURRENCY** to trade in the YES pool, exchanging it for **YES_TOKEN**.

At the same time, you keep the **NO_CURRENCY**. This is important: if the proposal is not approved, you can redeem the NO_CURRENCY back into regular currency, and the trade is effectively reverted.

If the proposal is approved, you instead end up with **YES_TOKEN**, which can be redeemed into the project’s token. In that case, the conditional purchase becomes a real token purchase.

## Further Reading

- **[How Futarchy Works](./how-futarchy-works.md)**  
  The core idea behind futarchy and how conditional markets produce a governance signal.

- **[Market Implementation](./market-implementation.md)**  
  How conditional tokens, liquidity pools, and the Gnosis Conditional Token Framework are used on-chain.

- **[Using Futarchy in Practice](./using-futarchy-in-practice.md)**  
  How DAOs and teams use futarchy signals in real governance decisions.
