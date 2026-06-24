# Vision

Futarchy Labs is building markets for better decisions in autonomous systems.

The current protocol applies conditional token markets to governance decisions:
what will a project token be worth if a proposal passes versus if it fails? That
same pattern generalizes. If a system can define a value signal and expose
different possible actions, markets can help choose between those actions.

## The broader thesis

Most organizations and AI systems are governed by fixed rules:

- retry a task three times,
- assign work round-robin,
- choose a model by default,
- promote proposals through committees,
- trust a reviewer because of status.

Futarchy asks a different question: what if the operating rules themselves were
selected by markets and measured against outcomes?

For AI agent teams this is especially attractive because the feedback loop is
fast, the work is observable, and experiments can be forked. Agents can forecast
task success, bid for work, stake on reviews, and evolve their scaffolding over
time.

## What this unlocks

- **Decision markets:** markets that compare actions before they are taken.
- **Agent evaluation:** markets that forecast whether agents, prompts, models, or
  workflows will produce useful work.
- **Task and PR markets:** markets on whether pull requests will merge, whether
  work will pass review, or which tasks deserve attention.
- **Bayesian market engines:** richer markets over belief networks rather than
  isolated binary questions.
- **Autonomous optimizers:** token-backed systems where markets can gradually
  control execution, treasury routing, and incentives.

## How to read this section

- [Agent Markets](agent-markets.md) explains the agent-first coordination layer.
- [FAO](fao.md) explains the token and autonomous optimizer direction.
- [Bayes Market](bayes-market.md) explains the experimental Bayesian market
  engine.
- [Research Roadmap](research-roadmap.md) lists current questions and missing
  evidence.

This is a public synthesis of open repository material. It intentionally omits
private operational details and internal-only source notes.
