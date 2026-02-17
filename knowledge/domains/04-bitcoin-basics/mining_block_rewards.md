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

**True.**

---

## Why the nonce alone is insufficient

The Bitcoin block header nonce is **32 bits**, giving:

```
2³² ≈ 4.29 billion possibilities
```

At modern hash rates, miners can exhaust this space **in milliseconds**.

So relying on the nonce alone would stall mining almost instantly.

---

## How miners expand the search space

Miners vary **other block components** to create new block header hashes:

### 1️⃣ **Coinbase transaction**

- Miners modify the **coinbase scriptSig** (often called _extra nonce_)
- This changes the **coinbase txid**
- Which changes the **Merkle root**
- Which changes the block header hash

This is the primary mechanism used in practice.

---

### 2️⃣ **Timestamp**

- Miners may slightly adjust the block timestamp (within consensus limits)
- This also changes the block header hash

---

### 3️⃣ **Transaction ordering / selection**

- Reordering transactions changes the Merkle root
- Less common than extranonce, but still valid

---

## Why the question mentions “coinbase-derived merkle root”

Because:

- The coinbase transaction is **fully controlled by the miner**
- It can be changed arbitrarily without affecting validity
- It gives an effectively unbounded search space

This is standard mining behavior.

---

## Exam-ready answer

> **True.**
> The 32-bit nonce can be exhausted quickly, so miners also vary other block components—most commonly the coinbase transaction, which alters the Merkle root and expands the proof-of-work search space.

These terms come from **cryptocurrency mining pool reward schemes**, primarily in Bitcoin and similar Proof-of-Work networks. They define **how miners are paid** for contributing hash power.

---

## 1️⃣ PPS – Pay Per Share

### Concept

In **PPS**, the pool pays you a **fixed amount for every valid share** you submit, regardless of whether the pool actually finds a block.

A _share_ = proof that you performed work at a certain difficulty threshold (lower than full network difficulty).

### Mechanics

- You submit shares.
- Each share has a mathematically expected value.
- You are paid immediately based on that expected value.
- The pool operator assumes all variance risk.

### Formula (simplified)

[
Payout = Share_Value = \frac{Block_Reward \times (1 - Pool_Fee)}{Network_Difficulty}
]

### Characteristics

| Aspect       | PPS                                      |
| ------------ | ---------------------------------------- |
| Variance     | Very low (stable income)                 |
| Risk         | Pool operator                            |
| Fees         | Higher (typically 3–5%+)                 |
| Suitable for | Small miners who want predictable income |

### Key Insight

You are effectively selling hashpower at a fixed price.

---

## 2️⃣ PPLNS – Pay Per Last N Shares

### Concept

In **PPLNS**, miners are paid only when the pool finds a block, and the reward is distributed among miners who submitted the last **N shares** before the block was found.

No guaranteed payout per share.

### Mechanics

- Pool finds a block.
- Look at the last N shares.
- Reward is distributed proportionally to contribution within those N shares.

### Characteristics

| Aspect       | PPLNS                  |
| ------------ | ---------------------- |
| Variance     | Higher                 |
| Risk         | Miner                  |
| Fees         | Lower (typically 1–2%) |
| Suitable for | Long-term miners       |

### Important Detail

If you disconnect before a block is found, your shares might **not** be included in the payout window.

### Key Insight

PPLNS reduces exploitability and discourages short-term switching behavior.

---

## 3️⃣ Pool Hopping

### Definition

**Pool hopping** is a strategy where miners switch between pools to exploit weaknesses in reward systems (especially older proportional systems).

### Why It Works (in flawed systems)

In simple proportional payout systems:

- Early shares in a mining round are worth more.
- Later shares become less valuable as the round lengthens.

So hoppers:

1. Join a pool at the start of a round.
2. Leave once expected value drops.
3. Move to a “fresh” pool.

This increases their expected return at the expense of loyal miners.

---

## Why PPS and PPLNS Were Developed

| System       | Vulnerable to Pool Hopping? |
| ------------ | --------------------------- |
| Proportional | Yes                         |
| PPS          | No                          |
| PPLNS        | No (designed to resist it)  |

PPLNS specifically fixes the economic flaw that made pool hopping profitable.

---

## Visual Intuition

### PPS

You get paid like a salaried employee — steady income, lower risk.

### PPLNS

You get paid like a commission worker — higher variance, but fair over time.

### Pool Hopping

Like jumping between restaurants right before tips are distributed.

---

## Practical Example (Bitcoin)

F2Pool, Antpool and Slush Pool historically offered different payout models (PPS, PPLNS, score-based variants).

Modern large pools often:

- Offer both PPS and PPLNS options.
- Charge higher fees for PPS due to variance risk.

---

## Summary

| Feature              | PPS                           | PPLNS                 |
| -------------------- | ----------------------------- | --------------------- |
| Payment timing       | Immediate per share           | Only when block found |
| Variance             | Low                           | High                  |
| Fee                  | Higher                        | Lower                 |
| Good for             | Small / stable income seekers | Long-term miners      |
| Resistant to hopping | Yes                           | Yes                   |
