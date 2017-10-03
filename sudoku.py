# work in progress !
def sudoku2(grid):
    if len(grid)!= 9: return False
    for row in grid:
        if hasDuplicate(row) or len(row)!=9:
            return False
    column_checked=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            column_checked.append(grid[j][i])
        if hasDuplicate(column_checked):
            return False
        else:
            column_checked=[]
    return True   
        
def hasDuplicate(a):
    import string
    seen=set()
    for x in a:
        if x in string.digits:
            if x not in seen:
                seen.add(x)
            else:
                return True
    return False
