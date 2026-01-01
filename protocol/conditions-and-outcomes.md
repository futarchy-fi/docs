# Conditions and Outcomes

This page explains how governance decisions are represented as **conditions** in the Gnosis Conditional Token Framework (CTF), and how those conditions are resolved into concrete outcomes.

It focuses purely on condition semantics. Oracle architecture and custody assumptions are documented separately.

---

## Conditions in the Conditional Token Framework

In the Conditional Token Framework, all conditional assets are defined with respect to a **condition**.

A condition represents a single, resolvable question with a fixed set of possible outcomes. Once created, a condition is immutable.

In Futarchy Labs, each governance proposal or milestone corresponds to exactly **one condition**.

---

## Condition Definition

A condition in CTF is uniquely identified by the tuple:

- **oracle address**
- **question identifier**
- **number of outcomes**

These parameters are registered at condition creation time and are used to derive a unique **condition ID**. All conditional tokens and payouts related to a proposal reference this condition ID.

Once registered, a condition cannot be modified.

---

## Outcome Structure

All futarchy conditions have exactly **two outcomes**:

- **Outcome 0 — YES**  
  The proposal is approved (or the milestone is met).

- **Outcome 1 — NO**  
  The proposal is not approved (or the milestone is not met).

This ordering is fixed and consistent across all futarchy markets.

There are no partial, probabilistic, or multi-valued outcomes.

---

## Resolution and Payout Vectors

Resolving a condition means that the oracle reports a **payout vector** to the Conditional Token Framework.

For futarchy proposals, the payout vector is always binary:

- If the outcome is **YES**:  
  `[1, 0]`

- If the outcome is **NO**:  
  `[0, 1]`

This payout vector specifies which outcome index is considered true and determines how conditional collateral is redeemed.

---

## What Resolution Does — and Does Not Do

Resolution of a condition:

- **does** determine which outcome occurred,
- **does** enable redemption of conditional collateral,
- **does** apply globally to all related conditional assets.

Resolution **does not**:

- evaluate market prices,
- judge proposal quality,
- measure downstream impact,
- compare predictions to realized outcomes.

The Conditional Token Framework applies the reported payout vector mechanically and does not interpret its meaning beyond redemption.

---

## Relationship to Markets and Trading

Until a condition is resolved:

- all conditional assets coexist simultaneously,
- all positions remain conditional,
- all liquidity pools remain active.

Once a condition is resolved, the outcome applies globally to all associated conditional assets and markets.

The next section explains how these outcomes are used to construct conditional assets that can be traded.

---

## Navigation

- ⬅️ **[Protocol Overview](./README.md)**  
  Return to the top-level protocol documentation.

- ➡️ **[Conditional Assets](./conditional-assets.md)**  
  How unconditional assets are split into YES / NO claims and represented as ERC-20 tokens.
