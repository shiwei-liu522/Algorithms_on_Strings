#Python3
import sys


class FindAllOccurrences:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.pattern_starts = self._get_pattern(self.text, self.pattern)

    @staticmethod
    def _get_prefix(s):
        res = [0]
        border = 0
        for i in range(1, len(s)):
            while (border > 0) and (s[i] != s[border]):
                border = res[border - 1]
            if s[i] == s[border]:
                border += 1
            else:
                border = 0
            res.append(border)
        return res

    def _get_pattern(self, text, pattern):
        s = "".join([pattern, "$", text])
        pref_func_arr = self._get_prefix(s)

        res = []
        for i in range(len(pattern) + 1, len(s)):
            if pref_func_arr[i] == len(pattern):
                start_pos = i - 2*len(pattern)
                res.append(start_pos)

        return res


if __name__ == "__main__":
    def sol():
        pattern = sys.stdin.readline().strip()
        text = sys.stdin.readline().strip()
        kmp = FindAllOccurrences(text, pattern)
        res = kmp.pattern_starts
        print(" ".join(map(str, res)))
    sol()
