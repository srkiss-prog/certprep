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
