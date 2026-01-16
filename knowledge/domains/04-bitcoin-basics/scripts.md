Below is a **precise, script-level comparison of Bitcoin output types**, followed by a **dedicated on-chain analyst perspective** that focuses on what can be inferred from blockchain data alone.

---

## Bitcoin Script / Output Types — Technical Comparison

### 1. P2PKH — _Pay to Public Key Hash_ (Legacy)

**ScriptPubKey**

```
OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

**Key properties**

- Introduced in early Bitcoin
- Spending reveals:

  - Full public key
  - ECDSA signature

- Address prefix: `1...`

**Pros**

- Simple and transparent
- Widely supported

**Cons**

- Largest on-chain footprint
- No malleability fix
- Worst fee efficiency

---

### 2. P2SH — _Pay to Script Hash_

**ScriptPubKey**

```
OP_HASH160 <scriptHash> OP_EQUAL
```

**Key properties**

- Address prefix: `3...`
- Actual spending conditions hidden until spend
- Enables multisig, timelocks, complex scripts

**Pros**

- Script abstraction
- Reduced output size
- Enables advanced constructions

**Cons**

- Script revealed at spend time
- Still legacy (pre-SegWit)

---

### 3. P2WPKH — _Pay to Witness Public Key Hash_ (SegWit v0)

**ScriptPubKey**

```
0 <20-byte pubKeyHash>
```

**Key properties**

- Native SegWit
- Address prefix: `bc1q...`
- Signature moved to witness (off main tx weight)

**Pros**

- ~40% fee savings vs P2PKH
- Fixes transaction malleability
- Cleaner UTXO set

**Cons**

- Slightly less backward compatible (old wallets)

---

### 4. P2WSH — _Pay to Witness Script Hash_ (SegWit v0)

**ScriptPubKey**

```
0 <32-byte scriptHash>
```

**Key properties**

- SegWit equivalent of P2SH
- Script revealed only when spent
- Ideal for multisig, Lightning funding

**Pros**

- Best fee efficiency for complex scripts
- Malleability resistant
- Clean separation of data

**Cons**

- Requires SegWit support

---

### 5. P2SH-P2WPKH / P2SH-P2WSH — _Nested SegWit_

**ScriptPubKey**

```
OP_HASH160 <redeemScriptHash> OP_EQUAL
```

Redeem script:

```
0 <hash>
```

**Key properties**

- Address prefix: `3...`
- Transitional format

**Pros**

- SegWit benefits with legacy compatibility

**Cons**

- Slightly larger than native SegWit
- Being phased out

---

### 6. P2TR — _Pay to Taproot_ (SegWit v1)

**ScriptPubKey**

```
1 <32-byte outputKey>
```

**Key properties**

- Address prefix: `bc1p...`
- Schnorr signatures
- MAST (Merkelized scripts)

**Pros**

- Best privacy currently available
- Multisig indistinguishable from single-sig
- Script paths hidden unless used
- Smaller signatures

**Cons**

- Newer; tooling still evolving

---

## Compact Comparison Table

| Type          | Address Prefix | Script Visibility | Fee Efficiency | Privacy   | Status       |
| ------------- | -------------- | ----------------- | -------------- | --------- | ------------ |
| P2PKH         | `1`            | Always            | ❌ Low         | ❌ Low    | Legacy       |
| P2SH          | `3`            | On spend          | ⚠️ Medium      | ⚠️ Medium | Legacy       |
| P2WPKH        | `bc1q`         | Always            | ✅ High        | ⚠️ Medium | Standard     |
| P2WSH         | `bc1q`         | On spend          | ✅ High        | ⚠️ Medium | Standard     |
| Nested SegWit | `3`            | On spend          | ⚠️ Medium      | ⚠️ Medium | Transitional |
| P2TR          | `bc1p`         | Hidden by default | ✅✅ Best      | ✅ Best   | Modern       |

---

## On-Chain Analyst View (Critical Comparison)

This section answers: **what can be inferred by observing the blockchain only**.

### Fingerprinting & Heuristics

| Script Type   | Analyst Can Infer                                                            |
| ------------- | ---------------------------------------------------------------------------- |
| P2PKH         | Single-sig wallet, legacy software, likely older UTXOs                       |
| P2SH          | Multisig _possible_ but unknown until spend                                  |
| P2WPKH        | Modern wallet, single-sig very likely                                        |
| P2WSH         | Multisig / Lightning / complex script likely                                 |
| Nested SegWit | Wallet upgrade in progress                                                   |
| P2TR          | **Impossible to distinguish single-sig vs multisig unless script path used** |

---

### Privacy Leakage at Spend Time

| Type               | Reveals Script?          | Reveals PubKeys? |
| ------------------ | ------------------------ | ---------------- |
| P2PKH              | Yes                      | Yes              |
| P2SH               | Yes (full script)        | Yes              |
| P2WPKH             | Yes                      | Yes              |
| P2WSH              | Yes (only executed path) | Yes              |
| P2TR (key path)    | ❌ No                    | ❌ No            |
| P2TR (script path) | Partial (only branch)    | Partial          |

**Taproot is a major privacy upgrade**:
From an analyst perspective, _most Taproot spends look identical_.

---

### UTXO Set & Economic Signals

- **P2PKH dominance** → old coins, custodial cold storage, dormant supply
- **P2WSH spikes** → Lightning channel opens/closes
- **P2TR growth** → modern wallets, institutional-grade custody
- **Nested SegWit decline** → ecosystem maturation

---

### Fee & Congestion Analytics

Analysts can infer:

- Fee sensitivity of wallet software
- Adoption curve of protocol upgrades
- Batch spending behavior (esp. P2TR + Schnorr aggregation)

---

## Strategic Summary

- **Developer view**:
  P2TR is the endgame — clean, private, efficient.

- **On-chain analyst view**:
  Taproot dramatically reduces inference power; legacy scripts remain the richest source of behavioral signals.

- **Security & privacy takeaway**:
  Moving from **P2PKH → P2WPKH → P2TR** is not cosmetic — it fundamentally alters what blockchain observers can learn.

If you want, next we can:

- Walk through **real transactions** and classify them as an analyst would
- Map script types to **Lightning internals**
- Do a **CBP-style exam drill** based on this topic
