# Sponsored Proposals

Sponsored Futarchy lets **activist investors and external contributors** fund proposals and earn discounted tokens **when** their ideas add measurable value. It brings *new capital + new ideas* into the DAO while keeping incentives aligned with tokenholders.

---

## What It Is (in one minute)

- Anyone can **sponsor** a proposal by posting funds in a DAO‑approved currency (e.g., **sDAI**, stablecoin, **WETH**).  
- Proposals are **selected** into a monthly evaluation slot (see “Slot Selection”).  
- The DAO runs an **advisory futarchy evaluation** (YES vs NO markets with a threshold).  
- If futarchy approves (and any required DAO vote passes), sponsors can **buy tokens at a discount** (vesting).  
- A small **at‑risk fraction** of the sponsorship (default **5%**) subsidizes markets if a proposal fails (anti‑spam + better signals).

---

## Why It Matters for DAOs

- **Capital inflow** without selling indiscriminately—only value‑creating proposals unlock discounted tokens.  
- **More ideas** from outsiders, not just insiders.  
- **Credibly neutral** selection + evaluation (market‑driven, transparently priced).  
- **Aligned ownership**—discount flows to those who take risk on value creation.

---

## Core Mechanics

### Sponsorship Deposit (DAO‑configured)
- **Currency:** DAO chooses the unit (e.g., sDAI / USDC / WETH).  
- **Minimum:** DAO sets a **minimum sponsorship amount** (to avoid spam).  
- **At‑risk fraction:** **5%** of the *purchase commitment* is earmarked for market subsidies if selected and the proposal **fails** futarchy or is later **rejected**. If the proposal **passes**, the at‑risk fraction is **refunded**.  
- **Refunds:**  
  - **Not selected:** sponsor can withdraw or roll to next cycle (default: full refund).  
  - **Selected but fails/rejected:** at‑risk portion is spent; the remainder is refunded.  
  - **Selected and passes:** purchase commitment is used to buy discounted tokens; vesting applies.

### Discount & Vesting (DAO‑configured)
- **Default discount:** **33%** (i.e., **+50%** bonus tokens for the same spend).  
- By policy:
  - **25%** of extra tokens → **Sponsor**  
  - **25%** of extra tokens → **Futarchy Protocol** (protocol reward)  
- **Vesting:** default **linear 12 months** (DAO can change; can vary per sponsorship program).

### Slot Selection (cadence & method)
- **Cadence:** start **monthly**.  
- **Mechanism:** default **top‑by‑sponsorship** at the selection event (after an ~2‑week window).  
  - *Option:* **weighted lottery by sponsorship** (keep as a future toggle).  
- **Rollover:** unselected proposals may roll into the next window unless withdrawn.

---

## DAO Governance & Execution

Two standard paths after a **positive futarchy evaluation**:

**(A) Requires DAO action (on‑chain change, treasury move, etc.)**  
- A **DAO vote** is held after futarchy recommends approval.  
- The **bonus/discount** for sponsors is *pre‑approved* by the DAO within the program, or
  proposals can stipulate whether a **DAO representative** may **suspend** the discount before payment is executed.

**(B) Independent project funded only by the sponsorship**  
- No DAO vote needed if execution does not touch DAO treasury or parameters, and sends only sponsorship money to a contractor.
- **Payments** to the contractor can be staged (milestones).
- A **DAO representative** may **veto** the stream at any time; the sponsor
  receives any **unspent funds back**, plus a **pro‑rata** portion of the promised discounted tokens based on funds spent to date.  
- Proposals specify whether **discount is revocable** by a DAO representative.

> **Multisig custody:** We recommend a **2‑of‑3 multisig** (e.g., two DAO reps + one trusted technical party) to manage funds for sponsorship and futarchy liquidity.  
> The same multisig may allocate liquidity to evaluation markets and settle outcomes.

---

## Roles & Responsibilities

**DAO**
- Configure program parameters (currency, minimum, discount %, vesting, at‑risk %).
- Approve overall liquidity and **who** can allocate it (multisig).  
- Define selection cadence and method (top‑by‑sponsorship; optional weighted lottery).  
- Choose governance hook (Advisory, Veto/Kleros, or FAO — Futarchy Autonomous Optimizer).

**Sponsor**
- Post deposit (purchase commitment + at‑risk fraction).  
- Draft proposal; update during the 2‑week window.  
- If selected and approved: receive **discounted tokens** on vesting schedule.  
- If selected and fails/rejected: absorb at‑risk fraction (default 5%); remainder refunded.

**Futarchy Labs / Operators**
- Run conditional spot markets (YES/NO), arbitrage bots, solver integrations.  
- Provide evaluation infra (TWAP computation, market UX).  
- Optionally serve as third signer on the 2‑of‑3 multisig.

---

## Process & Timeline (monthly cadence)

**Window 1 (≈ 2 weeks) — Sponsorship period**  
- Sponsors submit deposits and proposal drafts; can amend and add funds.  
- End of window: **selection event** picks **top‑by‑sponsorship** (default).  
  - Unselected proposals can roll over to next month.

**Window 2 (≈ 1 week) — Futarchy evaluation**  
- YES/NO markets open for the selected proposal; DAO‑seeded liquidity is deployed.  
- Threshold check: **YES > NO + threshold** (default 1%) using TWAP over the window.  

**Window 3 (≈ 1 week) — Decision & settlement**  
- **Path A:** DAO vote if required (on‑chain changes/treasury).  
- **Path B:** Independent project executes per proposal; DAO rep retains veto if configured.  
- If approved: **discounted tokens** are purchased and start **vesting (12m)**.  
- If failed/rejected: **at‑risk 5%** is spent on market subsidies; remainder refunded.
- YES/NO markets can remain open for this window until the proposal has been approved definitively.
- Outcome finality via **Reality.eth + Kleros** (oracle does not publish thresholds; it resolves outcomes and any governance checks).

> **Throughput:** Expect **1 sponsored proposal per month**.  
> Liquidity can often support this + **1 non‑sponsored advisory proposal** per month.

---

## Parameters (recommended defaults)

- **Currency:** sDAI (or stablecoin/WETH; DAO decides).  
- **Minimum sponsorship:** set by DAO.  
- **At‑risk fraction:** **5%** of purchase commitment (spent if fail/reject).  
- **Discount:** **33.33%** (default), with **50% extra tokens** split as **25% sponsor / 25% Futarchy Protocol**.
- **Vesting:** **12 months linear** (applies to discounted tokens and protocol fee share).  
- **Threshold floor:** **1%** YES over NO (raise for high‑stakes changes).
- **Threshold scaling:** per “Thresholds vs. Sponsorship Size”.
- **Selection cadence:** **monthly**; **top‑by‑sponsorship** (optionally: weighted lottery).  
- **Multisig:** **2‑of‑3** (2 DAO reps + 1 technical co‑signer).
- **Governance hook:** **Advisory** by default; **Veto/Kleros** or **FAO (Futarchy Autonomous Optimizer)** as the DAO matures.
- **Sponsored tokens pool:** pre-set cap held by 2-of-3 multisig; program pauses when depleted.

---

## Thresholds vs. Sponsorship Size (impact justification)

Why scale the futarchy **threshold** with the sponsorship size?  
Because the discounted **bonus tokens** are effectively a **prize** for creating a value-adding proposal.
To keep that prize reasonable, we recommend setting the **Threshold scaling:** so that it represents an effective **5% prize cap**:
the total bonus tokens (at market value) should be ≤ **5%** of the **expected increase in market cap** implied by futarchy.

**Compute it**

Let:
- `S` = sponsorship amount (e.g., 100,000 sDAI)
- `d` = discount (e.g., `0.3333` for 33.33%)
- `M` = current circulating token market cap
- `prize_cap` = `0.05` (5%)
- **Bonus value at market** = `S × d / (1 − d)`  
  - 33.33% discount → bonus ≈ `0.5000 × S` (≈ 50% of S)

Then:
- **Required impact (market cap increase)**  
  `Impact_required = Bonus_value / prize_cap`
- **Threshold (%), applied to YES vs NO TWAP**  
  `Threshold = max(1%, Impact_required / M)`

**Example (your default numbers):**  
`S = 100k, d = 0.3333` ⇒ `Bonus ≈ 50k` ⇒ with 5% cap → `Impact_required = 1,000,000`.  
If `M = 50,000,000`, then `Threshold = 1,000,000 / 50,000,000 = 2%`.

**Rule of thumb**
- 33.33% discount: `Threshold ≈ 10.0 × (S / M)` 
- Always floor at **1%**.

> **Note:** If using the **33.33%** program where **+50% extra tokens** are split **25% sponsor / 25% Futarchy Protocol**, **Bonus_value** is the **total** extra tokens (sponsor + protocol), since both are justified by the same measured impact.

---

## Sponsored Tokens Pool (Cap)

The DAO should pre-allocate a **pool of tokens** for sponsored sales, held by the program multisig (recommended **2-of-3**).  
- This pool **caps** total discounted tokens across approved sponsored proposals.  
- When the pool is **depleted**, the program **pauses** until the DAO replenishes it by vote.  
- Unused tokens **return to treasury** at program sunset (or at a review checkpoint).

---


## Risks & Safeguards

- **Spam/low‑quality proposals** → minimum sponsorship and **5% at‑risk**; market costs discourage noise.  
- **Self‑dealing** → markets price long‑term value; DAO/rep can veto; thresholds can be higher for sensitive changes.  
- **Thin markets** → DAO‑seeded liquidity; at‑risk subsidies; arbitrage keeps YES/NO coherent.  
- **Duplicated ideas** → initial **central curation** may reject duplicates; future IP/attribution features planned.

---

## Worked Example (numbers)

- Sponsor commits **$100k sDAI**; **at‑risk 5% = $5k**.  
- DAO discount is **33%** → sponsor receives **+25% tokens** for the $100k if approved (vesting 12m), with Futarchy Protocol receiving another +25% tokens. 
- If **selected & passes**: $100k buys discounted tokens; **$5k** refunded (was at‑risk, unused).  
- If **selected & fails/rejected**: **$5k** spent to subsidize markets; **$95k** refunded.  
- If **not selected**: sponsor may withdraw or roll to next month (default: full refund).

*Alternative:* If DAO sets **33% discount**, **+50% tokens** are minted relative to full‑price: **25%** of the extra tokens → **Sponsor**; **25%** → **Futarchy Protocol** (both vest 12m).

---

## Cross‑References

- **Adoption levels:** see [Adoption Levels](./adoption-levels.md) (Advisory‑first; Sponsored as Level 2).  
- **How to wire it up:** see [DAO Integration Guide](./integration.md).  
- **Common concerns:** see [DAO FAQ](./faq.md) (manipulation, liquidity, oracle/Kleros, thresholds).

---

## Navigation

- ⬆️ **[DAO Operator Guide](./README.md)**
- ⬅️ **[DAO FAQ](./faq.md)**
- 🔁 **[Using Futarchy in Practice](../using-futarchy-in-practice.md)**
