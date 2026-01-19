## Drill Set: 2026-01-19 — Symmetric vs Asymmetric Cryptography

### SPEED DRILL (25 questions total)

Q1) Symmetric encryption uses the same secret key for encryption and decryption.

- Correct answer: TRUE
- Justification: One shared secret key is used on both sides in symmetric schemes.
- Tag(s): symmetric, basics

Q2) Asymmetric encryption uses the same key for encryption and decryption, but different key sizes.

- Correct answer: FALSE
- Justification: Asymmetric uses a keypair (public/private), not one key with different sizes.
- Tag(s): trap, asymmetric, basics

Q3) In public-key cryptography, a message encrypted with a recipient’s public key can be decrypted with the recipient’s private key.

- Correct answer: TRUE
- Justification: Public-key encryption is designed so only the corresponding private key can decrypt.
- Tag(s): asymmetric, encryption

Q4) If you encrypt with a private key, you achieve confidentiality because only the private key holder can decrypt it.

- Correct answer: FALSE
- Justification: “Encrypting with the private key” is better thought of as signing; confidentiality comes from encrypting to a public key.
- Tag(s): trap, signatures, encryption

Q5) Symmetric encryption is typically faster than asymmetric cryptography for large amounts of data.

- Correct answer: TRUE
- Justification: Symmetric ciphers are designed for high-throughput bulk encryption.
- Tag(s): symmetric, performance

Q6) Asymmetric cryptography eliminates the need for key distribution entirely.

- Correct answer: FALSE
- Justification: You still need authentic distribution of public keys (identity binding) to avoid MITM.
- Tag(s): trap, key-management, asymmetric

Q7) A digital signature provides integrity and authenticity, not confidentiality.

- Correct answer: TRUE
- Justification: Signatures prove who authorized data and that it wasn’t altered, but don’t hide it.
- Tag(s): signatures, properties

Q8) A MAC (message authentication code) is typically built from symmetric primitives and requires a shared secret.

- Correct answer: TRUE
- Justification: MAC verification requires the same shared secret used to generate it.
- Tag(s): mac, symmetric

Q9) If two parties already share a secret key, they can use symmetric cryptography for confidentiality and integrity (with authenticated encryption or MAC).

- Correct answer: TRUE
- Justification: Shared secret enables symmetric encryption and message authentication.
- Tag(s): symmetric, mac, ae

Q10) Asymmetric cryptography is mainly used in Bitcoin to encrypt all transaction data on-chain.

- Correct answer: FALSE
- Justification: Bitcoin transactions are public; asymmetric cryptography is used for signatures and keypairs, not bulk encryption.
- Tag(s): trap, bitcoin, asymmetric

Q11) In Bitcoin, ECDSA/Schnorr signatures are asymmetric: signing uses a private key and verification uses a public key.

- Correct answer: TRUE
- Justification: That private/public separation is the defining feature of asymmetric signatures.
- Tag(s): bitcoin, signatures, asymmetric

Q12) Symmetric encryption can provide non-repudiation because both parties share the same key.

- Correct answer: FALSE
- Justification: With a shared key, either party could have produced a MAC, so you can’t prove which one did.
- Tag(s): trap, non-repudiation, mac

Q13) Public-key encryption is primarily used to solve the “securely share a secret over an insecure channel” problem.

- Correct answer: TRUE
- Justification: A common use is establishing/transporting symmetric keys without a pre-shared secret.
- Tag(s): asymmetric, key-exchange

Q14) Key exchange protocols (e.g., Diffie–Hellman) can let two parties agree on a shared symmetric key without sending that key directly.

- Correct answer: TRUE
- Justification: The protocol derives a shared secret from exchanged public values.
- Tag(s): key-exchange, symmetric

Q15) Encrypt-then-MAC (or AEAD) is used because encryption alone does not automatically guarantee integrity.

- Correct answer: TRUE
- Justification: Confidentiality without integrity can be malleable; authenticated encryption addresses this.
- Tag(s): integrity, ae, trap

Q16) Which is the best example of symmetric cryptography in typical systems?
A) RSA signature verification
B) AES-GCM encryption
C) ECDSA signing
D) Schnorr signature verification

- Correct answer: B
- Justification: AES-GCM is a symmetric authenticated-encryption scheme.
- Tag(s): symmetric, ae

Q17) Which statement best matches “asymmetric encryption”?
A) Same key encrypts and decrypts
B) Public key encrypts, private key decrypts
C) Hashing with a public key
D) Encrypting with the private key for secrecy

- Correct answer: B
- Justification: Public-key encryption uses a public/private keypair with different roles.
- Tag(s): asymmetric, encryption, trap

Q18) In Bitcoin, what is the primary cryptographic purpose of your private key?
A) Decrypting blocks
B) Generating hashes for mining
C) Signing transactions to authorize spending
D) Verifying other people’s signatures

- Correct answer: C
- Justification: Spending requires producing a valid signature with the private key.
- Tag(s): bitcoin, signatures

Q19) What is the core limitation of MACs compared to digital signatures?
A) MACs are slower than signatures
B) MACs require a shared secret, so they don’t provide non-repudiation
C) MACs can’t provide integrity
D) MACs only work for public messages

- Correct answer: B
- Justification: Shared-key authentication can’t prove which party created the tag.
- Tag(s): mac, non-repudiation, trap

Q20) Why are hybrid schemes commonly used in practice (asymmetric + symmetric)?
A) Asymmetric is faster for bulk data
B) Symmetric avoids the need for any keys
C) Asymmetric establishes a key; symmetric encrypts the bulk data efficiently
D) Symmetric provides public verification

- Correct answer: C
- Justification: Public-key operations are expensive; symmetric handles large payloads efficiently.
- Tag(s): hybrid, performance

Q21) Which is the main risk if you don’t authenticate public keys (e.g., you accept a fake key)?
A) Collision attacks on hashes
B) Man-in-the-middle attacks
C) Faster encryption
D) Replay protection

- Correct answer: B
- Justification: An attacker can substitute their key and intercept encrypted communication.
- Tag(s): trap, asymmetric, mitm

Q22) Which pairing is correct?
A) AES = asymmetric; RSA = symmetric
B) ECDSA = symmetric; SHA-256 = asymmetric
C) AES = symmetric; ECDSA = asymmetric
D) Diffie–Hellman = symmetric; MAC = asymmetric

- Correct answer: C
- Justification: AES is symmetric; ECDSA is asymmetric signature cryptography.
- Tag(s): trap, symmetric, asymmetric

Q23) What does a digital signature allow a verifier to check?
A) Only that the data is secret
B) That the signer had the corresponding private key and the data wasn’t altered
C) That the signer shared a symmetric key with the verifier
D) That the data was mined into a block

- Correct answer: B
- Justification: Signature verification checks authenticity and integrity for that message.
- Tag(s): signatures, properties

Q24) Which statement is most accurate about symmetric encryption key distribution?
A) It’s trivial because the key can be public
B) It’s hard because both parties must securely obtain the same secret key
C) It’s solved by hashing the message
D) It’s unnecessary if you use a MAC

- Correct answer: B
- Justification: Securely sharing a secret key is the classic key distribution problem.
- Tag(s): symmetric, key-management, trap

Q25) Which is the best description of Diffie–Hellman’s role (conceptually)?
A) A symmetric cipher for encrypting blocks
B) A hash function used in mining
C) A key agreement method to derive a shared secret
D) A signature algorithm for authorizing transactions

- Correct answer: C
- Justification: DH enables two parties to compute a shared key from exchanged public values.
- Tag(s): key-exchange, asymmetric, trap

## Drill Set: 2026-01-19 — Symmetric vs Asymmetric Cryptography (Append A)

### SPEED DRILL (25 new questions total)

Q26) Symmetric cryptography uses two different keys: one to encrypt and one to decrypt.

- Correct answer: FALSE
- Justification: Using two different keys is the hallmark of asymmetric (public-key) cryptography.
- Tag(s): trap, symmetric, basics

Q27) Asymmetric cryptography is commonly used to establish or transport a symmetric session key, then symmetric encryption protects the bulk data.

- Correct answer: TRUE
- Justification: This is the standard hybrid design used in many real-world protocols.
- Tag(s): hybrid, asymmetric, symmetric

Q28) In a hybrid scheme, the large data payload is typically encrypted with the recipient’s public key for efficiency.

- Correct answer: FALSE
- Justification: Public-key encryption is slow, so it usually protects only a small session key, not bulk data.
- Tag(s): trap, hybrid, performance

Q29) A public key can be shared openly, but you must ensure it’s the correct key for the intended identity.

- Correct answer: TRUE
- Justification: Unauthenticated public keys enable man-in-the-middle substitution.
- Tag(s): asymmetric, key-management, mitm

Q30) A MAC provides non-repudiation because only the sender could have generated it.

- Correct answer: FALSE
- Justification: With a shared secret, either party could have produced a valid MAC.
- Tag(s): trap, mac, non-repudiation

Q31) A digital signature allows anyone with the public key to verify authenticity and integrity of the signed message.

- Correct answer: TRUE
- Justification: Public verification is a defining feature of signatures.
- Tag(s): signatures, asymmetric

Q32) If you lose your private key, you cannot decrypt messages that were encrypted to your public key.

- Correct answer: TRUE
- Justification: Decryption requires the private key corresponding to the public key used for encryption.
- Tag(s): asymmetric, encryption

Q33) Diffie–Hellman key exchange without authentication is still vulnerable to a man-in-the-middle attack.

- Correct answer: TRUE
- Justification: An attacker can establish separate shared secrets with each side unless identities/keys are authenticated.
- Tag(s): trap, key-exchange, mitm

Q34) Reusing the same nonce/IV with the same key in an AEAD scheme is generally safe if the plaintext changes.

- Correct answer: FALSE
- Justification: Nonce reuse can catastrophically break confidentiality and/or integrity in many AEAD modes.
- Tag(s): trap, ae, nonce

Q35) In asymmetric signatures, signing uses the private key and verification uses the public key.

- Correct answer: TRUE
- Justification: The key roles differ for signing vs verifying.
- Tag(s): signatures, asymmetric

Q36) Public-key encryption automatically guarantees message integrity even if you don’t use any authentication.

- Correct answer: FALSE
- Justification: Encryption does not necessarily authenticate; integrity typically requires AEAD, MAC, or a signature.
- Tag(s): trap, encryption, integrity

Q37) “Secret-key cryptography” is another name for symmetric cryptography.

- Correct answer: TRUE
- Justification: Both parties rely on a shared secret key.
- Tag(s): symmetric, basics

Q38) A MAC can be verified by anyone who has access to the public key.

- Correct answer: FALSE
- Justification: MAC verification requires the shared secret key, not a public key.
- Tag(s): trap, mac

Q39) In Bitcoin spending, the public key is used to verify a signature authorizing a transaction.

- Correct answer: TRUE
- Justification: Nodes verify signatures using the public key revealed in the spending path.
- Tag(s): bitcoin, signatures

Q40) Hashing is a form of encryption because it transforms plaintext into unreadable output.

- Correct answer: FALSE
- Justification: Hashing is one-way commitment/integrity tooling, not reversible encryption.
- Tag(s): trap, hashing-vs-encryption

Q41) Which primitive primarily provides non-repudiation?
A) MAC
B) Digital signature
C) Symmetric encryption
D) Hash function

- Correct answer: B
- Justification: Signatures are publicly verifiable and attributable to a private key holder.
- Tag(s): signatures, non-repudiation

Q42) Which statement best describes symmetric encryption?
A) Public key encrypts and private key decrypts
B) Same key encrypts and decrypts
C) Private key encrypts and public key decrypts
D) Anyone can decrypt if they know the hash

- Correct answer: B
- Justification: Symmetric schemes use one shared secret key for both directions.
- Tag(s): symmetric, basics

Q43) In Bitcoin, which algorithm category best matches ECDSA/Schnorr?
A) Symmetric encryption
B) Asymmetric digital signature
C) Hash function
D) Key stretching

- Correct answer: B
- Justification: They are public-key signature schemes.
- Tag(s): bitcoin, signatures, asymmetric

Q44) What is the missing security property when you perform Diffie–Hellman without authenticating the other party?
A) Confidentiality
B) Integrity
C) Authentication
D) Compression

- Correct answer: C
- Justification: Without authentication, DH can be intercepted and relayed by a MITM.
- Tag(s): trap, key-exchange, authentication

Q45) In a typical hybrid encryption design, what does the sender encrypt with the recipient’s public key?
A) The entire file contents
B) The symmetric session key
C) The recipient’s private key
D) The MAC tag

- Correct answer: B
- Justification: Public-key encryption is used to protect a small session key.
- Tag(s): hybrid, asymmetric

Q46) Which construction most directly provides confidentiality and integrity together?
A) Raw encryption only
B) Hashing only
C) AEAD (e.g., AES-GCM)
D) Public key only

- Correct answer: C
- Justification: AEAD is designed to provide authenticated encryption.
- Tag(s): ae, symmetric

Q47) Which is a common symmetric cipher?
A) AES
B) ECDSA
C) RSA
D) Diffie–Hellman

- Correct answer: A
- Justification: AES is a symmetric block cipher.
- Tag(s): symmetric, trap

Q48) Which statement about MACs vs signatures is correct?
A) MACs are publicly verifiable
B) Signatures require a shared secret
C) MACs require a shared secret; signatures do not
D) MACs provide non-repudiation

- Correct answer: C
- Justification: MACs are symmetric; signatures are asymmetric with public verification.
- Tag(s): mac, signatures, trap

Q49) Which key must remain secret to preserve security?
A) Public key
B) Private key
C) Address string
D) Certificate

- Correct answer: B
- Justification: The private key (and any symmetric keys) must remain secret.
- Tag(s): keys, trap

Q50) What is the best description of the “key distribution problem” for symmetric cryptography?
A) Symmetric keys are too long to store
B) Both parties must securely obtain the same secret key
C) Public keys are hard to compute
D) Hashes can’t be verified

- Correct answer: B
- Justification: Symmetric security depends on securely sharing a secret key.
- Tag(s): symmetric, key-management

## Drill Set: 2026-01-19 — Symmetric vs Asymmetric Cryptography (Append B)

### SPEED DRILL (25 new questions total)

Q51) Asymmetric encryption and digital signatures are the same operation performed in reverse.

- Correct answer: FALSE
- Justification: They are different primitives with different security goals (confidentiality vs authenticity/integrity).
- Tag(s): trap, asymmetric, signatures

Q52) A digital signature can be verified by a third party without any shared secret between verifier and signer.

- Correct answer: TRUE
- Justification: Verification uses the signer’s public key.
- Tag(s): signatures, asymmetric

Q53) If an attacker replaces a recipient’s public key with their own, public-key encryption can be compromised via man-in-the-middle.

- Correct answer: TRUE
- Justification: The sender may encrypt to the attacker’s key if key authenticity is not checked.
- Tag(s): trap, mitm, key-management

Q54) Schnorr signatures are a symmetric-key mechanism.

- Correct answer: FALSE
- Justification: Schnorr is an asymmetric (public-key) signature scheme.
- Tag(s): trap, signatures, asymmetric

Q55) ECDH is primarily a key agreement method, not a bulk encryption algorithm.

- Correct answer: TRUE
- Justification: ECDH derives a shared secret; symmetric encryption typically uses that secret.
- Tag(s): key-exchange, asymmetric

Q56) Digital signatures help detect message tampering because any change invalidates signature verification.

- Correct answer: TRUE
- Justification: Signatures bind the signed message to the signer’s private key.
- Tag(s): signatures, integrity

Q57) For a group of N users, pairwise symmetric shared keys scale roughly like N(N−1)/2.

- Correct answer: TRUE
- Justification: Each pair needs a distinct shared key in a naive symmetric-only model.
- Tag(s): symmetric, key-management, trap

Q58) In typical public-key systems, the public key can be derived from the private key, but not feasibly the other way around.

- Correct answer: TRUE
- Justification: Public keys are computed from private keys via a one-way math relationship.
- Tag(s): asymmetric, keys

Q59) Many systems sign a hash of the message rather than signing the full message bytes directly.

- Correct answer: TRUE
- Justification: Hash-then-sign is common for efficiency and standardization.
- Tag(s): signatures, hashing

Q60) A MAC tag can be shown to any third party as proof that a specific sender authored the message.

- Correct answer: FALSE
- Justification: Because the receiver shares the key, they could have forged the same MAC.
- Tag(s): trap, mac, non-repudiation

Q61) A Bitcoin address is literally the public key used to verify signatures.

- Correct answer: FALSE
- Justification: Addresses are encodings of hashes/script identifiers; public keys are typically revealed when spending.
- Tag(s): trap, bitcoin, keys

Q62) Asymmetric cryptography is commonly used for small pieces of data (like key exchange/signatures), while symmetric cryptography handles bulk encryption.

- Correct answer: TRUE
- Justification: This reflects the speed/size tradeoffs between public-key and symmetric primitives.
- Tag(s): hybrid, performance

Q63) If two parties already share a high-entropy secret key securely, they do not need asymmetric cryptography just to communicate confidentially.

- Correct answer: TRUE
- Justification: A pre-shared key can be sufficient for symmetric encryption plus integrity protection.
- Tag(s): symmetric, key-management

Q64) A one-time pad is a symmetric-key technique.

- Correct answer: TRUE
- Justification: It uses a shared secret key of equal length to the message.
- Tag(s): symmetric, trap

Q65) Using a strong symmetric cipher automatically provides perfect secrecy without any additional requirements.

- Correct answer: FALSE
- Justification: Perfect secrecy is a special property (e.g., OTP) and practical schemes rely on correct modes/nonces.
- Tag(s): trap, symmetric, ae

Q66) In Bitcoin, what proves you are authorized to spend from an output?
A) Your ability to decrypt the output
B) A valid digital signature meeting the script conditions
C) Your hash rate
D) The txid of the previous transaction

- Correct answer: B
- Justification: Spending requires satisfying the script, typically by providing a valid signature.
- Tag(s): bitcoin, signatures

Q67) Which is best described as a key agreement / key exchange method?
A) ECDH
B) AES
C) SHA-256
D) ECDSA

- Correct answer: A
- Justification: ECDH (Diffie–Hellman on elliptic curves) derives a shared secret.
- Tag(s): key-exchange, asymmetric, trap

Q68) Which requirement most directly supports non-repudiation?
A) Shared secret between parties
B) Publicly verifiable digital signatures
C) A checksum on the ciphertext
D) A longer symmetric key

- Correct answer: B
- Justification: Public verification tied to a private key holder enables non-repudiation.
- Tag(s): signatures, non-repudiation

Q69) What is the main practical downside of symmetric authentication (MAC) for attribution?
A) It requires a public key
B) Either party with the shared key can generate the MAC
C) It cannot detect tampering
D) It encrypts the data

- Correct answer: B
- Justification: Shared keys prevent attributing authorship to a single party.
- Tag(s): mac, trap

Q70) In a PKI (certificate) model, the main job of a certificate is to:
A) Hide the public key
B) Bind a public key to an identity
C) Make encryption faster
D) Replace hashing

- Correct answer: B
- Justification: Certificates authenticate that a public key belongs to a specific entity.
- Tag(s): pki, key-management, trap

Q71) In protocols like TLS, which cryptography typically encrypts the bulk application data after the handshake?
A) Asymmetric encryption
B) Symmetric encryption
C) Hashing only
D) Proof-of-work

- Correct answer: B
- Justification: TLS uses symmetric session keys for bulk data encryption.
- Tag(s): hybrid, symmetric

Q72) Which is a key scalability advantage of asymmetric cryptography?
A) It eliminates the need for any keys
B) A single keypair can be used to receive encrypted messages from many senders
C) It is always faster than symmetric crypto
D) It provides perfect secrecy automatically

- Correct answer: B
- Justification: Anyone can encrypt to your public key without pre-sharing a secret.
- Tag(s): asymmetric, key-management, trap

Q73) What does “encrypt-then-MAC” (or AEAD) most directly achieve?
A) Confidentiality only
B) Integrity only
C) Confidentiality plus integrity/authentication
D) Non-repudiation

- Correct answer: C
- Justification: Authenticated encryption protects both secrecy and tamper detection.
- Tag(s): ae, integrity, trap

Q74) Which pairing is correct for signature systems?
A) Public key signs; private key verifies
B) Private key signs; public key verifies
C) Same key signs and verifies
D) Hash verifies; nonce signs

- Correct answer: B
- Justification: Signature verification is public; signing requires the private key.
- Tag(s): signatures, trap

Q75) Which item is intended to be openly shareable?
A) Symmetric session key
B) Private key
C) Public key
D) Shared MAC key

- Correct answer: C
- Justification: Public keys are meant to be distributed; private/symmetric keys must remain secret.
- Tag(s): keys, basics
