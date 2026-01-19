# Fast-Fail Patterns

Recurring mistakes, traps, and “looks true but isn’t” patterns found during drills.

## Hash Functions (Bitcoin)

- Confusing hashing with encryption: “looks random” ≠ secrecy; hashes don’t conceal guessable inputs.
- Mixing up collision resistance vs second-preimage resistance (the “any two” vs “given one” distinction).
- Assuming a `txid` uniquely encodes/contains the transaction data rather than merely identifying/committing to it.
- Reversing `HASH160` order (it’s `RIPEMD-160(SHA-256(x))`, not the other way around).
- Treating collision breaks as “everything stops” (PoW search is primarily preimage-style, not collision-finding).
- Assuming address checksums provide adversarial security rather than typo detection.
- Forgetting that transaction ordering matters for merkle roots (set vs sequence confusion).
- Mixing up what commits to witness data in SegWit (`txid`/header merkle root vs witness commitment / `wtxid` concepts).
- Assuming hashes provide authentication or confidentiality without a secret (MAC) or signature.

## Symmetric vs Asymmetric Cryptography

- Mixing up confidentiality vs authenticity: signatures/MACs don’t make data secret; encryption doesn’t automatically authenticate unless AEAD/MAC is used.
- “Encrypt with private key for secrecy” confusion: private-key “encryption” is effectively signing; confidentiality uses recipient’s public
  key.
- Assuming asymmetric crypto removes all key-distribution problems: you still must authenticate public keys to avoid MITM.
- Claiming symmetric systems provide non-repudiation: shared keys mean either party could have generated the MAC.
- Confusing key exchange (DH/ECDH) with encryption: DH agrees a shared secret; you still need symmetric encryption for data.
- Forgetting that unauthenticated DH/ECDH is MITM-vulnerable (you must authenticate identities/keys).
- Reusing an AEAD nonce/IV under the same key (can break confidentiality/integrity even if “the plaintext is different”).
- Treating a Bitcoin address as a public key or assuming transactions are encrypted on-chain (Bitcoin primarily uses signatures, not confidentiality).

## Digital Signatures

- Confusing signatures with encryption: signatures don’t hide data; they authenticate/ensure integrity.
- “Encrypt with private key” confusion: that’s conceptually signing; confidentiality uses public-key encryption to a recipient.
- Over-claiming what a signature proves: it proves key authorization of bytes, not intent, truth, or meaning.
- Mixing MACs and signatures: MACs require shared secrets and don’t provide public verifiability/non-repudiation.
