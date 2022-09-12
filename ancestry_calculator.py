from exceptions import ComputeException


class AncestryCalculator:
    def __init__(self, transactions):
        self.transactions = transactions

    def generate_pairs(self):
        tx_hash = {}
        for tx in self.transactions:
            tx_hash[tx["txid"]] = True

        pairs = []
        for mainTxn in self.transactions:
            for inTx in mainTxn['vin']:
                if inTx['txid'] in tx_hash:
                    pairs.append([inTx['txid'], mainTxn['txid']])
        return pairs

    def visit(self, node, graph, visited):
        if node in visited: return visited[node]

        parents = set()
        if node in graph:
            for parent in graph[node]:
                parents.add(parent)
                parents.update(self.visit(parent, graph, visited))

        visited[node] = parents
        return parents

    def compute(self, n):
        try:
            pairs = self.generate_pairs()
            graph = {}
            for parent, child in pairs:
                if child not in graph:
                    graph[child] = [parent]
                else:
                    graph[child].append(parent)

            ancestry = {}
            for k in graph:
                if k not in ancestry:
                    self.visit(k, graph, ancestry)

            return list(dict(sorted(ancestry.items(), reverse=True, key=lambda item: len(item[1]))[:n]).keys())
        except RuntimeError as e:
            raise ComputeException("Exception occurred while computing the ancestry" + str(e))
