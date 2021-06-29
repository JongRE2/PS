# 과제 4번 코드란

def solution(N, duration, cost):
    dp = [0] * (N + 1)

    def dynamic_programming():
        max_val = 0
        for i in range(N - 1, -1, -1):# 8일째때 퇴사 / 7(인덱스6)일째부터 1일(인덱스0)까지
            day = (i+1) + duration[i] #실제 '일'로 맞춤
            if N - 1 == i:
                dp[i] = cost[i]  # 퇴사전날까지 딱 일했을때
            if day == N+1:
                dp[i] = max(dp[i+1],cost[i])
            elif day < N+1:
                dp[i] = max(dp[i+1],cost[i]+dp[i+duration[i]])
            elif day > N+1:
                dp[i] = dp[i+1]
        max_val = dp[0]
        return max_val

    result = dynamic_programming()
    return result


N = 10
duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
print(solution(N, duration, cost))