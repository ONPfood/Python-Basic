# 이것이 나의 첫번째 파이썬 파일이다.

# 1. 변수

# 변수 이름을 지을 때의 규칙 (Naming Rules)
# **영문자, 숫자, 언더바(_)**만 사용할 수 있습니다.
# 숫자로 시작할 수 없습니다. (예: 1st_name (X), name1 (O))
# 대소문자를 구분합니다. (Apple과 apple은 서로 다른 변수입니다.)
# 파이썬다운 작명 관례 (Snake Case)
# 파이썬 개발자들은 여러 단어를 조합해 변수 이름을 지을 때 **언더바(_)**를 사용하는 
# **스네이크 케이스(Snake Case)**를 권장합니다.

# [변수 이름] = [저장할 값]
age = 25          # 정수(int)
name = "Gemini"   # 문자열(str)
height = 175.5    # 실수(float)
is_student = True # 불리언(bool, 참/거짓)

# 다중 할당 (Multiple Assignment)
x, y, z = 10, 20, 30
a = b = c = "Python"

# 변수 값 바꾸기 (Swapping)
a = 1
b = 2
a, b = b, a  # 이제 a는 2, b는 1이 됩니다.


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

