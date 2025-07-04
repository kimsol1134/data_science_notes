from scipy.stats import binom

# 지시사항 1 : 아래에 코드를 작성하세요.
ans1 = 1-binom.cdf(17,25,0.5)


# 지시사항 2 : 아래에 코드를 작성하세요.
ans2 = binom.pmf(10,10,0.5)


# 소수점 둘째자리까지 반올림 출력
print(f"ans1: {ans1:.2f}, ans2: {ans2:.2f}")