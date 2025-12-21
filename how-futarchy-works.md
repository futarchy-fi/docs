# How Futarchy Works

This page explains the core idea and mechanism behind Futarchy Labs.

It is recommended reading before diving into governance usage or trading details.

---

## The Problem Futarchy Tries to Solve

Governance decisions are hard.

Proposals often involve complex, uncertain tradeoffs, and it is difficult to know in advance which actions will actually improve outcomes. Voting aggregates preferences, but it does not aggregate information about consequences very well.

Futarchy approaches this problem by asking a different question:

**Instead of asking people how they want to vote, what if we ask them what they think will create value?**

---

## Values vs. Beliefs

Futarchy separates two roles that are often mixed together:

- **Values**: What outcomes matter  
- **Beliefs**: Which actions will best achieve those outcomes  

Humans decide values. Markets aggregate beliefs.

At Futarchy Labs, the chosen outcome metric is the project’s token value, used as a proxy for collective expectations about the project’s success.

---

## Counterfactual Worlds

For each proposal, Futarchy Labs considers two possible worlds:

- **YES** — the proposal is approved
- **NO** — the proposal is not approved

Rather than predicting the future, the system allows participants to trade on **counterfactual versions of the project’s token**, conditional on which world occurs.

This creates two markets, one for each world.

---

## Conditional Token Markets

When participants trade in these markets, they are not making unconditional bets.

Instead, they are buying or selling **conditional exposure** to the token.

- Trades in the **YES** market only take effect if the proposal is approved.
- Trades in the **NO** market only take effect if the proposal is not approved.

If the relevant world does not occur, the trade is reverted and funds are returned.

All trading happens in the present. There is no future price measurement.

---

## What the Prices Represent

Because trades are conditional, market prices can be interpreted as:

- The market’s current valuation of the token **if the proposal is approved**
- The market’s current valuation of the token **if the proposal is not approved**

These prices reflect participants’ beliefs, incentives, and information **at the time the decision is made**.

They are not predictions that get checked later, and they are not settled based on observed outcomes.

This makes Futarchy Labs fundamentally different from traditional prediction markets.

---

## The Role of the Oracle

An oracle is used only to determine **which world occurred**: whether the proposal was approved or not.

The oracle does not measure outcomes, assess success, or resolve prices.

Once the proposal outcome is known, conditional trades are either applied or reverted accordingly.

---

## Why This Produces a Useful Signal

Futarchy markets allow participants to express beliefs in more than one way.

If you believe approving a proposal will increase value, you can buy the token in the **YES** market.  
If you believe approving it will decrease value, you can sell the token in the **YES** market.

Likewise, if you believe rejecting a proposal will increase value, you can buy the token in the **NO** market.  
If you believe rejecting it will decrease value, you can sell the token in the **NO** market.

In all cases, participants are taking positions that only apply if the corresponding world occurs.

As participants buy and sell in both markets, prices adjust to balance all of these views. The resulting YES and NO prices reflect the market’s collective assessment of which decision is expected to create more value, given the opportunity to express both positive and negative beliefs.

Participants are free to take positions in either or both markets; how positions combine is discussed in the trading section.

---

## What Futarchy Is — and Is Not

Futarchy Labs is:

- A way to aggregate beliefs using markets
- A tool for evaluating governance decisions
- A source of continuous, incentive-aligned signals

Futarchy Labs is not:

- A traditional voting system
- A prediction market with future resolution
- A guarantee that decisions will succeed

How the signal is used — advisory, binding, or otherwise — is up to each project.

---

## What’s Next

- Learn how these markets work in detail:  
  **[Trading in Futarchy Markets](./trading-in-futarchy.md)**

- See how teams apply this signal in governance:  
  **[Using Futarchy in Practice](./using-futarchy-in-practice.md)**

- Explore deeper theory and limitations:  
  **[Appendices](./appendices.md)**

