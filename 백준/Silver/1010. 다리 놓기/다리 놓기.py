
T = int(input())  # 테스트케이스 개수 입력

for _ in range(T):
    N, M = map(int, input().split())  # 서쪽 N개, 동쪽 M개 사이트

    # DP 테이블 초기화 (31x31 크기, 문제 제한이 최대 30이니까 31까지 잡음)
    dp = [[0] * 31 for _ in range(31)]

    # ✅ 초기 조건: 서쪽 사이트가 0개라면 (n=0), 동쪽이 몇 개든 고를 필요가 없으므로 경우의 수는 1
    # 즉, dp[0][m] = 1
    for i in range(31):
        dp[0][i] = 1

    # ✅ 점화식 적용
    # dp[n][m] = dp[n][m-1] + dp[n-1][m-1]
    # 의미:
    # - m번째 동쪽 사이트를 "안 쓴다" → dp[n][m-1]
    # - m번째 동쪽 사이트를 "쓴다"   → dp[n-1][m-1]
    # 두 경우를 합친 게 dp[n][m]
    for m in range(1, 31):       # 동쪽 사이트 개수 1 ~ 30
        for n in range(1, m + 1):  # 서쪽 사이트 개수 1 ~ m (n>m이면 불가능)
            dp[n][m] = dp[n][m - 1] + dp[n - 1][m - 1]

    # ✅ 최종 답: N개의 서쪽 사이트를 M개의 동쪽 사이트와 연결하는 경우의 수
    print(dp[N][M])
