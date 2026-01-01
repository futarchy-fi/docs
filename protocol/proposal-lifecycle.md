# Proposal Lifecycle

This page describes the end-to-end lifecycle of a futarchy proposal in Futarchy Labs, from creation to resolution and settlement.

It provides a chronological overview of what happens on-chain and how this connects to governance processes. Detailed mechanics are documented elsewhere and are linked throughout.

---

## Overview

At a high level, a futarchy proposal goes through the following stages:

1. Proposal Creation and Condition Setup
2. Market initialization
3. Liquidity Provision
4. Trading phase
5. Governance decision
6. Condition resolution
7. Settlement and redemption
8. After the Proposal

This page focuses on **what happens**, not on governance norms or trading strategies.

---

## 1. Proposal Creation and Condition Setup

The first step in the futarchy lifecycle is performed atomically by the **Seer FutarchyFactory** contract.

In a single transaction, the factory:
- creates a new on-chain futarchy proposal,
- defines the binary condition (YES / NO) associated with that proposal,
- and configures the oracle that will later resolve the outcome.

Although these actions occur together at the implementation level, they represent two distinct conceptual responsibilities, which are described separately below.

---

### 1.1 Proposal Creation

At the protocol level, a futarchy proposal is created by deploying a new **FutarchyProposal** contract.

Proposals are created permissionlessly by calling the **FutarchyFactory.createProposal(...)** function. Creating a proposal does not require prior DAO approval and does not, by itself, execute or approve any governance action.

In this sense, proposal creation is the act of **instantiating a futarchy market**, not the act of making a governance decision.

Creating a proposal typically involves specifying:
- a human-readable **market name**,
- the **project or governance token** whose price impact is being evaluated,
- a **trading currency** (often a stablecoin),
- metadata for the oracle question (category, language),
- and timing and bond parameters for oracle resolution.

The factory emits a `NewProposal` event containing:
- the address of the newly deployed `FutarchyProposal` contract,
- the associated Conditional Tokens `conditionId`,
- and the oracle `questionId`.

A proposal contract serves as an on-chain anchor for:
- the conditional markets,
- the oracle question and condition,
- and later settlement and redemption.

The proposal contract **does not**:
- execute governance actions,
- enforce voting rules,
- or determine whether a proposal is “good” or “bad”.

It exists solely to coordinate markets, conditions, and resolution.

For a developer reference and examples, see:
- https://seer-3.gitbook.io/seer-documentation/developers/interact-with-seer/futarchy-market
- https://seer-3.gitbook.io/seer-documentation/developers/contracts/futarchy-test/futarchyproposal

---

### 1.2 Condition and Oracle Setup

At the same time as the proposal is created, the factory defines a **binary condition** in the Gnosis Conditional Token Framework and configures the oracle responsible for resolving it.

Each proposal corresponds to exactly one condition with two outcomes:
- **YES** — the proposal is approved,
- **NO** — the proposal is not approved.

The condition is associated with a **reality.eth question** whose text describes precisely what it means for the proposal to be approved. The exact wording of this question is critical: only the question text, as asked on reality.eth, determines how the condition will later resolve.

The oracle used by default is the **FutarchyRealityProxy**, which integrates:
- reality.eth for answer submission,
- and Kleros for decentralized dispute resolution.

The oracle’s authority is intentionally narrow. It is responsible only for attesting to whether the proposal outcome is YES or NO. It does not:
- evaluate market prices,
- judge proposal quality,
- or measure downstream impact.

Once configured, the condition and oracle setup is immutable. All conditional assets and markets created for the proposal reference this condition for the remainder of the lifecycle.

For trust assumptions and oracle mechanics, see:
- **[Custody and Oracles](./custody-and-oracles.md)**

---

This step initializes everything needed for futarchy markets to exist, but it does not yet involve trading, governance decisions, or settlement. Those occur in subsequent stages of the lifecycle.

---

## 2. Market Initialization

Once a proposal and its associated condition are defined, the protocol initializes the **market infrastructure** required for futarchy trading.

Market initialization refers to the creation of liquidity pools over conditional assets. It does not imply that liquidity is immediately available, only that the pools exist and can accept liquidity and trades.

---

### Primary Pools

For each proposal, two primary liquidity pools are initialized:

- **YES market** — `YES_TOKEN / YES_CURRENCY`  
- **NO market** — `NO_TOKEN / NO_CURRENCY`

Each pool corresponds to a distinct counterfactual world defined by the proposal’s condition. All assets in a pool are scoped to the same outcome.

---

### Auxiliary Pools

In addition to the primary pools, auxiliary pools may be initialized for indexing, routing, or integration purposes (for example, to support certain aggregators or solvers).

These pools do not change the semantics of futarchy markets and may not be directly used by the Futarchy Labs interface.

---

### Liquidity at Initialization

Market initialization does **not** require liquidity to be provided immediately.

Pools may exist in an uninitialized or empty state until liquidity is added by any participant.

Liquidity provision is described separately in the next section.

---

### AMM Selection

The specific automated market maker (AMM) used for pool creation depends on the deployment:

- On **Gnosis Chain**, pools are typically created on **Swapr V3**.
- On **Ethereum Mainnet**, pools are typically created on **Uniswap V3**.

Pool parameters (such as fee tiers and tick ranges) are configurable per deployment and may vary across chains or DAOs.

---

## 3. Liquidity Provision

Liquidity provision is permissionless at the protocol level: **anyone can provide liquidity** to any futarchy pool.

At the protocol level, liquidity provision follows standard AMM mechanics and does not require special permissions or roles.

In practice, during early deployments, liquidity is often provided by the DAO sponsoring or approving a futarchy pilot.

A common operational pattern is:
- the DAO allocates project tokens and trading currency,
- funds are transferred to a multisig or treasury-controlled account,
- liquidity is provided to the relevant conditional pools on behalf of the DAO.

This is an operational choice, not a protocol requirement.

Dedicated contracts for managing futarchy liquidity are planned to simplify and automate this process in the future. These contracts are not required for futarchy to function and are documented separately.

See:
- **[Liquidity Pools](./liquidity-pools.md)** for pool mechanics
- **[Liquidity Management](./liquidity-management.md)** for current practices and future plans

---

## 4. Trading Phase

Once markets are initialized, trading is permissionless and continuous.

At the protocol level:
- there is **no fixed trading window**,
- trading is **never disabled**,
- and markets may exist before, during, and after governance voting.

Trading can occur even if only one of the two pools has liquidity, although in practice liquidity is typically provided symmetrically at initialization.

---

### Trading Before and During Governance

Futarchy markets are often created **before** a proposal is formally put to a governance vote.

This allows markets to produce price signals that voters may consider during deliberation. For futarchy signals to be meaningful, trading should ideally occur **before the outcome is known**. If it is already clear that a proposal will pass or fail, prices in the counterfactual pool no longer convey useful information.

Trading continues during the governance process itself. The protocol does not enforce any coupling between market activity and voting timelines.

---

### Trading After a Decision Is Known

It is possible to trade **after a governance decision is socially known but before oracle resolution**.

In this phase:
- participants may already have strong confidence in which outcome will resolve,
- prices in the pool corresponding to the expected winning outcome tend to converge toward the unconditional spot price,
- prices in the losing pool become less economically relevant.

However, both pools remain active and tradable until resolution.

---

### Trading After Oracle Resolution

Even after the oracle resolves the condition, trading is not disabled at the protocol level.

At resolution:
- conditional assets in the winning branch become freely redeemable for unconditional assets,
- the winning pool effectively becomes another liquidity pool for the underlying token,
- prices in that pool should converge to the spot market price, assuming efficient markets.

The losing branch becomes economically irrelevant, as its assets have zero redemption value, but the protocol does not require explicit shutdown of pools.

---

### Relationship Between Trading and Signals

During the trading phase:
- participants trade conditional assets,
- prices emerge for each counterfactual world,
- futarchy signals are derived from **relative prices** between the YES and NO markets.

If markets are initialized symmetrically and receive little or no trading activity, prices in both pools remain equal and the futarchy signal is neutral.

---

### Proposal Changes During Trading

The oracle question text is **immutable** once the proposal is created.

Off-chain proposal discussions or minor revisions may occur during the trading phase, but only the oracle question — as originally asked — determines how the condition will resolve.

As a result, participants should ensure that the core substance of a proposal is well defined before markets are widely promoted.

---

## 5. Governance Decision

Futarchy does not replace governance by default.

At the protocol level, futarchy markets produce price signals, but they do not execute decisions or enforce outcomes. How those signals are interpreted is a governance choice made by each DAO.

---

### Advisory by Default

By default, futarchy is **advisory**:

- existing governance processes remain unchanged,
- decision makers (e.g. voters, councils, multisigs) may consider futarchy market prices when deliberating,
- no on-chain action is triggered automatically by market outcomes.

This allows futarchy to be adopted incrementally without changing a DAO’s governance framework.

---

### Who Makes the Decision

The final decision on a proposal is made by the DAO’s existing governance mechanism, which may include:

- tokenholder voting,
- a multisig,
- a council or committee,
- or another decision-making body.

Futarchy markets inform these decisions but do not replace them unless explicitly configured to do so.

---

### Deadlines and Default Outcomes

Each futarchy proposal has a deadline.

If a proposal is not approved by the relevant governance process before its deadline, the outcome is treated as **NO**. This ensures that unresolved or abandoned proposals resolve deterministically.

---

### Interpreting Futarchy Signals

DAOs may define explicit rules for interpreting futarchy signals.

A common pattern is to compute an **impact estimate** based on market prices, such as the difference between the YES and NO market prices (often using a time-weighted average price).

For example, a DAO might adopt rules such as:
- recommend **For** if the estimated impact exceeds a positive threshold,
- recommend **Against** if it falls below a negative threshold,
- treat the signal as **Neutral** otherwise.

These rules are **off-chain governance conventions**, not protocol requirements.

Different DAOs may choose different thresholds, averaging windows, or decision rules depending on their risk tolerance and governance culture.

---

### Binding and Hybrid Models

While advisory use is the default, futarchy can also be used in **hybrid or binding configurations**, where:

- market signals gate proposals,
- markets act as a veto mechanism,
- or market outcomes directly trigger on-chain actions.

Such configurations require explicit governance decisions and are not enabled automatically by the protocol.

---

This stage concludes once the governance process determines whether the proposal is approved or not. The next step is condition resolution, where the oracle formally records this outcome on-chain.

---

## 6. Condition Resolution

Once the governance decision is known, the outcome of the proposal must be formally recorded on-chain.

This is done by resolving the proposal’s oracle question on **reality.eth**, which determines how the associated Conditional Token Framework condition will settle.

---

### Reporting the Outcome

At present:
- **anyone** may submit an answer to the reality.eth question,
- submitted answers are subject to a challenge period,
- disputes are resolved via **Kleros**.

The reported answer must correspond to one of the two defined outcomes:
- **YES** — the proposal was approved,
- **NO** — the proposal was not approved.

Once the answer is finalized, the **FutarchyRealityProxy** reports the outcome to the Conditional Token Framework as a payout vector:

- YES → `[1, 0]`
- NO → `[0, 1]`

This payout vector is applied mechanically to all conditional assets.

---

### Incentives and Correctness

Reality.eth uses an economic incentive mechanism to encourage correct reporting:

- submitting an answer requires posting a bond,
- incorrect answers may be challenged by other participants,
- successful challengers are rewarded with the bonded stake,
- unresolved disputes are escalated to Kleros for arbitration.

As a result, even though anyone may submit an answer, there is a financial incentive for the final outcome to reflect the true governance decision.

---

### Operational Practice

In current deployments, the initial answer is often submitted by parties closely involved in the governance process (for example, DAO operators or Futarchy Labs), as they are best positioned to observe when a proposal has formally passed or failed.

This is an **operational choice**, not a protocol requirement. The protocol does not grant special reporting privileges to any party.

---

### Deadlines and Default Outcomes

Each proposal includes a deadline, which is encoded into the oracle question asked on reality.eth.

The deadline defines what the **correct outcome** should be after that time. If a proposal has not been approved by its deadline, the correct resolution is **NO**.

However, the protocol does not automatically resolve conditions at the deadline. Resolution still requires an answer to be submitted and finalized on reality.eth, following the standard reporting and dispute process.

As a result:
- the deadline ensures that proposals have a deterministic correct outcome,
- but settlement still depends on oracle resolution,
- and conditional assets may remain unresolved until a valid answer is finalized.

---

### Future Extensions

The resolution mechanism is designed to support additional incentive structures in the future, such as:
- explicit rewards for third-party reporters,
- automated reporting by governance contracts,
- or tighter integration between governance execution and oracle resolution.

These extensions are not required for the protocol to function and can be introduced without changing the core futarchy mechanism.

---

## 7. Settlement and Redemption

Once the condition is resolved, the futarchy markets transition from conditional to unconditional behavior.

---

### Effect of Resolution on Assets

After resolution:

- conditional assets corresponding to the **winning outcome** become redeemable for the underlying unconditional assets,
- conditional assets corresponding to the **losing outcome** have zero redemption value,
- all conditional accounting is finalized using the payout vector reported by the oracle.

This applies globally to all conditional assets and markets associated with the proposal.

---

### Redemption Mechanics

Redemption is handled via the **FutarchyRouter**.

When redeeming, the router:
- unwraps ERC-20 conditional assets into their underlying ERC-1155 positions,
- redeems those positions on the Conditional Token Framework,
- returns the corresponding unconditional ERC-20 assets to the user.

Redemption is **optional**. Users may choose when (or whether) to redeem.

---

### Effect on Liquidity Pools and Trading

Resolution does not disable trading at the protocol level.

After resolution:
- pools corresponding to the **losing outcome** become economically irrelevant, as their assets have zero value,
- pools corresponding to the **winning outcome** effectively become regular liquidity pools for the underlying asset.

Because winning conditional assets can be freely converted into unconditional assets, prices in the winning pool should converge to the spot market price, assuming efficient markets.

As a result, trading may continue in the winning pool even after resolution.

---

### Finality of Settlement

Once resolution has occurred:
- no further oracle interaction is required,
- no additional settlement steps are needed,
- all conditional positions have a well-defined economic value.

At this point, the futarchy evaluation is complete from a protocol perspective.

---

## 8. After the Proposal

After settlement, the futarchy proposal enters a completed state.

At this point:
- the proposal contract remains on-chain as a permanent historical record,
- all associated conditions have been resolved,
- and all conditional assets have a well-defined final economic value.

Price data and market activity from the proposal may be indexed and analyzed for governance learning, evaluation of futarchy signals, or historical reference.

Similar proposals or milestones may be evaluated again in the future by creating **new futarchy proposals**.

Re-running a proposal always creates a **new condition**, even if the proposal text or intent is similar. Past market outcomes do not affect the resolution of future proposals.

---

## Navigation

- ⬆️ **[Protocol Overview](./README.md)**
- ⬅️ **[Liquidity Pools](./liquidity-pools.md)**
- ➡️ **[Using Futarchy in Practice](../using-futarchy-in-practice.md)**  
  Governance norms, thresholds, and design choices.
