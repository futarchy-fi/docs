# DAO Partner Guide

Welcome to the **DAO Partner Guide** for Futarchy Labs.

Our mission is to help DAOs make better decisions, raise tokenholder confidence, and create lasting value by using **Token Futarchy** — conditional spot markets on token price that reveal the expected impact of proposals before they are adopted.

## Why Futarchy Matters for DAOs

DAO governance today often struggles with:
- **Low confidence**: tokenholders can’t easily know if a proposal will help or harm.
- **Concentrated voting**: a few whales often determine the outcome.
- **Unclear signals**: even when markets react, it’s hard to tie moves to specific proposals.

Futarchy addresses this by:
- Creating **YES/NO conditional markets** for each proposal.
- Using price differences to show the **expected token price impact**.
- Requiring proposals to “prove themselves” in markets before they move forward.

This transforms governance into a **value-driven process**: proposals only pass when the market predicts they will increase the token’s value.

## A Real Example

In 2024, MakerDAO rebranded as “Sky.” Within ten days, MKR/SKY tokens lost ~20% of market value (over $500M). Many blamed the rebrand, but it was impossible to know for sure — the timing could have been coincidence. Futarchy solves this: by comparing conditional prices *with vs without* the rebrand **beforehand**, MakerDAO could have quantified the expected impact and avoided a costly decision.

## How Token Futarchy Works (Light Version)

- A proposal is introduced.
- We create two conditional markets:
  - **YES Pool**: token price if the proposal passes.
  - **NO Pool**: token price if the proposal fails.
- Traders buy/sell in these pools.
- After a 7-day **decision window**, the system compares the average prices (TWAP).
- If YES > NO by a threshold (default: 1%), the proposal is recommended.

This ensures proposals are judged by their *expected effect on value*.

<pre> ```mermaid flowchart LR A[Proposal Submitted] --> B[Conditional YES/NO Markets] B --> C[TWAP Window (7d)] C --> D{Threshold met?} D -->|Yes| E[DAO implements proposal] D -->|No| F[Proposal rejected] ``` </pre>

## Levels of Adoption

Futarchy can integrate at different levels, depending on how much autonomy a DAO wants:

- **Level 0 — Milestone Futarchy**  
  Markets track token impact of milestones (e.g., “Launch feature X by Q3”). Signals only.

- **Level 1 — Advisory Futarchy**  
  Proposals are evaluated in conditional markets. Results guide tokenholder votes, or act as a veto requirement.

- **Level 2 — Sponsored Futarchy**  
  Outsiders (activists) can fund proposals. If markets approve, sponsors buy DAO tokens at a discount, bringing new capital and alignment.

- **Level 3 — FAO (Futarchy Autonomous Optimizer)**  
  A fully on-chain futarchy agent. Holds treasury, runs proposal auctions, executes changes automatically. Pure market-driven governance.

## Benefits for DAOs

- **Higher tokenholder confidence**: decisions are backed by measurable, market-driven evidence.
- **Funding inflow**: sponsored proposals bring new capital directly into the DAO.
- **Legitimacy**: shows the community and outsiders that governance is guided by value creation, not politics.
- **Scalability**: futarchy filters noise, ensuring attention goes to high-impact proposals.

## Next Steps

- Start small with **Milestone Futarchy** to test signals.
- Graduate to **Advisory Futarchy** for major proposals.
- Explore **Sponsored Futarchy** to attract capital and ideas.
- Long-term: experiment with **FAO modules** for autonomous optimization.

👉 See the [Appendices](../appendices/glossary.md) for terminology and technical details.

