# DAO Integration Guide

This page explains how a DAO can set up futarchy evaluation in practice.  
It covers liquidity, oracle setup, thresholds, governance hooks, and pilot timelines.

---

## Liquidity

**Default pilot size:** ~$100k of protocol-owned liquidity (e.g. 50/50 TOKEN–stable).  
- At this depth, a $500 trade moves price ~2%.  
- Ensures informed traders can shift prices, but prevents cheap manipulation.  
- The DAO earns LP fees back on its own liquidity.

**Flexibility:**  
- Milestone markets can use less liquidity (e.g. $25–50k).  
- Concentrated liquidity (v3-style) or weighted pools can reduce capital requirements.

---

## Oracle Setup

Futarchy requires a way to determine which market (YES or NO) should pay out:

- **Default:** **Reality.eth + Kleros arbitration** for disputes on whether a proposal has been approved or rejected.
- **FAO mode:** In fully autonomous futarchies, the `Futarchy Oracle` contract compares TWAP(YES) vs TWAP(NO) over the decision window. The oracle result directly triggers execution.

---

## Decision Window

- **Default:** 7 days.  
- **Shorter:** 3 days for fast-moving proposals (higher risk of thin markets).  
- **Longer:** 14–21 days for high-stakes proposals.  

During the window, prices are continuously tracked, and the oracle computes a **time-weighted average (TWAP)** to prevent last-minute manipulation.

---

## Thresholds

- **Default:** 1% difference between YES and NO (YES > NO + 1%).  
- **Critical proposals:** Require higher thresholds (e.g. 5–10%).  
- **Sponsored futarchy:** Threshold may scale with sponsorship size, ensuring bigger proposals need stronger market support.

---

## Liquidity Management

**Funding source:** Liquidity can come from the DAO treasury or external sponsors.  

**Multisig custody:**  
We recommend a **2-of-3 multisig** to hold funds allocated to futarchy markets.  
- **Signers:** typically 2 DAO representatives + 1 Futarchy Labs (or another trusted technical party).  
- **Why 2/3:** lightweight enough for quick operations (creating/redeeming conditional pools), but still secure.  

**Lifecycle:**  
1. DAO approves a proposal committing funds for futarchy liquidity.  
2. Funds are moved to the multisig.  
3. The multisig creates positions in YES/NO pools for proposals (and optionally milestones).  
4. After resolution, funds are redeemed and returned to the DAO treasury (minus IL, plus any LP fees earned).  

---

## Allocation of Liquidity

- **DAO Proposal:** The DAO decides how much liquidity to allocate (e.g. $100k).  
- **Multisig Execution:** The multisig chooses *which proposals/milestones* to seed liquidity for, following the DAO’s guidance.  
  - Example: “DAO commits $100k to futarchy. Multisig will allocate to proposals that have cleared the futarchy slot auction.”  
- **Milestones:** If milestones are funded, the DAO should pre-approve which ones are eligible.  

---

## Governance Hooks

DAOs can decide how to use futarchy recommendations:  

- **Advisory (recommended default)** — futarchy evaluation runs on proposals and the results are shown alongside Snapshot/on-chain votes, guiding delegates.  
- **Veto** — proposals must pass futarchy evaluation (checked via Kleros governance) before advancing to a vote or execution.  
- **Autonomous (FAO)** — the Futarchy Oracle result triggers automatic execution on-chain.  

**Important:** The **oracle does not publish thresholds**. It only publishes the binary outcome (YES/NO) or whether a proposal passed the required threshold, via Reality.eth + Kleros. The futarchy evaluation process performs the threshold check.

👉 Next: Read about [Adoption Levels](./adoption-levels.md) or see [Sponsored Proposals](./sponsorship.md) for capital inflow options.

---

## Navigation

- ⬆️ **[DAO Operator Guides](./index.md)**  
  Overview and quick links for DAO stakeholders.

- ⬅️ **[Adoption Levels](./adoption-levels.md)**  
  Step-by-step paths from advisory to autonomous futarchy.

- ➡️ **[Sponsored Proposals](./sponsorship.md)**  
  Mechanics and incentives for sponsored futarchy.

- ➡️ **[DAO FAQ](./faq.md)**  
  Answers to common questions and concerns.
