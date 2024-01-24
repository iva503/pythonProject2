import math


def detect_collision(first, second, radius_first, radius_second):
    if (math.sqrt((first.x - second.x) ** 2 + (first.y - second.y) ** 2) <= radius_first+radius_second):
        return True
    return False