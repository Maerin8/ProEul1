("FINDING THE NUMBER OF PATHS THROUGH A GRID")
("Rules: You must start in the top-left while only moving right or down")
cube_size = int(input("Enter size of cube:\t"))
cube_size +=1
#this line of code gets rid of the "fat" around the border

cube_array = [[0 for i in range(cube_size)]for j in range(cube_size)]
##dynamic array for cube size
cube_array[0][0] = 1
#sets the top left of the array to 1

def neh_add(x,y):
    if(x != 0):
        cube_array[x][y] += cube_array[x - 1][y]
        #if value borders the top, don't add
    if(y != 0):
        cube_array[x][y] += cube_array[x][y - 1]
        #if value borders the left, don't add




for ii in range(cube_size):
    for jj in range(cube_size):
        neh_add(ii,jj)
    #print(cube_array[ii])
    #print uncomment this line of code to see the entire grid (messy w/o formatting but readable up to 10)

print(cube_array[cube_size -1][cube_size-1])
#subtracting cubesize back to add the "fat"
