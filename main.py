from transaction_fetcher import TransactionFetcher

BASE_URL = "https://blockstream.info"


def main():
    transactions = TransactionFetcher(BASE_URL).fetch_block_transactions(680000)
    print(transactions)


if __name__ == '__main__':
    main()
