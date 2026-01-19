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

## Symmetric vs Asymmetric Cryptography

- Symmetric encryption: Same secret key encrypts and decrypts.
- Asymmetric (public-key) cryptography: Uses a keypair with different roles for public vs private keys.
- Public key: Shareable key used to verify signatures or encrypt to a recipient.
- Private key: Secret key used to sign (and to decrypt in public-key encryption).
- Digital signature: Cryptographic proof of authenticity and integrity; publicly verifiable.
- MAC: Shared-secret message authentication tag providing integrity/authentication, not non-repudiation.
- Key exchange (Diffie–Hellman): Protocol to derive a shared secret without sending it directly.
- ECDH: Elliptic-curve Diffie–Hellman; key agreement method to derive a shared secret.
- Hybrid encryption: Asymmetric establishes a session key; symmetric encrypts bulk data.
- AEAD: Authenticated encryption with associated data; provides confidentiality + integrity.
- Nonce / IV: Per-message value required by many encryption modes; must follow uniqueness/randomness rules for security.
- MITM attack: Attacker substitutes keys/relays messages when identities/keys aren’t authenticated.
- PKI / certificate: Mechanism for binding a public key to an identity to enable authenticated key distribution.
- RSA: Public-key algorithm historically used for encryption/signatures (conceptually asymmetric).
- ECC: Elliptic-curve cryptography; public-key cryptography family used by Bitcoin for signatures.
- ECDSA: Elliptic-curve digital signature algorithm used in Bitcoin (asymmetric signatures).
- Schnorr signature: Public-key signature scheme used in modern Bitcoin script contexts (asymmetric signatures).
- One-time pad (OTP): Symmetric scheme with perfect secrecy when key is truly random, secret, and used only once.

## Digital Signatures

- Verification: Checking a signature is valid for a given message and public key.
- Authenticity: Assurance the message was authorized by the private key corresponding to a given public key.
- Integrity: Assurance the signed message bytes were not altered after signing.
- Non-repudiation: Property where third parties can verify a signature as evidence of authorization (assuming private key control).
- Hash-then-sign: Common pattern of signing a fixed-size hash digest of the message rather than the full message.
