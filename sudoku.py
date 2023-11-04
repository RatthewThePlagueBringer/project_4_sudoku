import pygame, sys
from constants import *
from board import Board
from sudoku_generator import *


def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    select_mode_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 45)

    # Color background
    screen.fill(SCREEN_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, BLACK)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 250))
    screen.blit(title_surface, title_rectangle)

    # Initialize and draw title
    title_surface = select_mode_font.render("Select Game Mode:", 0, BLACK)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("EASY", 0, WHITE)
    medium_text = button_font.render("MEDIUM", 0, WHITE)
    hard_text = button_font.render("HARD", 0, WHITE)

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(DARK_BLUE)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(DARK_BLUE)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(DARK_BLUE)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 50))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50))
    hard_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 50))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    # Checks if user chooses easy mode
                    easy = 1
                    return easy
                    # return  # If the mouse is on the start button, we can return to main
                elif medium_rectangle.collidepoint(event.pos):
                    # Checks if user chooses medium mode
                    medium = 40
                    return medium
                elif hard_rectangle.collidepoint(event.pos):
                    # Checks if user chooses hard mode
                    hard = 50
                    return hard
        pygame.display.update()


def draw_other_buttons(screen):
    # Initialize title font
    buttons_font = pygame.font.Font(None, 50)

    # Initialize buttons
    # Initialize text first
    reset_text = buttons_font.render("RESET", 0, WHITE)
    restart_text = buttons_font.render("RESTART", 0, WHITE)
    exit_text = buttons_font.render("EXIT", 0, WHITE)

    # Initialize button background color and text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(DARK_BLUE)
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(DARK_BLUE)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(DARK_BLUE)
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 375))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 375))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 375))

    # Draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    buttons = [reset_rectangle, restart_rectangle, exit_rectangle]

    return buttons

# Handle user input errors
def error_message(error):
    message_font = pygame.font.Font(None, 30)
    user_error_message = message_font.render(error, 0, DODGER_BLUE)

    # Initialize button background color and text
    error_message_surface = pygame.Surface(
        (user_error_message.get_size()[0] + 15, user_error_message.get_size()[1] + 15))
    error_message_surface.fill(BG_COLOR)
    error_message_surface.blit(user_error_message, (10, 10))
    error_message_rectangle = error_message_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 325))

    # Write message on the screen
    screen.blit(error_message_surface, error_message_rectangle)

    pygame.display.flip()  # Update the display

    pygame.time.delay(800)  # Display the message for 0.8 sec

    # Clear the error message from the screen
    screen.fill(BG_COLOR)
    pygame.display.flip()


def draw_game_over(screen, winner):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)

    if winner != 0:
        text = 'Game Won!'
    else:
        text = "Game Over :("

    game_over_surf = game_over_font.render(text, 0, DARK_BLUE)
    game_over_rect = game_over_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    restart_surf = game_over_font.render(
        'RESTART', 0, DARK_BLUE)
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)

    #  Added key to return to main menu
    menu_surf = game_over_font.render(
        'Press m to return to the main menu...', 0, DARK_BLUE)
    menu_rect = menu_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(menu_surf, menu_rect)

    pygame.display.update()


def main():
    game_over = False
    winner = 0

    # template
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    # Let use select game difficulty from the draw_game_start() function
    selected_difficulty = draw_game_start(screen)
    sudoku_board = generate_sudoku(9, selected_difficulty)

    # Create an instance of the Board class with the generated Sudoku board
    board = Board(WIDTH, HEIGHT, screen, selected_difficulty, sudoku_board[0])
    clicked_cell = None
    sketched_val = 0

    while True:
        # event listeners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_pos = pygame.mouse.get_pos()

                # Handle three buttons: 'reset', 'restart', and 'exit'
                for i, button in enumerate(draw_other_buttons(screen)):
                    # if user clicks the button
                    if button.collidepoint(mouse_pos):
                        # reset board
                        if i == 0:
                            board.reset_to_original()
                        # restart game
                        elif i == 1:
                            main()
                        # quit game
                        elif i == 2:
                            pygame.quit()
                            sys.exit()

                clicked_row = int(event.pos[1] / CELL_SIZE)
                clicked_col = int(event.pos[0] / CELL_SIZE)
                # print(event.pos[1], event.pos[0])

                # Update the selected cell
                board.select(clicked_row, clicked_col)
                clicked_cell = board.click(int(event.pos[1]), int(event.pos[0]))

            if event.type == pygame.KEYDOWN:
                # let user input number in the cell
                if pygame.K_1 <= event.key <= pygame.K_9:
                    sketched_val = event.key - pygame.K_1 + 1
                    board.sketch(sketched_val)
                # update the original 2d list with the new value user inputs
                elif event.key == pygame.K_RETURN:
                    board.place_number(sketched_val)
                # let user clear the value cell when typing 'backspace'
                elif event.key == pygame.K_BACKSPACE:
                    board.clear()

                # else:
                #     value_err = "Error: Please enter a valid number between 1 and 9."
                #     error_message(value_err)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and board.is_full():
                        game_over = True

        if game_over:
            if board.board == sudoku_board[1]:
                winner = 1
            elif board.board != sudoku_board[1]:
                winner = 0
            pygame.display.update()
            draw_game_over(screen, winner)

        # Draw the board and other buttons
        screen.fill(BG_COLOR)
        screen.fill(BG_COLOR)
        board.update_board()
        board.draw()
        draw_other_buttons(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
