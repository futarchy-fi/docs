# Futarchy Labs Documentation Style Guide

## Goals

Our documentation should be:

- Clear to new readers
- Precise for builders, integrators, traders, sponsors, and researchers
- Honest about what the protocol does and does not guarantee
- Consistent in terminology, links, navigation, and public/private boundaries

## Voice and tone

- Use direct, concrete language.
- Prefer short sentences.
- Avoid hype such as "revolutionary", "guaranteed", or "always wins".
- Prefer "market signal", "measurement", "conditional claim", and "decision
  market" when those terms are precise.
- Explain experimental systems as experimental. Do not imply production
  guarantees before they exist.

## Audience

Write for a mixed audience:

- technically curious readers,
- AI agent builders,
- protocol researchers,
- grant-givers and investors,
- DAO operators,
- traders,
- integrators,
- sponsors.

Not every page needs to address every audience. The page title, introduction,
and navigation placement should make the intended reader obvious.

## Terminology (must be consistent)

### Core terms (preferred)

- **Decision market**: preferred umbrella term for a market used to compare
  actions or policies.
- **Conditional market**: a market whose asset value depends on a future
  decision or outcome.
- **Conditional token**: a token redeemable for the underlying asset if an
  outcome is selected.
- **YES** and **NO**: outcomes for a proposal market.
  - If PASS/FAIL is used, write **YES (PASS)** once, then use YES/NO consistently.
- **Agent market**: a market that scores, selects, funds, or routes work among
  AI agents or agent teams.
- **FAO**: Futarchy Autonomous Optimizer.

### Forbidden / must-qualify terms

- Do not imply that markets guarantee correctness.
- Do not describe internal-only systems, hostnames, signer coordination, private
  contacts, or incident runbooks in public docs.
- Use "prediction market" only when it is the accurate term, or when explicitly
  contrasting prediction markets with decision markets.

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
- Prefer relative links within `content/`.
- Link to Deployments and Addresses when a page mentions live systems.
- Link to Risks and Guarantees when a page mentions guarantees, automation, or
  market authority.

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

## Publication criteria

A public docs page is ready when:

- It has a clear audience and purpose.
- It uses canonical terminology
- It links to Deployments & Addresses when relevant
- It links to Risks & Guarantees when relevant
- It has no raw placeholders visible to readers
- It does not expose internal-only notes, secrets, private operational details,
  private contact data, or non-public source material
