# Futarchy.FI Documentation

Welcome to the Futarchy.FI documentation.

Futarchy.FI is a **governance protocol** that uses **conditional token markets** to evaluate governance decisions.

Instead of voting directly on proposals without feedback, participants trade on **counterfactual versions of a project’s token**:
- one conditional on the proposal being approved (YES),
- one conditional on the proposal being rejected (NO).

By comparing prices in these two markets **before a decision is made**, Futarchy produces an incentive-aligned signal about which choice is expected to create more value for the project.

This repository documents the **live Futarchy protocol**, its governance use cases, and recommended operational practices. Some sections also describe features that are launching soon; these are clearly indicated where relevant.

---

## Start Here (Core Concepts)

If you are new to futarchy, start with these pages:

- **[How Futarchy Works](./how-futarchy-works.md)**  
  The core idea: counterfactual markets, conditional assets, and belief aggregation.

- **[Trading in Futarchy Markets](./trading-in-futarchy.md)**  
  How YES/NO markets work, what traders are actually buying and selling, and how positions resolve.

- **[Futarchy Protocol](./protocol/README.md)**  
  On-chain architecture: conditions, conditional assets, liquidity pools, oracles, and settlement.

---

## Using Futarchy in Governance

These sections are most relevant for DAOs and governance operators.

- **[DAO Operator Guides](./dao/index.md)**  
  How DAOs use futarchy in practice, recommended defaults, and governance integration patterns.

  - [Adoption Levels](./dao/adoption-levels.md) — advisory → sponsored → autonomous (FAO)
  - [Integration Guide](./dao/integration.md) — liquidity, oracles, thresholds, timelines
  - [DAO FAQ](./dao/faq.md) — manipulation, noise, liquidity, oracles
  - [Sponsored Proposals](./dao/sponsorship.md) — attracting capital and ideas via sponsored futarchy

- **[Using Futarchy in Practice](./using-futarchy-in-practice.md)**  
  How to interpret futarchy signals, handle close calls, and apply market outputs in real governance.
  *(Work in progress)*

---

## Guides by Audience

- **[DAO Operators](./dao/index.md)**  
  Recommended defaults, governance hooks, and operational considerations.

- **[Traders](./traders/index.md)**  
  Trading mechanics, risks, and arbitrage in YES/NO markets.  
  *(Some sections coming soon.)*

- **[Activist Sponsors](./activists/index.md)**  
  Sponsoring proposals, participating in selection, and influencing roadmaps.  
  *(Expanding alongside Sponsored Futarchy.)*

---

## Reference & Background

- **[Appendices](./appendices/index.md)**  
  Glossary, definitions, and supporting material.

---

## What Futarchy Is — and Is Not

Futarchy is:
- a way to aggregate **beliefs** using markets,
- a tool for evaluating governance decisions,
- a source of **continuous, incentive-aligned signals**.

Futarchy is not:
- a replacement for governance by default,
- a prediction market resolved on future outcomes,
- a guarantee that approved proposals will succeed.

By default, futarchy provides **recommendations**.  
How those recommendations are used — advisory, veto-based, or autonomous — is a governance choice made by each DAO.
