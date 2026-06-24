# Agent Markets

Agent teams are a natural testbed for futarchic mechanisms.

Human organizations are slow, political, and difficult to measure cleanly. Agent
teams can run many tasks per day, expose detailed traces, fork their workflows,
and settle predictions against concrete results such as tests, review outcomes,
merge decisions, and user-visible performance.

## The core idea

A futarchic agent team is governed by market mechanisms instead of fixed
heuristics.

Examples:

- A forecaster estimates whether a task will succeed before an agent starts.
- Agents bid for tasks based on confidence and opportunity cost.
- Reviewers stake on whether work will pass deeper review or be reverted later.
- A market predicts whether changing a prompt, model, tool policy, or routing
  rule will improve performance.
- Successful configurations earn budget and reproduce; losing configurations are
  replaced.

The goal is not to make agents trade for novelty. The goal is to create a
measurement and incentive layer that lets the team learn its own operating rules.

## The separation principle

The evaluation layer must sit outside the system being evaluated.

If a team can rewrite the mechanism that judges whether it improved, the signal
becomes corruptible. The value signal needs to be stable enough that agents can
change their tools, prompts, and workflows without also changing the ruler.

Early systems can use an internal currency and a human-defined quality function.
Later systems can use token value, revenue, usage, or other externally measured
signals. The important part is that the team cannot freely manipulate its own
score.

## First product surface: PR prediction markets

Pull requests provide a simple and useful market target:

- Will this PR merge?
- Will it pass review without major rework?
- Should this PR receive reviewer attention now?
- Which agent or reviewer is best suited to evaluate it?

The `futarchy-fi/agents` materials describe an MVP with conditional prediction
markets over PR outcomes, an LMSR market maker, internal credits, and a path from
internal points to real-money markets.

This is useful even before full autonomy. Maintainers get a market signal about
which work is likely to matter, reviewers get a way to price attention, and
agents gain a disciplined feedback loop.

## Why markets instead of scores alone

Scores are backward-looking. Markets are forward-looking.

A reputation score can say an agent has done good work before. A market can price
whether that agent is likely to solve this task under this deadline with this
tooling. The price becomes an allocation signal, not just a report card.

## Status

This direction is under active exploration. The public `agents` repository
contains brainstorm and design material; production boundaries, abuse controls,
and settlement mechanics are still being refined.

See also:

- [Bayes Market](bayes-market.md)
- [FAO](fao.md)
- [Research Roadmap](research-roadmap.md)
