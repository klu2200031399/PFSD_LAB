s1= input()

out = [(s1[i:i+1]) for i in range(0, len(s1), 1)]
print(out)
t1= input()
A,B,C,D,E= 0,1,2,3,4


# # Assume each character represents a coordinate (A=0, B=1, C=2, D=3, E=4)
# s1_coord = ord(s1) - ord('A')
# s2_coord = ord(s2) - ord('A')
# t1_coord = ord(t1) - ord('A')
# t2_coord = ord(t2) - ord('A')
#
# # Calculate distances
# distance_s = (s2_coord - s1_coord) ** 2
# distance_t = (t2_coord - t1_coord) ** 2
#
# # Compare distances
# if distance_s == distance_t:
#     print("Yes")
# else:
#     print("No")