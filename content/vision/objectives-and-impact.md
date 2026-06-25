# Objectives and Impact Markets

The live futarchy.fi protocol uses token value because it is a readily
observable market signal for governance experiments. The broader vision is more
general: any system that can define a value signal can ask markets which action
is expected to improve that signal.

## From token price to chosen objectives

Token value is useful when the question is whether a proposal improves the
market's expectation of a project. It is not the only possible objective.

Other objectives can include:

- revenue,
- usage,
- retention,
- deploy frequency,
- issue-resolution rate,
- agent reliability,
- security incidents avoided,
- grant impact,
- scientific or public-health metrics.

The mechanism is the same at a high level:

1. Define the objective.
2. Define who or what measures it.
3. Open conditional markets over possible actions.
4. Compare the market-implied value of the objective under each action.
5. Use the signal to allocate attention, funding, authority, or execution.

The hard part is not only market design. It is objective design: choosing a
metric that is meaningful, hard to game, and credible to the people who must
trust the result.

## Public goods and nonprofit funding

One research direction from the public `futarchy-fi/agents` materials is
[Futarchy Nonprofits](https://github.com/futarchy-fi/agents/blob/main/docs/brainstorm/18-futarchy-nonprofits.md):
credibly neutral, impact-directed funding for public-good projects.

The idea is to replace "which charity feels persuasive?" with a market question:
which proposal is expected to create the most measured impact, net of cost?

A public-goods fund could work roughly as follows:

1. A fund defines an objective metric and an oracle or evaluator for that metric.
2. Donors contribute either unrestricted funding or marginal funding orders.
3. Builders submit proposals designed to improve the metric.
4. Conditional markets estimate the value of the objective if each proposal is
   selected, compared with a null proposal.
5. Funding goes to proposals whose estimated impact clears the donor-defined
   impact-per-dollar threshold.

In this model, a donation can behave more like a limit order for impact. A donor
does not only say "I support this domain"; they can say "I am willing to fund
work if the market estimates at least this much impact per dollar."

## Marginal impact

The important quantity is marginal impact: the difference between the objective
metric if a proposal is selected and the objective metric if no proposal is
selected.

That framing matters because many grant and nonprofit systems struggle with
credit assignment. It is not enough to ask whether a metric improved. The useful
question is whether this proposal caused an improvement relative to the
available alternatives.

Markets can help estimate that before funds are spent. Later measurement can
still be used to settle impact certificates, update reputations, and improve the
next round of funding.

## Status

This is a research direction, not a deployed product. The public docs should use
it as an example of the broader objective-market pattern: futarchy is not only
about token price. Token markets are one gateway into a larger design space for
choosing actions under uncertainty.

See also:

- [How Futarchy Works](../how-futarchy-works.md)
- [Agent Markets](agent-markets.md)
- [Research Roadmap](research-roadmap.md)
