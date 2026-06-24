# FAO: Futarchy Autonomous Optimizer

FAO stands for Futarchy Autonomous Optimizer.

The FAO work explores how futarchy can move from an advisory signal into a
programmable optimizer: a token, treasury, liquidity, and proposal system whose
actions are increasingly governed by market signals.

## What FAO is trying to prove

The long-term question is whether an autonomous system can allocate resources,
evaluate proposals, and improve itself through market-selected actions.

Key ingredients:

- **A token-backed objective:** the market has a stake in whether the system
  becomes more valuable.
- **Sale and treasury mechanics:** capital enters the system under transparent
  rules.
- **Ragequit and exit guarantees:** participants should have defined exit rights
  while administrative controls mature.
- **Conditional liquidity:** liquidity can move between spot and proposal-linked
  conditional markets.
- **Official proposal sources:** the system can identify which markets are
  eligible to influence execution.

## What exists today

The public FAO repository contains Solidity contracts and design documents for:

- the FAO ERC-20 token,
- sale and ragequit mechanics,
- milestone-based insider vesting,
- liquidity management,
- proposal-source contracts,
- integration with futarchy-style conditional markets.

Some parts are experimental or pre-production. Treat this as an active research
and implementation track, not a claim that every design is live at full scale.

## Relationship to futarchy markets

Classic futarchy asks: which action will improve a chosen value metric?

FAO asks a more system-level version: can a market-governed organization route
capital, proposals, liquidity, and execution toward actions that increase its own
measured value?

This connects the live futarchy protocol to the agent-market vision. Conditional
markets can evaluate specific actions; FAO explores the container that could make
those evaluations executable.

## Open questions

- Which objective is robust enough for autonomous execution?
- How much authority should be advisory, veto-like, or automatic at each stage?
- What treasury limits and exit rights are needed before real capital is safe?
- How should agent work, PR markets, and proposal markets feed into the same
  optimizer?

See [Research Roadmap](research-roadmap.md) for current gaps.
