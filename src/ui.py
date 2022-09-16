"""Module with balls visualization"""

import pygame
import time

from src.config import Config
from src.field import ColoredBall, Field


class UI:
    """Visualization class"""

    def __init__(self):
        self._field = Field(handle_collisions=Config.HANDLE_COLLISIONS)

        pygame.init()
        pygame.font.init()
        self._font = pygame.font.SysFont(name=Config.FONT_NAME, size=Config.FONT_SIZE)

        self._window = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption('Balls')

    def run(self, show_stats: bool = False):
        """Starts visualization

        Parameters:
            show_stats (bool): if True, then the total energy of the system will be displayed on the screen
        """
        self._field.clear_balls()
        self._field.add_balls(Config.N_BALLS)

        clock = pygame.time.Clock()

        prev_time = time.time()

        while not any(event.type == pygame.QUIT for event in pygame.event.get()):
            clock.tick(Config.FPS)

            current_time = time.time()
            dt = current_time - prev_time
            prev_time = current_time

            self._window.fill(Config.BACKGROUND_COLOR)
            self.draw_balls()

            if show_stats:
                self.draw_energy()

            self._field.move_all(time= dt * Config.TARGET_FPS)
            pygame.display.flip()

    def draw_balls(self):
        """Draws all balls"""
        for ball in self._field:
            self.draw_ball(ball)

    def draw_ball(self, ball: ColoredBall):
        """Draws ball on the screen

        Parameters:
            ball (ColoredBall): ball to draw
        """
        coords = (round(ball.x), round(ball.y))
        pygame.draw.circle(self._window, ball.color, coords, ball.radius)

    def draw_energy(self):
        """Shows total kinetic energy value"""
        text_surface = self._font.render(f'{self._field.total_energy:.02f}J', False, Config.FONT_COLOR)
        self._window.blit(text_surface, dest=(
            Config.WIDTH - text_surface.get_width(),
            Config.HEIGHT - text_surface.get_height(),
        ))
