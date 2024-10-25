#  count amount of numbers with length n and even sum of digits

def digit_sum(n):
    dp = [[[0 for i in range(2)] for j in range(10)] for k in range(n)]
    for i in range(10):
        dp[0][i][i&1] = 1
    for i in range(1, n):
        for j in range(10):
            for k in range(10):
                dp[i][j][0] += dp[i-1][k][j&1]
                dp[i][j][1] += dp[i-1][k][~(j&1)]
    
    total = 0
    # print(dp)
    for i in range(1,10):
        total += dp[-1][i][0]
    return total


def bruteForce(n):
    # total = 0
    # for i in range(10**(n-1), 10**n):
    #     if sum(map(int, str(i))) % 2 == 0:
    #         total += 1
    # return total
    return (10**n-10**(n-1) )//2 

if __name__ == "__main__":
    print(digit_sum(1), bruteForce(1))
    print(digit_sum(2), bruteForce(2))
    print(digit_sum(3), bruteForce(3))
    print(digit_sum(4), bruteForce(4))
    print(digit_sum(5), bruteForce(5))
    print(digit_sum(6), bruteForce(6))