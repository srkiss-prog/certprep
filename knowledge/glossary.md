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
- ECDSA nonce (`k`): Per-signature secret value that must be unique/unpredictable; reuse can reveal the private key.
- Sighash (Bitcoin): Transaction digest that a Bitcoin signature commits to, determined by signature-hash rules.
- Transaction malleability: Changing a transaction’s representation in a way that preserves validity but changes its identifier.
- Signature encoding (e.g., DER/canonical): Rules for representing signatures to prevent ambiguous encodings and malleability issues.

## Keys & Addresses

- Address: Human-friendly encoding that represents a script destination (not a key).
- UTXO: Unspent transaction output; the spendable “coins” locked by a script.
- scriptPubKey (locking script): Output script that defines the spending conditions for an output.
- scriptSig: Legacy input unlocking data that can provide signatures/public keys/scripts to satisfy spending conditions.
- Witness: SegWit input unlocking data (e.g., signatures) provided separately from legacy transaction serialization.
- P2PKH: Pay-to-PubKey-Hash; locking script that commits to `HASH160(pubkey)`.
- P2SH: Pay-to-Script-Hash; locking script that commits to `HASH160(redeemScript)`.
- Redeem script: Script revealed when spending a P2SH output to satisfy the committed script hash.
- Witness program: SegWit output program (version + data) that defines how an output can be spent (commonly encoded as Bech32).
- Bech32: Address encoding used for SegWit witness programs with strong typo-detection checksum properties.
- Bech32m: Modified Bech32 checksum encoding used for SegWit v1+ witness programs (e.g., Taproot).
- Base58Check: Base58 encoding with a version/payload and checksum used by legacy address formats and WIF.
- WIF: Wallet Import Format; Base58Check encoding for private keys (plus metadata like compression flag).
- HD wallet: Hierarchical deterministic wallet that derives many keys/addresses from a single root secret (seed).
- xpub: Extended public key used to derive child public keys/addresses (watch-only; cannot spend).
- xprv: Extended private key used to derive child private keys for spending.
- Change address: Wallet-generated address used to receive leftover value from your own transaction output.
- P2WPKH: Pay-to-Witness-PubKey-Hash; SegWit v0 output type locking to a 20-byte pubkey hash witness program.
- Taproot / P2TR: SegWit v1 output type (Pay-to-Taproot), typically encoded using Bech32m.
- Multisig: Script condition requiring multiple signatures/keys to spend.
