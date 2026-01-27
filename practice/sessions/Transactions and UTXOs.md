## Drill Set: 2026-01-20 — Transactions & UTXOs

### SPEED DRILL (25 questions total)

Q1) In Bitcoin, transactions consume UTXOs as inputs and create new UTXOs as outputs.

- Correct answer: TRUE
- Justification: Inputs spend previous outputs; outputs create new spendable UTXOs.
- Tag(s): utxo, transactions, basics

Q2) A transaction input directly contains the coin value being spent.

- Correct answer: FALSE
- Justification: The value is defined by the referenced UTXO, not stored in the input itself.
- Tag(s): trap, inputs, utxo

Q3) If an output is spent, it is removed from the UTXO set.

- Correct answer: TRUE
- Justification: Spent outputs are no longer unspent and are removed from the UTXO set.
- Tag(s): utxo, state

Q4) A transaction can have more value in its outputs than the sum of its inputs.

- Correct answer: FALSE
- Justification: That would create value from nothing; outputs must be ≤ inputs, with the difference as fee.
- Tag(s): trap, fees, conservation

Q5) The transaction fee equals the sum of inputs minus the sum of outputs.

- Correct answer: TRUE
- Justification: Any leftover value becomes the miner fee.
- Tag(s): fees, basics

Q6) An unconfirmed transaction can still create spendable outputs that may be spent in child transactions.

- Correct answer: TRUE
- Justification: Unconfirmed outputs can be spent in a chain (subject to mempool policy).
- Tag(s): mempool, chaining, trap

Q7) A coinbase transaction spends a previous UTXO like any normal transaction.

- Correct answer: FALSE
- Justification: Coinbase creates new coins and does not have normal inputs.
- Tag(s): trap, coinbase

Q8) A transaction ID (txid) uniquely identifies the transaction’s contents under legacy rules, but can change under malleability in some cases.

- Correct answer: TRUE
- Justification: Malleability can alter serialized data while keeping a spend valid, changing the txid.
- Tag(s): txid, malleability, trap

Q9) In the UTXO model, account balances are stored directly on-chain per address.

- Correct answer: FALSE
- Justification: Bitcoin tracks discrete unspent outputs, not account balances.
- Tag(s): trap, utxo, accounts

Q10) A transaction output includes a locking script that defines the conditions required to spend it.

- Correct answer: TRUE
- Justification: The output script (scriptPubKey) specifies spending conditions.
- Tag(s): scripts, outputs

Q11) If you reuse an input from the same UTXO in two different transactions, both can confirm (double spend).

- Correct answer: FALSE
- Justification: Only one spend of a UTXO can be confirmed; the other is invalid.
- Tag(s): trap, double-spend, utxo

Q12) The mempool is a pool of unconfirmed transactions maintained by nodes.

- Correct answer: TRUE
- Justification: Nodes hold valid, unconfirmed transactions in their mempool.
- Tag(s): mempool, basics

Q13) A transaction with zero fee is always invalid by consensus.

- Correct answer: FALSE
- Justification: Zero-fee is allowed by consensus; it may be rejected by policy.
- Tag(s): trap, fees, policy-vs-consensus

Q14) The UTXO set represents the current spendable state of the blockchain.

- Correct answer: TRUE
- Justification: It’s the collection of all unspent outputs at a given chain tip.
- Tag(s): utxo, state

Q15) A transaction output can be “dust” if it’s too small to be worth spending under typical fee policies.

- Correct answer: TRUE
- Justification: Dust outputs are often uneconomical to spend due to fees.
- Tag(s): dust, fees, trap

Q16) Which best describes a UTXO?
A) A confirmed transaction in the mempool
B) An unspent transaction output that can be spent if you meet its script conditions
C) A private key stored in a wallet
D) A block header field

- Correct answer: B
- Justification: UTXOs are the spendable outputs referenced by new transactions.
- Tag(s): utxo, basics

Q17) Which item is required to compute a transaction fee?
A) The number of inputs only
B) The sum of input values and sum of output values
C) The block height
D) The address checksum

- Correct answer: B
- Justification: Fee = sum(inputs) − sum(outputs).
- Tag(s): fees, trap

Q18) Which statement about coinbase outputs is correct?
A) They can be spent immediately
B) They cannot be spent until they reach a maturity period
C) They are always zero-value
D) They are only for fees, not new coins

- Correct answer: B
- Justification: Coinbase outputs require a maturity period before spending.
- Tag(s): coinbase, maturity, trap

Q19) Which is the most accurate description of “change” in a transaction?
A) The fee paid to miners
B) The leftover input value sent back to the sender
C) The script that locks the outputs
D) The UTXO set size

- Correct answer: B
- Justification: Change returns remaining value to the sender after paying recipients and fee.
- Tag(s): change, outputs, trap

Q20) Which statement is correct about transaction inputs?
A) They create new coins
B) They reference previous outputs and provide unlocking data
C) They store their own value fields
D) They are never signatures

- Correct answer: B
- Justification: Inputs reference UTXOs and include data to satisfy the locking script.
- Tag(s): inputs, scripts

Q21) If a transaction has two inputs of 0.6 BTC each and two outputs of 0.5 BTC each, the fee is:
A) 0.0 BTC
B) 0.1 BTC
C) 0.2 BTC
D) 1.0 BTC

- Correct answer: C
- Justification: Inputs 1.2 BTC − outputs 1.0 BTC = 0.2 BTC fee.
- Tag(s): fees, arithmetic, trap

Q22) Which statement best distinguishes consensus rules from mempool policy?
A) Consensus rules are optional; mempool policy is mandatory
B) Consensus rules decide validity; mempool policy decides relay/mining preferences
C) Mempool policy can create coins
D) Consensus rules only apply to unconfirmed transactions

- Correct answer: B
- Justification: Consensus defines validity; policy governs relay/mining acceptance.
- Tag(s): policy-vs-consensus, trap

Q23) Which is true about a UTXO’s “owner”?
A) Ownership is stored as a balance in an address
B) Ownership is whoever can satisfy the locking script
C) Ownership is whoever mined the block
D) Ownership is whoever first broadcasts a spend

- Correct answer: B
- Justification: Control is defined by the ability to satisfy the script conditions.
- Tag(s): scripts, trap

Q24) Which statement about transaction size and fees is most accurate?
A) Fees are based on the number of outputs only
B) Fees are typically based on transaction size (bytes) rather than value
C) Fees are fixed by consensus
D) Fees are paid by outputs, not inputs

- Correct answer: B
- Justification: Fee markets price by bytes (weight/vbytes), not by value.
- Tag(s): fees, size, trap

Q25) Which output type most directly locks to a script hash?
A) P2PKH
B) P2SH
C) P2TR
D) P2WPKH

- Correct answer: B
- Justification: P2SH outputs commit to the hash of a redeem script.
- Tag(s): p2sh, scripts, trap

## Drill Set: 2026-01-20 — Transactions & UTXOs (Append A — Level 3)

### SPEED DRILL (25 new questions total)

Q26) A transaction output’s value is defined in the output itself, not in the locking script.

- Correct answer: TRUE
- Justification: The amount is a numeric field in the output; the script only defines spending conditions.
- Tag(s): outputs, trap

Q27) A transaction can be valid even if it is not relayed by most nodes due to policy.

- Correct answer: TRUE
- Justification: Policy affects relay/mining, not consensus validity.
- Tag(s): policy-vs-consensus, trap

Q28) Replace-by-Fee (RBF) allows a sender to replace an unconfirmed transaction with a higher-fee version under certain rules.

- Correct answer: TRUE
- Justification: RBF is a mempool policy that permits fee-bumping by replacement.
- Tag(s): rbf, mempool, trap

Q29) In Bitcoin, the “UTXO set” includes unconfirmed outputs from the mempool.

- Correct answer: FALSE
- Justification: The UTXO set reflects confirmed chain state only, not mempool outputs.
- Tag(s): trap, utxo, mempool

Q30) An input references a previous output using a transaction ID and output index (vout).

- Correct answer: TRUE
- Justification: Inputs identify the exact prior output by txid + output index.
- Tag(s): inputs, basics

Q31) A transaction can have zero outputs and still be valid.

- Correct answer: FALSE
- Justification: Transactions must have at least one output; otherwise value has nowhere to go.
- Tag(s): trap, outputs

Q32) Child-pays-for-parent (CPFP) is a fee-bumping method that relies on spending an unconfirmed output.

- Correct answer: TRUE
- Justification: A high-fee child can incentivize miners to include the parent.
- Tag(s): cpfp, mempool, trap

Q33) The sum of input values must equal the sum of output values exactly for a transaction to be valid.

- Correct answer: FALSE
- Justification: The difference is the transaction fee, which can be nonzero.
- Tag(s): trap, fees

Q34) A transaction output can be spent only once; any second attempt is invalid.

- Correct answer: TRUE
- Justification: Spending a UTXO removes it from the UTXO set.
- Tag(s): utxo, double-spend

Q35) In Bitcoin, signatures in inputs typically authorize spending by satisfying the output’s locking script.

- Correct answer: TRUE
- Justification: Inputs provide unlocking data (signature/pubkey/scripts) to satisfy the script.
- Tag(s): scripts, signatures

Q36) A higher-fee child transaction can make a low-fee parent more likely to be mined (CPFP).

- Correct answer: TRUE
- Justification: Miners may include the package to collect the combined fees.
- Tag(s): cpfp, fees

Q37) A transaction’s fee is explicitly specified in a “fee” field.

- Correct answer: FALSE
- Justification: Fees are implicit: inputs minus outputs.
- Tag(s): trap, fees

Q38) An output can be “provably unspendable” (e.g., OP_RETURN), effectively removing value from circulation.

- Correct answer: TRUE
- Justification: OP_RETURN outputs are unspendable and are typically used for data, not value.
- Tag(s): op_return, trap

Q39) Transaction weight/vsize affects fee rates because miners generally select by fee per weight/byte.

- Correct answer: TRUE
- Justification: Fee markets typically price in sats per vbyte/weight units.
- Tag(s): fees, size, trap

Q40) A transaction can spend outputs from multiple previous transactions in a single transaction.

- Correct answer: TRUE
- Justification: Inputs can reference multiple UTXOs from different txids.
- Tag(s): inputs, utxo

Q41) Which best describes “RBF”?
A) A consensus rule requiring minimum fees
B) A policy that allows replacing an unconfirmed transaction with a higher-fee version
C) A rule that prevents any replacement of unconfirmed transactions
D) A method to create coins

- Correct answer: B
- Justification: RBF is a policy for replacing unconfirmed transactions.
- Tag(s): rbf, mempool, trap

Q42) What identifies a specific UTXO being spent?
A) The sender’s address
B) The txid and output index (vout)
C) The scriptPubKey only
D) The block height only

- Correct answer: B
- Justification: Inputs reference UTXOs by txid + vout.
- Tag(s): utxo, inputs, trap

Q43) Which statement about mempool transactions is most accurate?
A) They are part of consensus state
B) They can be dropped or evicted without changing chain validity
C) They are permanently stored in blocks
D) They can’t be replaced

- Correct answer: B
- Justification: Mempool is local/policy-based; transactions can be evicted or replaced.
- Tag(s): mempool, policy-vs-consensus, trap

Q44) Which is true about coinbase transactions?
A) They must reference a previous output
B) They create new coins and collect fees
C) They can be spent immediately
D) They are invalid if they have any outputs

- Correct answer: B
- Justification: Coinbase creates new coins and claims fees; it has no normal inputs.
- Tag(s): coinbase, trap

Q45) Which output type is most directly associated with OP_RETURN?
A) Spendable output with a scriptPubKey condition
B) Provably unspendable output used to embed data
C) Multi-signature output
D) P2TR output

- Correct answer: B
- Justification: OP_RETURN marks outputs as unspendable and used for data.
- Tag(s): op_return, trap

Q46) Which statement about transaction malleability is correct?
A) It changes the UTXO set without changing any transaction bytes
B) It can alter a transaction’s txid without invalidating the spend
C) It only affects confirmed transactions
D) It is impossible after SegWit for all transactions

- Correct answer: B
- Justification: Malleability can change txid while keeping the spend valid.
- Tag(s): malleability, trap

Q47) Which is a valid reason to use CPFP instead of RBF?
A) The original transaction is already confirmed
B) You don’t control the original transaction inputs but you can spend one of its outputs
C) You want to lower the fee
D) RBF is required by consensus

- Correct answer: B
- Justification: CPFP works by spending the parent’s output, which may be possible even if you didn’t create the parent.
- Tag(s): cpfp, rbf, trap

Q48) Which is the best description of “transaction chaining”?
A) Spending outputs from unconfirmed transactions in a sequence
B) Combining multiple inputs into one output only
C) Encrypting a transaction before broadcasting
D) Replacing transactions in the mempool

- Correct answer: A
- Justification: Chaining uses unconfirmed outputs as inputs in new transactions.
- Tag(s): chaining, mempool

Q49) Which statement about dust is most accurate?
A) Dust outputs are invalid by consensus
B) Dust outputs can be valid but may be rejected by policy as uneconomical to spend
C) Dust refers to any output below 1 BTC
D) Dust outputs are always OP_RETURN outputs

- Correct answer: B
- Justification: Dust is policy/fee-related, not necessarily invalid by consensus.
- Tag(s): dust, policy-vs-consensus, trap

Q50) Which best describes why transactions have a “change output”?
A) To pay miners directly
B) To return leftover input value to the sender
C) To store address balances
D) To reduce tx size

- Correct answer: B
- Justification: Change returns excess input value after payments and fees.
- Tag(s): change, outputs

## Drill Set: 2026-01-20 — Transactions & UTXOs (Append B — Level 3)

### SPEED DRILL (25 new questions total)

Q51) A transaction with one input and one output can still pay a fee.

- Correct answer: TRUE
- Justification: The fee is the difference between the input value and output value.
- Tag(s): fees, basics

Q52) A transaction is invalid if any input references a non-existent or already-spent output.

- Correct answer: TRUE
- Justification: Inputs must reference an existing unspent output.
- Tag(s): utxo, validation

Q53) A mempool replacement (RBF) must always increase the fee rate compared to the replaced transaction.

- Correct answer: TRUE
- Justification: Policy requires a higher fee rate to accept the replacement.
- Tag(s): rbf, policy, trap

Q54) A transaction that creates outputs but has no inputs is always invalid.

- Correct answer: FALSE
- Justification: Coinbase transactions have no normal inputs and can be valid in a block.
- Tag(s): trap, coinbase

Q55) In Bitcoin, the sum of all UTXOs represents the total coin supply at a given block height.

- Correct answer: TRUE
- Justification: The UTXO set reflects all spendable outputs, which sum to the current supply.
- Tag(s): utxo, supply, trap

Q56) If a transaction has multiple inputs, each input can have its own scriptSig/witness.

- Correct answer: TRUE
- Justification: Each input provides its own unlocking data for the referenced output.
- Tag(s): inputs, scripts

Q57) The “nLockTime” field can make a transaction invalid until a certain block height or time.

- Correct answer: TRUE
- Justification: nLockTime enforces a minimum height/time before the transaction is valid.
- Tag(s): nlocktime, trap

Q58) The UTXO model prevents double spending by ensuring each output can be consumed only once.

- Correct answer: TRUE
- Justification: Consensus rules prevent spending an already-spent output.
- Tag(s): utxo, double-spend

Q59) A transaction’s validity depends on mempool policy.

- Correct answer: FALSE
- Justification: Validity is consensus; policy only affects relay/mining.
- Tag(s): policy-vs-consensus, trap

Q60) The locktime applies to each input separately and is stored in the input.

- Correct answer: FALSE
- Justification: nLockTime is a transaction-level field, not per-input.
- Tag(s): trap, nlocktime

Q61) A transaction can be valid but never appear in a block if no miner includes it.

- Correct answer: TRUE
- Justification: Validity doesn’t guarantee inclusion; miners choose what to include.
- Tag(s): mempool, fees

Q62) “Sequence” (nSequence) values are completely ignored in modern Bitcoin and have no effect.

- Correct answer: FALSE
- Justification: nSequence can signal opt-in RBF and is used with relative timelocks.
- Tag(s): trap, nsequence, rbf

Q63) Relative timelocks (BIP68/CSV) can restrict spending until a certain number of blocks or time has passed since the UTXO was confirmed.

- Correct answer: TRUE
- Justification: CSV enforces relative locktime based on UTXO age.
- Tag(s): csv, timelock, trap

Q64) A transaction’s weight depends on its inputs/outputs and whether it uses witness data.

- Correct answer: TRUE
- Justification: Witness data is discounted, affecting weight/vsize.
- Tag(s): fees, weight, segwit

Q65) If the sum of outputs exceeds the sum of inputs, the transaction is still valid as long as it pays a fee.

- Correct answer: FALSE
- Justification: Outputs cannot exceed inputs; there is no “negative fee.”
- Tag(s): trap, fees

Q66) Which field can signal opt-in RBF?
A) nLockTime
B) nSequence
C) scriptPubKey
D) txid

- Correct answer: B
- Justification: RBF is signaled via nSequence below a threshold.
- Tag(s): rbf, nsequence, trap

Q67) Which is true about time-locked transactions?
A) They are invalid forever
B) They are valid only after the specified height/time
C) They can bypass script rules
D) They must be coinbase transactions

- Correct answer: B
- Justification: Timelocks delay validity until a specified time or block height.
- Tag(s): timelock, trap

Q68) Which statement best describes transaction “weight”?
A) A metric combining base size and witness size used for fee calculation
B) The total BTC value of inputs
C) The number of outputs only
D) A field stored in the block header

- Correct answer: A
- Justification: Weight accounts for witness discount and influences fee rates.
- Tag(s): weight, fees, trap

Q69) Which statement about coinbase maturity is correct?
A) It is a mempool policy only
B) It is a consensus rule preventing immediate spending of coinbase outputs
C) It applies to all outputs
D) It is optional for miners

- Correct answer: B
- Justification: Coinbase maturity is enforced by consensus.
- Tag(s): coinbase, maturity, trap

Q70) If a transaction is replaced via RBF, the original transaction is automatically confirmed.

- Correct answer: FALSE
- Justification: Replacement removes the original from the mempool; it is not confirmed.
- Tag(s): rbf, trap

Q71) A valid transaction can include multiple outputs to different recipients in one transaction.

- Correct answer: TRUE
- Justification: Transactions commonly pay multiple outputs.
- Tag(s): outputs, basics

Q72) A “double spend” is any transaction with more than one input.

- Correct answer: FALSE
- Justification: Double spending refers to spending the same UTXO twice.
- Tag(s): trap, double-spend

Q73) If a transaction is mined, all of its inputs must correspond to UTXOs that were unspent at the time of inclusion.

- Correct answer: TRUE
- Justification: Consensus rules require referenced outputs to be unspent at inclusion.
- Tag(s): utxo, validation

Q74) A transaction can be valid even if it is non-standard by policy rules.

- Correct answer: TRUE
- Justification: Policy affects relay/mining, not consensus validity.
- Tag(s): policy-vs-consensus, trap

Q75) Which is most accurate about dust limits?
A) They are fixed by consensus and never change
B) They are policy thresholds that can vary by node implementation
C) They prevent UTXO creation entirely
D) They are stored in the block header

- Correct answer: B
- Justification: Dust is a policy concept and can vary by node.
- Tag(s): dust, policy-vs-consensus, trap
