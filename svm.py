import numpy as np
import pygame
from sklearn import svm


def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if __name__ == '__main__':

    pygame.init()

    scr = pygame.display.set_mode((600, 400))
    scr.fill((255, 255, 255))
    pygame.display.update()


    clock = pygame.time.Clock()
    FPS = 60

    xxx = []
    yyy = []

    points = []
    clusters = []
    p = True
    while p:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                p = False
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    pygame.draw.circle(scr, (255, 0, 0), i.pos, 5)
                    points.append(i.pos)
                    clusters.append(0)
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 3:
                    pygame.draw.circle(scr, (0, 255, 0), i.pos, 5)
                    points.append(i.pos)
                    clusters.append(1)
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 2:
                    scr.fill((255, 255, 255))
                    points = []
                    clusters = []
            if i.type == pygame.KEYDOWN:
                alg = svm.SVC(kernel='linear')
                alg.fit(points, clusters)
                w = alg.coef_[0]

                a = -w[0] / w[1]
                xx = np.linspace(100, 500, 600)
                yy = (a * xx - alg.intercept_[0] / w[1])
                b = 10000
                point = []

                for j in range(0, len(points)):
                    for i in range(0, len(yy)):
                        if b > distance(points[j][0], points[j][1], xx[i], yy[i]):
                            b = distance(points[j][0], points[j][1], xx[i], yy[i])
                            point = [j, i]

                print('b: ', b)
                print(points)
                print(alg.support_vectors_)
                pygame.draw.line(scr, (0, 255, 255), (xx[0], yy[0]), (xx[len(xx) - 1], yy[len(yy) - 1]), 2)
                pygame.draw.line(scr, (0, 255, 255), (xx[0] - b, yy[0] - b), (xx[len(xx) - 1] - b, yy[len(yy) - 1] - b),
                                 2)
                pygame.draw.line(scr, (0, 255, 255), (xx[0] + b, yy[0] + b), (xx[len(xx) - 1] + b, yy[len(yy) - 1] + b),
                                 2)

        clock.tick(FPS)
        pygame.display.update()