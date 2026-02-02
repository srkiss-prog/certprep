## Drill Set: 2026-01-20 — Mining and Block Rewards

### SPEED DRILL (25 questions total)

Q1) Bitcoin miners perform proof-of-work by hashing block headers to find a hash below a target.

- Correct answer: TRUE
- Justification: Mining searches for a header hash under the current target.
- Tag(s): pow, mining, basics

Q2) The block reward is paid directly by users in the block as transaction fees.

- Correct answer: FALSE
- Justification: The block reward includes newly minted coins plus fees; new coins are not paid by users.
- Tag(s): trap, block-reward, fees

Q3) The coinbase transaction creates new bitcoins and collects transaction fees.

- Correct answer: TRUE
- Justification: Coinbase has no normal inputs and pays the subsidy plus fees to the miner.
- Tag(s): coinbase, block-reward

Q4) A block subsidy is constant and never changes over time.

- Correct answer: FALSE
- Justification: The subsidy halves at scheduled intervals.
- Tag(s): trap, halving

Q5) Bitcoin’s block subsidy halves roughly every 210,000 blocks.

- Correct answer: TRUE
- Justification: Halving is based on block count, about every four years.
- Tag(s): halving, block-reward

Q6) Miners can choose which transactions to include, often prioritizing higher fee rates.

- Correct answer: TRUE
- Justification: Miners select transactions based on policy/fee incentives.
- Tag(s): fees, mempool

Q7) Difficulty adjustment changes the hash function used for mining.

- Correct answer: FALSE
- Justification: The hash function stays the same; the target changes.
- Tag(s): trap, difficulty

Q8) A valid block must reference the previous block’s hash in its header.

- Correct answer: TRUE
- Justification: The previous block hash links blocks into a chain.
- Tag(s): block-header, chain

Q9) The total block reward equals the block subsidy plus the fees from transactions in that block.

- Correct answer: TRUE
- Justification: Miner revenue = subsidy + fees.
- Tag(s): block-reward, fees

Q10) Mining is primarily about verifying transactions, not performing proof-of-work.

- Correct answer: FALSE
- Justification: Mining’s defining task is PoW; validation is done by all nodes.
- Tag(s): trap, mining

Q11) A miner can spend the coinbase reward immediately after mining a block.

- Correct answer: FALSE
- Justification: Coinbase outputs have a maturity requirement before spending.
- Tag(s): trap, coinbase, maturity

Q12) Hashrate is a measure of the total computational power devoted to mining.

- Correct answer: TRUE
- Justification: Hashrate estimates hashes per second on the network.
- Tag(s): hashrate, mining

Q13) A higher difficulty target makes mining easier.

- Correct answer: FALSE
- Justification: A lower target makes mining harder; “higher difficulty” means lower target.
- Tag(s): trap, difficulty

Q14) The proof-of-work target is adjusted to keep average block times around 10 minutes.

- Correct answer: TRUE
- Justification: Difficulty retargeting aims to stabilize block intervals.
- Tag(s): difficulty, target

Q15) Orphaned/stale blocks do not receive block rewards because they are not in the best chain.

- Correct answer: TRUE
- Justification: Only blocks in the best chain are rewarded.
- Tag(s): stale, rewards

Q16) Which component is directly hashed in proof-of-work?
A) Full block contents as text
B) Block header
C) UTXO set
D) Wallet seed

- Correct answer: B
- Justification: Mining hashes the block header.
- Tag(s): pow, block-header, trap

Q17) Which is true about mining difficulty?
A) It is fixed by users each day
B) It adjusts based on time to mine recent blocks
C) It depends on the total BTC supply
D) It is unrelated to hash rate

- Correct answer: B
- Justification: Difficulty adjusts based on how quickly blocks were mined.
- Tag(s): difficulty, trap

Q18) Which statement best describes the “block subsidy”?
A) The sum of all transaction fees
B) New bitcoins created with each block
C) The miner’s electricity cost
D) The amount of data in the block

- Correct answer: B
- Justification: The subsidy is the newly minted coin portion of the reward.
- Tag(s): subsidy, block-reward

Q19) What happens to the block subsidy over time?
A) It increases with demand
B) It remains constant
C) It decreases on a fixed schedule (halving)
D) It is random each block

- Correct answer: C
- Justification: The subsidy halves on a fixed schedule.
- Tag(s): halving, trap

Q20) Which best describes a mining pool?
A) A wallet type for miners
B) A group of miners sharing work and rewards
C) A mempool policy
D) A type of block header

- Correct answer: B
- Justification: Pools aggregate hash power and split rewards.
- Tag(s): mining, pools

Q21) If two valid blocks are found at the same height, the network temporarily has a fork until one chain becomes longer.

- Correct answer: TRUE
- Justification: Competing blocks create a temporary fork resolved by the longest chain rule.
- Tag(s): fork, consensus

Q22) Which is a correct statement about transaction fees in mining?
A) Fees are destroyed, not paid to miners
B) Fees are collected by the miner who includes the transaction
C) Fees are paid to the oldest UTXO
D) Fees are fixed by consensus

- Correct answer: B
- Justification: Fees go to the miner of the block that includes the transaction.
- Tag(s): fees, mining

Q23) Why does proof-of-work make it costly to rewrite history?
A) Because blocks are encrypted
B) Because each block requires significant computational work to find
C) Because nodes forbid reorgs
D) Because the mempool prevents it

- Correct answer: B
- Justification: Rewriting requires redoing PoW for the replaced blocks.
- Tag(s): pow, security, trap

Q24) Which is the correct relationship between target and difficulty?
A) Higher target means higher difficulty
B) Higher target means easier mining (lower difficulty)
C) Target and difficulty are unrelated
D) Target is the same as block reward

- Correct answer: B
- Justification: A higher target makes it easier to find a valid hash.
- Tag(s): target, difficulty, trap

Q25) Which is most accurate about miner revenue as subsidies decline?
A) It becomes only transaction fees over time
B) It is fixed by consensus forever
C) It becomes zero because mining stops
D) It increases automatically each year

- Correct answer: A
- Justification: Over time, subsidy decreases and fees make up more of the reward.
- Tag(s): fees, block-reward, trap

## Drill Set: 2026-01-20 — Mining and Block Rewards (Append A — Level 3)

### SPEED DRILL (25 new questions total)

Q26) Miners compete by varying header fields (such as nonce/extranonce-related data) to find a valid hash under the target.

- Correct answer: TRUE
- Justification: Mining is repeated header hashing with changing candidate values.
- Tag(s): pow, nonce, trap

Q27) The 10-minute block interval is guaranteed exactly by consensus for every block.

- Correct answer: FALSE
- Justification: 10 minutes is a long-run average target, not a per-block guarantee.
- Tag(s): trap, difficulty, timing

Q28) Difficulty retargeting is based on elapsed time for a recent block window, not on transaction count.

- Correct answer: TRUE
- Justification: The protocol adjusts target according to observed block production time.
- Tag(s): difficulty, retarget, trap

Q29) A miner can claim any block reward amount they want in coinbase; nodes will accept it if PoW is valid.

- Correct answer: FALSE
- Justification: Nodes enforce the maximum allowed subsidy+fees; overpaying coinbase is invalid.
- Tag(s): trap, consensus, coinbase

Q30) Transaction fees available to a miner depend on which transactions they include in the block.

- Correct answer: TRUE
- Justification: Miner fee revenue equals fees of included transactions.
- Tag(s): fees, mining

Q31) A stale/orphan block can still contribute work but does not earn the block reward on the best chain.

- Correct answer: TRUE
- Justification: Only best-chain blocks receive spendable rewards.
- Tag(s): stale, rewards

Q32) The merkle root in the block header commits to the block’s transaction list.

- Correct answer: TRUE
- Justification: Any transaction change changes the merkle root.
- Tag(s): merkle, block-header

Q33) Raising hashrate (with difficulty fixed) tends to shorten expected block intervals.

- Correct answer: TRUE
- Justification: More hash attempts per second means faster expected target hits.
- Tag(s): hashrate, difficulty, trap

Q34) Mining pools eliminate variance entirely for participants.

- Correct answer: FALSE
- Justification: Pools reduce variance but do not remove it completely.
- Tag(s): trap, pools

Q35) A miner can include an invalid transaction and still have the block accepted if PoW is strong enough.

- Correct answer: FALSE
- Justification: Consensus validation rejects blocks containing invalid transactions.
- Tag(s): trap, consensus, validation

Q36) As subsidy decreases over halvings, long-term miner income relies more on fees.

- Correct answer: TRUE
- Justification: Subsidy declines on schedule, increasing fee share importance.
- Tag(s): halving, fees

Q37) Difficulty adjusts every block in Bitcoin mainnet consensus.

- Correct answer: FALSE
- Justification: Bitcoin retargets on a larger fixed interval, not each block.
- Tag(s): trap, difficulty, retarget

Q38) The coinbase transaction includes arbitrary miner-chosen data in its input script area.

- Correct answer: TRUE
- Justification: Coinbase input can contain extra data/commitments within consensus limits.
- Tag(s): coinbase, block-structure, trap

Q39) If two pools find competing blocks at the same height, one may become stale after a chain tip race.

- Correct answer: TRUE
- Justification: Temporary forks resolve when one branch gains more work.
- Tag(s): fork, stale, pools

Q40) Proof-of-work secures ordering/history by making alternative histories computationally expensive.

- Correct answer: TRUE
- Justification: Reorg attempts require redoing cumulative work.
- Tag(s): pow, security

Q41) Which value must a miner never exceed in coinbase reward for a block to be valid?
A) Subsidy only
B) Subsidy + included fees
C) Included fees only
D) Any amount is fine

- Correct answer: B
- Justification: Consensus caps coinbase value at subsidy plus total transaction fees.
- Tag(s): coinbase, consensus, trap

Q42) Which component most directly links a block to its parent?
A) Nonce
B) Timestamp
C) Previous block hash
D) Merkle root

- Correct answer: C
- Justification: Previous block hash is the hash pointer to parent.
- Tag(s): block-header, chain

Q43) What is the primary reason miners care about fee rate rather than only total fee?
A) Fee rate better reflects reward per limited block space
B) Consensus requires highest total fee first
C) Total fee is unknown before mining
D) Fee rate changes block subsidy

- Correct answer: A
- Justification: Block space is limited, so miners optimize revenue density.
- Tag(s): fees, mining, trap

Q44) Which statement about halving is correct?
A) It halves transaction fees
B) It halves subsidy on a fixed block schedule
C) It doubles hashrate
D) It is triggered by mempool size

- Correct answer: B
- Justification: Halving is a protocol schedule tied to block height.
- Tag(s): halving, trap

Q45) Which event can cause a temporary chain fork without any rule violation?
A) Two valid blocks found near-simultaneously
B) A block with invalid signatures
C) A miner claiming too much subsidy
D) A node restart

- Correct answer: A
- Justification: Natural propagation races can create temporary competing tips.
- Tag(s): fork, consensus, trap

Q46) Which field in the header is adjusted by retarget indirectly through consensus parameters?
A) Version
B) bits (compact target)
C) Merkle root
D) Previous hash

- Correct answer: B
- Justification: bits encodes the target threshold used for PoW.
- Tag(s): target, difficulty, header

Q47) A mining pool “share” is best described as:
A) A confirmed block on mainnet
B) A partial proof used by the pool to measure contributed work
C) A private key fragment
D) A mempool transaction

- Correct answer: B
- Justification: Shares are lower-difficulty proofs for payout accounting.
- Tag(s): pools, shares, trap

Q48) Which scenario most directly reduces expected time to next block (before retarget)?
A) Lower network hashrate
B) Higher network hashrate
C) Higher transaction count only
D) Smaller mempool

- Correct answer: B
- Justification: More hashrate increases PoW attempt rate.
- Tag(s): hashrate, timing, trap

Q49) Which statement is most accurate about stale blocks?
A) They are invalid blocks
B) They are valid blocks not on the selected best chain
C) They always pay partial reward
D) They are blocks with no transactions

- Correct answer: B
- Justification: Stale blocks can be valid but lose the chain race.
- Tag(s): stale, trap

Q50) Which is the best description of miner revenue in a single block?
A) Subsidy only
B) Fees only
C) Subsidy + fees from included transactions
D) Hardware cost reimbursement

- Correct answer: C
- Justification: Block reward combines minted subsidy and collected fees.
- Tag(s): block-reward, fees

## Drill Set: 2026-01-20 — Mining and Block Rewards (Append B — Level 3)

### SPEED DRILL (25 new questions total)

Q51) Proof-of-work validation by nodes is cheap compared with performing the full mining search.

- Correct answer: TRUE
- Justification: Verifying one candidate hash is far cheaper than finding one by brute force.
- Tag(s): pow, validation, trap

Q52) Miners can set arbitrary timestamps far in the future with no validation limits.

- Correct answer: FALSE
- Justification: Consensus/policy impose bounds on acceptable block timestamps.
- Tag(s): trap, timestamp, consensus

Q53) A reorg replaces one best-chain tip with another chain that has more cumulative work.

- Correct answer: TRUE
- Justification: Chain selection follows cumulative proof-of-work.
- Tag(s): reorg, consensus

Q54) If block demand is high, miners may include lower-fee transactions first to keep fees fair.

- Correct answer: FALSE
- Justification: Economic incentives usually favor higher fee-rate transactions.
- Tag(s): trap, fees, mining

Q55) The subsidy eventually trends toward zero according to Bitcoin’s issuance schedule.

- Correct answer: TRUE
- Justification: Repeated halvings reduce subsidy over time.
- Tag(s): subsidy, halving

Q56) Mining profitability depends on both revenue (subsidy+fees) and costs (electricity/hardware/operations).

- Correct answer: TRUE
- Justification: Profit is income minus costs.
- Tag(s): mining, economics

Q57) A block can be valid PoW-wise but still rejected if it violates consensus transaction rules.

- Correct answer: TRUE
- Justification: Blocks must satisfy PoW and full consensus validation.
- Tag(s): consensus, validation, trap

Q58) Difficulty retargeting exists primarily to keep issuance predictable despite hashrate changes.

- Correct answer: TRUE
- Justification: Stable block timing supports predictable schedule behavior.
- Tag(s): difficulty, issuance, trap

Q59) Mining pools guarantee higher long-term expected reward than solo mining for the same hashrate.

- Correct answer: FALSE
- Justification: Expected value is similar; pools mostly reduce payout variance.
- Tag(s): trap, pools, variance

Q60) A miner can include their own low-fee transaction if they choose, trading off potential fee revenue.

- Correct answer: TRUE
- Justification: Miners control block composition subject to consensus limits.
- Tag(s): fees, mining, trap

Q61) A 51% attack implies attackers can permanently break signature cryptography.

- Correct answer: FALSE
- Justification: Majority hash power affects ordering/reorg capability, not signature math.
- Tag(s): trap, 51-attack, security

Q62) The nonce field alone may be insufficient search space, so miners also vary other block components (e.g., coinbase-derived merkle root).

- Correct answer: TRUE
- Justification: Miners expand search space beyond nonce when exhausted.
- Tag(s): nonce, merkle, mining

Q63) Higher fee pressure can increase the share of miner income coming from fees versus subsidy.

- Correct answer: TRUE
- Justification: Fee revenue composition depends on transaction demand and fee rates.
- Tag(s): fees, block-reward

Q64) A miner must include all valid mempool transactions to produce a valid block.

- Correct answer: FALSE
- Justification: Miners can include any subset of valid transactions.
- Tag(s): trap, mempool, mining

Q65) Difficulty adjustment can lag sudden hashrate changes, causing temporary deviation from 10-minute blocks.

- Correct answer: TRUE
- Justification: Retarget happens periodically, not instantly.
- Tag(s): difficulty, timing, trap

Q66) Which statement best describes a 51% attack capability?
A) Create coins arbitrarily
B) Reverse some recent transactions and censor transactions temporarily
C) Steal private keys from addresses
D) Change subsidy schedule without consensus software changes

- Correct answer: B
- Justification: Majority hash power can influence ordering/reorgs but not cryptographic ownership.
- Tag(s): 51-attack, security, trap

Q67) Which best describes “cumulative work” in chain selection?
A) Number of transactions only
B) Sum of fees only
C) Aggregate proof-of-work represented by the chain
D) Number of miners in pools

- Correct answer: C
- Justification: Nodes follow chain with greatest cumulative work.
- Tag(s): consensus, pow

Q68) Which factor does NOT directly change block subsidy amount for a specific height?
A) Block height/halving schedule
B) Consensus rules
C) Mempool congestion
D) Issuance schedule

- Correct answer: C
- Justification: Congestion affects fees, not subsidy schedule.
- Tag(s): subsidy, trap

Q69) Which is most accurate about pool payouts?
A) Shares are final on-chain rewards
B) Pool payout schemes divide earned rewards according to contributed work rules
C) Shares replace proof-of-work
D) Pools pay only when subsidy is zero

- Correct answer: B
- Justification: Pools track work shares and distribute rewards by scheme.
- Tag(s): pools, shares

Q70) Which statement about stale blocks is correct?
A) They prove no work was done
B) They may contain valid PoW but lose best-chain selection
C) They invalidate all descendant blocks forever
D) They always have invalid timestamps

- Correct answer: B
- Justification: Stale blocks can be valid but not selected.
- Tag(s): stale, trap

Q71) If fees in a block are unusually high, miner revenue for that block can exceed the subsidy by a larger margin.

- Correct answer: TRUE
- Justification: Revenue composition can vary block-by-block based on fees.
- Tag(s): fees, block-reward

Q72) Which miner behavior most directly maximizes short-term revenue per block candidate?
A) Ignoring fee rates
B) Selecting transactions with strongest fee-rate package economics under size limits
C) Always mining empty blocks only
D) Including only oldest transactions

- Correct answer: B
- Justification: Revenue optimization typically follows fee-rate-driven selection.
- Tag(s): fees, mining, trap

Q73) Which is true about block rewards on stale branches?
A) They are spendable after maturity anyway
B) They are not part of accepted chain state and thus not spendable
C) They are merged into next best-chain reward
D) They are paid by pools only

- Correct answer: B
- Justification: Only accepted-chain coinbase outputs enter spendable UTXO state.
- Tag(s): stale, rewards, trap

Q74) Which field is most directly used to prove PoW threshold satisfaction?
A) Version
B) Computed block hash relative to target
C) Coinbase output value
D) Merkle tree depth

- Correct answer: B
- Justification: Validity depends on block hash being below target.
- Tag(s): pow, target

Q75) Which is most accurate about long-run security budget trends?
A) Subsidy grows forever
B) Fees are expected to become increasingly important as subsidy declines
C) Mining becomes irrelevant after first halving
D) Difficulty removes fee markets

- Correct answer: B
- Justification: With declining subsidy, fees are expected to carry more security budget weight.
- Tag(s): fees, subsidy, trap
