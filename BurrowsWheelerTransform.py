#Python3
import sys


class BurrowsWheelerTransform:
    def __init__(self, text):
        self.text = text
        self.bwt = self._bwt(self.text)

    @staticmethod
    def _bwt(text):
        matrix = [text]
        for i in range(len(text) - 1):
            text = text[-1] + text[:-1]
            matrix.append(text)

        matrix.sort()

        res = "".join([s[-1] for s in matrix])
        return res


if __name__ == "__main__":
    def sol():
        text = sys.stdin.readline().strip()
        bwt = BurrowsWheelerTransform(text)
        print(bwt.bwt)
    sol()

