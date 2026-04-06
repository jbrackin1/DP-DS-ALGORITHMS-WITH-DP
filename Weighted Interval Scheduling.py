from bisect import bisect_right

def weighted_interval_scheduling(start, end, value):
    n = len(start)
    if not (len(end) == len(value) == n):
        raise ValueError("Input lists must match length")

    # jobs sorted by end time: (s, e, v, orig_idx)
    jobs = sorted([(start[i], end[i], value[i], i) for i in range(n)], key=lambda x: x[1])
    s = [j[0] for j in jobs]
    e = [j[1] for j in jobs]
    v = [j[2] for j in jobs]
    orig = [j[3] for j in jobs]

    # p[i]: last index j < i with e[j] <= s[i], for i in 0..n-1
    p = [bisect_right(e, s[i]) - 1 for i in range(n)]

    # dp[i] = best value using first i jobs (i from 0..n), dp[0]=0
    dp = [0] * (n + 1)
    take = [False] * (n + 1)

    for i in range(1, n + 1):
        # job index in arrays is i-1
        without = dp[i-1]
        with_job = v[i-1] + (dp[p[i-1] + 1] if p[i-1] != -1 else 0)
        if with_job > without:
            dp[i] = with_job
            take[i] = True
        else:
            dp[i] = without
            take[i] = False

    # reconstruct chosen jobs (in sorted order), map back to original indices (1-based)
    chosen_sorted = []
    i = n
    while i > 0:
        if take[i]:
            chosen_sorted.append(i-1)
            i = p[i-1] + 1
        else:
            i -= 1
    chosen_sorted.reverse()
    chosen_original_1based = [orig[j] + 1 for j in chosen_sorted]

    return dp[n], chosen_original_1based

# Example
if __name__ == "__main__":
    s = [1,3,6,2]
    e = [3,5,9,8]
    v = [5,6,5,8]
    print(weighted_interval_scheduling(s,e,v))  # (11, [1,2])