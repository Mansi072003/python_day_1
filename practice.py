data = ["hello",  "Python3", "#", "code", " "]
only_strings = [item for item in data if item.isalpha() or item.isspace()]

print(only_strings)


n = 7  
count = 0

while n:
    count += n & 1 
    n >>= 1  

print(count)  


for i in range(5):
    print (i)
    i=i+2


# matrix multiplication

A =[[1,2],
    [3,4]]

B =[[5,6],
    [7,8]]

result = [[0,0],
        [0,0]]
if(len(A)!=len(B)): 
    print("Not possible")
else:
  for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]
for row in result:
    print(row)
