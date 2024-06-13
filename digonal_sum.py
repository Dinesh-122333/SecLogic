mat = [

[1,1,1,1],

[1,1,1,1],

[1,1,1,1],

[1,1,1,1]

]


# Output: 


# 8
def sum_diagonals(mat):
    
    if not mat or any(len(row) != len(mat) for row in mat):
        return "The matrix is not square"

    pri_dig = 0
    sec_dig = 0
    
    
    for i in range(len(mat)):
        pri_dig += mat[i][i]
        sec_dig += mat[i][len(mat) - 1 - i] 

    return pri_dig, sec_dig
