from ancestry_calculator import AncestryCalculator
from transaction_fetcher import TransactionFetcher

# This can move to config
BASE_URL = "https://blockstream.info"

# We can take this as input. Either from cmd like or http
BLOCK_HEIGHT = 680000

def main():
    transactions = TransactionFetcher(BASE_URL, BLOCK_HEIGHT).fetch_block_transactions()
    log(transactions)
    top_ten = AncestryCalculator([['A', 'D'], ['A', 'G'], ['F', 'G'], ['G', 'K'], ['G', 'L'], ['F', 'L']]).compute()
    log(top_ten)

if __name__ == '__main__':
    main()
