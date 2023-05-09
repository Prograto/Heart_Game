import pygame
from chandu import*
def final_game(score):
    # Initialize Pygame
    pygame.init()
    # Set the window size
    win_width = 360
    win_height = 670
    window = pygame.display.set_mode((win_width, win_height))

    # Set the title of the game window
    pygame.display.set_caption("Fail in Love to Fall")

    # Define some colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Define a font for the menu items
    menu_font = pygame.font.SysFont(None, 50)
    menu = pygame.font.SysFont(None, 20)
    start_item = menu_font.render("Start", True, white)
    high_scores_item = menu_font.render("High Scores", True, white)
    exit_item = menu_font.render("Exit", True, white)
    text1 = menu.render("We can change the images in the game by replacing",True,white)
    text2 = menu.render("user0.png as you picture kelly.jpg it is background",True,white)
    text3 = menu.render("object.png these are Hearts Keep in mind replace", True, white)
    text4 = menu.render("the image having same deminsions and format in it.", True, white)

    start_item_pos = (win_width / 2 - start_item.get_width() / 2, 200)
    high_scores_item_pos = (win_width / 2 - high_scores_item.get_width() / 2, 300)
    exit_item_pos = (win_width / 2 - exit_item.get_width() / 2, 400)


    def start_game():
        global score
        score = my_game()
    s = menu_font.render("Old Score:" + str(score), True, white)
    s_item_pos = ((win_width / 2 - exit_item.get_width() / 2)-70, 500)
    def view_high_scores():
        pass
    def exit_game():
        pygame.quit()
        exit()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if start_item_pos[0] <= pos[0] <= start_item_pos[0] + start_item.get_width() and \
                        start_item_pos[1] <= pos[1] <= start_item_pos[1] + start_item.get_height():
                    start_game()
                elif high_scores_item_pos[0] <= pos[0] <= high_scores_item_pos[0] + high_scores_item.get_width() and \
                        high_scores_item_pos[1] <= pos[1] <= high_scores_item_pos[1] + high_scores_item.get_height():
                    view_high_scores()
                elif exit_item_pos[0] <= pos[0] <= exit_item_pos[0] + exit_item.get_width() and \
                        exit_item_pos[1] <= pos[1] <= exit_item_pos[1] + exit_item.get_height():
                    exit_game()

        window.fill(black)

        # Draw the menu items
        window.blit(start_item, start_item_pos)
        window.blit(high_scores_item, high_scores_item_pos)
        window.blit(exit_item, exit_item_pos)
        window.blit(text1,[10,10])
        window.blit(text2, [10, 25])
        window.blit(text3, [10, 40])
        window.blit(text4, [10, 55])
        window.blit(s, s_item_pos)

        pygame.display.update()

    pygame.quit()
