# Overview

Mining is proof‑of‑work: miners hash block headers to find a hash below the target. The block reward equals the block subsidy (new coins) plus transaction fees. Subsidy halves roughly every 210,000 blocks, so fees make up more of miner revenue over time. Difficulty adjusts to keep block times near 10 minutes by changing the target, not the hash function. Coinbase transactions create new coins and have a maturity period. Only blocks in the best chain receive rewards; stale blocks do not.

# Target

difficulty ↑
⇒ target ↓
⇒ valid hash range shrinks
⇒ hashes must be numerically smaller
⇒ most-significant bits must be zero
⇒ more leading zeros appear

**Target defines how rare a valid hash is.
Rarer hashes → lower target → higher difficulty.**

| Target | Difficulty |
| ------ | ---------- |
| High   | Low        |
| Low    | High       |

**Target** (in Proof-of-Work, e.g. Bitcoin) is:

> **The maximum numeric value a block hash is allowed to have in order to be considered valid.**

Formally:

```
valid block ⇔ hash(block_header) ≤ target
```

---

## Precise definition

- The hash function (Bitcoin: double SHA-256) outputs a **256-bit integer**
- All possible hashes are in the range:

```
0 ≤ hash ≤ 2²⁵⁶ − 1
```

- The **target** is a 256-bit integer inside that range
- Any hash **numerically less than or equal to the target** satisfies Proof-of-Work

---

## What target controls

The target directly controls **how hard mining is**:

```
P(success per hash) = target / 2²⁵⁶
```

- **Higher target** → more valid hashes → easier mining
- **Lower target** → fewer valid hashes → harder mining

---

## Relationship to difficulty

Difficulty is derived from the target:

```
difficulty = max_target / current_target
```

- `max_target` = easiest allowed target (difficulty = 1)
- Target ↓ ⇒ Difficulty ↑

So:

- **Target** = protocol-level threshold
- **Difficulty** = human-readable measure of how small that threshold is

---

## Where target appears in Bitcoin

- Stored in block headers as **`nBits`** (compact encoding)
- Fully expanded to a 256-bit integer during block validation
- Enforced by every full node

---

## Minimal intuition

> **Target defines how small a hash must be to “win.”
> Smaller target → rarer win → more work required.**

**Correct answer: B) bits (compact target)**

Here’s the precise reasoning, step by step.

---

## What “retarget” means in Bitcoin consensus

Bitcoin uses **Proof of Work** with a **difficulty retarget** every 2016 blocks (~2 weeks).
The goal is to keep the average block interval close to **10 minutes**, regardless of how much hash power joins or leaves the network.

This retargeting is a **consensus rule**, not a miner choice.

---

## Which header field represents difficulty?

The Bitcoin block header has these fields:

- `version`
- `previous block hash`
- `merkle root`
- `timestamp`
- **`bits`**
- `nonce`

The **`bits` field** encodes the **target threshold** that a block hash must be below.
It is a _compact representation of the target_, often called the **compact target**.

👉 **Difficulty is derived from the target, and the target is encoded in `bits`.**

---

## Why “indirectly through consensus parameters”?

Because:

- Consensus rules define:
  - retarget interval (2016 blocks)
  - target block time (10 minutes)
  - maximum adjustment factor (×4 / ÷4)

- From these rules, nodes **compute a new target**
- That target is then **encoded into the `bits` field**
- Miners must use that `bits` value, or their block is invalid

So:

- Consensus does **not** say “set difficulty to X”
- Consensus says “compute a new target using these rules”
- That computed target ends up **stored in `bits`**

That’s why the question says **“adjusted indirectly through consensus parameters”**

---

Miners cannot set arbitrary timestamps far in the future. Bitcoin enforces consensus validation limits on block timestamps.
