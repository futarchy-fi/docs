# Risks and Guarantees

Futarchy markets provide useful signals, but they do not remove risk.

## Mechanical guarantees

The protocol can mechanically guarantee only what the contracts enforce.

Examples:

- Conditional assets are backed by collateral in the Conditional Token Framework.
- Splitting creates matching conditional claims for mutually exclusive outcomes.
- After resolution, the winning outcome is redeemable according to the reported
  payout vector.
- Merging matched YES and NO positions can recover underlying collateral before
  resolution.

These guarantees depend on the deployed contracts, token approvals, and the
correct oracle path for the market.

## What markets do not guarantee

Markets do not guarantee:

- that a proposal is morally good,
- that a proposal will succeed after approval,
- that liquidity will be deep,
- that prices are manipulation-proof,
- that every relevant participant has traded,
- that the chosen metric captures everything the community values.

Futarchy produces a price signal. Governance, execution, and interpretation still
matter.

## Main risk categories

### Market risk

Thin liquidity, high slippage, low participation, or short trading windows can
weaken the signal.

### Metric risk

If the system optimizes the wrong objective, markets can faithfully optimize the
wrong thing. This is the usual Goodhart problem.

### Oracle risk

Current markets rely on an oracle path to decide whether the YES or NO world
occurred. Bad question wording, unclear resolution sources, or disputes can
delay settlement.

### Smart contract risk

Contracts can have bugs, integration assumptions can be wrong, and wrappers or
AMMs can behave unexpectedly under edge cases.

### Governance risk

Advisory signals can be ignored. Binding signals can be overused before trust is
earned. Projects should increase authority gradually.

## Recommended posture

Start with advisory markets, publish assumptions clearly, use conservative
thresholds for high-stakes decisions, and expand automation only after the system
has produced a track record.
