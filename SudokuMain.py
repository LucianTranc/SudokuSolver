# Lucian Tranc
# ltranc@uoguelph.ca
# Personal Sudoku Project

import pygame
import random


def update_board_values():
    # This function is used to update the values in the Sudoku table
    for x in range(9):
        for y in range(9):
            if str(board[x][y]) == '0':
                text_surface = myfont.render(str(' '), False, (0, 0, 0))
            else:
                text_surface = myfont.render(str(board[x][y]), False, (0, 0, 0))

            screen.blit(text_surface, (x_start * 2 + 21 + (53 * (x - 1)), y_start * 2 + 11 + (53 * (y - 1))))


def draw_board():
    # this function is used to draw over the existing table in oder to refresh the table in the pygame window
    for y in range(9):
        for x in range(9):
            rect = pygame.Rect(x_start+x*block_size+(x*gap), y_start+y*block_size+(y*gap), block_size, block_size)
            pygame.draw.rect(screen, (255, 255, 255), rect)

    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_start, y_start + 474), 4)
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_start + 474, y_start), 4)
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start + 474), (x_start + 474, y_start + 474), 4)
    pygame.draw.line(screen, (0, 0, 0), (x_start + 474, y_start), (x_start + 474, y_start + 474), 4)
    pygame.draw.line(screen, (0, 0, 0), (x_start + 156, y_start), (x_start + 156, y_start + 474), 4)
    pygame.draw.line(screen, (0, 0, 0), (x_start + 315, y_start), (x_start + 315, y_start + 474), 4)
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start + 156), (x_start + 474, y_start + 156), 4)
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start + 315), (x_start + 474, y_start + 315), 4)


def exists_empty_cell(board, empty_cell):
    # this function is used to determine if there remains any empty cells in the sudoku table
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                empty_cell[0] = row
                empty_cell[1] = col
                return True
    return False


def is_valid_move(board, empty_cell, num):
    # this function is used to determine if a move adheres to the rules of sudoku
    row = empty_cell[0] - empty_cell[0] % 3
    col = empty_cell[1] - empty_cell[1] % 3
    is_valid_section = True
    is_valid_row = True
    is_valid_col = True
    for i in range(3):
        for j in range(3):
            if board[i+row][j+col] == num:
                is_valid_section = False
                break
    for i in range(9):
        if board[empty_cell[0]][i] == num:
            is_valid_row = False
            break
    for i in range(9):
        if board[i][empty_cell[1]] == num:
            is_valid_col = False
            break

    return is_valid_section and is_valid_row and is_valid_col


def sudoku(board):
    # this is the recursive function that is used for the algorithm. Its base case is when the entire table is filled
    # the initial call returns true if all the cells are filled correctly
    # the backtracking is implemented by returning false if no values satisfy the rules of sudoku. This resets the
    # previous value back to zero and calls itself once again

    empty_cell = [0, 0]

    if not exists_empty_cell(board, empty_cell):
        return True

    for num in range(1, 10):
        if is_valid_move(board, empty_cell, num):
            board[empty_cell[0]][empty_cell[1]] = num
            draw_board()
            update_board_values()
            pygame.display.update()
            if sudoku(board):
                return True
            board[empty_cell[0]][empty_cell[1]] = 0
            draw_board()
            update_board_values()
            pygame.display.update()

    return False


def board_generator(board):
    # this function is a near copy of the recursive backtracking algorithm however its purpose is to create brand new
    # valid sudoku boards. This is done using the backtracking algorithm and with a random order of numbers.
    empty_cell = [0, 0]

    if not exists_empty_cell(board, empty_cell):
        return True

    # num is shuffled so the values added to the board are random
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(num)

    for i in range(0, 8):
        if is_valid_move(board, empty_cell, num[i]):
            board[empty_cell[0]][empty_cell[1]] = num[i]
            if board_generator(board):
                return True
            board[empty_cell[0]][empty_cell[1]] = 0

    return False


def board_puzzle_generator(board):
    # this function takes the fully generated sudoku board and creates it into a puzzle by removing random cells for
    # the backtracking algorithm to solve once again.
    for i in range(0, 9):
        for j in range(0, 9):
            num = random.randint(1, 10)
            if num < 6:
                board[i][j] = 0


def clear_board(board):
    # this function is used to reset the sudoku board
    for i in range(0, 9):
        for j in range(0, 9):
            board[i][j] = 0


if __name__ == "__main__":
    # the initial board is created
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    x_start = 50
    y_start = 50
    block_size = 50
    gap = 3
    background_colour = (200, 200, 200)
    (width, height) = (585, 640)
    clock = pygame.time.Clock()
    # the pygame window is created
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Sudoku Solver')
    screen.fill(background_colour)
    # the blank board is drawn
    draw_board()
    # the title is drawn above the board
    pygame.font.init()
    font_size = 30
    myfont = pygame.font.SysFont('Arial', font_size)
    title_header = myfont.render('Sudoku Backtracking Algorithm', False, (0, 0, 0))
    screen.blit(title_header, (x_start, y_start - font_size - 5))
    font_size = 20
    pygame.display.update()
    # main game loop
    running = True
    while running:
        # exit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # button is drawn for solving the sudoku board
        solve_button = pygame.Rect(x_start + 183, y_start + 500, 100, 50)
        pygame.draw.rect(screen, (255, 255, 255), solve_button)
        button_text1 = myfont.render('Solve', False, (0, 0, 0))
        screen.blit(button_text1, (x_start + 195, y_start + 507))
        # button is drawn for generating a new sudoku board
        refresh_button = pygame.Rect(x_start + 30, y_start + 500, 100, 50)
        pygame.draw.rect(screen, (255, 255, 255), refresh_button)
        button_text2 = myfont.render('New', False, (0, 0, 0))
        screen.blit(button_text2, (x_start + 47, y_start + 507))

        if event.type == pygame.MOUSEBUTTONDOWN:
            # event handler for the solve button
            if solve_button.collidepoint(event.pos):
                sudoku(board)
                pygame.draw.rect(screen, (230, 230, 230), solve_button)
                screen.blit(button_text1, (x_start + 195, y_start + 507))
            # event handler for the refresh button
            if refresh_button.collidepoint(event.pos):
                clear_board(board)
                board_generator(board)
                board_puzzle_generator(board)
                pygame.draw.rect(screen, (230, 230, 230), refresh_button)
                screen.blit(button_text2, (x_start + 47, y_start + 507))

        draw_board()
        update_board_values()
        pygame.display.update()
