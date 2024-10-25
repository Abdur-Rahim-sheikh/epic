from bisect import bisect_left as bs

def greatestIncreasingSubsequence(seq):
    """
    Given a sequence of numbers, return the greatest increasing subsequence
    """
    n = len(seq)
    # Initialize the list with 1
    ls = [seq[0]]
    for i in range(1, n):
        idx = bs(ls, seq[i])
        if idx == len(ls):
            ls.append(seq[i])
        else:
            ls[idx] = seq[i]
    return ls

if __name__ == "__main__":
    seq = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print(greatestIncreasingSubsequence(seq))