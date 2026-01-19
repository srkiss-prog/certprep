# Definition

Symmetric crypto uses one shared secret key for encryption/decryption (fast, good for bulk data) but has a key-distribution problem. Asymmetric crypto uses a public/private keypair: public-key encryption enables secure key transport; digital signatures provide authenticity + integrity with public verification and non-repudiation (private key signs, public key verifies). In practice, systems use hybrids: asymmetric to agree on/transport a symmetric session key, symmetric (often AEAD) for data. In Bitcoin, asymmetric cryptography is used for signatures, not to encrypt transactions.

# MAC vs AEAD

Below is a **precise, security-engineering–oriented explanation** of **MAC** and **AEAD**, followed by how each maps into **Bitcoin protocol design** and finally how an **on-chain analyst** should reason about them.

---

## 1. MAC (Message Authentication Code)

### What it is

A **MAC** is a cryptographic primitive that provides:

- **Integrity** – the message was not modified
- **Authenticity** – the message was created by someone holding a shared secret

Formally:

```
tag = MAC(key, message)
```

Verification recomputes the MAC and compares tags.

### What it does _not_ do

- ❌ No confidentiality (message is still plaintext)
- ❌ No non-repudiation (anyone with the key could have created it)

### Common constructions

- **HMAC-SHA256** (most common)
- **CMAC (AES-CMAC)**
- **Poly1305** (often paired with ChaCha20)

### Mental model

> “If the MAC verifies, the message is exactly what the key-holder sent.”

---

## 2. AEAD (Authenticated Encryption with Associated Data)

### What it is

**AEAD** combines **encryption + authentication** in a single, misuse-resistant construction.

It guarantees:

- **Confidentiality**
- **Integrity**
- **Authenticity**

And additionally supports:

- **Associated Data (AD)** → authenticated but not encrypted metadata

Formally:

```
(ciphertext, tag) = AEAD_Encrypt(key, nonce, plaintext, associated_data)
```

### Popular AEAD schemes

- **AES-GCM**
- **ChaCha20-Poly1305**
- **AES-CCM**

### Why AEAD exists

Before AEAD, people did:

- Encrypt-then-MAC ❌
- MAC-then-Encrypt ❌
- Encrypt-and-MAC ❌

AEAD enforces the _correct_ composition by design.

### Mental model

> “If decryption succeeds, everything (including metadata) is authentic.”

---

## 3. Relationship Between MAC and AEAD

| Property         | MAC | AEAD |
| ---------------- | --- | ---- |
| Integrity        | ✅  | ✅   |
| Authenticity     | ✅  | ✅   |
| Confidentiality  | ❌  | ✅   |
| Associated Data  | ❌  | ✅   |
| Misuse-resistant | ⚠️  | ✅   |

**Key insight:**
👉 **AEAD internally uses a MAC**, but safely binds it to encryption.

---

## 4. Bitcoin Protocol Context

### Bitcoin does **not** use AEAD

This is intentional.

Bitcoin’s design goals:

- Public verifiability
- Deterministic validation
- No shared secrets
- No confidentiality at consensus layer

### Where MACs appear conceptually (but not directly)

Bitcoin avoids symmetric primitives in consensus rules. Instead it uses:

- **Hash-based integrity** (SHA-256, double-SHA256)
- **Digital signatures** (ECDSA / Schnorr)

| Bitcoin Primitive | Cryptographic Role                        |
| ----------------- | ----------------------------------------- |
| Hash              | Integrity (tamper evidence)               |
| Merkle root       | Batch integrity                           |
| Signature         | Authenticity + authorization              |
| MAC               | ❌ (not suitable for public verification) |
| AEAD              | ❌ (no encryption at consensus layer)     |

### Why MAC / AEAD are unsuitable on-chain

- MACs require **shared secrets**
- AEAD requires **secret keys**
- Bitcoin validation must be:

  - Stateless
  - Public
  - Recomputable by anyone

> A MAC would make a transaction unverifiable without the secret → breaks consensus.

---

## 5. Where AEAD _does_ exist around Bitcoin (off-chain)

### Lightning Network

- Uses **ChaCha20-Poly1305 (AEAD)**
- Protects:

  - Onion routing payloads
  - Channel messages

- Reason: peer-to-peer communication **does** require confidentiality

### Wallet internals

- Seed storage
- Backup encryption
- Hardware wallet communication

These are **not consensus-critical**, so AEAD is appropriate.

---

## 6. On-Chain Analyst Context (Very Important)

### Analyst viewpoint: what you can and cannot infer

| Question                      | MAC / AEAD            | Bitcoin On-Chain      |
| ----------------------------- | --------------------- | --------------------- |
| Can I see encrypted payloads? | Yes (AEAD ciphertext) | No encryption         |
| Can I verify authenticity?    | No (without key)      | Yes (signatures)      |
| Can I detect tampering?       | No (without key)      | Yes (hashes)          |
| Can metadata leak info?       | Yes (AD, lengths)     | Yes (script, amounts) |

### Key analyst insight

> **Bitcoin replaces MACs with signatures and AEAD with transparency.**

This is why on-chain analysis is possible at all.

### Practical analyst mapping

- **MAC tag ≈ signature** (but asymmetric and publicly verifiable)
- **AEAD integrity ≈ script + sighash rules**
- **AEAD associated data ≈ sighash flags / script context**

But:

- No confidentiality
- No hidden metadata at L1

---

## 7. One-Sentence Summary (Exam-ready)

- **MAC** authenticates and protects integrity using a shared secret.
- **AEAD** encrypts _and_ authenticates data safely in one construction.
- **Bitcoin avoids both** at the consensus layer, using hashes and signatures instead.
- **On-chain analysts benefit** because everything required for verification is public.
