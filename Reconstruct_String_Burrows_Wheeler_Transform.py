#Python3

import sys
from collections import defaultdict


class Reconstruct:
    def __init__(self, bwt):
        self.bwt = bwt
        self.text = self._text(self.bwt)

    @staticmethod
    def _text(bwt):
        last_column = bwt
        fir_column = "".join(sorted(bwt))
        fir_char_to_cnt = []
        fir_counter = defaultdict(int)
        last_char_to_cnt = []
        last_counter = defaultdict(int)

        for i in range(len(bwt)):
            fir_char_to_cnt.append(fir_counter[fir_column[i]])
            fir_counter[fir_column[i]] += 1
            last_char_to_cnt.append(last_counter[last_column[i]])
            last_counter[last_column[i]] += 1
        last_char_id = dict()

        for i in range(len(bwt)):
            last_char_id[(last_column[i], last_char_to_cnt[i])] = i
        s = ""
        i = 0
        for _ in range(len(bwt)):
            i = last_char_id[(fir_column[i], fir_char_to_cnt[i])]
            s += fir_column[i]

        return s


if __name__ == "__main__":
    def sol():
        bwt = sys.stdin.readline().strip()
        i_bwt = Reconstruct(bwt)
        print(i_bwt.text)
    sol()
