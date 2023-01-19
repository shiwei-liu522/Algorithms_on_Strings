#Python3
import sys


def build_suffix_array(text):
    data = []
    for i in range(len(text)):
        data.append((text[i:], i))
    data.sort(key=lambda x: x[0])
    result = [i for s, i in data]
    return result


if __name__ == "__main__":
    def sol():
        text = sys.stdin.readline().strip()
        print(" ".join(map(str, build_suffix_array(text))))
    sol()
