from bisect import bisect_right


def totalValue (startTime, endTime, value, cost, budget):
    n = len(startTime)
    if not (len(endTime) == len(value) == len(cost) == n):
        raise ValueError("All input lists must have the same length")
    jobs = sorted([(startTime[i], endTime[i], value[i], cost[i], i) for i in range(n)], key=lambda x: x[1])
    s = [job[0] for job in jobs]
    e = [job[1] for job in jobs]
    v = [job[2] for job in jobs]
    c = [job[3] for job in jobs]
    orig_idx = [job[4] for job in jobs]

    # p[i] = index of last job that ends <= s[i], using job indices 0..n-1
    ends = e
    p = [bisect_right(ends, s[i]) - 1 for i in range(n)]    # so jobs dont overlap
    # dp[i][b]: best value using first i jobs (jobs 0..i-1) with budget b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    take = [[False] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        vi = v[i-1]
        ci = c[i-1]
        pi = p[i-1] + 1  # convert to dp row index last nonoverlapping time
        for b in range(budget + 1):
            # skip
            best = dp[i-1][b]
            choose = False
            # take if affordable
            if b >= ci:
                val_with = dp[pi][b - ci] + vi
                if val_with > best:
                    best = val_with
                    choose = True
            dp[i][b] = best
            take[i][b] = choose

    # reconstruct chosen jobs (indices in sorted array)
    b = budget
    chosen_sorted = []
    i = n
    while i > 0:
        if take[i][b]:
            chosen_sorted.append(i-1)
            b -= c[i-1]
            i = p[i-1] + 1
        else:
            i -= 1
    chosen_sorted.reverse()

    chosen_original = [orig_idx[j] + 1 for j in chosen_sorted]
    return dp[n][budget], chosen_original

startTime = [1, 3, 6, 2]
endTime   = [3, 5, 9, 8]
value     = [5, 6, 5, 8]
cost      = [2, 2, 3, 4]
budget    = 5

print(totalValue(startTime, endTime, value, cost, budget))