# Fast-Fail Patterns

## HASH

      - Confusing hashing with encryption: “looks random” ≠ secrecy; hashes don’t conceal guessable inputs.
      - Mixing up collision resistance vs second-preimage resistance (the “any two” vs “given one” distinction).
      - Assuming txid uniquely encodes/contains the transaction data rather than merely identifying it.
      - Reversing HASH160 order (it’s RIPEMD-160 after SHA-256, not the other way around).
