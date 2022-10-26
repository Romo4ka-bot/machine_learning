import numpy as np
import pygame

class Point:
    def __init__(self, x, y, color='black', cluster=None):
        self.x = x
        self.y = y
        self.color = color
        self.cluster = cluster

    @property
    def pos(self):
        return self.x, self.y

    def dist(self, point):
        return np.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.cluster, (self.x, self.y), 10)


def mark(points):
    new_points = list(points)
    eps = 100
    minPoints = 3
    colorNumber = 0
    clr = ['black', 'pink', 'purple', 'orange', 'cyan', 'yellow', 'green', 'grey']

    for i in range(len(new_points)):
        if new_points[i].cluster is not None:
            continue

        neighbors = calc_neighbors(new_points, new_points[i], eps)
        
        if len(neighbors) < minPoints:
            new_points[i].cluster = clr[0]
            continue

        new_points[i].cluster = clr[colorNumber + 1]

        z = 0
        while z < len(neighbors):
            iN = neighbors[z]

            if new_points[iN].cluster == clr[0]:
                new_points[iN].cluster = clr[colorNumber + 1]

            if new_points[iN].cluster is not None:
                z += 1
                continue

            new_points[iN].cluster = clr[colorNumber + 1]

            new_neighbors = calc_neighbors(new_points, new_points[iN], eps)

            if len(new_neighbors) >= minPoints:
                for neighbor in new_neighbors:
                    if neighbor not in neighbors:
                        neighbors.append(neighbor)
            z += 1
        colorNumber += 1
    return new_points

def calc_neighbors(points, point, eps):
    neighbors = []
    for i in range(len(points)):
        if point.dist(points[i]) < eps:
            neighbors.append(i)
    return neighbors

def draw():
    R = 10
    points = []
    pygame.init()
    new_points = []
    screen = pygame.display.set_mode([800, 600])
    screen.fill(color='white')
    pygame.display.update()
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.draw.circle(screen, color='black', center=event.pos, radius=R)
                pnt = Point(event.pos[0], event.pos[1])
                points.append(pnt)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                new_points = mark(points)

                for point in new_points:
                    point.draw(screen)

                for point in points:
                    point.cluster = None

            pygame.display.update()


if __name__ == '__main__':
    draw()