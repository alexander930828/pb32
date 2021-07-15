# 최댓값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최댓값

def find_max(a):
    max_n = a[0]
    n = len(a)
    for i in range(1, n):
        if max_n < a[i]:
            max_n = a[i]
    return max_n

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))

# 최댓값의 위치 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중에서 최댓값이 있는 위치(O부터 n-1까지의 값)

def find_max_idx(a):
    max_idx = 0
    n = len(a)
    for i in range(1, n):
        if a[max_idx] < a[i]:
            max_idx = i
    return max_idx

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max_idx(v))
