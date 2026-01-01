# DAO FAQ

## Can futarchy markets be manipulated?

Markets can always be influenced in the short term — but futarchy is designed to make manipulation *costly*.  
- Conditional markets are subsidized and liquid, so any trader trying to “push” prices without real information creates a profit opportunity for informed participants.  
- Informed traders (“wolves”) profit by trading against uninformed manipulators (“sheep”), pushing prices toward accurate expectations.  
- Futarchy uses **time-weighted average price (TWAP)** over the decision window, making last-minute price manipulation ineffective.

The net result: attempts at manipulation often transfer wealth from manipulators to informed traders—helping the final prices remain accurate.

> **Further reading:** Robin Hanson’s paper, *A Manipulator Can Aid Prediction Market Accuracy*, explores this dynamic in detail.  
> [Access the paper (PDF)](http://robinhanson.com/biashelp.pdf)

---

## How does futarchy isolate the effect of a proposal, when token prices move for many reasons?

This is a core feature of futarchy. Instead of watching the token’s live market, we compare **two parallel markets**:  
- **YES Market** — token value *if the proposal passes*.  
- **NO Market** — token value *if the proposal fails*.  

Because both YES and NO markets face the same external noise (macro conditions, BTC price moves, etc.), the **difference between them isolates the causal impact of the decision itself**.

---

## Who provides liquidity for these markets?

By default, the **DAO itself seeds protocol-owned liquidity** into the YES/NO pools.
- This ensures enough depth that small trades don’t move prices too much.
- The DAO earns LP fees back.  
- Optionally, outside LPs can also participate, but protocol-owned liquidity is the baseline.

---

## How much liquidity is needed?

For pilot futarchy markets we recommend seeding around **$100k** of protocol-owned liquidity (e.g. a 50/50 TOKEN–stable pool).  
At this depth, a ~$500 trade moves the price by about 2%.  

This balance is usually enough to:
- Ensure noise traders cannot cheaply swing the signal.  
- Provide informed traders room to express conviction.  
- Let the DAO earn back LP fees on its own liquidity.

---

## How much impermanent loss (IL) do LPs incur in futarchy markets?

Providing liquidity to **conditional YES/NO pools** is not significantly riskier than providing liquidity to a standard TOKEN–stable pool.  

Here’s why:  
- At settlement, only one side (YES or NO) ends up valuable — but those tokens unwrap back into the same underlying TOKEN or stablecoin.  
- The DAO’s LP position from the “losing” side reverts to worthless conditional tokens, while the “winning” side holds assets equivalent to what a normal LP position would have after impermanent loss.  
- In practice, IL is the same as if you had just LP’d TOKEN–stable during the evaluation window.  

**Key point:** Futarchy doesn’t add an *extra* layer of impermanent loss beyond what DAOs already face when providing liquidity in AMMs. The main “cost” is the *opportunity cost* of locking liquidity during the evaluation window.

---

## What if there isn’t enough participation?

Low participation is a real risk — but futarchy is designed so that the signal remains meaningful even with modest activity.

- **Bootstrapping:** Protocol-owned liquidity ensures the market always has depth.  
- **Arbitrage:** Any participant can use the deployed arbitrage contracts to keep YES and NO aligned with the spot price.  
- **Signal quality:** If very few trades occur, the result is that YES and NO prices stay close to the spot price — effectively indicating “no measurable impact” from the proposal. That in itself is a valid signal.  

**Mitigation:** As more traders join, price differences sharpen. Even with modest participation, futarchy markets can still reveal when a proposal has a clear expected impact.

---

## How does futarchy integrate with Snapshot or on-chain votes?

There are three ways DAOs can adopt futarchy:
1. **Advisory** — futarchy runs in parallel, and results are displayed in Snapshot (informing delegates before they vote).  
2. **Veto** — proposals must pass futarchy evaluation to move forward to Snapshot or on-chain execution.  
3. **Autonomous (FAO)** — futarchy oracle automatically triggers execution when YES > NO by threshold.

---

## What happens if YES and NO are very close?

If the difference between YES and NO is below the **threshold** (default 1%), the system recommends **rejection**.  
- This avoids approving proposals where the market is ambivalent.  
- DAOs can tune the threshold higher for big proposals (e.g. treasury moves) to demand stronger evidence.

---

## What metric are we actually optimizing for? Is it always the token price, or can we use other success measures (TVL, user growth, revenue)? 

Futarchy Labs focuses mainly on the use of **token price** because it’s simple, liquid, and aligned with holder value.  
But DAOs can also define other metrics (e.g. TVL, active users) or even composite ones, and run futarchy on those instead.

---

## Who runs the oracle, and can it be trusted?

Advisory and veto futarchy implementations currently uses **Reality.eth + Kleros** arbitration.
Disputes on whether the proposal has been approved can be escalated to Kleros Court.

Fully decentralized FAOs (Futarchy Autonomous Optimizer) contracts instead use the on-chain Futarchy Oracle.
The on-chain oracle directly compares YES vs NO TWAPs during the evaluation period and decides whether the proposal will be executed.

---

## How do you avoid self-dealing proposals?
Markets price in long-term token value, not just short-term effects.  
If a proposal transfers value unfairly (e.g. to a proposer), traders anticipate dilution + future risks, and the YES price will drop.

---

## What are the risks for DAOs?

Like any governance system, futarchy has trade-offs. Key risks include:

- **Thin markets → weak signals.**  
  If liquidity or participation is low, market prices may not reflect real expectations.  
  *Mitigation:* DAOs seed protocol-owned liquidity and provide subsidies to ensure depth.

- **Bad metric choice → Goodhart’s law.**  
  If the chosen metric doesn’t reflect true value (e.g. focusing only on TVL), proposals may optimize for the wrong thing.  
  *Mitigation:* Start with token price, and consider composite metrics carefully.

- **Short-term orientation.**  
  Markets aggregate the preferences of participating token holders. If too few long-term holders trade, short-term price movements may dominate.  
  *Mitigation:* Begin with **advisory futarchy** to build confidence, and for FAOs adopt mechanisms that slow or limit treasury use (e.g. **DAICO-style** structures where funds are released gradually).

---

## Navigation

- ⬆️ **[DAO Operator Guides](./index.md)**  
  Overview and quick links for DAO stakeholders.

- ➡️ **[Adoption Levels](./adoption-levels.md)**  
  Step-by-step paths from advisory to autonomous futarchy.

- ➡️ **[DAO Integration Guide](./integration.md)**  
  Practical setup for liquidity, oracles, and governance hooks.

- ➡️ **[Sponsored Proposals](./sponsorship.md)**  
  How sponsorship works and when discounts apply.
