# Program to find the Diagonal Difference of a given Matrix 
arr = [[11, 2, 4,], [4, 5, 6], [10, 8, -12]]

# [11, 2,   4]
# [4,  5,   6]
# [10, 8, -12]
# [1,  2,   3]


# print(arr[0][0])
# print(arr[1][1])
# print(arr[2][2])

# print(arr[0][2])
# print(arr[1][1])
# print(arr[2][0])

l = len(arr)

s1, s2 = 0, 0

for i in range(l):
	s1 += arr[i][i]
	s2 += arr[i][l-1-i]	


print(s1)
print(s2)
print("total_sum of diagonal is :", s2-s1)