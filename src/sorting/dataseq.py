from random import randint
import pygame

from .colors import white, red, green, blue, bg_color


min_e = 1
max_e = 100


class DataSequence:

    state_list = []

    def __init__(self, size):
        self.elements = [randint(min_e, max_e) for _ in range(size)]
        self.current_state = 0
        self.comparison = 0
    
    def visualize_text(self, surface):
        font1 = pygame.font.SysFont('courier', 14)
        comparison = self.state_list[self.current_state].get('comparison', 0)
        text = f'Number of Comparison {comparison}'
        surface.blit(font1.render(text, True, ((128, 128, 255))), (5, 500))
    
    def visualize(self, surface, x, y, width, delimiter, hm):
        state = self.state_list[self.current_state]
        objs = state.get('elements', [])
        idx1 = state.get('idx1')
        idx2 = state.get('idx2')
        # x, y, width, delimiter, hm = self.get_surface_conf(surface)
        surface.fill(bg_color)
        for i in range(len(objs)):
            current_color = white
            if i == idx1:
                current_color = red
            elif i == idx2:
                current_color = green
            pygame.draw.rect(
                surface,
                current_color,
                (x, y, width, objs[i] * hm)
            )
            x += delimiter + width
        self.visualize_text(surface)
        self.current_state = min(self.current_state + 1, len(self.state_list) - 1)

    def save_state(self, idx1=None, idx2=None):
        sort_state = {
            'elements': self.elements.copy(),
            'idx1': idx1,
            'idx2': idx2,
            'comparison': self.comparison
        }
        self.state_list.append(sort_state)
    
    def swap(self, idx1, idx2):
        self.comparison += 1
        self.elements[idx1], self.elements[idx2] = self.elements[idx2], self.elements[idx1]
        self.save_state(idx1, idx2)
    
    def set_value(self, idx1, value):
        self.comparison += 1
        self.elements[idx1] = value
        self.save_state(idx1)
    
    def __len__(self):
        return len(self.elements)
    
    def __getitem__(self, idx):
        return self.elements[idx]
    
    def is_sorted(self):
        return all(self.elements[i] <= self.elements[i + 1] for i in range(len(self) - 1))
