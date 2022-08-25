"""Module with ball math model"""

from math import hypot, pi

from src.config import Config


class Ball:
    """Mathematical and physical model of motion and absolutely
    elastic collision of _balls in two-dimensional space.

    Attributes:
        x (float): x-coordinate of the ball center
        y (float): y-coordinate of the ball center
        vx (float): x-speed or value of the change in the x-coordinate per unit of time
        vy (float): y-speed or value of the change in the y-coordinate per unit of time
        ax (float): x-acceleration or coefficient of change of vx per unit of time, strictly positive
        ay (float): y-acceleration or coefficient of change of vy per unit of time, strictly positive
        radius (float): ball radius value, strictly positive
    """

    def __init__(
            self,
            x: float, y: float,
            vx: float, vy: float,
            ax: float, ay: float,
            radius: float,
    ):
        self.x, self.vx, self.ax = x, vx, ax
        self.y, self.vy, self.ay = y, vy, ay
        self.radius = radius

    @property
    def mass(self) -> float:
        """Mass of the ball"""
        return pi * self.radius ** 2

    def move(self, time: float = 1.0):
        """Recalculates changes in the coordinates of the center and velocities
        along the axes for a given amount of time

        Parameters:
            time (float): amount of time
        """
        self.x += self.vx * time
        self.y += self.vy * time
        self.vx *= self.ax
        self.vy *= self.ay

    def bounce_off(self, max_x: float, max_y: float, min_x: float, min_y: float):
        """This method pushes the ball away from the wall
        if the distance from the center to it is less than the radius

        Parameters:
            max_x (float): maximum x-coordinate
            max_y (float): maximum y-coordinate
            min_x (float): minimum x-coordinate
            min_y (float): minimum y-coordinate
        """
        if (self.x - self.radius) <= min_x:
            self.vx = -self.vx
            self.x = min_x + self.radius

        if (self.x + self.radius) >= max_x:
            self.vx = -self.vx
            self.x = max_x - self.radius

        if (self.y - self.radius) <= min_y:
            self.vy = -self.vy
            self.y = min_y + self.radius

        if (self.y + self.radius) >= max_y:
            self.vy = -self.vy
            self.y = max_y - self.radius

    @staticmethod
    def is_overlaps(a: 'Ball', b: 'Ball') -> bool:
        """Checks if two balls overlap (collide)

        Parameters:
            a (Ball): first ball instance
            b (Ball): second ball instance

        Returns:
            (bool) True if the distance between balls is less than the sum of the radii, False otherwise
        """
        return Ball.distance(a, b) + Config.OVERLAP_EPS < a.radius + b.radius

    @staticmethod
    def handle_collision(a: 'Ball', b: 'Ball'):
        """Handles collision between balls with updating velocities

        Parameters:
            a (Ball): first ball
            b (Ball): second ball
        """
        # Distance between balls
        distance = Ball.distance(a, b)

        # Normal
        nx = (b.x - a.x) / distance
        ny = (b.y - a.y) / distance

        # Tangent
        tx = -ny
        ty = nx

        # Dot product normal
        dp_norm1 = a.vx * nx + a.vy * ny
        dp_norm2 = b.vx * nx + b.vy * ny

        # Conservation of momentum in 1D
        p1 = (dp_norm1 * (a.mass - b.mass) + 2 * b.mass * dp_norm2) / (a.mass + b.mass)
        p2 = (dp_norm2 * (b.mass - a.mass) + 2 * a.mass * dp_norm1) / (a.mass + b.mass)

        # Dot product tangent
        first_dp_tan = a.vx * tx + a.vy * ty
        second_dp_tan = b.vx * tx + b.vy * ty

        # Update ball velocities
        a.vx = tx * first_dp_tan + nx * p1
        a.vy = ty * first_dp_tan + ny * p1
        b.vx = tx * second_dp_tan + nx * p2
        b.vy = ty * second_dp_tan + ny * p2

        # Calculate balls overlap
        overlap = a.radius + b.radius - distance + Config.OVERLAP_EPS

        # Calculate the ratio of radii
        a_part = a.radius / (a.radius + b.radius)
        b_part = b.radius / (a.radius + b.radius)

        # Push balls away from each other
        a.x -= overlap * a_part * nx
        a.y -= overlap * a_part * ny
        b.x += overlap * b_part * nx
        b.y += overlap * b_part * ny

    @staticmethod
    def distance(a: 'Ball', b: 'Ball') -> float:
        """Calculates euclidean distance between balls

        Parameters:
            a (Ball): first ball
            b (Ball): second ball

        Returns:
            (float): euclidean distance
        """
        return hypot(a.x - b.x, a.y - b.y)

    @property
    def energy(self) -> float:
        """Calculates the kinetic energy of a moving ball

        Returns:
            (float): the kinetic energy in joules
        """
        return self.mass * (self.vx ** 2 + self.vy ** 2) / 2
