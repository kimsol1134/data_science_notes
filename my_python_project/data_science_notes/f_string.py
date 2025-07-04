name = "엘리스"
age = 25

print(f"안녕하세요, 저는 {name}이고, 나이는 {age}살입니다.")

# 계산식에 사용
a = 5
b = 10
print(f"{a} + {b} = {a + b}")

# 함수 호출 결과 삽입
def greet(name):
    return f"{name}님 반갑습니다!"
print(f"인사말: {greet("재협")}")

#소수점 표현 지정
pi = 3.141592
print(f"원주율은 {pi:.2f}입니다.")

#천 단위 콤마 찍기
money = 1234556789
print(f"금액: {money:,}원")