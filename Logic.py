from Sort import *
from Settings import element_count as ec


class Engine:
    running = True
    pause = False
    show_help = False
    algorithm = None
    sort = MergeSort(ec)
    element_count = ec
