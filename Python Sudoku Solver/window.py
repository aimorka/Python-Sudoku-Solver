import pygame

WIDTH = 550
background_color = (251,247,245)
element_color = (52, 31, 151)
buffer = 5
grid = [[0,0,0,0,6,0,0,0,5],
        [3,5,0,0,0,0,1,0,7],
        [9,0,4,0,0,1,8,0,0],
        [0,0,0,4,0,5,0,0,8],
        [0,4,0,0,0,0,9,0,0],
        [7,0,5,6,8,0,0,0,0],
        [0,0,0,0,7,0,0,3,9],
        [2,7,9,5,0,3,0,8,1],
        [5,8,0,1,9,6,0,4,2]]

def insert(win, position):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid[i-1][j-1] != 0): ##if our spot is filled return
                    return
                if (event.key == 48): ##0 is mapped to 48 in ascii nomenclature
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50 + buffer,50-2*buffer, 50-2*buffer)) ##x coord, y coord, height, width of rect| buffer sccounts for boundary lines
                    pygame.display.update()
                    return
                if (0 < event.key - 48 < 10): ##when we want to insert we overwrite a blank rectangle then
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50 + buffer,50-2*buffer, 50-2*buffer))
                    value = myfont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50 + 15, position[1]*50 + 15))
                    grid[i-1][j-1] = event.key - 48 ##update our backend grid
                    pygame.display.update()
                    return
                return
                    
                    
                    
                

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")

    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0,10):
        if i % 3 == 0:
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 4)  
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4)

        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 2)  ##windoe, color, start coor, end coor, width
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2)
    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, element_color)
                win.blit(value, ((j+1)*50 +15, (i*1)*50 + 65)) ##i travels vertically(up and down), each row j travels horizontally each column(left and right)
        pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.QUIT()
                return

print(grid)
main()
print(grid)