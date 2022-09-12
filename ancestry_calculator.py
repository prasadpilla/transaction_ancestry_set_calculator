class AncestryCalculator:
    def __init__(self, pairs):
        self.pairs = pairs

    def visit(self, node, graph, visited):
        if node in visited: return visited[node]

        parents = set()
        if node in graph:
            for parent in graph[node]:
                parents.add(parent)
                parents.update(self.visit(parent, graph, visited))

        visited[node] = parents
        return parents

    def compute(self):
        graph = {}
        for parent, child in self.pairs:
            if child not in graph:
                graph[child] = [parent]
            else:
                graph[child].append(parent)

        ancestry = {}
        for k in graph:
            if k not in ancestry:
                self.visit(k, graph, ancestry)

        top_ten_nodes = dict(sorted(ancestry.items(), reverse=True, key=lambda item: len(item[1]))[:10]).keys()

        return top_ten_nodes
