from itertools import takewhile

# ======================================================================================================================

q1 = {
    "a": 1,
    "b": 1,
    "c": 1
}

q2 = {
    "a": 2,
    "c": 1,
    "d": 1
}

s = sum(2 if q1[q] == q2[q] else 1 for q in q1.keys() & q2.keys())
# q1.keys() & q2.keys() => keep if key in q1 and q2
print("Result Expression 1:")
print(s)

# ======================================================================================================================

p1 = [1, 3, 5]
p2 = [1, 4, 7]

s = len(list(takewhile(lambda x: x[0] == x[1], zip(p1, p2))))
print("\nResult Expression 2:")
print(s)
"""
takewhile()

pred, seq

seq[0], seq[1], until pred fails

takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
"""

# ======================================================================================================================

sequence = [1, 3, 2, 1, 4, 5]
print("sum", sum([1 for a, b in zip(sequence[:-1], sequence[1:]) if a >= b]))


# => Đặt so le để so sánh 2 số cạnh nhau

# ======================================================================================================================

# Có thể coi 1 > 0 có kết quả là 1

# ======================================================================================================================


def rotate_image(a):
    return list(zip(*reversed(a)))


arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print("reversed arr")
print(list(reversed(arr)))

print("result")
print(rotate_image(arr))

# ======================================================================================================================

# Swap trong python
# a, b = b, a

# ======================================================================================================================

x = '123'
print(f'{x.center(5, "*")=}')

# ======================================================================================================================

"""
TÌM TỔNG MA TRẬN 3 * 3 TỪ MA TRẬN TO
"""
def my(arr):
    return [[sum(sum(x[i:i + 3]) for x in arr[j:j + 3])
                                 for i in range(len(arr[0]) - 2)]
                                 for j in range(len(arr) - 2)]

# ======================================================================================================================

"""
if else trong mang
"""
def arrayReplace(i, e, s):
    return [x if x != e else s for x in i]

# ======================================================================================================================

"""
Xác định xem 2 ô cơ có cùng màu ? https://prnt.sc/s29w6y
"""
def chessBoardCellColor(cell1, cell2):
    return (sum(map(ord, cell1+cell2))) % 2 == 0  # Tổng index của các ô trong bảng chia hết cho 2 là cùng màu
cell1 = "A1"
cell2 = "C3"
print(f'{chessBoardCellColor(cell1, cell2)=}')

# ======================================================================================================================
