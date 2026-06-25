# Research Roadmap

This page collects the public research questions that still need evidence,
prototype results, or external collaboration.

## Agent evaluation

- What is the simplest market that improves task routing quality?
- Do PR prediction markets produce useful reviewer attention signals?
- Are issue-resolution markets more useful because agents can both forecast and
  act on the issue?
- Which quality markets best predict regressions, reverts, and follow-up fixes?
- How should agents earn, spend, and lose internal currency?
- How much human oversight is needed before market outcomes can drive execution?
- Which review outcomes are objective enough for early settlement?
- How should agent reputation combine accuracy, calibration, specialization,
  volume, and recent performance?

## Market mechanisms

- When is LMSR sufficient, and when do conditional AMMs or order books work
  better?
- How should market subsidies be sized for small agent teams?
- What abuse controls are needed for public agent-market participation?
- How can markets reward good forecasts without encouraging low-quality action?
- What is the right market design for donor limit orders on impact per dollar?
- How should conservative impact estimates be calculated across multiple
  trading windows?

## Bayesian markets

- Which belief-network structures are expressive enough for real work but still
  tractable?
- When should exact inference be required, and when can approximation be shown
  safely?
- How should deterministic replay and hash stability be maintained as formulas
  become more expressive?
- What UI makes conditional belief updates understandable to humans?

## Autonomous optimizers

- Which objective signals are robust enough for executable autonomy?
- What treasury limits, timelocks, and exit rights are required at each authority
  level?
- How should token value, usage, revenue, and other metrics be combined or kept
  separate?
- What should remain human-governed even when market signals are strong?

## Impact and public goods

- Which public-good metrics are measurable without becoming easy to game?
- Can markets estimate marginal impact before grants are distributed?
- How should null proposals be used to estimate what would happen without new
  funding?
- What settlement assets and oracle designs make impact markets credible?
- Can marginal impact certificates improve credit assignment for donors and
  builders?

## AI trust markets

- Which safety, reliability, and adoption questions can be resolved from public
  data?
- How should vulnerability reports be verified without centralizing trust?
- Can market-implied trust scores help registries rank agents, skills, and MCP
  servers?
- How should Sybil resistance work for agent reputation?

## Funding and collaboration

We are interested in collaborators who can help with mechanism design,
prediction-market engineering, agent evaluation, formal verification, and
grant-funded research pilots.

See [Investors and Grant Makers](../funding/README.md).
