def max_of(a):
    maximum = a[0]  # 첫 번째 원소를 최댓값으로 설정

    for i in range(1, len(a)):  # 두 번째 원소부터 순차적으로 비교
        if a[i] > maximum:
            maximum = a[i]  # 더 큰 값이 있으면 갱신
    return maximum  # 최종 최댓값 반환

print("배열의 최댓값을 구합니다. ")
num = int(input("원소 수를 입력하세요.: "))
x = []

for i in range(num):
    b=int(input(f"x[{i}]값을 입력하세요.: "))
    x.append(b)
print(f"최댓값은 {max_of(x)}입니다.")


