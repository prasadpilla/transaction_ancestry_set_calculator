import requests


class TransactionFetcher:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_block_hash(self, block_height: int):
        response = requests.get(f'{self.base_url}/api/block-height/{block_height}')
        if response.status_code != 200:
            print(f'Failed to fetch the block for the given block height: {block_height}')
        # TODO: Handle exceptions and bubble up
        return response.text

    def fetch_block_transactions(self, block_height: int):
        block_hash = self.fetch_block_hash(block_height)
        response = requests.get(f'{self.base_url}/api/block/{block_hash}/txs')
        if response.status_code != 200:
            print(f'Failed to fetch the transactions list for the hash: {block_hash}')
        # TODO: Handle exceptions and bubble up
        return response.json()

