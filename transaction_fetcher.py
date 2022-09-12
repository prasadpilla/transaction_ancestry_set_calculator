import time

import requests

from logger import log


class TransactionFetcher:
    def __init__(self, base_url, block_height):
        self.base_url = base_url
        self.block_height = block_height

    def fetch_block_hash(self):
        response = requests.get(f'{self.base_url}/api/block-height/{self.block_height}')

        if response.status_code != 200:
            log(f'Failed to fetch the block for the given block height: {self.block_height}')

        # TODO: Handle exceptions and bubble up
        return response.text

    def fetch_block_transactions_for_index(self, block_hash, index):
        log(f'Fetching for block hash: {block_hash}, index: {index}')
        response = requests.get(f'{self.base_url}/api/block/{block_hash}/txs/{index}')

        if response.status_code == 404:
            log(f'Reached the end index for the block hash: {block_hash}, index: {index}')
            return []

        if response.status_code != 200:
            log(f'Failed to fetch the transactions list for the hash: {block_hash}')

        # TODO: Handle exceptions and bubble up
        return response.json()

    def fetch_block_transactions(self):
        all_transactions = []
        index = 25
        block_hash = self.fetch_block_hash()
        while True:
            transactions = self.fetch_block_transactions_for_index(block_hash, index)
            # TODO: Revisit later: Hack to avoid limits while debugging.
            # We might actually need have some time between calls in prod as well, but more on that later.
            time.sleep(1)
            index += 25

            if len(transactions) == 0:
                break
            else:
                all_transactions.append(transactions)

        return all_transactions








