# Custody and Oracles

This page explains how collateral custody and outcome resolution work in Futarchy Labs.

It describes where funds are held, how conditions are resolved, and which components are trusted to report governance outcomes. These are the core trust assumptions of the system.

---

## Collateral Custody

All collateral used in Futarchy Labs markets is held by the **Gnosis Conditional Token Framework (CTF)** contract.

When assets are split into conditional positions, the underlying collateral is transferred into the CTF contract and locked there until the associated condition is resolved. Conditional tokens represent accounting claims on this locked collateral.

As a result:

- collateral is **not** held by Futarchy Labs–specific contracts,
- collateral is **not** held by liquidity pool contracts,
- collateral remains fully controlled by the CTF contract until redemption.

This custody model is identical to that used by existing production prediction markets built on CTF.

---

## Deployed CTF Contracts

The same Conditional Token Framework is deployed across multiple chains and reused by several large applications.

- **Ethereum Mainnet**  
  Gnosis Conditional Tokens:  
  https://etherscan.io/address/0xC59b0e4De5F1248C1140964E0fF287B192407E0C

- **Gnosis Chain**  
  Gnosis Conditional Tokens:  
  https://gnosisscan.io/address/0xCeAfDD6bc0bEF976fdCd1112955828E00543c0Ce  
  Used by **:contentReference[oaicite:0]{index=0}** to custody all collateral in its markets.

- **Polygon**  
  Gnosis Conditional Tokens:  
  https://polygonscan.com/address/0x4D97DCd97eC945f40cF65F87097ACe5EA0476045  
  Used by **:contentReference[oaicite:1]{index=1}** to custody all collateral in its markets.

Futarchy Labs relies on this same, battle-tested custody mechanism.

---

## Conditions and Oracle Requirements

In the Conditional Token Framework, every conditional market is defined by a **condition**.

A condition is identified by:
- an **oracle address**,
- a **question or condition identifier**,
- the number of possible outcomes.

The oracle address is a mandatory component. CTF itself does not evaluate outcomes or determine truth; it relies on the specified oracle contract to report the final result.

Without a valid oracle report, a condition cannot be resolved and collateral cannot be redeemed.

---

## Building on Seer

Futarchy Labs is built on top of the **Seer** prediction market protocol and reuses several of its smart contracts.

Seer is a production deployment of markets built using the Gnosis Conditional Token Framework and has been used extensively on Gnosis Chain. Futarchy Labs leverages this existing infrastructure rather than introducing a new custody or resolution system.

In particular, Futarchy Labs uses Seer contracts to:
- define and manage proposal-specific conditions,
- connect governance outcomes to CTF condition resolution,
- route trades and liquidity into conditional markets.

---

## Oracle and Resolution Architecture

Outcome resolution in Futarchy Labs uses **:contentReference[oaicite:2]{index=2}**, with dispute resolution handled by **:contentReference[oaicite:3]{index=3}**.

The contract responsible for reporting outcomes to the Conditional Token Framework is:

- **FutarchyRealityProxy**  
  `0x03E1fCfE3F1edc5833001588fb6377cB50A61cfc`

This contract is the **only** component authorized to call `reportPayouts()` on the CTF contract for futarchy proposals.

---

## How Outcomes Are Resolved

The resolution flow is as follows:

1. Each proposal is associated with a **reality.eth question** that asks whether the proposal was approved (YES) or not (NO).
2. Once the governance process concludes, an answer is submitted to reality.eth.
3. If the answer is uncontested, it becomes final after the challenge period.
4. If the answer is disputed, resolution is escalated to Kleros for decentralized arbitration.
5. Once finalized, the **FutarchyRealityProxy** reports the outcome to the Conditional Token Framework.

The reported outcome is expressed as a payout vector and applied mechanically by the CTF contract.

---

## Scope and Limitations of the Oracle

The oracle’s authority is intentionally limited.

The oracle:
- **does** attest to which governance outcome occurred,
- **does** enable redemption of conditional collateral,

The oracle **does not**:
- evaluate market prices,
- judge proposal quality,
- measure downstream impact,
- determine whether a proposal was “good” or “bad”.

Its sole role is to report a binary governance fact: **YES or NO**.

---

## Relevant Deployed Contracts

The following deployed contracts adapt Seer’s architecture to futarchy-style governance decisions:

- **FutarchyProposal**  
  `0xec4fb999Db0e8cA28011D85EAD177810055b484c`  
  Defines proposal metadata and condition parameters.

- **FutarchyRealityProxy**  
  `0x03E1fCfE3F1edc5833001588fb6377cB50A61cfc`  
  Bridges reality.eth outcomes to the Conditional Token Framework.

- **FutarchyFactory**  
  `0xe789e4A240d153AC55e32106821e785E71f6b792`  
  Deploys futarchy markets using standardized parameters.

- **FutarchyRouter**  
  `0xE2996f6BC88ba0f2Ad3a6E2A71ac55884ec9F74E`  
  Routes trades and liquidity into the appropriate conditional pools.

These contracts reuse Seer’s battle-tested design while adapting it to governance-based conditions rather than prediction questions.

---

## Further Reading

- Seer futarchy markets:  
  https://seer-3.gitbook.io/seer-documentation/developers/interact-with-seer/futarchy-market

- reality.eth documentation:  
  https://reality.eth.link/

- Kleros documentation:  
  https://docs.kleros.io/

- Conditional Token Framework contracts:  
  https://github.com/gnosis/conditional-tokens-contracts

  
--- 

## Navigation

- ⬆️ **[Protocol Overview](./README.md)**  
  Overview of the Futarchy Labs on-chain protocol architecture.

- ➡️ **[Conditions and Outcomes](./conditions-and-outcomes.md)**  
  How governance decisions are represented as resolvable conditions.

- 🔁 **[Proposal Lifecycle](./proposal-lifecycle.md)**  
  How custody and oracle resolution fit into the end-to-end proposal flow.
