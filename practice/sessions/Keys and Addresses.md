## Drill Set: 2026-01-20 — Keys & Addresses

### SPEED DRILL (25 questions total)

Q1) In Bitcoin, a private key is used to create signatures that authorize spending.

- Correct answer: TRUE
- Justification: Spending requires producing a valid signature with the private key required by the script.
- Tag(s): keys, signatures, bitcoin

Q2) A Bitcoin address is the same thing as a private key encoded in Base58.

- Correct answer: FALSE
- Justification: An address is an encoding of a script identifier (e.g., HASH160 or a witness program), not a private key.
- Tag(s): trap, addresses, keys

Q3) Public keys can be shared openly; revealing a public key does not reveal the corresponding private key (assuming secure cryptography).

- Correct answer: TRUE
- Justification: Public-key cryptography relies on private key secrecy with public key distribution.
- Tag(s): keys, asymmetric

Q4) Losing your private key can make funds effectively unspendable even if you still know your address.

- Correct answer: TRUE
- Justification: The address is not a credential; the private key (or other required spending data) is.
- Tag(s): trap, keys, custody

Q5) A Bitcoin address is a human-friendly representation of where funds are “stored.”

- Correct answer: FALSE
- Justification: Bitcoin tracks UTXOs locked by scripts; addresses are encodings that help construct those scripts.
- Tag(s): trap, utxo, addresses

Q6) In P2PKH, the output locks to a public key hash, and the spending input later reveals a public key and signature.

- Correct answer: TRUE
- Justification: The spender provides the pubkey and a valid signature matching that pubkey hash condition.
- Tag(s): p2pkh, hash160, scripts

Q7) Base58Check includes a checksum that helps detect common transcription errors in legacy addresses.

- Correct answer: TRUE
- Justification: Base58Check uses a checksum (from double-SHA256) to catch typos.
- Tag(s): base58check, checksum

Q8) Bech32 addresses are just Base58Check addresses with different characters.

- Correct answer: FALSE
- Justification: Bech32 is a different encoding used for SegWit witness programs and has different checksum behavior.
- Tag(s): trap, bech32, segwit

Q9) In Bitcoin, “owning an address” means knowing the private key that can satisfy the corresponding locking script.

- Correct answer: TRUE
- Justification: Control is defined by the ability to satisfy spending conditions, typically via a private key signature.
- Tag(s): trap, keys, scripts

Q10) A wallet must broadcast your private key to the network to receive coins to an address.

- Correct answer: FALSE
- Justification: Receiving only requires giving someone an address; private keys are never broadcast.
- Tag(s): trap, wallet, keys

Q11) A compressed public key and an uncompressed public key can correspond to the same private key.

- Correct answer: TRUE
- Justification: Public key compression changes representation, not the underlying keypair relationship.
- Tag(s): trap, keys, pubkey

Q12) A checksum on an address is meant to prevent attackers from stealing funds by making addresses cryptographically secure.

- Correct answer: FALSE
- Justification: Checksums are for error detection, not adversarial security.
- Tag(s): trap, checksum

Q13) In many common address types, what’s encoded is not “a public key” but a script identifier (e.g., pubkey hash or script hash).

- Correct answer: TRUE
- Justification: P2PKH/P2SH encode hashes; SegWit encodes a witness program.
- Tag(s): addresses, scripts, trap

Q14) WIF (Wallet Import Format) is commonly used to represent private keys for import/export.

- Correct answer: TRUE
- Justification: WIF is a Base58Check encoding used to encode private keys with version/compression info.
- Tag(s): wif, keys

Q15) If two different addresses receive funds, those funds are necessarily controlled by two different private keys.

- Correct answer: FALSE
- Justification: One wallet/seed can derive many addresses; multiple addresses can be controlled by the same root secret.
- Tag(s): trap, wallet, derivation

Q16) Which statement best describes a Bitcoin address?
A) A secret key used to spend funds
B) A publicly shareable identifier used to construct a locking script
C) A signature proving payment
D) The transaction id of the last incoming payment

- Correct answer: B
- Justification: Addresses are shareable encodings used to create scriptPubKey conditions.
- Tag(s): addresses, scripts, trap

Q17) In a typical P2PKH spend, what does the spender reveal?
A) Only the address
B) A public key and a signature
C) The private key
D) The block header

- Correct answer: B
- Justification: The pubkey and a valid signature satisfy the pubkey-hash locking condition.
- Tag(s): p2pkh, scripts

Q18) What is the primary purpose of an address checksum?
A) Prevent man-in-the-middle attacks
B) Detect likely typos/transcription errors
C) Prove the sender owns the address
D) Encrypt the address contents

- Correct answer: B
- Justification: Checksums are error-detection features.
- Tag(s): checksum, trap

Q19) Which is most accurate about “funds in an address”?
A) Coins are stored inside the address string
B) Coins are stored in your wallet file
C) UTXOs are locked by scripts; addresses are encodings used to create those scripts
D) Coins are stored on miners’ computers until spent

- Correct answer: C
- Justification: Bitcoin’s state is UTXOs locked by script conditions; addresses are a convenience layer.
- Tag(s): utxo, scripts, trap

Q20) Which is the best description of a private key’s role?
A) It’s a public identifier for receiving
B) It’s a secret used to authorize spending via signatures
C) It’s the checksum for an address
D) It’s the merkle root of your wallet

- Correct answer: B
- Justification: Private keys are secret signing keys used to satisfy spending conditions.
- Tag(s): keys, signatures

Q21) Which address type is most associated with Bech32 encoding?
A) Legacy P2PKH (Base58Check)
B) SegWit witness programs (e.g., P2WPKH/P2WSH)
C) Coinbase transaction IDs
D) Private keys in WIF

- Correct answer: B
- Justification: Bech32 encodes SegWit witness versions/programs.
- Tag(s): bech32, segwit, trap

Q22) What does WIF primarily encode?
A) A public key
B) A private key (plus metadata like compression flag)
C) A transaction signature
D) A merkle proof

- Correct answer: B
- Justification: WIF is a Base58Check format for representing private keys for import/export.
- Tag(s): wif, keys, trap

Q23) If someone has your address, what can they do with it?
A) Spend your funds
B) Derive your private key instantly
C) Send funds to a script that you may be able to spend from (if you control the keys)
D) Decrypt your wallet

- Correct answer: C
- Justification: Addresses are for receiving; spending requires satisfying the script with keys/signatures.
- Tag(s): trap, addresses

Q24) Which pairing is correct?
A) Public key = secret; private key = public
B) Public key verifies; private key signs
C) Public key signs; private key verifies
D) Address equals the private key

- Correct answer: B
- Justification: Signature creation uses the private key; verification uses the public key.
- Tag(s): keys, signatures, trap

Q25) Which statement about address reuse is most accurate?
A) Reuse is recommended because it improves privacy
B) Reuse is harmless because addresses are secret
C) Reuse can reduce privacy by linking payments, even if funds remain secure
D) Reuse is required for SegWit

- Correct answer: C
- Justification: Reuse makes on-chain linkage easier; it’s a privacy issue rather than a spending-security benefit.
- Tag(s): privacy, addresses, trap

## Drill Set: 2026-01-20 — Keys & Addresses (Append — Level 3)

### SPEED DRILL (25 new questions total)

Q26) A single wallet seed can deterministically generate many different addresses without generating new randomness each time.

- Correct answer: TRUE
- Justification: HD wallets derive many keys/addresses from one root secret deterministically.
- Tag(s): trap, hd-wallets, derivation

Q27) An extended public key (xpub) is sufficient to create valid spending signatures.

- Correct answer: FALSE
- Justification: Spending requires private keys (xprv/derived privkeys), not an xpub.
- Tag(s): trap, xpub, keys

Q28) Address formats can encode different script types (e.g., legacy, SegWit, Taproot), not just different “spellings” of the same destination.

- Correct answer: TRUE
- Justification: Different address types correspond to different script templates/witness programs.
- Tag(s): addresses, scripts, trap

Q29) In SegWit, the witness (signatures) is excluded from the txid calculation.

- Correct answer: TRUE
- Justification: SegWit separates witness data so the legacy txid does not commit to witness.
- Tag(s): segwit, txid, trap

Q30) A watch-only wallet can safely receive and monitor funds without having the private keys.

- Correct answer: TRUE
- Justification: It can derive/track addresses and balances, but cannot spend.
- Tag(s): wallet, xpub, trap

Q31) If you accidentally publish a private key in WIF, an attacker can spend any UTXOs locked to scripts controlled solely by that key.

- Correct answer: TRUE
- Justification: Whoever controls the private key can generate valid spend authorizations.
- Tag(s): wif, keys, custody

Q32) For P2WPKH, the address encodes a witness program that ultimately locks to a public key hash.

- Correct answer: TRUE
- Justification: P2WPKH is a SegWit v0 witness program using a 20-byte pubkey-hash.
- Tag(s): segwit, p2wpkh, trap

Q33) Taproot (P2TR) addresses are most commonly encoded using Bech32m.

- Correct answer: TRUE
- Justification: SegWit v1 witness programs (Taproot) use Bech32m encoding.
- Tag(s): taproot, bech32m, trap

Q34) A “change address” is a special address type that is invalid for receiving external payments.

- Correct answer: FALSE
- Justification: Change is a wallet practice (sending change to yourself), not a distinct address type.
- Tag(s): trap, wallet, privacy

Q35) If you reuse the same address for multiple payments, you may harm privacy even if spending security remains intact.

- Correct answer: TRUE
- Justification: Reuse makes on-chain linkage easier.
- Tag(s): privacy, addresses

Q36) A Bitcoin address checksum is designed to detect random network corruption of transactions after broadcast.

- Correct answer: FALSE
- Justification: Address checksums help humans catch typos before broadcast; they don’t protect network data integrity.
- Tag(s): trap, checksum

Q37) In P2SH, the output commits to a script hash, and the redeem script is revealed when spending.

- Correct answer: TRUE
- Justification: The spender provides the redeem script and data to satisfy it.
- Tag(s): p2sh, scripts

Q38) Knowing a public key hash (e.g., HASH160) is sufficient to reconstruct the original public key.

- Correct answer: FALSE
- Justification: Hashes are one-way; many pubkeys map to a digest in principle.
- Tag(s): trap, hash160, keys

Q39) If you have the correct xpub, you can derive receiving addresses but you cannot derive the corresponding private keys.

- Correct answer: TRUE
- Justification: The xpub supports public derivation but not private-key recovery.
- Tag(s): xpub, derivation

Q40) A single transaction output can be locked to multiple keys (e.g., multisig), so “one address = one key” is not a rule.

- Correct answer: TRUE
- Justification: Script conditions can require multiple signatures/keys.
- Tag(s): trap, multisig, scripts

Q41) Which item is safe to share for a watch-only wallet setup?
A) Seed phrase
B) xprv (extended private key)
C) xpub (extended public key)
D) WIF private key

- Correct answer: C
- Justification: An xpub enables address derivation and monitoring but not spending.
- Tag(s): xpub, wallet, trap

Q42) Which address type is most directly associated with Taproot?
A) P2PKH
B) P2SH
C) P2TR
D) P2WPKH

- Correct answer: C
- Justification: Taproot outputs use Pay-to-Taproot (P2TR).
- Tag(s): taproot, addresses

Q43) What does a wallet generally need to spend from a standard single-sig output?
A) Only the address
B) The private key (or signing ability) that satisfies the locking script
C) Only the public key
D) Only the checksum

- Correct answer: B
- Justification: Spending requires producing valid signatures for the script.
- Tag(s): keys, scripts, trap

Q44) Which description best fits “xprv”?
A) Extended public key used for watch-only
B) Extended private key used to derive private keys for spending
C) Address checksum format
D) A block header field

- Correct answer: B
- Justification: xprv can derive child private keys (and thus can spend).
- Tag(s): xprv, keys, trap

Q45) In SegWit terminology, what does an address (Bech32/Bech32m) primarily encode?
A) A full public key
B) A witness program (version + program data)
C) A private key
D) A transaction signature

- Correct answer: B
- Justification: SegWit addresses encode witness version and program bytes.
- Tag(s): segwit, witness-program, trap

Q46) Which statement about “wallet balance” is most accurate?
A) It’s an account balance stored on-chain
B) It’s a sum of UTXOs the wallet believes it can spend
C) It’s stored inside your address
D) It’s enforced by address checksums

- Correct answer: B
- Justification: Wallets track UTXOs and compute balances locally from chain data.
- Tag(s): utxo, wallet, trap

Q47) Which concept best explains how a wallet can generate many addresses from one seed?
A) Proof-of-work
B) Deterministic derivation (HD wallet)
C) Mining difficulty
D) Base58Check checksum

- Correct answer: B
- Justification: HD wallets deterministically derive many keys/addresses from one root.
- Tag(s): hd-wallets, derivation, trap

Q48) Which action most directly improves on-chain privacy?
A) Reusing one address for all receipts
B) Using a fresh address for new receipts (when practical)
C) Publishing your xprv for transparency
D) Turning off checksums

- Correct answer: B
- Justification: Fresh addresses reduce linkage between payments.
- Tag(s): privacy, trap

Q49) Which pairing is correct for SegWit address encoding?
A) SegWit v0 uses Bech32m
B) SegWit v1 uses Base58Check
C) SegWit v0 uses Bech32; SegWit v1 uses Bech32m
D) SegWit v0 uses WIF

- Correct answer: C
- Justification: Bech32 is used for v0; Bech32m is used for v1+ witness programs.
- Tag(s): segwit, bech32, bech32m, trap

Q50) If an attacker learns your xpub, what is the most realistic direct impact?
A) They can spend your funds immediately
B) They can derive your private keys
C) They can track derived addresses and harm privacy
D) They can change consensus rules

- Correct answer: C
- Justification: An xpub enables address derivation/monitoring, which is a privacy risk.
- Tag(s): xpub, privacy, trap
