mat = [

[1,1,1,1],

[1,1,1,1],

[1,1,1,1],

[1,1,1,1]

]


# Output: 


# 8


pri_dig = 0
sec_dig = 0

    
for i in range(len(mat)):
    pri_dig += mat[i][i]
    sec_dig += mat[i][len(mat) - 1 - i] 

# print(pri_dig, sec_dig)
print(pri_dig + sec_dig)

