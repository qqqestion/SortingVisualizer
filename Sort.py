from abc import ABC, abstractmethod
from random import randint
from Settings import *
import pygame


class AbstractSort(ABC):

    def __init__(self, size):
        if size < 0:
            raise RuntimeError
        self.elements = [randint(1, 30) for x in range(size)]
        self.size = size
        self.n_comparison = 0

    def get_number_of_comparisons(self):
        return self.n_comparison

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def next_step(self):
        pass

    @classmethod
    def create_from_instance(cls, size):
        return cls(size)

    def get_surface_conf(self, surface):
        swidth, sheight = surface.get_size()
        swidth -= 10
        width = round(swidth / self.size)
        delimiter = round(width / 20)
        width -= delimiter * 2

        x = 5
        y = sheight // 10
        hm = 3
        return (x, y, width, delimiter, hm)


class SelectionSort(AbstractSort):

    sort_type = 'Selection Sort'

    def __init__(self, size=30):
        super().__init__(size)
        self.icur_elem = 1
        self.i = 0
        self.sorted_size = 1

    def next_step(self):
        if self.sorted_size != self.size:
            self.n_comparison += 1
            if self.elements[self.icur_elem] < self.elements[self.i] or self.i == self.icur_elem:
                current_element = self.elements[self.icur_elem]
                self.elements.pop(self.icur_elem)
                self.elements.insert(self.i, current_element)
                self.i = 0
                self.icur_elem += 1
                self.sorted_size += 1
            else:
                self.i += 1

    
    def print_dict(self):
        print('Dict')
        for stat in self.__dict__.items():
            print(stat)
    
    def draw(self, surface):
        x, y, width, delimiter, hm = self.get_surface_conf(surface)

        for i in range(len(self.elements)):
            if i == self.i:
                pygame.draw.rect(
                    surface,
                    current_compare_color,
                    (x, y, width, self.elements[i] * hm)
                )
            elif i == self.icur_elem:
                pygame.draw.rect(
                    surface,
                    current_element_color,
                    (x, y, width, self.elements[i] * hm)
                )
            else:
                pygame.draw.rect(
                    surface,
                    all_elements_color,
                    (x, y, width, self.elements[i] * hm)
                )
            x += delimiter + width


class MergeSort(AbstractSort):

    sort_type = 'Merge Sort'

    def __init__(self, size=30):
        super().__init__(size)
        self.elements = list(map(lambda x: [x], self.elements))

    def merge(self, a, b):
        res = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        res.extend(a[i:] if i < len(a) else b[j:])
        return res

    def next_step(self):
        pass

    def draw(self, surface):
        return super().draw(surface)
