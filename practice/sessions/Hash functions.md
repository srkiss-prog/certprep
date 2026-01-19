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

## Drill Set: 2026-01-16 — Hash Functions (Bitcoin)

### SPEED DRILL (25 new questions total)

Q26) In Bitcoin, the block hash (“block id”) is computed from the block header, not by hashing the entire block body directly.

- Correct answer: TRUE
- Justification: The identifier miners work on and nodes reference is the (double-)hash of the header.
- Tag(s): block-structure, double-sha256, trap

Q27) A hash can act as a commitment: you can reveal the original data later and others can verify it matches the prior hash.

- Correct answer: TRUE
- Justification: Publishing the digest commits you to the data because any change would change the digest.
- Tag(s): hash-basics, integrity

Q28) If preimage resistance failed, someone could efficiently derive a private key from a P2PKH address.

- Correct answer: FALSE
- Justification: Addresses are (encoded) hashes of public-key material/script identifiers, not reversible mappings to private keys.
- Tag(s): trap, hash-vs-keys, addresses

Q29) SPV-style verification relies on merkle proofs plus block headers to check inclusion of a transaction.

- Correct answer: TRUE
- Justification: A merkle branch plus the header’s merkle root allows inclusion verification without all transactions.
- Tag(s): merkle, spv

Q30) If collision resistance were broken for SHA-256, Bitcoin mining would immediately stop working.

- Correct answer: FALSE
- Justification: Mining is a preimage-style search against a target; collisions don’t directly prevent finding valid header hashes.
- Tag(s): trap, properties, pow, sha256

Q31) Changing any field in a block header (e.g., timestamp, nonce, merkle root) changes the resulting header hash.

- Correct answer: TRUE
- Justification: The hash is computed over the header bytes, so any modification changes the digest.
- Tag(s): block-structure, hash-basics

Q32) HASH160-style 20-byte identifiers are used for both P2PKH (pubkey hash) and P2SH (script hash).

- Correct answer: TRUE
- Justification: Both encodings use a 20-byte hash (commonly HASH160) as the key identifier.
- Tag(s): hash160, addresses, scripts

Q33) The checksum in Base58Check is designed to prevent attackers from stealing funds by cryptographically protecting the address.

- Correct answer: FALSE
- Justification: It’s primarily for typo/error detection, not adversarial security.
- Tag(s): trap, base58check, checksum

Q34) Collision resistance means it should be infeasible to find any two different inputs that produce the same digest.

- Correct answer: TRUE
- Justification: The goal is to make “two distinct messages, same hash” computationally infeasible.
- Tag(s): properties, collision

Q35) Swapping the order of two transactions in a block can change the merkle root even if the set of transactions is unchanged.

- Correct answer: TRUE
- Justification: The merkle tree commits to ordering via the hashing structure, not just the set.
- Tag(s): merkle, trap

Q36) Hash linking of blocks implies that changing an old block forces redoing proof-of-work for that block and all later blocks to keep the chain consistent.

- Correct answer: TRUE
- Justification: Altering a block changes its header hash, breaking descendants’ “previous block hash” references.
- Tag(s): hash-pointers, pow, chain-security

Q37) A txid is a hash-based identifier/commitment to a transaction’s contents; it is not itself a digital signature.

- Correct answer: TRUE
- Justification: Signatures prove authorization, while a txid is a digest used for identification and commitment.
- Tag(s): txid, trap, signatures

Q38) In SegWit, the wtxid commits to witness data, while the legacy txid does not include witness data.

- Correct answer: TRUE
- Justification: SegWit separates witness from the legacy serialization used for the txid.
- Tag(s): segwit, txid, wtxid

Q39) Wallet software should reject a Base58Check address string with an invalid checksum as likely mistyped.

- Correct answer: TRUE
- Justification: The checksum is specifically there to catch transcription errors.
- Tag(s): base58check, checksum, practice

Q40) A plain hash function, by itself, provides message authentication without any secret information.

- Correct answer: FALSE
- Justification: Authentication requires a secret (e.g., MAC) or signature; a bare hash is publicly computable.
- Tag(s): trap, hash-basics, authentication

Q41) Which property most directly means “given a digest, it’s infeasible to find any input that hashes to it”?
A) Preimage resistance
B) Collision resistance
C) Determinism
D) Avalanche effect

- Correct answer: A
- Justification: Preimage resistance is exactly the “given hash, find input” hardness property.
- Tag(s): properties, preimage

Q42) In a standard P2SH output, what is hashed to produce the 20-byte script hash identifier?
A) The private key
B) The public key
C) The redeem script
D) The block header

- Correct answer: C
- Justification: P2SH pays to the hash of a redeem script that is revealed when spending.
- Tag(s): scripts, p2sh, hash160

Q43) A merkle inclusion proof (merkle branch) primarily consists of:
A) All transactions in the block
B) The sibling hashes along the path to the merkle root
C) The block’s nonce values tried by miners
D) The UTXO set snapshot

- Correct answer: B
- Justification: You only need the neighboring hashes needed to recompute the root.
- Tag(s): merkle, spv

Q44) In Base58Check (conceptually), the checksum is derived from:
A) RIPEMD-160(payload)
B) The last 4 bytes of SHA-256(payload)
C) The first 4 bytes of double-SHA256(version + payload)
D) A signature over the address by miners

- Correct answer: C
- Justification: Base58Check uses a 4-byte checksum from double-SHA256 of the data being encoded.
- Tag(s): base58check, checksum, double-sha256

Q45) In Bitcoin usage, “block id” most commonly refers to:
A) The merkle root
B) The double-SHA256 of the block header (often called the block hash)
C) The SHA-256 of the entire block body
D) The txid of the coinbase transaction

- Correct answer: B
- Justification: The commonly referenced block identifier is the header hash.
- Tag(s): block-structure, double-sha256, trap

Q46) Which block-header field links a block to its parent?
A) Merkle root
B) Target (bits)
C) Previous block hash
D) Version

- Correct answer: C
- Justification: Each header contains the previous block’s header hash as a hash pointer.
- Tag(s): hash-pointers, block-structure

Q47) Why use HASH160-style 20-byte identifiers in address/script contexts?
A) To make hashes reversible for recovery
B) To encrypt the public key on-chain
C) To get a shorter identifier while retaining strong cryptographic properties
D) To add a secret key into the address

- Correct answer: C
- Justification: A 160-bit identifier is shorter for scripts/encodings while remaining cryptographically robust in context.
- Tag(s): hash160, addresses, trap

Q48) The merkle root in a block header most directly commits to:
A) The global UTXO set
B) The mempool contents
C) The block’s transaction list
D) The private keys of miners

- Correct answer: C
- Justification: The merkle root is computed from hashes of the transactions in that block.
- Tag(s): merkle, block-structure

Q49) Which statement about txid vs wtxid is correct?
A) They are always identical for all transactions
B) They differ only for SegWit transactions with witness data, and the wtxid commits to the witness
C) The wtxid excludes witness data while the txid includes it
D) The txid is computed from the block header

- Correct answer: B
- Justification: SegWit introduces wtxid to include witness commitment; legacy txid does not include witness.
- Tag(s): segwit, txid, wtxid, trap

Q50) If you can efficiently find collisions for HASH160, what does that most directly enable (in principle)?
A) Deriving a private key from an address
B) Creating two different pubkeys or redeem scripts that map to the same 20-byte identifier
C) Decrypting on-chain transaction data
D) Forging valid ECDSA signatures

- Correct answer: B
- Justification: A collision means two distinct inputs can share the same digest/identifier, even though it doesn’t directly yield keys or signatures.
- Tag(s): properties, collision, hash160, trap

## Drill Set: 2026-01-16 — Hash Functions (Bitcoin) — Level 3

### SPEED DRILL (25 new questions total)

Q51) Cryptographic hash functions used in Bitcoin output a fixed-length digest regardless of input size.

- Correct answer: TRUE
- Justification: A core property is fixed-size output for arbitrary-length inputs.
- Tag(s): hash-basics

Q52) Bitcoin uses hashing to derive a public key from a private key.

- Correct answer: FALSE
- Justification: Public keys are derived via elliptic-curve multiplication, not hashing.
- Tag(s): trap, keys

Q53) When mining difficulty changes, Bitcoin changes the target threshold, not the SHA-256 algorithm.

- Correct answer: TRUE
- Justification: Difficulty retargeting adjusts the acceptable hash target; the hash function stays the same.
- Tag(s): pow, difficulty, trap

Q54) In SegWit blocks, the merkle root stored in the block header is computed from wtxids instead of txids.

- Correct answer: FALSE
- Justification: The header’s merkle root commits to txids; witness data is committed via a separate witness commitment.
- Tag(s): trap, segwit, merkle

Q55) “Double-SHA256” means applying SHA-256 to the 32-byte hash output of SHA-256, not to the human-readable hex string.

- Correct answer: TRUE
- Justification: Double hashing is performed on bytes; hex is just a display encoding.
- Tag(s): double-sha256, trap

Q56) A plain hash provides integrity checking, but by itself it does not provide authentication.

- Correct answer: TRUE
- Justification: Anyone can compute the same hash; authentication requires a secret (MAC) or a signature.
- Tag(s): authentication, hash-basics

Q57) If a transaction’s contents change, its txid changes, which can cascade into a different merkle root and thus a different block header hash.

- Correct answer: TRUE
- Justification: Hash commitments propagate upward through the merkle root into the block header hash.
- Tag(s): merkle, txid, block-structure

Q58) Base58Check is designed so that if you change one character in an address, it will still always be accepted.

- Correct answer: FALSE
- Justification: The checksum is intended to make most accidental changes invalid.
- Tag(s): trap, base58check, checksum

Q59) A cryptographic hash function is a one-to-one (invertible) mapping from inputs to outputs.

- Correct answer: FALSE
- Justification: Hashes are many-to-one due to fixed-length output, so they cannot be invertible.
- Tag(s): trap, hash-basics

Q60) Finding any two different messages with the same SHA-256 digest is an example of a collision.

- Correct answer: TRUE
- Justification: Two distinct inputs that hash to the same output are, by definition, a collision.
- Tag(s): properties, collision

Q61) Preimage resistance guarantees that collisions are impossible.

- Correct answer: FALSE
- Justification: Collisions must exist for fixed-length hashes; resistance is about computational infeasibility.
- Tag(s): trap, properties

Q62) In Bitcoin, “hashrate” is best thought of as how many hash computations per second miners collectively perform.

- Correct answer: TRUE
- Justification: Hashrate is a rate of attempted hashes in proof-of-work.
- Tag(s): pow, mining

Q63) If you know the HASH160 (pubkey hash) from a P2PKH output, you can verify a candidate public key matches it by hashing the public key and comparing.

- Correct answer: TRUE
- Justification: P2PKH spends reveal a pubkey, and nodes check it hashes to the committed pubkey hash.
- Tag(s): hash160, p2pkh

Q64) RIPEMD-160 is directly used as the proof-of-work hash function in Bitcoin.

- Correct answer: FALSE
- Justification: Bitcoin PoW uses (double-)SHA-256 on the block header.
- Tag(s): trap, pow, ripemd160

Q65) Tagged hashing (as used in Taproot/Schnorr contexts) is primarily a domain-separation technique to keep different hash uses from colliding semantically.

- Correct answer: TRUE
- Justification: Tagging scopes the hash to a specific purpose to avoid cross-protocol reuse pitfalls.
- Tag(s): taproot, tagged-hash, trap

Q66) Which statement best captures what miners are “searching for” in proof-of-work?
A) A block header whose hash is numerically below a target
B) A pair of transactions with the same txid
C) A private key that matches a given address
D) A merkle proof that is shortest

- Correct answer: A
- Justification: Mining is a preimage-style search for a header hash under the current target.
- Tag(s): pow, trap

Q67) What does the witness commitment in SegWit most directly commit to?
A) The previous block hash
B) The set of witness data for transactions in the block
C) The global UTXO set
D) The miner’s payout address

- Correct answer: B
- Justification: SegWit adds a commitment structure so witness data is committed without changing the txid-based merkle root.
- Tag(s): segwit, witness, trap

Q68) SHA-256 produces an output of:
A) 128 bits
B) 160 bits
C) 256 bits
D) 512 bits

- Correct answer: C
- Justification: SHA-256 outputs a 256-bit (32-byte) digest.
- Tag(s): sha256

Q69) In a merkle tree, an internal node hash is typically computed from:
A) The XOR of its children’s hashes
B) The concatenation of its children’s hashes, then hashing that
C) The average of its children’s hashes
D) The longest child hash

- Correct answer: B
- Justification: Merkle trees hash combined child hashes to build a single root commitment.
- Tag(s): merkle, trap

Q70) Which is the most accurate description of Base58Check’s checksum purpose?
A) Prevent malicious redirection attacks by cryptographically securing the address
B) Catch accidental typos and transcription errors
C) Encrypt the payload so it can’t be read
D) Prove ownership of the corresponding private key

- Correct answer: B
- Justification: The checksum is an error-detection feature, not an anti-theft mechanism.
- Tag(s): base58check, checksum, trap

Q71) Which pair correctly matches the “given X, find Y” property?
A) Given a digest, find any message → collision resistance
B) Given a message, find a different message with same digest → second-preimage resistance
C) Given two messages, show they differ → determinism
D) Given a message, compute its digest → preimage resistance

- Correct answer: B
- Justification: Second-preimage is “given one message, find another with the same hash.”
- Tag(s): properties, trap

Q72) Which of the following is NOT primarily a hash function use-case in Bitcoin?
A) Committing to transactions via a merkle root
B) Difficulty-based proof-of-work searching
C) Producing short identifiers like HASH160
D) Encrypting transaction data for confidentiality

- Correct answer: D
- Justification: Bitcoin does not use hashing to encrypt on-chain data.
- Tag(s): trap, hash-vs-encryption

Q73) A typical P2PKH spend validates which hash relationship?
A) RIPEMD-160(SHA-256(pubkey)) equals the pubkey hash in the locking script
B) SHA-256(privkey) equals the pubkey hash in the locking script
C) SHA-256(signature) equals the txid
D) RIPEMD-160(txid) equals the block hash

- Correct answer: A
- Justification: Nodes check the revealed pubkey hashes to the HASH160 committed in the output.
- Tag(s): p2pkh, hash160, trap

Q74) If you can find preimages for SHA-256 efficiently, what does that most directly threaten in Bitcoin?
A) The ability to find blocks below a target becomes impossible
B) Commitments based on hashes (e.g., identifiers and hash pointers) lose their “one-way” safety
C) ECDSA signatures become automatically forgeable
D) The network cannot relay transactions

- Correct answer: B
- Justification: Efficient preimages undermine the one-way nature of hash commitments even though signatures are separate.
- Tag(s): properties, preimage, trap

Q75) Difficulty adjustment most directly changes which quantity?
A) The hash function used by miners
B) The target threshold used to judge whether a block header hash is valid
C) The number of transactions per block
D) The size of a SHA-256 digest

- Correct answer: B
- Justification: Retargeting changes the threshold so blocks continue to arrive at a roughly steady rate.
- Tag(s): pow, difficulty, trap
