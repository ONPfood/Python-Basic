# dan = int(input("몇 단을 출력할까요? (2~9): "))

# if 2 <= dan <= 9:
#     print(f"--- {dan}단 시작 ---")
#     for i in range(1, 10):
#         print(f"{dan} x {i} = {dan * i}")
# else:
#     print("2에서 9 사이의 숫자만 입력해주세요.")

dan = 5

print(f"====== {dan} 시작 ======")

for i in range(1,10):
    print( dan, i, dan * i)

print ("=", 30)