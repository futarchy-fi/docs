# Applications

Futarchy Labs applies market mechanisms to decision problems where information is
distributed and incentives matter.

## Current application: governance and proposal evaluation

The live futarchy.fi protocol evaluates governance proposals with conditional
token markets:

- YES market: token value if the proposal is approved.
- NO market: token value if the proposal is rejected.
- Signal: compare the YES and NO time-weighted average prices.

This is useful for DAOs, token projects, and communities that want market-based
input before making consequential decisions.

Start with:

- [DAO Operator Guide](../dao/README.md)
- [Integration Guide](../dao/integration.md)
- [Sponsored Proposals](../dao/sponsorship.md)

## Emerging application: autonomous agent teams

Agent teams create a faster feedback loop:

- task success can be measured,
- review outcomes are observable,
- agents can be forked and compared,
- internal currency can bootstrap incentives before real-money markets.

Start with:

- [Agent Markets](../vision/agent-markets.md)
- [Bayes Market](../vision/bayes-market.md)

## Shared pattern

Across both applications, the pattern is the same:

1. Define what the system values.
2. Expose alternative actions or states.
3. Let markets price which action is expected to improve the value signal.
4. Start with advisory signals.
5. Add stronger execution hooks only after the signal earns trust.
