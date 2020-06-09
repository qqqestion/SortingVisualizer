from random import randint
import pygame
import time
from conf import screen_width, screen_height
from DataSeq import DataSequence
from QuickSort import launch_quick_sort
from MergeSort import launch_merge_sort
from BubbleSort import launch_bubble_sort
from SelectionSort import launch_selection_sort
from InsertionSort import launch_insertion_sort
from ShellSort import launch_shell_sort


pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Algorithms Visualization')
pygame.display.update()


def test_sort(sort, num_test):
    for i in range(50):
        elements = [randint(1, 1000) for _ in range(num_test)]
        sort(elements, 0, len(elements))
        if not all(elements[i] <= elements[i + 1] 
                   for i in range(len(elements) - 1)):
            print('Not Okay')
            exit()
    print('Okay')


def calculate_num(a):
    res = {}
    for num in a:
        if num not in res:
            res[num] = 0
        res[num] += 1
    return res


def main():
    surface = pygame.Surface((screen_width, screen_height))
    ds = DataSequence(100)
    # print(ds.elements)
    nums = calculate_num(ds.elements)
    elems = ds.elements.copy()
    # TODO: write something to choose sorts
    # launch_merge_sort(ds)
    # launch_quick_sort(ds)
    # launch_bubble_sort(ds)
    # launch_selection_sort(ds)
    # launch_insertion_sort(ds)
    launch_shell_sort(ds)
    sorted_nums = calculate_num(ds.elements)
    if nums != sorted_nums:
        print('SOS')
        print('Origin:', nums)
        print('Sorted:', sorted_nums)
        exit()
    if not all(ds[i] <= ds[i + 1] for i in range(len(ds) - 1)):
        print('SOS')
        print('Origin:', elems)
        print('Sorted:', ds.elements)
        exit()
    # print(ds.elements)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        ds.visualize(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        # time.sleep(.3)


if __name__ == "__main__":
    # test_sort(merge_sort, 500)
    main()
