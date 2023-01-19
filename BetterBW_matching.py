#Python3

import sys

class BWMatching:
    def __init__(self, bwt):
        self.bwt = bwt
        self.starts, self.occ_count_before = self._preprocess(self.bwt)

    @staticmethod
    def _preprocess(bwt):
        first_col = sorted(bwt)
        starts = dict()
        unique_chars = set()

        for i in range(len(bwt)):
            char = first_col[i]

            if char not in starts:
                starts[char] = i
                unique_chars.add(char)

        occ_count_before = {char: [0] for char in unique_chars}
        for i in range(len(bwt)):
            cur_char = bwt[i]
            for char in unique_chars:
                value = occ_count_before[char][-1]
                if char == cur_char:
                    value += 1

                occ_count_before[char].append(value)
        return starts, occ_count_before

    def count(self, pattern):
        num = 0
        top = 0
        bottom = len(self.bwt) - 1
        while top <= bottom:
            if len(pattern):
                char = pattern[-1]
                pattern = pattern[:-1]
                contains_char = False
                for i in range(top, bottom + 1):
                    if self.bwt[i] == char:
                        contains_char = True
                        break

                if contains_char:
                    top = self.starts[char] + self.occ_count_before[char][top]
                    bottom = self.starts[char] + self.occ_count_before[char][bottom + 1] - 1
                else:
                    break
            else:
                num = bottom - top + 1
                break
        return num


if __name__ == "__main__":
    def sol():
        bwt = sys.stdin.readline().strip()
        pattern_count = int(sys.stdin.readline().strip())
        patterns = sys.stdin.readline().strip().split()
        bwm = BWMatching(bwt)
        occ_count = []
        for pattern in patterns:
            num_occur = bwm.count(pattern)
            occ_count.append(num_occur)
        print(" ".join(map(str, occ_count)))
    sol()
