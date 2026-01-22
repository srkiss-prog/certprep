## Drill Set: 2026-01-19 — Digital Signatures

### SPEED DRILL (25 questions total)

Q1) A digital signature provides authenticity and integrity for a specific message.

- Correct answer: TRUE
- Justification: Signatures let verifiers confirm who authorized the message and that it wasn’t altered.
- Tag(s): signatures, properties

Q2) Digital signatures encrypt the message so only the intended recipient can read it.

- Correct answer: FALSE
- Justification: Signatures don’t hide data; they prove authenticity/integrity.
- Tag(s): trap, signatures-vs-encryption

Q3) In public-key signatures, the private key is used to sign and the public key is used to verify.

- Correct answer: TRUE
- Justification: Verification is public; signing requires the secret private key.
- Tag(s): signatures, asymmetric

Q4) If a signature verifies successfully, it guarantees the signer intended the message’s meaning.

- Correct answer: FALSE
- Justification: Signatures prove the key authorized the bytes, not the human intent or semantics.
- Tag(s): trap, semantics

Q5) Digital signatures provide non-repudiation in the sense that a valid signature can be shown to third parties as proof of authorization (assuming key control).

- Correct answer: TRUE
- Justification: Public verification ties the signature to the signer’s private key control.
- Tag(s): non-repudiation, signatures

Q6) If you change even one bit of the signed message, the signature should fail to verify.

- Correct answer: TRUE
- Justification: Signatures bind to the exact message bytes (often via a hash).
- Tag(s): integrity, signatures

Q7) A MAC and a digital signature provide the same properties because both detect tampering.

- Correct answer: FALSE
- Justification: MACs require a shared secret and don’t provide public verifiability/non-repudiation.
- Tag(s): trap, mac, signatures

Q8) A signature scheme typically signs a hash of the message rather than the full message directly.

- Correct answer: TRUE
- Justification: Hash-then-sign is common for efficiency and standardization.
- Tag(s): hashing, signatures

Q9) A digital signature can be verified by anyone who has the signer’s public key.

- Correct answer: TRUE
- Justification: Public verification is a core feature of signatures.
- Tag(s): signatures, public-key

Q10) If an attacker learns your public key, they can sign transactions as you.

- Correct answer: FALSE
- Justification: Signing requires the private key; the public key is meant to be shared.
- Tag(s): trap, keys

Q11) In Bitcoin, signatures are primarily used to authorize spending of UTXOs according to script conditions.

- Correct answer: TRUE
- Justification: Spending typically requires producing a valid signature for the referenced output.
- Tag(s): bitcoin, utxo, signatures

Q12) In Bitcoin, the signature proves you own coins stored in your address.

- Correct answer: FALSE
- Justification: Bitcoin tracks spendable outputs; signatures prove authorization to spend an output, not “ownership” of an address.
- Tag(s): trap, bitcoin, utxo

Q13) A valid signature does not prevent someone else from copying it and replaying it on a different message.

- Correct answer: TRUE
- Justification: Signatures are bound to a specific message; copying doesn’t help on a different message.
- Tag(s): trap, replay, signatures

Q14) If a signature verifies, it proves the message was not modified after signing.

- Correct answer: TRUE
- Justification: Verification fails if the message bytes differ from what was signed.
- Tag(s): integrity, signatures

Q15) Digital signatures require the verifier to have a shared secret key with the signer.

- Correct answer: FALSE
- Justification: Verification uses the public key; no shared secret is required.
- Tag(s): trap, asymmetric

Q16) Which key is required to create (produce) a digital signature?
A) The signer’s public key
B) The signer’s private key
C) The verifier’s public key
D) A shared MAC key

- Correct answer: B
- Justification: Only the private key holder can produce signatures that verify under the public key.
- Tag(s): signatures, keys, trap

Q17) Which property is NOT primarily provided by a digital signature?
A) Authenticity
B) Integrity
C) Confidentiality
D) Public verifiability

- Correct answer: C
- Justification: Signatures don’t hide content; encryption provides confidentiality.
- Tag(s): trap, signatures-vs-encryption

Q18) In Bitcoin, what does a signature most directly prove?
A) The transaction is encrypted
B) The signer knows the private key required by the script to authorize spending
C) The miner included the transaction in a block
D) The transaction fee is sufficient

- Correct answer: B
- Justification: Signatures satisfy spending conditions by proving private key control.
- Tag(s): bitcoin, scripts, signatures

Q19) Why is “hash-then-sign” commonly used?
A) To make signatures reversible
B) To allow encrypting the message
C) To sign a fixed-size digest efficiently regardless of message length
D) To avoid needing a private key

- Correct answer: C
- Justification: Hashing yields a fixed-size input for the signature algorithm.
- Tag(s): hashing, signatures, trap

Q20) Which statement best distinguishes a MAC from a digital signature?
A) MACs are public-key; signatures are symmetric-key
B) MACs require a shared secret; signatures are publicly verifiable with a public key
C) MACs provide confidentiality; signatures provide integrity
D) MACs are used only in Bitcoin

- Correct answer: B
- Justification: MACs are symmetric authentication; signatures enable public verification and non-repudiation.
- Tag(s): mac, signatures, trap

Q21) If someone can verify a signature, what must they have (at minimum)?
A) The signer’s private key
B) The signer’s public key and the signed message
C) The verifier’s private key
D) The shared secret used for encryption

- Correct answer: B
- Justification: Verification needs the public key and the exact message the signature covers.
- Tag(s): signatures, public-key, trap

Q22) If a private key is compromised, what is the best immediate implication for signatures made with it?
A) Past signatures become invalid automatically
B) The attacker can create new signatures that verify as you
C) Your public key becomes secret
D) Hash functions stop working

- Correct answer: B
- Justification: A compromised private key allows forging new valid signatures.
- Tag(s): keys, compromise, trap

Q23) Which statement about signatures and message meaning is most accurate?
A) Signatures guarantee the signer understood the message
B) Signatures guarantee the signer agrees with the message
C) Signatures guarantee only that the signer’s key authorized the exact bytes signed
D) Signatures guarantee confidentiality

- Correct answer: C
- Justification: Signatures bind to bytes, not interpretation.
- Tag(s): trap, semantics, signatures

Q24) What prevents an attacker from taking a valid signature on Message A and using it to validate Message B?
A) Nothing; signatures are reusable on any message
B) The public key changes every time
C) Verification includes the message; changing the message breaks verification
D) The message is encrypted

- Correct answer: C
- Justification: Signatures verify against the specific message content.
- Tag(s): signatures, integrity, trap

Q25) Which is a typical role of signatures in secure systems?
A) Error detection for typos
B) Proving authorization and preventing undetected modification
C) Making ciphertext shorter
D) Speeding up hashing

- Correct answer: B
- Justification: Signatures are used to authorize and to detect tampering.
- Tag(s): signatures, properties

## Drill Set: 2026-01-19 — Digital Signatures (Append — Level 3)

### SPEED DRILL (25 new questions total)

Q26) A signature is valid only with respect to the exact message that was signed.

- Correct answer: TRUE
- Justification: Verification checks the signature against the specific message bytes and public key.
- Tag(s): signatures, integrity

Q27) Digital signatures inherently hide the content of a message from observers.

- Correct answer: FALSE
- Justification: Signatures are not encryption; they don’t provide confidentiality.
- Tag(s): trap, signatures-vs-encryption

Q28) If you reuse the same ECDSA nonce (`k`) for two different messages, the private key can be recoverable in principle.

- Correct answer: TRUE
- Justification: ECDSA critically depends on unique, unpredictable nonces; reuse can leak the private key.
- Tag(s): trap, ecdsa, nonce

Q29) In signature systems, the public key must be authenticated/bound to an identity to prevent impersonation.

- Correct answer: TRUE
- Justification: If you trust a fake public key, you can be tricked into accepting forged-looking “identities.”
- Tag(s): trap, key-management, pki

Q30) A valid signature proves the signer used their private key at the moment the message was created.

- Correct answer: FALSE
- Justification: It proves private-key authorization of the bytes, not the time of signing.
- Tag(s): trap, semantics

Q31) In Bitcoin, signatures don’t sign “the txid”; they sign a transaction digest (sighash) that commits to specific fields.

- Correct answer: TRUE
- Justification: Bitcoin signatures cover a hashed serialization of the transaction per sighash rules.
- Tag(s): bitcoin, sighash, trap

Q32) If any field covered by the signature digest changes (e.g., an input or output), the signature should fail verification.

- Correct answer: TRUE
- Justification: Changing committed fields changes the digest and breaks signature validity.
- Tag(s): bitcoin, signatures, integrity

Q33) A digital signature can be verified without knowing the message, as long as you have the public key.

- Correct answer: FALSE
- Justification: Verification requires the exact message (or its digest) that was signed.
- Tag(s): trap, verification

Q34) A signature is only meaningful if the verifier knows which public key it should verify against.

- Correct answer: TRUE
- Justification: The same bytes could verify under one key and fail under another; key selection matters.
- Tag(s): trap, public-key, verification

Q35) In Bitcoin, a signature alone is sufficient to spend any UTXO.

- Correct answer: FALSE
- Justification: Spending must satisfy the specific script conditions (e.g., provide correct pubkey, signatures, scripts).
- Tag(s): trap, bitcoin, scripts

Q36) “Malleability” in signatures/transactions refers to changing data in a way that preserves validity but changes an identifier.

- Correct answer: TRUE
- Justification: Some forms of modification can keep a spend valid while changing the transaction id or encoding.
- Tag(s): trap, malleability

Q37) A digital signature’s security relies on keeping the public key secret.

- Correct answer: FALSE
- Justification: Public keys are meant to be public; private keys (and symmetric keys) must remain secret.
- Tag(s): trap, keys

Q38) In Bitcoin, SegWit reduces certain transaction malleability issues by moving signatures (witness) out of the txid hash.

- Correct answer: TRUE
- Justification: SegWit separates witness so txid excludes signatures, mitigating malleability vectors.
- Tag(s): bitcoin, segwit, malleability, trap

Q39) A signature check typically includes validating the signature encoding format and that it’s in an allowed/canonical range.

- Correct answer: TRUE
- Justification: Implementations enforce strict encoding and validity rules to avoid ambiguity and vulnerabilities.
- Tag(s): signatures, encoding, trap

Q40) “Non-repudiation” means no one else can ever produce a valid signature under your public key.

- Correct answer: FALSE
- Justification: It means third parties can verify authorization by a key holder (assuming key control), not that compromise is impossible.
- Tag(s): trap, non-repudiation

Q41) Which component must stay secret to prevent forgery?
A) Public key
B) Private key
C) Signature
D) Message

- Correct answer: B
- Justification: Anyone with the private key can create valid signatures.
- Tag(s): keys, trap

Q42) Which statement best describes what a signature verifies?
A) The message was encrypted
B) The message hash matches the block hash
C) The signer’s private key authorized the message and it wasn’t modified
D) The message came from a specific IP address

- Correct answer: C
- Justification: Verification checks authenticity (key authorization) and integrity.
- Tag(s): signatures, properties, trap

Q43) In Bitcoin, where are signatures typically provided when spending (conceptually)?
A) In the block header
B) In the UTXO set
C) In the spending transaction’s unlocking data (scriptSig / witness)
D) In the previous transaction’s outputs

- Correct answer: C
- Justification: The spender provides signatures in the input’s unlocking data/witness.
- Tag(s): bitcoin, scripts, segwit, trap

Q44) What is the main reason many systems sign a hash (digest) instead of the full message?
A) Hashing makes the message secret
B) Hashing yields a fixed-size input and standardizes what is being signed
C) Hashing removes the need for keys
D) Hashing makes signatures reversible

- Correct answer: B
- Justification: A fixed-size digest is efficient and consistent regardless of message length.
- Tag(s): hashing, signatures, trap

Q45) Which scenario is most directly addressed by authenticating public keys (e.g., certificates/PKI)?
A) Collision attacks on hash functions
B) Man-in-the-middle key substitution
C) Faster encryption
D) Larger key sizes

- Correct answer: B
- Justification: Authentication binds a public key to an identity to prevent substitution.
- Tag(s): pki, mitm, trap

Q46) In Bitcoin, which statement about “signing the transaction” is most accurate?
A) You sign the final txid string
B) You sign a digest of the transaction per sighash rules
C) You sign the block header
D) You sign the public key

- Correct answer: B
- Justification: Bitcoin signs a computed transaction digest that commits to selected parts of the transaction.
- Tag(s): bitcoin, sighash, trap

Q47) A MAC differs from a signature because:
A) A MAC can be verified publicly
B) A MAC uses a shared secret and can’t prove which party created it
C) A MAC provides confidentiality by default
D) A MAC requires a public keypair

- Correct answer: B
- Justification: Shared-key authentication lacks public verifiability and non-repudiation.
- Tag(s): mac, signatures, trap

Q48) If a private key is compromised, which action is most directly required to restore trust?
A) Keep using the same key; signatures will detect the attacker
B) Rotate to a new keypair and update any key bindings (addresses/scripts/certificates)
C) Make the public key secret
D) Increase the transaction fee

- Correct answer: B
- Justification: Compromise means the attacker can forge signatures; you must replace the key and update references.
- Tag(s): keys, compromise, trap

Q49) Which is a realistic consequence of not strictly defining signature encoding rules?
A) Faster verification
B) Ambiguous or multiple representations of “the same” signature, enabling malleability-like issues
C) Perfect secrecy
D) Automatic non-repudiation

- Correct answer: B
- Justification: Loose encoding rules can allow alternate valid encodings, causing ambiguity and malleability vectors.
- Tag(s): encoding, malleability, trap

Q50) What does a Bitcoin signature ultimately authorize?
A) Ownership of an address
B) Spending of a specific output under the script’s conditions
C) Mining rights for a block
D) Decryption of transaction data

- Correct answer: B
- Justification: It authorizes spending according to script rules for that UTXO.
- Tag(s): bitcoin, utxo, trap
