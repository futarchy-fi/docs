# How Futarchy Works

This page explains the core idea behind futarchy and how Futarchy Labs is
exploring it.

It is recommended reading before diving into governance usage or trading details.

---

## The Problem Futarchy Tries to Solve

Important decisions are hard.

Proposals often involve complex, uncertain tradeoffs, and it is difficult to know
in advance which actions will actually improve outcomes. Votes, committees, and
expert reviews can express preferences, but they do not always aggregate
information about consequences very well.

Futarchy approaches this problem by asking a different question:

**Instead of asking people how they want to vote, what if we ask them what they think will create value?**

A useful shorthand: a normal prediction market is about betting on **what will
happen**; futarchy is about betting on **what should happen**, relative to a
chosen objective. More precisely, traders price which decision they expect to
better achieve the goal the system has chosen.

---

## Values vs. Beliefs

Futarchy separates two roles that are often mixed together:

- **Values**: What outcomes matter  
- **Beliefs**: Which actions will best achieve those outcomes  

Humans decide values. Markets aggregate beliefs.

For a for-profit company, the objective might be share price, enterprise value,
revenue, or another measure of long-term business success. For a DAO or crypto
organization, the closest market-priced analogue is often token value. For a
nonprofit, the objective might be marginal impact per dollar. For an agent team,
it might be task success, reliability, security, or issue-resolution rate.

The deeper pattern is that a system chooses an objective, then markets estimate
which action is most likely to improve it. The important part is that the
objective and measurement process are defined outside the market being used to
choose actions.

This is why futarchy can apply beyond token governance. In a public-goods or
nonprofit setting, for example, donors could define an impact metric and markets
could estimate which proposal produces the most marginal impact per dollar. See
[Objectives and Impact Markets](vision/objectives-and-impact.md).

---

## The general pattern

A futarchic mechanism has five basic parts:

1. A community, company, protocol, or agent team defines what it wants to
   improve.
2. A proposal or action set is put forward.
3. Markets are opened on the possible worlds created by those actions.
4. Traders price which world is expected to better achieve the chosen objective.
5. The system uses the market signal to guide a decision.

That decision might remain advisory, or it might later control funding,
execution, treasury routing, task assignment, or other incentives.

---

## Counterfactual Worlds

For each decision, futarchy compares possible worlds.

In a simple proposal market, the two worlds are:

- **YES** - the proposal is approved
- **NO** - the proposal is not approved

Other markets could compare product launches, hiring plans, grant proposals,
agent configurations, model choices, or public-good interventions. The key move
is the same: price the world if the action happens against the world if it does
not.

---

## Conditional Markets

When participants trade in these markets, they are not making unconditional bets.
They are taking positions that only apply in a specific world.

In the current `futarchy.fi` experiment, this is implemented with conditional
token markets:

- Trades in the **YES** market only take effect if the proposal is approved.
- Trades in the **NO** market only take effect if the proposal is not approved.

If the relevant world does not occur, the trade is reverted and funds are returned.

In other designs, the conditional asset could be linked to share price, revenue,
an impact metric, a reliability score, or another objective. The mechanism is
not tied to tokens; tokens are the first practical implementation surface because
crypto already has tradable assets, public governance actions, and programmable
settlement.

---

## What the Prices Represent

Because trades are conditional, prices can be interpreted as the market's
estimate of the chosen objective in each world.

For example:

- In a token-governance market, prices can estimate token value if a proposal is
  approved versus rejected.
- In a company setting, markets could estimate share price or another business
  metric under different decisions.
- In an agent team, markets could estimate whether a task will pass review,
  whether a change will reduce regressions, or whether a tool is reliable.
- In a public-goods setting, markets could estimate marginal impact under each
  proposed intervention.

These prices reflect participants' beliefs, incentives, and information at the
time the decision is made.

Some futarchy designs require later measurement of the objective. The current
`futarchy.fi` governance markets are narrower: they compare conditional spot
markets during the decision window, and do not wait for a future success metric
to be observed.

---

## The Role of Measurement and Oracles

Every futarchy needs a credible measurement layer.

In the current `futarchy.fi` governance markets, an oracle is used only to
determine **which world occurred**: whether the proposal was approved or not. The
oracle does not decide whether the proposal was good. It only reports the
decision outcome so conditional trades can be applied or reverted.

Other futarchy designs may need an oracle for the objective itself: revenue,
usage, safety incidents, public-good impact, or another measured outcome. That
measurement problem is often the hardest part of the design. If the metric is
easy to manipulate, the market will optimize the wrong thing.

---

## Why This Produces a Useful Signal

Futarchy markets let participants express beliefs with incentives attached.

If you believe an action improves the objective, you can take a position that
pays in the world where that action happens. If you believe it makes the
objective worse, you can take the other side.

In the current token-market implementation, this means:

- If you believe approving a proposal will increase value, you can buy in the
  **YES** market.
- If you believe approving it will decrease value, you can sell in the **YES**
  market.
- If you believe rejection is better, you can trade the **NO** market instead.

In all cases, participants are taking positions that only apply if the corresponding world occurs.

As participants buy and sell in both markets, prices adjust to balance all of these views. The resulting YES and NO prices reflect the market’s collective assessment of which decision is expected to create more value, given the opportunity to express both positive and negative beliefs.

Participants are free to take positions in either or both markets; how positions combine is discussed in the trading section.

---

## Where futarchy.fi Fits

Futarchy is still underexplored. Public implementations are early, and the most
visible live experiments have been crypto-native because crypto provides
tradable assets, transparent governance, and programmable settlement.

`futarchy.fi` should be read in that light: it is an experiment in conditional
governance markets using token value as the current objective proxy. It is a
working surface for learning about market creation, liquidity, conditional
assets, oracle boundaries, and trader behavior. It is not the full scope of what
futarchy can become.

Other crypto-native experiments, such as
[MetaDAO](https://docs.metadao.fi/governance/overview), show the same broader
direction: markets can become a decision layer, not only a forecasting venue.

---

## What Futarchy Is — and Is Not

Futarchy is:

- A way to aggregate beliefs using markets.
- A tool for evaluating decisions against a chosen objective.
- A source of incentive-aligned signals for funding, governance, agent
  coordination, and execution.

Futarchy is not:

- A traditional voting system.
- A guarantee that decisions will succeed.
- A substitute for choosing good objectives.
- A reason to automate high-stakes decisions before the signal has earned trust.

How the signal is used — advisory, binding, or otherwise — is up to each project.

---

## What’s Next

- Learn how these markets work in detail:  
  **[Trading in Futarchy Markets](./trading-in-futarchy.md)**

- See current applications:  
  **[Applications](./use-cases/README.md)**

- Explore deeper theory and limitations:  
  **[Appendices](./appendices/README.md)**
