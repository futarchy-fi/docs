# Live Systems and Public Repos

This page lists public surfaces and repositories. It is not a private deployment
runbook and does not include credentials, signer instructions, or internal
operator procedures.

## Public sites

| Surface | URL | Purpose |
|---|---|---|
| Futarchy interface | [futarchy.fi](https://futarchy.fi/) | Live conditional market interface |
| Documentation | [docs.futarchy.fi](https://docs.futarchy.fi/) | Public documentation and vision hub |
| Status | [status.futarchy.fi](https://status.futarchy.fi/) | Service status |
| Bayes Market | [bayes.futarchy.ai](https://bayes.futarchy.ai/) | Experimental Bayesian prediction-market engine |

## Public repositories

| Repo | Purpose |
|---|---|
| [docs](https://github.com/futarchy-fi/docs) | This documentation site |
| [interface](https://github.com/futarchy-fi/interface) | Public futarchy.fi frontend |
| [futarchy](https://github.com/futarchy-fi/futarchy) | Smart contracts for futarchy and conditional markets |
| [futarchy-indexers](https://github.com/futarchy-fi/futarchy-indexers) | Indexing infrastructure for on-chain market data |
| [futarchy-api](https://github.com/futarchy-fi/futarchy-api) | Market data API |
| [FAO](https://github.com/futarchy-fi/FAO) | Futarchy Autonomous Optimizer contracts |
| [agents](https://github.com/futarchy-fi/agents) | Futarchic agent organization research and prototypes |
| [bayes-market](https://github.com/futarchy-fi/bayes-market) | Bayesian prediction-market engine |

## Contract references

Contract addresses can change by chain and deployment. Public docs should link to
verified explorer pages or public repository constants when available.

Known conceptual components include:

- `FutarchyFactory` for creating proposal markets,
- `FutarchyProposal` instances for market-specific state,
- `FutarchyRouter` for split, merge, and redeem operations,
- Gnosis Conditional Token Framework contracts,
- ERC-20 wrappers around conditional positions,
- Reality.eth / Kleros resolution paths for current advisory/veto-style markets.

For mechanics, see [Proposal Lifecycle](protocol/proposal-lifecycle.md) and
[Custody and Oracles](protocol/custody-and-oracles.md).

## What is intentionally omitted

This page does not publish:

- operational credentials,
- non-public signer coordination,
- internal hostnames or SSH instructions,
- private incident runbooks,
- private contact lists,
- internal-only wiki material.
