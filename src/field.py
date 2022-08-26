"""Module with balls system"""

from itertools import combinations

from src.ball import Ball
from src.config import Config


class ColoredBall(Ball):
    """Extended with color ball model

    Attributes:
        color (tuple): color in RGB format
    """

    def __init__(self, color: tuple, **kwargs):
        super(ColoredBall, self).__init__(**kwargs)
        self.color = color

    def __hash__(self):
        return hash((self.x, self.y))


class Field:
    """System with balls"""

    def __init__(self, handle_collisions: bool):
        self._balls = list()
        self._handle_collisions = handle_collisions

    @property
    def total_energy(self) -> float:
        """Calculates energy of the whole system

        Returns:
            (float): total kinetic energy of system
        """
        return sum(ball.energy for ball in self._balls)

    def add_balls(self, n_balls: int):
        """Adds random balls to the field, so that none of them overlap with the other

        Parameters:
            n_balls (int): amount of balls to add
        """
        for _ in range(n_balls):
            new_ball = self.get_random_ball()

            while any(ColoredBall.is_overlaps(new_ball, other_ball) for other_ball in self._balls):
                new_ball = self.get_random_ball()

            self._balls.append(new_ball)

    @staticmethod
    def get_random_ball() -> ColoredBall:
        """Creates ball with random stats"""
        radius = Config.random_radius
        return ColoredBall(
            x=Config.get_random_x_coord(radius),
            y=Config.get_random_y_coord(radius),
            vx=Config.random_x_speed,
            vy=Config.random_y_speed,
            ax=Config.random_x_acceleration,
            ay=Config.random_y_acceleration,
            radius=radius,
            color=Config.random_color,
        )

    def clear_balls(self):
        self._balls.clear()

    def move_all(self, time: float):
        """Calculates next system state

        Parameters:
            time (float): amount of time
        """
        overlapping = set()

        if self._handle_collisions:
            for a, b in combinations(self._balls, r=2):
                if ColoredBall.is_overlaps(a, b):
                    overlapping.update({a, b})
                    ColoredBall.handle_collision(a, b)

        for ball in self._balls:
            if ball not in overlapping:
                ball.move(time=time)
                ball.bounce_off(
                    min_x=Config.BALL_MIN_X_COORD,
                    max_x=Config.BALL_MAX_X_COORD,
                    min_y=Config.BALL_MIN_Y_COORD,
                    max_y=Config.BALL_MAX_Y_COORD,
                )

    def __iter__(self):
        return iter(self._balls)
