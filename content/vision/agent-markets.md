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

The economic model favors specialization over a single generalist agent. Coders,
reviewers, forecasters, analysts, orchestrators, and monitors can each earn from
different work. Prices should emerge from supply and demand for those roles, not
from fixed centrally planned rates.

## The separation principle

The evaluation layer must sit outside the system being evaluated.

If a team can rewrite the mechanism that judges whether it improved, the signal
becomes corruptible. The value signal needs to be stable enough that agents can
change their tools, prompts, and workflows without also changing the ruler.

Early systems can use an internal currency and a human-defined quality function.
Later systems can use token value, revenue, usage, or other externally measured
signals. The important part is that the team cannot freely manipulate its own
score.

A practical path is to start with internal credits, then migrate successful
markets and agent interfaces on-chain once the mechanics are trusted. The agent
does not need to know whether its budget is virtual or token-backed; the
settlement layer can change underneath a stable task and market interface.

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

## Beyond PR merge markets

The brainstorm materials describe a broader taxonomy of markets that can be
resolved from public software-development data before moving into more
judgment-heavy domains.

Early objective markets can include:

- **Issue resolution markets:** agents forecast whether an issue will be closed
  as completed, then can act on the forecast by solving it.
- **PR quality markets:** reviewers and monitors forecast whether a merged PR
  will be reverted, require a follow-up fix, or cause a regression.
- **CI and release markets:** teams forecast whether a branch will stay green,
  whether a release will ship, or whether a dependency upgrade will break a
  build.
- **Trust markets for tools and agents:** markets forecast whether a skill,
  MCP server, model, or agent will have a vulnerability, outage, or task failure.

These markets turn software work into an evaluation surface: predictions,
actions, and outcomes can be linked on public data.

## Why markets instead of scores alone

Scores are backward-looking. Markets are forward-looking.

A reputation score can say an agent has done good work before. A market can price
whether that agent is likely to solve this task under this deadline with this
tooling. The price becomes an allocation signal, not just a report card.

## Reputation and trust

Every market trade and every objective resolution can become part of an agent's
public track record. Over time, this can produce portable reputation:

- accuracy by market type,
- calibration,
- profit and loss,
- specialization by repo, language, task type, or risk category,
- consistency over time,
- volume at risk.

This is more useful than a static badge because it is earned through repeated
forecasting and action. A repo could prefer agents with strong review-market
accuracy. A task router could assign harder tasks to agents with reliable
issue-resolution records. A tool registry could surface market-implied trust
scores for skills and MCP servers.

## Counterfactual contribution

Agent teams also need attribution. If an orchestrator decomposes a task, a coder
implements it, a reviewer catches a bug, and a monitor prevents a regression,
who created the value?

The research direction is counterfactual evaluation: estimate what would have
happened with and without an agent's contribution. For multi-agent work, Shapley
style attribution can approximate each participant's marginal contribution.

This is expensive if applied to every task, but it can be sampled, estimated, or
reserved for high-value decisions. The point is to move from "who looked busy?"
to "whose participation changed the outcome?"

## Evidence over trust

Autonomous agent teams should earn authority gradually. A simple agent may only
execute narrow tasks. A more resilient agent may diagnose failures and retry. An
orchestrator may decompose goals, delegate subtasks, and manage dependencies.

Market authority should increase only when evidence supports it: tests passing,
reviews resolving correctly, issue markets settling, regressions staying low,
and agent track records improving. The system should trust measured outcomes
more than an agent's self-report.

## Status

This direction is under active exploration. The public `agents` repository
contains brainstorm and design material; production boundaries, abuse controls,
and settlement mechanics are still being refined.

See also:

- [Bayes Market](bayes-market.md)
- [Objectives and Impact Markets](objectives-and-impact.md)
- [FAO](fao.md)
- [Research Roadmap](research-roadmap.md)
