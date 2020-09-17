"""
Given a matrix mat[][] of size M*N. Traverse and print the matrix in spiral form.
Input:
    4 4
    [1 2 3 4
     5 6 7 8
     9 10 11 12
     13 14 15 16]

Output:
    1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

steps:
   [
         --1----->
        /\        |
        |         2
        4         |
        |         \/
         <---3----
    4 loops for each direction:
    Let s_row=0, e_row=3 pointing to starting and ending of row (M[s_row]=1, M[e_row]=13)
        s_col=0, e_col=3 pointing to starting and ending of row (M[s_col]=1, M[e_col]=4)

        case 1: (1, 2, 3, 4) (00, 01, 02, 03)
            for i in range(s_col, e_col)
                print M[s_row][i]  ---> s_row is constant to 0
        --> Eliminate first row
        s_row++

        case 2: (8, 12, 16) (13, 23, 33)
            for i in range(s_row, e_row)
                print M[i][e_row]
        --> Eliminate last col
        e_col--

        # As we are printing row check if row is left or not
        s_row <= e_row
            case 3: (15, 14, 13) (23, 13, 03)
                for i in range(e_col, s_col-1,-1) Reverse
                    print M[e_row][i]
            e_row--

        # As we are printing column check if col is left or not
        s_col <= e_col
            case 4: (9, 5) (20, 10)
                for i in range(e_row, s_row-1,-1) upward
                    print M[i][s_col]
            s_col++
   ]

"""
from numpy import array


def spirally_traversing(arr, row, col):
    s_row, s_col = 0, 0
    e_row ,e_col = row-1, col-1

    while s_row <= e_row and s_col <= e_col:
        for i in range(s_col, e_col+1):
            print(arr[s_row][i], end=" ") #s_row=0, i=0,1,2,3
        s_row += 1
        for i in range(s_row, e_row+1):
            print(arr[i][e_col], end=" ") # i=1,2,3 e_row=3
        e_col -= 1

        if s_row <= e_row:
            for i in range(e_col, s_col-1, -1):
                print(arr[e_row][i], end=" ") # i=3,2,1   e_row=1
            e_row -= 1
        if s_col <= e_col:
            for i in range(e_row, s_row-1, -1):
                print(arr[i][s_col], end=" ")
            s_col += 1
    print()

if __name__ == "__main__":
    row_col = "10 2" #"4 4"
    row_col = list(map(int, row_col.split()))
    row, col = row_col[0], row_col[1]
    arr = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16"
    arr = "1 2 3 4 5 6 7 8 9 10 11 12"
    arr = "9 54 33 58 88 45 57 9 95 98 14 53 46 65 71 54 52 2 77 67"
    entries = list(map(int, arr.split()))
    matrix = array(entries).reshape(row, col)
    #print("1 2 3 4 8 12 11 10 9 5 6 7")
    #print("1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10")
    print("9 54 58 45 9 98 53 65 54 2 67 77 52 71 46 14 95 57 88 33")
    spirally_traversing(matrix, row, col)
