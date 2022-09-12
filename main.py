from ancestry_calculator import AncestryCalculator
from exceptions import FetchException, ComputeException
from logger import log
from transaction_fetcher import TransactionFetcher

# This can move to config
BASE_URL = "https://blockstream.info"

# We can take this as input. Either from cmd like or http
BLOCK_HEIGHT = 680000


def main():
    try:
        transactions = TransactionFetcher(BASE_URL, BLOCK_HEIGHT).fetch_block_transactions()
        top_ten = AncestryCalculator(transactions).compute(10)
        log(f'\nHere are the top 10 transactions with most ancestors(direct and indirect): \n {top_ten}')
    except FetchException as e:
        log("Error occurred while fetching the transactions" + str(e))
    except ComputeException as e:
        log("Error occurred while computing the ancestry" + str(e))
    except RuntimeError as e:
        log("Something went wrong, please try again later" + str(e))


if __name__ == '__main__':
    main()
