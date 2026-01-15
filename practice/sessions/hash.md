Q1) A hash function always produces the same output for the same input.

- Correct answer: TRUE
- Justification: Determinism is required so everyone can verify the same digest for the same data.
- Tag(s): hash-basics, determinism

Q2) Hash functions are primarily used in Bitcoin to encrypt data so it stays secret on-chain.

- Correct answer: FALSE
- Justification: Hashes provide integrity/commitment, not confidentiality.
- Tag(s): trap, hash-vs-encryption

Q3) Preimage resistance means it’s infeasible to find any input that matches a given hash output.

- Correct answer: TRUE
- Justification: Given a digest, finding a corresponding message should be computationally infeasible.
- Tag(s): properties, preimage

Q4) Collision resistance means it’s infeasible to find a different input with the same hash as a known input.

- Correct answer: FALSE
- Justification: That describes second-preimage resistance; collision resistance is finding any two distinct inputs with the same hash.
- Tag(s): trap, properties, collision-vs-second-preimage

Q5) Bitcoin proof-of-work uses SHA-256 on the block header.

- Correct answer: TRUE
- Justification: Mining searches for a block header hash below a target using SHA-256.
- Tag(s): bitcoin-use, pow, sha256

Q6) Bitcoin uses double-SHA256 for both block header hashing (PoW) and transaction IDs (txid).

- Correct answer: TRUE
- Justification: Both the block header hash and the legacy txid are double-SHA256 of serialized data.
- Tag(s): bitcoin-use, double-sha256

Q7) A hash pointer is a pointer plus the hash of the referenced data, enabling tamper evidence.

- Correct answer: TRUE
- Justification: Changing the referenced data changes its hash, breaking the pointer’s integrity check.
- Tag(s): hash-pointers, integrity

Q8) If you know a transaction’s txid, you can reconstruct the full transaction without any other data.

- Correct answer: FALSE
- Justification: A txid is a digest/identifier; you still need the transaction data from elsewhere.
- Tag(s): trap, txid, data-availability

Q9) The merkle root in a block header commits to the set and ordering of transactions in that block.

- Correct answer: TRUE
- Justification: Any change to a transaction or its position changes the merkle root.
- Tag(s): merkle, block-structure

Q10) A merkle proof can show a transaction is in a block without downloading every transaction in that block.

- Correct answer: TRUE
- Justification: Merkle inclusion proofs allow verification using a branch of hashes up to the root.
- Tag(s): merkle, spv

Q11) RIPEMD-160 is used in Bitcoin to make hashes longer for better security.

- Correct answer: FALSE
- Justification: RIPEMD-160 is used (with SHA-256) to produce a shorter 160-bit identifier (HASH160).
- Tag(s): trap, ripemd160, hash160

Q12) HASH160 commonly refers to RIPEMD-160(SHA-256(data)).

- Correct answer: TRUE
- Justification: Bitcoin uses SHA-256 followed by RIPEMD-160 for certain address/script identifiers.
- Tag(s): hash160, ripemd160

Q13) Base58Check uses a checksum derived from double-SHA256 to detect typos.

- Correct answer: TRUE
- Justification: The checksum helps catch errors; it’s not meant to be a security mechanism against attackers.
- Tag(s): base58check, checksum

Q14) Collision resistance implies preimage resistance.

- Correct answer: FALSE
- Justification: These are distinct properties; one does not automatically guarantee the other.
- Tag(s): trap, properties

Q15) Changing one bit of input typically changes about half the bits of a secure hash output.

- Correct answer: TRUE
- Justification: This is the avalanche effect expected from good cryptographic hashes.
- Tag(s): properties, avalanche

Q16) Which Bitcoin component is directly used as the input to proof-of-work hashing?
A) Full block (all transactions)
B) Block header
C) UTXO set
D) Wallet seed

- Correct answer: B
- Justification: Miners repeatedly hash the block header (with varying nonce/fields) to meet the target.
- Tag(s): pow, block-structure

Q17) Which pair best matches the properties of a cryptographic hash used in Bitcoin?
A) Reversible and compressible
B) Deterministic and preimage-resistant
C) Randomized and reversible
D) Secret-key and decryptable

- Correct answer: B
- Justification: Verification requires determinism, and security relies on one-way properties like preimage resistance.
- Tag(s): hash-basics, properties

Q18) What is the primary purpose of a merkle tree in Bitcoin blocks?
A) Encrypt transactions
B) Compress signatures
C) Efficient inclusion proofs and commitment to transactions
D) Prevent double spending by itself

- Correct answer: C
- Justification: Merkle trees allow compact proofs that a transaction is included in a committed set.
- Tag(s): merkle, spv

Q19) Which construction is commonly associated with P2PKH-style identifiers in Bitcoin?
A) SHA-1(pubkey)
B) RIPEMD-160(pubkey)
C) RIPEMD-160(SHA-256(pubkey)) (HASH160)
D) SHA-256(RIPEMD-160(pubkey))

- Correct answer: C
- Justification: Bitcoin commonly uses HASH160 to derive a 20-byte identifier from a public key.
- Tag(s): addresses, hash160

Q20) A common trap: “Hashing provides confidentiality because outputs look random.” What’s correct?
A) True; randomness implies secrecy
B) True; hashes are encryption without keys
C) False; hashes don’t hide data from someone who already has the input or can guess it
D) False; hashes are only used for signing

- Correct answer: C
- Justification: Hashes are not encryption; if inputs are guessable, outputs can be checked by hashing guesses.
- Tag(s): trap, hash-vs-encryption

Q21) Which statement best describes a txid in Bitcoin (simplified, legacy)?
A) The encrypted transaction payload
B) A double-SHA256 digest of the serialized transaction
C) A RIPEMD-160 digest of the block header
D) The merkle root of the block

- Correct answer: B
- Justification: The txid is (traditionally) the double-SHA256 of the transaction serialization.
- Tag(s): txid, double-sha256

Q22) What does “second-preimage resistance” protect against most directly?
A) Finding any two messages with the same hash
B) Given a specific message, finding a different one with the same hash
C) Recovering a message from its hash
D) Proving a message was signed

- Correct answer: B
- Justification: Second-preimage targets the “given this message, find another with same digest” scenario.
- Tag(s): properties, second-preimage

Q23) Why is double-SHA256 sometimes used instead of a single SHA-256 in Bitcoin contexts?
A) To make hashing reversible for auditing
B) To reduce the output size to 160 bits
C) To defend against certain structural weaknesses and as a conservative design choice
D) To add a secret key

- Correct answer: C
- Justification: Double hashing is a conservative pattern; it doesn’t add a key or make hashes reversible.
- Tag(s): trap, double-sha256, design

Q24) Which is the best description of a “hash pointer” used in blockchains?
A) A URL to a block explorer
B) A pointer that is valid only if the referenced data’s hash matches
C) A private key that unlocks a UTXO
D) A compressed public key

- Correct answer: B
- Justification: The stored hash makes tampering detectable because altered data won’t match.
- Tag(s): hash-pointers, integrity

Q25) If two different transactions had the same txid, what property would be violated (in principle)?
A) Determinism
B) Collision resistance (as applied to the txid hash)
C) Confidentiality
D) Availability

- Correct answer: B
- Justification: Distinct inputs producing the same digest is a collision scenario.
- Tag(s): properties, collision, txid
