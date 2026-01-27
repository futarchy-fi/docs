# Futarchy.FI Documentation Style Guide

## Goals
Our documentation should be:
- Clear to new readers
- Precise for integrators and power users
- Honest about what the protocol does and does not guarantee
- Consistent in terminology, links, and structure

## Voice and tone
- Use direct, concrete language.
- Prefer short sentences.
- Avoid hype (“revolutionary”, “guaranteed”, “always wins”).
- Prefer “signal”, “measurement”, “conditional claim” over “prediction”.

## Audience and page metadata
Every page MUST start with:

> **Type:** Tutorial | How-to | Reference | Explanation  
> **Audience:** General | DAO Operator | Trader | Sponsor  
> **Status:** Stable | Draft | WIP

## Terminology (must be consistent)
### Core terms (preferred)
- **Decision market** (preferred)  
  Optional synonyms: “counterfactual market”, “conditional spot market”
- **Conditional token**: a token redeemable for the underlying asset if an outcome is selected.
- **YES** and **NO**: outcomes for a proposal market.
  - If PASS/FAIL is used, write **YES (PASS)** once, then use YES/NO consistently.

### Forbidden / must-qualify terms
- “Prediction market” MUST NOT be used unless:
  - we explicitly contrast it with decision markets, OR
  - we clarify “not oracle-resolved on an external future event.”

## The decision rule (canonical snippet)
Wherever the signal is described, reuse identical wording:

> **Decision Rule (Signal):** Compare the TWAP of the YES market price vs the TWAP of the NO market price over the trading window. The higher TWAP indicates the higher conditional spot valuation under that decision branch.

(If the implementation is more specific, add a single “Implementation details” subsection and link to it.)

## Document structure
Use this default structure unless it clearly does not apply:
1. What this page is for (1–3 sentences)
2. Prerequisites / assumptions
3. Main content (task steps, concept explanation, or reference tables)
4. Failure modes / gotchas (if relevant)
5. Links to related pages (2–6 bullets)

## Headings
- Use sentence case headings.
- Avoid deeply nested headings (> H3) unless necessary.

## Links
- Use descriptive link text (not “click here”).
- Prefer relative links within the repo.
- If a page is WIP, mark it in the link text: “(WIP)”.

## Formatting conventions
- Use bullet lists for lists.
- Use numbered lists for procedures.
- Use code fences with language tags (e.g. ```solidity, ```bash).
- Use blockquotes for notes:

> **Note:** …
> **Warning:** …

## Diagrams
- Prefer simple diagrams that clarify:
  - lifecycle (create market → trade → measure TWAP → decision → settlement)
  - token flows (mint/split/redeem)
- Mermaid is allowed if it renders well on GitHub.

## Risk language
- Never claim a guarantee unless it is purely mechanical and enforced by code.
- When describing risks, distinguish:
  - protocol/mechanical risks (contracts, settlement, measurement)
  - market risks (liquidity, slippage, manipulation)
  - governance risks (interpretation, close calls, social layer)

## “Done” criteria for a page
A page is **Stable** when:
- It has metadata (Type/Audience/Status)
- It uses canonical terminology
- It links to Deployments & Addresses when relevant
- It links to Risks & Guarantees when relevant
- It has no TODOs visible to readers
