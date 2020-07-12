from random import randint
import pygame
import time
import argparse

from sorting import (DataSequence, 
                     launch_quick_sort, 
                     launch_merge_sort, 
                     launch_bubble_sort, 
                     launch_selection_sort, 
                     launch_insertion_sort, 
                     launch_shell_sort)


def screen_init(width, height):
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Algorithms Visualization')
    pygame.display.update()
    return screen


def calculate_num(a):
    res = {}
    for num in a:
        if num not in res:
            res[num] = 0
        res[num] += 1
    return res

def get_surface_conf(surface, elements):
    swidth, sheight = surface.get_size()
    width = swidth // elements
    # delimiter = round(width / 20)
    delimiter = 1
    width -= 1
    # width -= delimiter * 2

    x = 0
    y = sheight // 10
    hm = 3
    return (x, y, width, delimiter, hm)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int, default=800, help='Screen width')
    parser.add_argument('--height', type=int, default=600, help='Screen height')
    parser.add_argument('--sort', 
                        type=str, 
                        choices=['quick_sort', 
                                 'merge_sort', 
                                 'bubble_sort', 
                                 'selection_sort', 
                                 'insertion_sort', 
                                 'shell_sort'], 
                        default='quick_sort',
                        help='Type of sorting')

    args = parser.parse_args()
    width = args.width
    height = args.height
    sort = 'launch_{}'.format(args.sort)
    return width, height, sort


def main():
    width, height, sort = parse_args()

    screen = screen_init(width, height)

    ds = DataSequence(100)
    x, y, width, delimiter, hm = get_surface_conf(screen, 
                                                  len(ds))
    exec(f'{sort}(ds)')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        ds.visualize(screen, x, y, width, delimiter, hm)
        pygame.display.update()


if __name__ == "__main__":
    # test_sort(merge_sort, 500)
    main()
