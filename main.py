# Bài 2:
'''
if __name__ == '__main__':
    n = int(input())
    ans = 1
    for i in range(2, n + 1): ans *= i
    print(ans)

# hàm zip là ghép 2 mảng với nhau
a = [1, 2, 3, 4]
b = ['a', 'b', 'c']
c = list(zip(a, b))
print(c)

# Nhập n, tính 1*n + 2*(n-1) + ... + n*1
n = int(input())
a = range(1, n + 1)
b = zip(a, a[::-1])
ans = 0
for x, y in b:
    ans += x * y
print(ans)

# tính fibonaci
n = int(input())
a = 1
b = 1
c = a + b
for _ in range(n):
    print(a, end=" ")
    a = b
    b = c
    c = a + b

# hoặc
n = int(input())
F = [1] * 2                                                                 # F = [1] * 2  <=> F = [1, 1]
for _ in range(n): F.append(F[-1] + F[-2])
print(*F[:n])

# Nhập vào một dãy số nguyên, tính tổng bình phương các phần tử
# s1 = a[1]*a[1] + .... + a[n]*a[n]
# s2 = a[1]*a[n] + .... + a[n]*a[1]
# s3 = a1 + (a1 + a2) + ... + (a1 + a2 + ... + an)

a = list(map(int, input().split()))
s1 = [x*x for x in a]
s2 = [x*y for x, y in zip(a, a[::-1])]
s3 = [x*y for x, y in zip(range(1, len(a) + 1), a[::-1])]
print(sum(s1), sum(s2), sum(s3), end="\n")

a = [1, 4, 5, 7, 6, 3, 2]
for i, x in enumerate(a):                                                   # => enumerate() chỉ số và giá trị
    print(i, x)

from math import sqrt
a = [1, 4, 5, 7, 6, 3, 2]
b = [x for x in a if x % 2 == 0]
c = [sqrt(x) for x in a if x > 0]
if b==[]: print('Khong co so chan')
else: print('Tong chan: ', sum(b))
print('Tong can cac so duong: ', sum(c))

# cho a1...an kiểm tra dãy có tăng dần hay không a1 < a2 < ... < an ?
a = list(map(int, input().split()))
b = [1 for x, y in zip(a, a[1:]) if x >= y]
if b == []: print('yes')
else: print('no')

# dãy con đơn điệu dài nhất
from bisect import bisect_left, bisect_right
# a = [3, 9, 424, 612]
#
# x = bisect_left(a, 21, 0, len(a))                                 # lower_bound in C++ : trả về vị trí đầu tiên >= x
# x = bisect_right(a, 21, 0, len(a))                                # lower_bound in C++ : trả về vị trí đầu tiên > x
#
# print(x)
a = list(map(int, input().split()))
b = [a[0]]
for x in a[1:]:
    if x > b[-1]: b.append(x)
    else:
        p = bisect_left(b, x, 0, len(b))
        b[p] = x
print("do dai day con don dieu tang dai nhat ", len(b), *b)

# tìm nghiệm x^x = a biết 1 < a <= 10^10
a = float(input())
left = 1
right = 10
while right - left > 1e-4:
    mid = (left + right) / 2
    if mid ** mid < a: left = mid
    else: right = mid
print(left)
'''

# Tìm điểm trong hình tròn gần 1 điểm M nhất
from math import sqrt
def kc(x, y, u, v): return (x - u) * (x - u) + (y - v) * (y - v)

if __name__ == '__main__':
    x, y, r, xM, yM = map(int, input().split())
    if kc(x, y, xM, yM) <= r: print(xM, yM)
    else:
        xP, yP = x, y
        while abs(xP - xM) > 1e-4 or abs(yP - yM) > 1e-4:
            xQ = (xP + xM) / 2
            yQ = (yP + yM) / 2
            if kc(x, y, xQ, yQ) > r * r: xM, yM = xQ, yQ
            else: xP, yP = xQ, yQ
        print(xM, yM)
