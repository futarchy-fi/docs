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
- **Default discount:** **20%** (i.e., **+25%** bonus tokens for the same spend).  
- **Alternative:** DAO can set **33%** discount (i.e., **+50%** bonus tokens). In that case, by policy:
  - **25%** of extra tokens → **Sponsor**  
  - **25%** of extra tokens → **Futarchy Protocol** (protocol fee)  
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
- No DAO vote needed if execution does not touch DAO treasury or parameters.  
- **Payments** to the proposer can be staged (milestones).  
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
- Choose governance hook (Advisory, Veto/Kleros, or FAO).

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
- Outcome finality via **Reality.eth + Kleros** (oracle does not publish thresholds; it resolves outcomes and any governance checks).

**Window 3 (≈ 1 week) — Decision & settlement**  
- **Path A:** DAO vote if required (on‑chain changes/treasury).  
- **Path B:** Independent project executes per proposal; DAO rep retains veto if configured.  
- If approved: **discounted tokens** are purchased and start **vesting (12m)**.  
- If failed/rejected: **at‑risk 5%** is spent on market subsidies; remainder refunded.

> **Throughput:** Expect **1 sponsored proposal per month**.  
> Liquidity can often support this + **1 non‑sponsored advisory proposal** per month.

---

## Parameters (recommended defaults)

- **Currency:** sDAI (or stablecoin/WETH; DAO decides).  
- **Minimum sponsorship:** set by DAO.  
- **At‑risk fraction:** **5%** of purchase commitment (spent if fail/reject).  
- **Discount:** **20%** (default), optional **33%** with **50% extra tokens** split as **25% sponsor / 25% Futarchy Protocol**.  
- **Vesting:** **12 months linear** (applies to discounted tokens and protocol fee share).  
- **Threshold:** **1%** YES over NO (raise for high‑stakes changes).  
- **Selection cadence:** **monthly**; **top‑by‑sponsorship** (optionally: weighted lottery).  
- **Multisig:** **2‑of‑3** (2 DAO reps + 1 technical co‑signer).  
- **Governance hook:** **Advisory** by default; **Veto/Kleros** or **FAO** as the DAO matures.

---

## Risks & Safeguards

- **Spam/low‑quality proposals** → minimum sponsorship and **5% at‑risk**; market costs discourage noise.  
- **Self‑dealing** → markets price long‑term value; DAO/rep can veto; thresholds can be higher for sensitive changes.  
- **Thin markets** → DAO‑seeded liquidity; at‑risk subsidies; arbitrage keeps YES/NO coherent.  
- **Duplicated ideas** → initial **central curation** may reject duplicates; future IP/attribution features planned.

---

## Worked Example (numbers)

- Sponsor commits **$100k sDAI**; **at‑risk 5% = $5k**.  
- DAO discount is **20%** → sponsor receives **+25% tokens** for the $100k if approved (vesting 12m).  
- If **selected & passes**: $100k buys discounted tokens; **$5k** refunded (was at‑risk, unused).  
- If **selected & fails/rejected**: **$5k** spent to subsidize markets; **$95k** refunded.  
- If **not selected**: sponsor may withdraw or roll to next month (default: full refund).

*Alternative:* If DAO sets **33% discount**, **+50% tokens** are minted relative to full‑price: **25%** of the extra tokens → **Sponsor**; **25%** → **Futarchy Protocol** (both vest 12m).

---

## Cross‑References

- **Adoption levels:** see [Adoption Levels](./adoption-levels.md) (Advisory‑first; Sponsored as Level 2).  
- **How to wire it up:** see [DAO Integration Guide](./integration.md).  
- **Common concerns:** see [DAO FAQ](./faq.md) (manipulation, liquidity, oracle/Kleros, thresholds).
