# Proposal Lifecycle

This page describes the end-to-end lifecycle of a futarchy proposal in Futarchy Labs, from creation to resolution and settlement.

It provides a chronological overview of what happens on-chain and how this connects to governance processes. Detailed mechanics are documented elsewhere and are linked throughout.

---

## Overview

At a high level, a futarchy proposal goes through the following stages:

1. Proposal creation
2. Condition and oracle setup
3. Market initialization
4. Trading phase
5. Governance decision
6. Condition resolution
7. Settlement and redemption
8. Post-proposal state

This page focuses on **what happens**, not on governance norms or trading strategies.

---

## 1. Proposal Creation

A futarchy proposal is created on-chain as a **FutarchyProposal** contract.

Anyone can create a proposal permissionlessly by interacting with the **Seer FutarchyFactory** contract. Creating a proposal does not require DAO approval.

However, not all proposals are guaranteed to appear in the Futarchy Labs user interface. The UI may apply additional curation or filtering rules. Alternative user interfaces or direct contract interaction can always be used.

A proposal contract typically contains:
- references to the underlying project token,
- references to the trading currency,
- parameters required to initialize markets and conditions,
- identifiers used to link to oracle questions and metadata.

Off-chain governance processes (forums, Snapshot, DAO UIs) are **not required** to create a proposal, but are commonly used in parallel.

[EXACT FIELDS STORED IN `FutarchyProposal` MAY BE DESCRIBED HERE OR LINKED TO CONTRACT SOURCE]

---

## 2. Condition and Oracle Setup

At proposal creation time, a **condition** is registered in the Gnosis Conditional Token Framework.

This condition:
- has exactly two outcomes (YES / NO),
- is associated with a specific oracle address,
- is linked to a reality.eth question that asks whether the proposal was approved.

Condition creation is handled by the Seer FutarchyFactory.

The oracle used by default is the **FutarchyRealityProxy**, which integrates with reality.eth and Kleros. Custom futarchy deployments could, in principle, use different oracle contracts.

[DETAILS ABOUT REALITY.ETH QUESTION FORMAT AND BOND PARAMETERS — TBD]

See **[Custody and Oracles](./market-implementation/custody-and-oracles.md)** for trust assumptions.

---

## 3. Market Initialization

After the proposal and condition are created, **liquidity pools are initialized**.

For each proposal, two primary markets are created:
- a YES market (`YES_TOKEN / YES_CURRENCY`)
- a NO market (`NO_TOKEN / NO_CURRENCY`)

Additional pools may also be initialized for indexing or integration purposes (for example, to support certain aggregators or solvers).

Market initialization does not require liquidity to be immediately provided.

Which AMM is used depends on the deployment:
- On Gnosis Chain, pools are typically created on Swapr V3.
- On Ethereum Mainnet, pools are typically created on Uniswap V3.

Pool parameters are configurable per deployment.

---

## 4. Liquidity Provision

Liquidity provision is permissionless at the protocol level: **anyone can provide liquidity** to any futarchy pool.

In practice, during early deployments, liquidity is often provided by the DAO sponsoring or approving a futarchy pilot.

Commonly, this works as follows:
- the DAO allocates project tokens and currency,
- funds are sent to a multisig,
- the multisig provides liquidity to the relevant conditional pools.

[PLANS FOR A DEDICATED FUTARCHY LIQUIDITY CONTRACT MAY BE DESCRIBED HERE]

See **[Liquidity Pools](./market-implementation/liquidity-pools.md)** for details.

---

## 5. Trading Phase

Once markets exist, trading is permissionless and continuous.

Key properties:
- there is **no fixed trading window**,
- trading does **not stop when governance voting begins**,
- markets may exist before a proposal is formally submitted to a DAO vote.

Trading can occur even if only one of the two pools has liquidity.

During this phase:
- participants trade conditional assets,
- prices emerge for each counterfactual world,
- futarchy signals are derived from relative prices.

Importantly, proposal text or intent may evolve off-chain during this period.

Whether such changes affect settlement depends entirely on how the oracle question is formulated.

[THIS IS A CRITICAL POINT — READERS SHOULD VERIFY THAT PROPOSAL CHANGES DO NOT INVALIDATE THE ORACLE QUESTION]

---

## 6. Governance Decision

Futarchy does not replace governance by default.

By default, futarchy is **advisory**:
- governance processes remain unchanged,
- decision makers may consider futarchy market prices when voting.

Who makes the final decision depends on the DAO:
- tokenholder vote,
- multisig,
- council,
- or other mechanism.

Each proposal has a deadline.  
If the proposal is not approved by the deadline, the outcome is treated as **NO**.

Some deployments may use explicit thresholds or rules to interpret futarchy signals.

[DETAILS ABOUT THRESHOLD-BASED RECOMMENDATIONS MAY BE ADDED HERE]

---

## 7. Condition Resolution

Once the governance decision is known, the outcome must be reported to reality.eth.

At present:
- **anyone** can submit an answer,
- the answer may be disputed,
- disputes are resolved via Kleros.

Once finalized, the FutarchyRealityProxy reports the outcome to the Conditional Token Framework as a payout vector:
- YES → `[1, 0]`
- NO → `[0, 1]`

If no valid resolution occurs by the deadline, the condition resolves to **NO**.

[DETAILS ABOUT WHO TYPICALLY REPORTS AND HOW INCENTIVES WORK — TBD]

---

## 8. Settlement and Redemption

After condition resolution:

- conditional assets corresponding to the winning outcome become redeemable,
- conditional assets corresponding to the losing outcome become worthless,
- liquidity pools effectively collapse into redeemable assets.

Redemption is handled via the FutarchyRouter, which:
- unwraps ERC-20 conditional assets,
- redeems underlying ERC-1155 positions,
- returns unconditional assets to users.

Trading naturally ceases once assets resolve.

---

## 9. After the Proposal

After settlement:
- proposal contracts remain on-chain as historical records,
- price data may be indexed for analytics or governance learning,
- similar proposals may be re-created as new futarchy proposals with new conditions.

Re-running a proposal always creates a **new condition**, even if the proposal text is similar.

---

## Navigation

- ⬅️ **[Market Implementation Overview](./market-implementation/index.md)**
- ⬅️ **[Liquidity Pools](./market-implementation/liquidity-pools.md)**
- ➡️ **[Using Futarchy in Practice](./using-futarchy-in-practice.md)**  
  Governance norms, thresholds, and design choices.
