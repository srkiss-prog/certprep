# Hash definition and properties

Hash functions map arbitrary data to a fixed-length digest deterministically. Good cryptographic hashes are preimage-resistant, second-preimage-resistant, and collision-resistant, and exhibit avalanche behavior. Bitcoin uses hashes for proof-of-work (SHA-256), linking blocks (hash pointers), transaction IDs (double-SHA256), merkle trees (efficient inclusion proofs), and address/checksum construction (SHA-256 + RIPEMD-160 for P2PKH/P2SH; Base58Check uses a checksum). Hashes provide integrity and commitment, not secrecy.

# What a Bitcoin Block Header Actually Contains

A Bitcoin _block header_ is 80 bytes and includes (simplified):

version
previous_block_hash ← THIS is the hash pointer
merkle_root
timestamp
difficulty_target
nonce

That previous_block_hash is:

SHA256(SHA256(previous_block_header))

Why This Is a _Hash Pointer_ (Even Without a “Pointer”)

A classical hash pointer is:

(reference, hash(data))

In Bitcoin:

Classical concept Bitcoin implementation
Pointer previous_block_hash
Data previous block header
Hash SHA-256d of that header

_The hash itself uniquely identifies the referenced data._
So Bitcoin uses content-addressing instead of memory pointers.

**The hash is the pointer.**

# Merkle Root

## Definition

A Merkle root is the single hash at the top of a Merkle tree, which is a binary tree of hashes built from a set of data items (e.g., transactions).

## How it works

Hash each transaction → leaf hashes

Pair hashes and hash them together → parent hashes

Repeat until one hash remains → Merkle root

## Why it matters

Compact commitment to all transactions in a block

Any change to any transaction changes the Merkle root

_Enables efficient verification with minimal data_

## Key properties

_O(log n) verification_

Strong integrity guarantees

Used in Bitcoin block headers

# Base58Check

## Definition

Base58Check is an encoding format used primarily in Bitcoin to encode binary data (like addresses) into a human-friendly string with built-in error detection.

## What it includes

- Version byte (e.g., address type)
- Payload (e.g., public key hash)
- Checksum (first 4 bytes of double SHA-256)
- Encoded using Base58

## Why Base58 (not Base64)

- Removes visually ambiguous characters:
- No 0 (zero), O (capital o)
- No I, l, +, /
- Safer for manual copy/paste

## Key properties

- Detects accidental errors (typos)
- Improves UX for addresses
- Not encryption, only encoding + checksum

# Avalanche Effect

A small change in input (e.g., flipping 1 bit) causes a large, unpredictable change (~50%) in output.
