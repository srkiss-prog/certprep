# Fast-Fail Patterns

Recurring mistakes, traps, and “looks true but isn’t” patterns found during drills.

## Hash Functions (Bitcoin)

- Confusing hashing with encryption: “looks random” ≠ secrecy; hashes don’t conceal guessable inputs.
- Mixing up collision resistance vs second-preimage resistance (the “any two” vs “given one” distinction).
- Assuming a `txid` uniquely encodes/contains the transaction data rather than merely identifying/committing to it.
- Reversing `HASH160` order (it’s `RIPEMD-160(SHA-256(x))`, not the other way around).
- Treating collision breaks as “everything stops” (PoW search is primarily preimage-style, not collision-finding).
- Assuming address checksums provide adversarial security rather than typo detection.
- Forgetting that transaction ordering matters for merkle roots (set vs sequence confusion).
- Mixing up what commits to witness data in SegWit (`txid`/header merkle root vs witness commitment / `wtxid` concepts).
- Assuming hashes provide authentication or confidentiality without a secret (MAC) or signature.

## Symmetric vs Asymmetric Cryptography

- Mixing up confidentiality vs authenticity: signatures/MACs don’t make data secret; encryption doesn’t automatically authenticate unless AEAD/MAC is used.
- “Encrypt with private key for secrecy” confusion: private-key “encryption” is effectively signing; confidentiality uses recipient’s public
  key.
- Assuming asymmetric crypto removes all key-distribution problems: you still must authenticate public keys to avoid MITM.
- Claiming symmetric systems provide non-repudiation: shared keys mean either party could have generated the MAC.
- Confusing key exchange (DH/ECDH) with encryption: DH agrees a shared secret; you still need symmetric encryption for data.
- Forgetting that unauthenticated DH/ECDH is MITM-vulnerable (you must authenticate identities/keys).
- Reusing an AEAD nonce/IV under the same key (can break confidentiality/integrity even if “the plaintext is different”).
- Treating a Bitcoin address as a public key or assuming transactions are encrypted on-chain (Bitcoin primarily uses signatures, not confidentiality).

## Digital Signatures

- Confusing signatures with encryption: signatures don’t hide data; they authenticate/ensure integrity.
- “Encrypt with private key” confusion: that’s conceptually signing; confidentiality uses public-key encryption to a recipient.
- Over-claiming what a signature proves: it proves key authorization of bytes, not intent, truth, or meaning.
- Mixing MACs and signatures: MACs require shared secrets and don’t provide public verifiability/non-repudiation.
- Thinking “signature proves time” or “signature proves intent”; without extra context, it only proves key authorization of specific bytes.
- Confusing what Bitcoin signs: the signature covers a transaction digest (sighash), not “the txid string”.
- Missing the ECDSA nonce requirement: nonce reuse/bad randomness can leak the private key.
- Ignoring encoding/canonical rules (leading to malleability-like issues): multiple valid encodings can change identifiers while keeping spends valid.

## Keys & Addresses

- Treating an address as where coins are stored (UTXOs are locked by scripts; addresses are encodings for those scripts).
- Confusing checksum with security (checksums catch typos; they don’t stop attackers).
- Mixing up what’s revealed when spending (typically signature + pubkey/script, not the private key).
- Confusing Bech32 vs Base58Check (different encodings; Bech32 is for SegWit witness programs).
- Assuming different addresses always mean different private keys (wallets derive many addresses from one root secret).
- Confusing “watch-only” (xpub) capability with spending capability (xpub tracks; private keys spend).
- Mixing up Bech32 vs Bech32m (SegWit v0 vs v1+ encoding) and assuming they’re interchangeable.
- Treating “change address” as a special address type rather than a wallet behavior (change can be any valid address type).
- Assuming one output always corresponds to one key (multisig and script conditions can require multiple keys).
- Confusing address knowledge with wallet knowledge (an address does not imply you can derive xpub/seed/private keys).
- Restoring a seed with the wrong derivation path/account or insufficient gap limit and concluding funds are “missing”.
- Mixing up nested SegWit (Base58Check P2SH wrapper) with native SegWit (Bech32/Bech32m witness programs).
- Overstating what an address checksum does (typo detection only; not network integrity or anti-theft).

## Transactions & UTXOs

- Thinking inputs “contain” value; value lives in the referenced UTXO, not the input.
- Treating addresses as account balances (Bitcoin tracks UTXOs, not accounts).
- Confusing mempool policy with consensus validity (zero-fee can be valid but not relayed/mined).
- Forgetting coinbase maturity (coinbase outputs aren’t immediately spendable).
- Miscomputing fees (fee is implicit: sum(inputs) − sum(outputs), not an explicit output).
- Assuming the UTXO set includes mempool outputs (it’s confirmed state only).
- Confusing RBF vs CPFP (replacement vs child spending) and when each applies.
- Forgetting that txid can change due to malleability for some transaction types.
- Thinking nLockTime/nSequence always invalidate a transaction (they enforce timing/relative constraints).
- Treating dust as consensus-invalid rather than policy-limited.
