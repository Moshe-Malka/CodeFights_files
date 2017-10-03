def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
    _matrix = matrix
    for r in rowsToDelete:
        del _matrix[r]
        r-=1
    for i in range(len(columnsToDelete)):
        c=columnsToDelete[i]
        if(i is not 0):
            c-=1
        for r in _matrix:
            r.pop(c)
        
    return _matrix




'''

Given a matrix, find its submatrix obtained by deleting the specified rows and columns.

Example

For

matrix = [[1, 0, 0, 2], 
          [0, 5, 0, 1], 
          [0, 0, 3, 5]]
rowsToDelete = [1] and columnsToDelete = [0, 2], the output should be

constructSubmatrix(matrix, rowsToDelete, columnsToDelete) = [[0, 2],
                                                             [0, 5]]
Input/Output

[time limit] 4000ms (py)
[input] array.array.integer matrix

2-dimensional array of integers.

Guaranteed constraints:
1 ≤ matrix.length ≤ 5,
1 ≤ matrix[0].length ≤ 5,
0 ≤ matrix[i][j] ≤ 15.

[input] array.integer rowsToDelete

Array of indices (0-based) of rows to be deleted.

Guaranteed constraints:
0 ≤ rowsToDelete.length ≤ 2,
0 ≤ rowsToDelete[i] < matrix.length.

[input] array.integer columnsToDelete

Array of indices (0-based) of columns to be deleted.

Guaranteed constraints:
0 ≤ columnsToDelete.length ≤ 2,
0 ≤ columnsToDelete[i] < matrix[0].length.

[output] array.array.integer

GIVE UP
CODE.PY
Saved
Python2

def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
    _matrix = matrix
    for r in rowsToDelete:
        del _matrix[r]
        r-=1
    for i in range(len(columnsToDelete)):
        c=columnsToDelete[i]
        if(i is not 0):
            c-=1
        for r in _matrix:
            r.pop(c)
        
    return _matrix
1
def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
2
    _matrix = matrix
3
    for r in rowsToDelete:
4
        del _matrix[r]
5
        r-=1
6
    for i in range(len(columnsToDelete)):
7
        c=columnsToDelete[i]
8
        if(i is not 0):
9
            c-=1
10
        for r in _matrix:
11
            r.pop(c)
12
        
13
    return _matrix
TESTS
CUSTOM TESTS
Sample tests passed
Click Submit to run the full test set and to save your solution
Test 1
Test 2
Test 3
Test 4
Test 5
Formatting
Font Size
14px
Code Completion
Auto-brackets
Editor
Type
Sublime
Theme
Dark
Hotkeys
CTRL + Enter
Submit Solution
CTRL + R
Run Solution
CTRL + S
Save Source Code
SKIP
RUN TESTS
SUBMIT



''''
