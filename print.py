# 이것이 나의 첫번째 파이썬 파일이다.
# 계속되지 안나?
# 아니네 ㅜㅜ
# 꿀렁 꿀렁 소리가 오류났다는 뜻이구나.

name = input("당신의 이름을 넣어 주세요.")
birth_year = int(input("당신의 생년을 넣어주세요(yyyy)"))

current_year = 2026
age = current_year - birth_year + 1

if age >=20:
    status = "성인"
else:
    status ="미성년"

print("-" * 30)
print(f"안녕하세요, {name}님!")
print(f"당신은 {age} 살이며, {status}입니다.")
print("-" * 30)

