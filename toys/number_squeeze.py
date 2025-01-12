import numpy as np
from  math import sqrt
k_max = 10

dp = [[0 for _ in range(2 * k_max + 1)] for _ in range(k_max + 1)]
dp[0][0] = 1
for k in range(1, k_max + 1):
    for n in range(2 * (k % 2), 2 * k + 1, 4):
        if ((k % 2 == 0) and (n == 0)):
            dp[k][n] = sqrt(2) * dp[k - 1][2]
        elif (n == 2 * k):
            dp[k][n] = -sqrt(n * (n - 1)) * dp[k - 1][n - 2]
        else:
            dp[k][n] = -sqrt(n * (n - 1)) * dp[k - 1][n - 2] + sqrt((n + 1) * (n + 2)) * dp[k - 1][n + 2]
for x in dp:
    print(x[2])