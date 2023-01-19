#Python3
import sys
from collections import deque


class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.tree = self._construct_tree(self.text)

    @staticmethod
    def _construct_tree(text):
        last_pos = len(text) - 1

        root = Node(
            parent=None,
            start_pos=None,
            length=None,
        )

        pos = 0
        while pos <= last_pos:
            cur_node = root

            pos_inner = pos
            while pos_inner <= last_pos:
                child_i = None
                for i, child in enumerate(cur_node.children):
                    if text[pos_inner] == text[child.start_pos]:
                        child_i = i
                if child_i is not None:
                    child = cur_node.children[child_i]
                    next_node = child
                    for j in range(child.length):
                        child_pos = child.start_pos + j
                        if text[pos_inner] != text[child_pos]:
                            split_node = Node(cur_node, child.start_pos, j)
                            split_node.children = [child]
                            cur_node.children.pop(child_i)
                            cur_node.children.append(split_node)
                            child.parent = split_node
                            child.start_pos = child_pos
                            child.length -= j
                            next_node = split_node
                            break

                        pos_inner += 1

                    cur_node = next_node
                else:
                    cur_node.add_child(pos_inner, last_pos - pos_inner + 1)
                    pos_inner = last_pos + 1

            pos += 1

        return root

    def print(self):
        q = deque([])
        for child in self.tree.children:
            q.append(child)

        while q:
            cur = q.popleft()
            print(self.text[cur.start_pos:(cur.start_pos + cur.length)])
            for child in cur.children:
                q.append(child)


class Node:
    def __init__(self, parent, start_pos, length):
        self.parent = parent
        self.start_pos = start_pos
        self.length = length
        self.children = []

    def add_child(self, start_pos, length):
        self.children.append(Node(self, start_pos, length))


if __name__ == "__main__":
    def sol():
        text = sys.stdin.readline().strip()
        tree = SuffixTree(text)
        tree.print()
    sol()
