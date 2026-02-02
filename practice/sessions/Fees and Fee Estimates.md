## Drill Set: 2026-01-20 — Fees & Fee Estimates

### SPEED DRILL (25 questions total)

Q1) In Bitcoin, the transaction fee is the sum of inputs minus the sum of outputs.

- Correct answer: TRUE
- Justification: Fees are implicit from the input/output difference.
- Tag(s): fees, basics

Q2) A transaction’s fee is written in a dedicated “fee” field in the transaction.

- Correct answer: FALSE
- Justification: There is no explicit fee field; it’s computed implicitly.
- Tag(s): trap, fees

Q3) Fee rates are typically quoted in sats per vbyte (sat/vB).

- Correct answer: TRUE
- Justification: Fee markets price by weight/virtual size, commonly expressed in sat/vB.
- Tag(s): fees, rate, weight

Q4) Increasing the fee rate generally increases the likelihood of faster confirmation.

- Correct answer: TRUE
- Justification: Miners tend to prioritize higher fee rates.
- Tag(s): fees, mempool, policy

Q5) A transaction’s fee rate depends on its absolute BTC value, not its size.

- Correct answer: FALSE
- Justification: Fee markets price by size (weight/vbytes), not transaction value.
- Tag(s): trap, fees, size

Q6) SegWit reduces the effective fee cost of witness data by applying a weight discount.

- Correct answer: TRUE
- Justification: Witness data counts less toward transaction weight.
- Tag(s): segwit, fees, weight

Q7) A larger transaction (more inputs/outputs) typically requires a higher total fee to reach the same fee rate.

- Correct answer: TRUE
- Justification: More bytes at the same sat/vB implies higher total fee.
- Tag(s): fees, size

Q8) A zero-fee transaction is always invalid by consensus.

- Correct answer: FALSE
- Justification: Zero-fee can be valid; it may be rejected by policy.
- Tag(s): trap, policy-vs-consensus

Q9) Fee estimation is deterministic and identical across all nodes.

- Correct answer: FALSE
- Justification: Estimates vary by node based on local mempool and policy settings.
- Tag(s): trap, fee-estimates, mempool

Q10) Replace-by-Fee (RBF) can be used to increase a fee for an unconfirmed transaction.

- Correct answer: TRUE
- Justification: RBF is a policy that allows fee-bumping by replacement.
- Tag(s): rbf, fees, policy

Q11) Child-Pays-For-Parent (CPFP) can increase effective fees by spending an unconfirmed output with a high-fee child.

- Correct answer: TRUE
- Justification: Miners may include the package to collect combined fees.
- Tag(s): cpfp, fees, mempool

Q12) The fee rate is calculated as (inputs − outputs) / vbytes.

- Correct answer: TRUE
- Justification: Fee = inputs − outputs; dividing by vsize yields sat/vB.
- Tag(s): fees, rate

Q13) Dust outputs are always invalid by consensus.

- Correct answer: FALSE
- Justification: Dust is a policy/economic concept, not necessarily consensus-invalid.
- Tag(s): trap, dust, policy

Q14) Consolidating many small UTXOs into one output can be cheaper when fees are low.

- Correct answer: TRUE
- Justification: Consolidation creates large transactions; doing it at low fees can save cost.
- Tag(s): utxo, fees, strategy

Q15) A transaction’s virtual size (vsize) is derived from its weight.

- Correct answer: TRUE
- Justification: vsize is weight divided by 4 (rounded up).
- Tag(s): weight, vsize, fees

Q16) Which statement best describes “fee rate”?
A) Total fee paid regardless of size
B) Fee per unit size (e.g., sat/vB)
C) The number of inputs
D) The transaction value

- Correct answer: B
- Justification: Fee rate is the fee per size unit.
- Tag(s): fees, rate, trap

Q17) Which policy tool is most directly used to bump the fee of your own unconfirmed transaction?
A) RBF
B) Coinbase maturity
C) OP_RETURN
D) ScriptSig

- Correct answer: A
- Justification: RBF replaces your unconfirmed tx with a higher-fee version.
- Tag(s): rbf, fees, trap

Q18) Which is a likely outcome of setting a very low fee rate when the mempool is congested?
A) Faster confirmation
B) Slower confirmation or non-confirmation
C) Higher priority by miners
D) Automatic fee increase by consensus

- Correct answer: B
- Justification: Low fee rate reduces priority during congestion.
- Tag(s): fees, mempool, trap

Q19) Which input choice typically increases transaction size the most?
A) Spending one large UTXO
B) Spending many small UTXOs
C) Spending a P2WPKH output
D) Spending a single P2TR output

- Correct answer: B
- Justification: Each additional input adds size; many small UTXOs add more bytes.
- Tag(s): utxo, fees, size

Q20) Which is most accurate about fee estimation?
A) It is a consensus rule
B) It depends on local mempool conditions and desired confirmation target
C) It is fixed at 1 sat/vB
D) It depends only on transaction value

- Correct answer: B
- Justification: Estimates are policy/market-driven and node-dependent.
- Tag(s): fee-estimates, mempool, trap

Q21) If you want to reduce fees, one common strategy is to minimize the number of inputs when possible.

- Correct answer: TRUE
- Justification: Fewer inputs generally means smaller size and lower fees at the same fee rate.
- Tag(s): fees, size, utxo

Q22) Which statement about CPFP is correct?
A) It requires access to the original transaction’s inputs
B) It works by spending an output of the unconfirmed transaction
C) It is a consensus rule
D) It always lowers the fee

- Correct answer: B
- Justification: CPFP uses a high-fee child that spends a parent’s output.
- Tag(s): cpfp, fees, trap

Q23) Which is the best description of “mempool fee spike”?
A) A decrease in transaction volume
B) A temporary rise in required fee rates due to higher demand
C) A consensus rule change
D) A mining reward increase

- Correct answer: B
- Justification: Higher demand raises fee rates needed for timely confirmation.
- Tag(s): fees, mempool, trap

Q24) Which statement about fee sniping is most accurate?
A) It is a standard fee estimate algorithm
B) It is the practice of miners attempting to re-mine recent blocks to capture fees
C) It increases transaction size
D) It is required by consensus

- Correct answer: B
- Justification: Fee sniping refers to miners trying to capture recent fees by reorgs.
- Tag(s): fees, mining, trap

Q25) Which statement about transaction fees is correct?
A) Fees are paid by outputs directly
B) Fees are paid by inputs implicitly via the input–output difference
C) Fees are always a fixed percentage of transaction value
D) Fees are stored in the block header

- Correct answer: B
- Justification: Inputs minus outputs defines the fee.
- Tag(s): fees, basics
