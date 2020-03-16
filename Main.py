import pygame
import random
from Settings import *
import Logic
import time
from Sort import *
import Screen


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Algorithms Visualization')
screen.fill(bg_color)

    
def create_visualization(elem_count, is_new=True):
    global engine, drawer
    if is_new:
        engine = Logic.Engine()
        engine.element_count = elem_count
        drawer = Screen.Canvas(
            (screen_width - screen_width // 5, screen_height - screen_height // 3),
            (0, screen_height - screen_height // 3),
            Screen.HelpWindow(
                (screen_width, screen_height // 3),
                (screen_width - screen_width // 5, 0),
                Screen.InfoWindow(
                    (screen_width // 5, screen_height - screen_height // 3)
                )
            )
        )
    else:
        engine.sort = engine.sort.create_from_instance(engine.element_count)
    drawer.connect_engine(engine)


def main():
    create_visualization(element_count, True)

    while engine.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    engine.running = False
                if event.key == pygame.K_UP:
                    engine.element_count = min(engine.element_count + 10, 100)
                    create_visualization(engine.element_count, False)
                if event.key == pygame.K_DOWN:
                    engine.element_count = max(engine.element_count - 10, 10)
                    create_visualization(engine.element_count, False)
                if event.key == pygame.K_SPACE:
                    engine.pause = not engine.pause
                if event.key == pygame.K_1:
                    engine.sort = SelectionSort(engine.element_count)

        if not engine.pause:
            engine.sort.next_step()
            screen.blit(drawer, (0, 0))
            drawer.draw(screen)
            time.sleep(0.4)
        pygame.display.update()
        # elements_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



if __name__ == "__main__":
    main()