import pygame
import random

def print_screen(screen):
    screen.fill("light green")
    for i in range(0, 640, 32):
        pygame.draw.line(screen, "black", (i, 0), (i, 512))
    for i in range(0, 512, 32):
        pygame.draw.line(screen, "black", (0, i), (640, i))


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        print_screen(screen)
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mole_in = [0, 0]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_in = [event.pos[0] // 32, event.pos[1] // 32]
                    for i in range(20):
                        for j in range(16):
                            if click_in[0] == mole_in[0] and click_in[1] == mole_in[1]:
                                print_screen(screen)
                                x = random.randrange(0, 20)
                                y = random.randrange(0, 16)
                                box_for_mole = [x, y]
                                screen.blit(mole_image, mole_image.get_rect(topleft=(box_for_mole[0] * 32, box_for_mole[1] * 32)))
                                mole_in = box_for_mole
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
