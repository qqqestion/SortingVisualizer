import pygame


colors = {
    'field_color': (25, 25, 25),
    'bg_color': (35, 35, 35),
    'element_color': (255, 255, 255),
    'current_element_color': (200, 50, 50),
    'current_compare_elem': (50, 200, 50)
}


class ScreeenHandle(pygame.Surface):

    def __init__(self, *args, **kwargs):
        if len(args) > 1:
            self.successor = args[-1]
            self.next_coord = args[-2]
            args = args[:-2]
        else:
            self.successor = None
            self.next_coord = (0, 0)
        super().__init__(*args, **kwargs)
        self.fill(colors['bg_color'])

    def draw(self, canvas):
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            self.successor.draw(canvas)
        
    def connect_engine(self, engine):
        self.engine = engine
        if self.successor is not None:
            self.successor.connect_engine(engine)


class Canvas(ScreeenHandle):

    def draw(self, canvas):
        self.fill(colors['field_color'])
        self.engine.sort.draw(self)
        super().draw(canvas)
        # self.fill(colors['current_element_color'])


class InfoWindow(ScreeenHandle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connect_engine(self, engine):
        super().connect_engine(engine)
    
    def draw(self, canvas):
        # self.fill((50, 200, 50))
        self.fill(colors['bg_color'])
        font1 = pygame.font.SysFont('courier', 14)
        data = []
        sort = self.engine.sort
        data.append(f'{sort.sort_type}')
        data.append(f'ComparisonNum: {sort.get_number_of_comparisons()}')
        data.append(f'CurrentElement: {sort.elements[sort.icur_elem]}')
        data.append(f'Elements: {sort.size}')
        for i, text in enumerate(data):
            self.blit(font1.render(text, True, ((128, 128, 255))), (10, 50 + 30 * i))
        super().draw(canvas)



class HelpWindow(ScreeenHandle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []
        self.data.append('SpacePlay/Stop')
        self.data.append('1 Selection Sort')
        self.data.append('2 Merge Sort')
        self.data.append('↑ Increase the number of Elements')
        self.data.append('↓ Decrease the number of Elements')
    
    def draw(self, canvas):
        self.fill(colors['bg_color'])
        font1 = pygame.font.SysFont("courier", 16)
        for i, text in enumerate(self.data):
            self.blit(font1.render(text, True, ((128, 128, 255))),
                        (50, 30 + 20 * i))
        super().draw(canvas)
