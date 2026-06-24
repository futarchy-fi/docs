# Public Market Launch Runbook

This is a public-safe outline for launching a futarchy market. It intentionally
does not include private signer instructions, internal service credentials, or
operator-only incident procedures.

## 1. Define the decision

Write the proposal in a way that can resolve to YES or NO.

Good market questions are:

- specific,
- tied to one decision,
- clear about the governance source of truth,
- clear about when the decision is final.

Avoid bundling multiple unrelated decisions into one market.

## 2. Choose assets

A basic futarchy market needs:

- a project or governance token,
- a trading currency,
- a YES branch,
- a NO branch.

The current protocol uses conditional token positions built on the Gnosis
Conditional Token Framework and wrapped as ERC-20 tokens for AMM compatibility.

## 3. Create the proposal market

At the protocol level, creating a futarchy proposal instantiates:

- an on-chain proposal contract,
- a Conditional Tokens condition,
- wrapped outcome tokens,
- oracle metadata for resolving whether YES or NO occurred.

See [Proposal Lifecycle](../protocol/proposal-lifecycle.md) for the full
protocol view.

## 4. Initialize liquidity pools

Create or identify the conditional pools:

- YES_TOKEN / YES_CURRENCY
- NO_TOKEN / NO_CURRENCY

Liquidity can be provided by the project, sponsors, or outside LPs. Early pilots
usually use project-provided liquidity so the market has enough depth to produce
a useful signal.

## 5. Open trading

During the trading window, participants can buy or sell exposure in either
conditional world. The decision signal is based on comparing prices across the
YES and NO pools, typically with a time-weighted average price.

## 6. Read the signal

The common advisory rule is:

```text
Approve if YES TWAP > NO TWAP + threshold.
Reject otherwise.
```

The threshold is a governance policy choice. A 1 percent floor is a common
starting point, with higher thresholds for larger or riskier decisions.

## 7. Resolve and settle

After the governance outcome is final, the oracle attests which branch occurred.
Winning conditional assets redeem for the underlying asset; losing conditional
assets redeem for zero.

## Public readiness checklist

Before making a market public, confirm:

- the proposal text is unambiguous,
- the resolution source is public,
- assets and token addresses are verified,
- liquidity assumptions are stated,
- the trading window and TWAP window are stated,
- the threshold rule is stated,
- user-facing risk language is visible,
- settlement path is documented.

See [Market Readiness Checklist](market-readiness-checklist.md).
