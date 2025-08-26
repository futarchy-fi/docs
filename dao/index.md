## How Token Futarchy Works

### Motivation

In 2024, MakerDAO rebranded to “Sky.” Within ten days, the token lost ~20% of its market value — over $500M.  
Many believed the rebrand caused this collapse, but without a way to isolate its effect it was impossible to know for sure.  

**Futarchy solves this.** By running *two parallel markets* — one where the rebrand happens, and one where it does not — the DAO could have seen the expected token price impact *before committing*.  

---

### Prediction vs Futarchy Markets

It helps to distinguish **prediction markets** from **futarchy markets**:

- **Prediction market:** “What’s the probability event X will happen?”  
- **Futarchy market:** “What will the token price be if we do X vs if we don’t?”  

Instead of betting on the chance of an outcome, futarchy isolates the *value impact of a decision*.

---

### Futarchy Evaluation

When a proposal is introduced, futarchy creates two conditional markets:

- **YES Market** — trades the token price *if the proposal passes*.  
- **NO Market** — trades the token price *if the proposal fails*.  

Traders buy and sell in these pools, revealing their beliefs about the impact.

After a decision window (default 7 days), the DAO compares the two average prices (TWAP).  
- If **YES > NO** by a threshold (default 1%), the proposal is recommended.
- Otherwise, it is rejected.

```mermaid
flowchart LR
  Y["YES price (TWAP)"] --> C{"YES > NO + Threshold?"}
  N["NO price (TWAP)"]  --> C
  C -- Yes --> R1["Recommendation: Approve"]
  C -- No  --> R2["Recommendation: Reject"]
```

---

### Trader Perspective (Illustration)

Even if this guide is for DAOs, seeing how traders act makes it clear:

- **Supporter’s trade:** *“I only want to invest if this proposal passes.”*  
  → They buy into the YES Market.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontSize':'12px','primaryColor':'#eef6ff','primaryBorderColor':'#7aa2ff','lineColor':'#7aa2ff'}}}%%
flowchart LR
  A["Buy in YES market (conditional)"] --> B{"Proposal approved?"}
  B -- Yes --> C["Redeem → tokens (investment executed)"]
  B -- No  --> D["Refund → funds returned"]
  classDef box fill:#f9f9ff,stroke:#7aa2ff,rx:6,ry:6;
  class A,B,C,D box;
```

- **Opponent’s trade:** *“I want to sell my tokens if this proposal passes.”*  
  → They sell into the YES Market (conditional exit).  

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontSize':'12px','primaryColor':'#eef6ff','primaryBorderColor':'#7aa2ff','lineColor':'#7aa2ff'}}}%%
flowchart LR
  A["Sell in YES market (conditional)"] --> B{"Proposal approved?"}
  B -- Yes --> C["Settle → stable (exit completed)"]
  B -- No  --> D["Revert → keep tokens"]
  classDef box fill:#f9f9ff,stroke:#7aa2ff,rx:6,ry:6;
  class A,B,C,D box;
```

These individual bets aggregate into a market price signal — the information the DAO cares about.

---

### Filtering Out Noise

A common question: *“But token prices move for many reasons. How can we know it’s about the proposal?”*  

Futarchy answers this by comparing **two parallel markets** — *with* vs *without* the proposal.  
Because both markets are subject to the same external factors, the **difference between them isolates the causal impact of the decision itself**.

(See the FAQ for more details on manipulation and noise.)

---

## Benefits for DAOs

- **Confidence** — tokenholders see measurable market signals before committing to proposals.  
- **Legitimacy** — decisions are backed by a credibly neutral process, giving even controversial outcomes a clear justification.  
- **Aligned ownership** — futarchy shifts token ownership toward participants who believe in and support the DAO’s long-term direction.  
- **New capital and ideas** — the Sponsored Proposals mechanism attracts outside sponsors who bring both funding and fresh proposals.  

> **Note:** Futarchy Evaluation only produces a **recommendation**.  
> The DAO chooses how to use it:
> - **Advisory** — market signal informs governance  
> - **Veto** — proposals must pass futarchy to move forward  
> - **Autonomous (FAO)** — proposals are automatically executed if futarchy approves  

---

---

## Learn More

- [FAQ](./faq.md) — answers to common questions (manipulation, noise, liquidity, Snapshot).  
- [Adoption Levels](./adoption-levels.md) — detailed guide to Milestone, Advisory, Sponsored, and FAO.  
- [Integration Guide](./integration.md) — how to set up futarchy in your DAO (liquidity, oracles, timelines).  
- [Sponsored Proposals](./sponsorship.md) — how sponsorship works, how DAOs attract capital, and how sponsors are rewarded.  

