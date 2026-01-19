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
