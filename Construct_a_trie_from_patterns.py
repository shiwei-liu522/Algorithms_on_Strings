#Python3
import sys
from collections import deque


class Trie:
    def __init__(self, patterns):
        self.patterns = patterns
        self.tree = Node(None, None, 0)
        self._construct_trie(self.patterns)

    def _construct_trie(self, patterns):
        n_id = 1
        for pattern in patterns:
            cur = self.tree
            for c in pattern:
                if c not in cur.children:
                    cur.add_child(c, n_id)
                    n_id += 1
                cur = cur.children[c]

    def print_adj_list(self):
        q = deque([self.tree])

        while q:
            cur = q.popleft()

            if cur.value is not None:
                print("{}->{}:{}".format(cur.parent.n_id, cur.n_id, cur.value))

            for node in cur.children.values():
                q.append(node)


class Node:
    def __init__(self, parent, value, n_id):
        self.parent = parent
        self.value = value
        self.n_id = n_id

        self.children = dict()

    def add_child(self, value, n_id):
        self.children[value] = Node(self, value, n_id)


if __name__ == "__main__":
    def sol():
        patterns = sys.stdin.read().split()[1:]
        tree = Trie(patterns)
        tree.print_adj_list()
    sol()
