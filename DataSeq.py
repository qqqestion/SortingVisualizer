from random import randint
from conf import white, red, green, blue, bg_color
import pygame


min_e = 1
max_e = 100


class DataSequence:

    state_list = []

    def __init__(self, size):
        self.elements = [randint(min_e, max_e) for _ in range(size)]
        self.current_state = 0
        self.comparison = 0

    def get_surface_conf(self, surface):
        swidth, sheight = surface.get_size()
        swidth -= 10
        width = swidth // len(self.elements)
        delimiter = round(width / 20)
        width -= delimiter * 2

        x = 5
        y = sheight // 10
        hm = 3
        return (x, y, width, delimiter, hm)
    
    def visualize_text(self, surface):
        font1 = pygame.font.SysFont('courier', 14)
        data = []
        comparison = self.state_list[self.current_state].get('comparison', 0)
        data.append(f'Number of Comparison {comparison}')
        for i, text in enumerate(data):
            surface.blit(font1.render(text, True, ((128, 128, 255))), (5, 500))
    
    def visualize(self, surface):
        objs = self.state_list[self.current_state].get('elements', [])
        idx1 = self.state_list[self.current_state].get('idx1')
        idx2 = self.state_list[self.current_state].get('idx2')
        middle = self.state_list[self.current_state].get('middle')
        x, y, width, delimiter, hm = self.get_surface_conf(surface)
        surface.fill(bg_color)
        for i in range(len(objs)):
            current_color = white
            if i == idx1:
                current_color = red
            elif i == idx2:
                current_color = green
            elif i == middle:
                current_color = blue
            pygame.draw.rect(
                surface,
                current_color,
                (x, y, width, objs[i] * hm)
            )
            x += delimiter + width
        self.visualize_text(surface)
        self.current_state = min(self.current_state + 1, len(self.state_list) - 1)

    def save_state(self, idx1=None, idx2=None, middle=None):
        sort_state = {
            'elements': self.elements.copy(),
            'idx1': idx1,
            'idx2': idx2,
            'middle': middle,
            'comparison': self.comparison
        }
        self.state_list.append(sort_state)
    
    def swap(self, idx1, idx2):
        self.comparison += 1
        self.save_state(idx1, idx2)
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp
        self.save_state(idx1, idx2)
    
    def set_value(self, idx1, value):
        self.comparison += 1
        self.save_state(idx1)
        self.elements[idx1] = value
        self.save_state(idx1)
    
    def __len__(self):
        return len(self.elements)
