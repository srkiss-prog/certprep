# Overview

Bitcoin uses the UTXO model: transactions consume existing outputs (inputs) and create new outputs (UTXOs). Inputs reference prior outputs and provide unlocking data; outputs include locking scripts. Fees are implicit: sum(inputs) − sum(outputs). The UTXO set is the spendable state at a given tip. Coinbase transactions create new coins and have a maturity delay. Mempool policy governs relay/mining, while consensus rules govern validity. Address “ownership” is simply the ability to satisfy an output’s script.

# UTXO set

The **UTXO set** is the **current global state of spendable bitcoin**.

More precisely:

> **The UTXO set is the collection of all Unspent Transaction Outputs that exist right now and can still be spent under their locking scripts.**

---

## What exactly is in the UTXO set?

Each entry in the UTXO set is uniquely identified by:

```
(txid, vout)
```

and contains:

- **Amount** (in satoshis)
- **Locking script** (scriptPubKey)
- **Script type** (P2PKH, P2WPKH, P2TR, etc.)

Example (conceptual):

```
(txid = abc123..., vout = 0)
amount = 150,000 sats
scriptPubKey = OP_0 <20-byte pubKeyHash>
```

If an output is **spent**, it is **removed** from the UTXO set.
If a transaction creates new outputs, those outputs are **added** to the UTXO set.

---

## Why the UTXO set matters (critical intuition)

Bitcoin does **not** track balances.

Instead:

- Your “balance” = **sum of UTXOs you control**
- Validation rule: **every input must reference an existing UTXO**

This is what prevents double spending.

---

## How the UTXO set changes (state transition)

For each valid transaction:

1. **Inputs**
   - Reference existing UTXOs
   - Those UTXOs are **deleted** from the set

2. **Outputs**
   - New UTXOs are **inserted** into the set

This is the **state transition function** of Bitcoin.

---

## Where is the UTXO set stored?

- **Every full node** maintains its own UTXO set
- Stored in a high-performance database (e.g. **LevelDB** in Bitcoin Core)
- Size: **multiple gigabytes** (millions of entries)

Nodes **do not** need old spent transactions to validate new ones—only the UTXO set.

---

## Why analysts and engineers care

### For protocol / node perspective

- UTXO set = **consensus-critical state**
- Corruption or mismatch → invalid node

### For on-chain analysis

- UTXO set snapshot = “who can spend what right now”
- Used to:
  - Estimate **liquidity**
  - Detect **dust**
  - Identify **consolidation behavior**
  - Model **coin age** and **supply dynamics**

### For fee and performance considerations

- Spending many UTXOs = larger tx size = higher fees
- UTXO bloat increases node resource requirements

---

## Common misconceptions (fast-fail patterns)

❌ “The blockchain stores balances”
✔️ It stores **transactions**; spendability is tracked via the UTXO set

❌ “UTXOs belong to addresses”
✔️ UTXOs are locked by **scripts**, not addresses

❌ “UTXO set is part of the block data”
✔️ It’s **derived state**, not directly serialized in blocks

---

## One-sentence summary (exam-ready)

> **The UTXO set is the continuously updated set of all unspent transaction outputs that define Bitcoin’s current spendable state and are required to validate new transactions.**

If you want, next we can contrast this with the **account model (Ethereum)** or walk through how a node builds the UTXO set from genesis block → tip.

Here’s a real-life, on-chain style example: the most common way UTXOs are locked and then spent is **P2WPKH** (SegWit “pay to public key hash”). It’s used by most modern wallets for regular payments.

# Example: P2WPKH UTXO (how it’s locked)

### The locking script (scriptPubKey) on the UTXO

This is what the output contains and it **defines the spending condition**:

```
0 <20-byte pubKeyHash>
```

In Script terms, that’s:

```
OP_0 OP_PUSHBYTES_20 <pubKeyHash>
```

Meaning: “To spend this UTXO, provide a witness that proves you control the public key whose HASH160 equals this 20-byte value.”

A concrete-looking example (hex form, typical on-chain):

```
0014d85c2b71d0060b09c9886aeb815e50991dda124d
```

- `00` = OP_0 (SegWit v0)
- `14` = push 0x14 bytes = 20 bytes
- then the 20-byte pubKeyHash

## How it’s spent (the unlocking data)

For P2WPKH, the **scriptSig is empty**, and the unlocking data goes in the **witness**:

Witness stack items:

1. `<signature>` (DER signature + 1-byte sighash type, usually `01` for SIGHASH_ALL)
2. `<public key>` (33-byte compressed pubkey starting with `02` or `03`)

So it looks like:

```
witness[0] = <sig>
witness[1] = <pubkey>
```

## What actually gets executed

When validating, Bitcoin effectively reconstructs a standard script template for P2WPKH spending:

```
OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

And then uses the witness items as inputs:

- It hashes the provided pubkey, checks it matches `<pubKeyHash>`,
- then checks the signature against the transaction digest.

## Mini mental model

- **UTXO output script (scriptPubKey)**: “Here are the rules.”
- **Spending input witness/scriptSig**: “Here is the proof I satisfy the rules.”

If you want, I can also give a _fully concrete_ example by pointing to a specific real transaction/UTXO and showing its exact scriptPubKey + witness (with txid/vout), but you didn’t ask for a specific tx so I kept it generic-but-realistic.

`nLockTime` and `nSequence` are **Bitcoin transaction fields that control _when_ a transaction (or an input) becomes valid**. They enable **absolute** and **relative** time locks.

Think of them as **temporal constraints on spending UTXOs**.

---

# nLockTime / nSequence

## 1️⃣ `nLockTime` — absolute time lock (transaction-level)

### What it is

`nLockTime` is a **32-bit field in the transaction** that says:

> “This transaction is **not valid** until a certain **block height** or **timestamp**.”

### How it works

- If `nLockTime < 500,000,000` → interpreted as **block height**
- If `nLockTime ≥ 500,000,000` → interpreted as **Unix timestamp (seconds)**

Example:

```
nLockTime = 850,000
```

→ transaction can only be included in block **≥ 850,000**

```
nLockTime = 1700000000
```

→ transaction valid only after that Unix time

### Important rule (exam trap)

`nLockTime` is **ignored** unless **at least one input** has:

```
nSequence < 0xffffffff
```

If all inputs have max sequence, the transaction is considered **final**.

---

## 2️⃣ `nSequence` — per-input relative lock & replaceability

### Originally (historical)

- Meant for transaction replacement
- Largely unused until later repurposed

### Today: two main meanings

---

## A) Relative timelocks (BIP-68)

`nSequence` can enforce:

> “This input can only be spent **X blocks or X seconds after the UTXO was confirmed**.”

### Format (simplified)

`nSequence` is a 32-bit field, interpreted as:

- **Most significant bit**:
  - `1` → disable relative locktime
  - `0` → enable relative locktime

- **Type flag**:
  - block-based or time-based

Example:

```
nSequence = 0x00000010
```

→ input spendable **16 blocks** after the UTXO’s confirmation

This is heavily used in:

- Lightning channels
- Payment channels
- Vault constructions

---

## B) Replace-By-Fee signaling (BIP-125)

If **any input** has:

```
nSequence < 0xfffffffe
```

the transaction signals **opt-in RBF**.

Meaning:

> “This transaction may be replaced by another one paying a higher fee.”

---

## 3️⃣ How `nLockTime` and `nSequence` interact

| Field       | Scope       | Type           | Purpose                          |
| ----------- | ----------- | -------------- | -------------------------------- |
| `nLockTime` | Transaction | Absolute       | Not valid before a time/height   |
| `nSequence` | Per input   | Relative / RBF | Delay spend or allow replacement |

### Key interaction rule

- `nLockTime` only works if **at least one input** has a non-final `nSequence`
- Relative timelocks via `nSequence` are **independent** per input

---

## 4️⃣ Real-world examples

### Example 1: “Don’t mine before block 900,000”

```
nLockTime = 900000
nSequence (one input) = 0xfffffffe
```

### Example 2: Lightning penalty delay

```
nSequence = 144
```

→ spendable after ~1 day (144 blocks)

### Example 3: RBF-enabled transaction

```
nSequence = 0xfffffffd
```

---

## 5️⃣ Exam-ready one-liners

- **`nLockTime`**: absolute time/height before which a transaction is invalid
- **`nSequence`**: per-input field enabling relative timelocks or fee replacement
- **Relative timelocks** depend on **UTXO confirmation**, not wall-clock time
- **RBF** is signaled via low `nSequence` values

---

## Common fast-fail misconceptions

❌ “`nSequence` is obsolete”
✔️ It’s critical for Lightning and relative locks

❌ “`nLockTime` delays mempool acceptance”
✔️ It delays **mining validity**, not propagation

❌ “All inputs must be non-final for `nLockTime`”
✔️ Only **one** input needs it

---

If you want, next we can:

- Walk through a **CLTV vs CSV script example**
- Tie this directly to **Lightning commitment transactions**
- Or do **CBP-style trick questions** on `nLockTime` / `nSequence`

# OP_RETURN

OP_RETURN outputs are provably unspendable because OP_RETURN immediately fails script execution, guaranteeing the output can never be spent and allowing nodes to safely exclude it from the UTXO set.

OP_RETURN exists to allow small, explicit data commitments on-chain in a way that is provably unspendable, economically costly, and does not bloat the UTXO set, preserving long-term node scalability.
