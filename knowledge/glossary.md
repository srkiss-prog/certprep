# Glossary

Canonical definitions for CBP/Bitcoin terms used across all domains.

## Hashing & Integrity

- Hash function: Deterministic function that maps arbitrary-length input to a fixed-length digest.
- Digest (hash): Fixed-length output of a hash function for a given input.
- Preimage resistance: Given a digest, infeasible to find an input that hashes to it.
- Second-preimage resistance: Given a specific input, infeasible to find a different input with the same digest.
- Collision resistance: Infeasible to find any two distinct inputs that hash to the same digest.
- Avalanche effect: Small input change produces an unpredictable, widespread change in the digest.
- Hash pointer: Reference to data plus its hash, enabling tamper-evident linking.

## Bitcoin-Specific Hash Uses

- SHA-256: 256-bit cryptographic hash used heavily in Bitcoin.
- Double-SHA256: Applying SHA-256 twice to bytes; used for block header hashing and legacy `txid`.
- RIPEMD-160: 160-bit hash used (after SHA-256) to create shorter identifiers in Bitcoin contexts.
- HASH160: `RIPEMD-160(SHA-256(x))`; used for P2PKH pubkey-hash and P2SH script-hash identifiers.
- Merkle tree: Hash tree that commits to a list of items and supports efficient inclusion proofs.
- Merkle root: Root hash of a merkle tree; in Bitcoin it commits to a block’s transaction list.
- Block header: Compact block metadata that is hashed for PoW and contains the previous block hash and merkle root.
- Target: Threshold value a block header hash must be below to be valid under PoW.
- Difficulty: Network-adjusted parameter that effectively changes the target so blocks arrive on schedule.
- Hashrate: Approximate rate of hash computations per second performed by miners.

## Transactions & SegWit

- txid: Transaction identifier traditionally computed as double-SHA256 of the non-witness transaction serialization.
- SegWit: Bitcoin upgrade that separates witness (signatures) from the legacy transaction serialization.
- Witness: Script/signature data used to satisfy spending conditions (separated in SegWit).
- wtxid: SegWit transaction identifier that commits to witness data (unlike legacy `txid`).

## Encoding & Checksums

- Base58Check: Base58 encoding with a version/payload and a 4-byte checksum to catch common transcription errors.
