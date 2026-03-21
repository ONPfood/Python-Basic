# 1. 제어문(조건문과 반복문)

# 제어문
score = int(input("점수는 (0~100)?"))
if score < 0 :
    print("too low!")

if score > 100 :
    print("too high!")

if score == 100:
    out_string = "참 잘했어요."
elif score == 0:
    out_string = "와~ 0점이에요"
else:
    out_string = "몇 개는 맞췄네요?"

print("-" * 30)
print(f"당신은 {score} 점이며, {out_string} 입니다.")
print("-" * 30)



# 반복문
for i in range(50,55):
    print (i)

a=["Marry","had","a","little","lamb"]
for i in range(len(a)):
    print (i, a[i])



