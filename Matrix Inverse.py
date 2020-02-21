def matrixTranspose(matrix):
    for a in range(0,len(matrix)):
        if len(matrix[0]) != len(matrix[a]):
            print("Invalid matrix. Try again.")
            break
        elif len(matrix) == 1:
            print(matrix)
    else:
        transpose = []
        for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix)):
                transpose.append(matrix[j][i])
        transposefinal = [
            transpose[k:k + len(matrix)]
            for k in range(0, len(transpose), len(matrix))
        ]
        print(transposefinal)

myMatrix = [[1, 2, 0, 1], [3, 100, 5, 22],[432,1,0,0]]
matrixTranspose(myMatrix)
