# Bayes Market

Bayes Market is an experimental prediction-market engine for richer belief
structures.

Most prediction markets ask one isolated question. Bayes Market explores markets
where prices are driven by a Bayesian inference model plus an LMSR market maker,
so users can trade on relationships between variables in a belief network.

Public repo: [futarchy-fi/bayes-market](https://github.com/futarchy-fi/bayes-market)  
Public endpoint: [bayes.futarchy.ai](https://bayes.futarchy.ai/)

## Why it matters

Autonomous systems rarely need only one binary forecast. They need structured
beliefs:

- If this task is assigned to this agent, how likely is success?
- If a reviewer flags a patch, how does that update merge probability?
- If a model performs well on one class of tasks, what does that imply for nearby
  tasks?
- If a proposal changes a product metric, what does that imply about token value?

A Bayesian market engine can make those dependencies explicit.

## Current architecture

The current public implementation is an event-sourced market backend with:

- append-only market events,
- hash-chained journals,
- an LMSR market maker,
- a Bayesian inference module,
- REST endpoints for markets, events, trades, metadata, account risk, positions,
  exposure, and PnL,
- a React/D3 frontend for visualizing belief networks.

The current deployment is experimental. State is in memory and reseeded on
restart, so it should be treated as a research system rather than durable
financial infrastructure.

## Launch-gate themes

The Bayes design docs emphasize evidence-driven gates:

- deterministic replay,
- solvency invariants,
- API contract stability,
- public route health,
- write-path security and abuse controls,
- UI operability,
- performance telemetry.

These gates are directly relevant to future agent markets. If agents trade,
stake, or route work through markets, the engine needs deterministic state,
auditable events, and explicit risk accounting.

## Relationship to the rest of Futarchy Labs

- Futarchy markets compare decision branches.
- Agent markets price work, review, and coordination.
- Bayes Market provides a path toward structured belief markets for complex,
  interdependent decisions.

Together, these form a stack for market-native autonomous coordination.
