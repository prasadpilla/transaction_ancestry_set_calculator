## Transaction Ancestry Sets

Every bitcoin transaction has inputs and outputs. When a transaction A uses an output of transaction B, B is a direct parent of A.

The transaction ancestry of A are all direct and indirect parents of A.



Write a program that:

Fetches all transactions for a block 680000
Determines the ancestor set for every transaction in the block (all ancestors need to be in the block as well)
Prints the 10 transaction with the largest ancestry sets.


Output format: txid and ancestry set size.

Use the Esplora HTTP API from blockstream to retrieve the data: https://github.com/Blockstream/esplora/blob/master/API.md

Hint: cache the API responses locally to avoid hitting rate limits.

Requirements
1. Print the output

2. Basic error reporting

3. Code is modular, bug-free and performant

