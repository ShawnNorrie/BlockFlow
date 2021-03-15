

live_grid = [[0,1,2,3,4,5,6,7,8],
            [0,1,2,3,4,5,6,7,8],
            [0,1,2,3,4,5,6,7,8],
            [0,1,2,3,4,5,6,7,8],
            [0,1,2,3,4,5,6,7,8],
            [0,1,2,3,4,5,6,7,8],
            [0,1,2,3,4,5,6,7,8],
            [0,1,2,3,4,5,6,7,8],
            [0,1,2,3,4,5,6,7,8]]

def display_grid(grid):

    for i in range (len(grid)):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - - - -")

        for j in range (len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end = "")

def unique_solution(solution1, grid):
     
    return false:

display_grid(live_grid)
