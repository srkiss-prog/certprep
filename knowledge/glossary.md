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
- UTXO: Unspent transaction output; the spendable units tracked by the protocol.
- Input (vin): References a previous output and provides unlocking data (scriptSig/witness).
- Output (vout): Creates a new spendable output with a locking script (scriptPubKey).
- scriptPubKey: Locking script that defines spending conditions for an output.
- scriptSig / witness: Unlocking data that satisfies the locking script.
- Coinbase transaction: Special transaction that creates new coins + collects fees; no normal inputs.
- Coinbase maturity: Minimum number of blocks before a coinbase output can be spent.
- Fee: Sum(inputs) − sum(outputs).
- Mempool: Node’s pool of valid, unconfirmed transactions.
- Dust: Output too small to be economical to spend.
- Change: Leftover input value sent back to the sender.
- Malleability: Changing a transaction’s encoding without invalidating the spend (can change txid).
- Policy vs consensus: Policy governs relay/mining; consensus governs validity.
- RBF (Replace-by-Fee): Mempool policy allowing replacement of an unconfirmed transaction with a higher-fee version.
- CPFP (Child Pays For Parent): Fee-bumping method using a high-fee child transaction spending a parent’s output.
- vout: Output index within a transaction used to identify a specific output.
- OP_RETURN: Script opcode that makes an output provably unspendable, typically used for data.
- Weight / vsize: Transaction size metrics that account for witness data, used to compute fee rates.
- nLockTime: Transaction-level field that prevents inclusion before a specified time or block height.
- nSequence: Per-input field used for relative timelocks and opt-in RBF signaling.
- CSV (CHECKSEQUENCEVERIFY): Opcode enabling relative timelocks based on input age.

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
- P2WSH: Pay-to-Witness-Script-Hash; SegWit v0 output type locking to a 32-byte witness script hash.
- Nested SegWit (P2SH-P2WPKH): SegWit spending wrapped in P2SH to use Base58Check addresses while spending via witness.
- Seed phrase (mnemonic): Human-readable backup that encodes/derives a wallet seed used for HD key derivation.
- Derivation path: HD wallet “address” within the tree (account/change/index) used to derive a specific child key.
- Gap limit: Wallet scanning window for derived addresses; too small can miss funds received at higher indices.
- Hardened derivation: HD derivation mode that prevents deriving child private keys from public-only derivation data.

## Mining & Block Rewards

- Proof-of-work (PoW): Mining process of hashing block headers until a hash is below the target.
- Block header: Compact block metadata hashed for PoW (includes previous hash, merkle root, time, bits, nonce).
- Target: Threshold a block hash must be below to be valid.
- Difficulty: Inverse-style measure of mining hardness; higher difficulty corresponds to a lower target.
- bits: Compact encoding of the current PoW target in the block header.
- Block subsidy: Newly minted bitcoins awarded per block by schedule.
- Block reward: Subsidy plus transaction fees from included transactions.
- Coinbase transaction: Special transaction that creates new coins and collects fees for the miner.
- Coinbase maturity: Required confirmation depth before coinbase outputs can be spent.
- Hashrate: Estimated hashes per second contributed by miners/network.
- Mining pool: Cooperative mining arrangement sharing work and payout variance.
- Share (pool share): Lower-difficulty proof submitted to a pool to measure contributed work.
- Stale block: Valid block not in the selected best chain after a fork race.
- Reorg (chain reorganization): Switch from one valid chain tip to another with more cumulative work.
- Cumulative work: Aggregate proof-of-work metric used for best-chain selection.
- Retarget interval: Fixed block window used to adjust difficulty target.
- Nonce / extra nonce: Miner-varied values used to expand PoW search space.
- Security budget: Miner incentive pool over time (subsidy + fees), with fee share expected to rise as subsidy declines.
- UTXO set is the current global state of spendable bitcoin.
