# DAO FAQ

## Can futarchy markets be manipulated?

Markets can always be influenced in the short term — but futarchy is designed to make manipulation *costly*.  
- Conditional markets are subsidized and liquid, so any trader trying to “push” prices without information creates an arbitrage opportunity.  
- Informed traders (“wolves”) profit by trading against uninformed manipulators (“sheep”), which pulls prices back to true expectations.  
- The DAO can use **time-weighted average price (TWAP)** over the decision window, making last-minute pumps ineffective.

The net result: attempts at manipulation usually transfer money from manipulators to informed traders, while the final prices remain accurate.

---

## How does futarchy isolate the effect of a proposal, when token prices move for many reasons?

This is a core feature of futarchy. Instead of watching the token’s live market, we compare **two parallel markets**:  
- **YES Market** — token value *if the proposal passes*.  
- **NO Market** — token value *if the proposal fails*.  

Because both YES and NO markets face the same external noise (macro conditions, BTC price moves, etc.), the **difference between them isolates the causal impact of the decision itself**.

---

## Who provides liquidity for these markets?

By default, the **DAO itself seeds protocol-owned liquidity** into the YES/NO pools (e.g. $100k).  
- This ensures enough depth that small trades don’t move prices too much (e.g. a $500 trade moves ~2%).  
- The DAO earns LP fees back.  
- Optionally, outside LPs can also participate, but protocol-owned liquidity is the baseline.

---

## What if there isn’t enough participation?

Markets are bootstrapped with:
- **Protocol subsidies** (seeding liquidity, rewarding early traders).  
- **Arbitrage bots** run by Futarchy Labs to keep YES + NO consistent with the spot market.  
- Incentives for **sponsors** and traders who bring information.  

Even with modest participation, the existence of subsidy and arbitrage ensures the prices remain informative.

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
