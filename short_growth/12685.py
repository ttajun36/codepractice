'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range (N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if j < bag[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i-1][0]]+bag[i-1][1])
            
            
print(dp[N][K])
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1,n):
    print(n)

'''
0 0 0 0 0 0 0 0
0 0 0 0 0 0 13 13
0 0 0 0 8 8 13 13
0 0 0 6 8 8 13 14
0 0 0 6 8 12 13 14
'''