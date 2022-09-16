"""Module with configurations"""

from random import randint, uniform


class Config:
    """Configuration variables and random stats generators"""

    WIDTH = 1000
    HEIGHT = 650

    N_BALLS = 5

    BALL_MIN_RADIUS = 45
    BALL_MAX_RADIUS = 45

    BALL_MIN_X_COORD = 0
    BALL_MAX_X_COORD = WIDTH
    BALL_MIN_Y_COORD = 0
    BALL_MAX_Y_COORD = HEIGHT

    BALL_MIN_X_SPEED = 0
    BALL_MAX_X_SPEED = 4
    BALL_MIN_Y_SPEED = 0
    BALL_MAX_Y_SPEED = 4

    BALL_MIN_X_ACCELERATION = 1 - 1e-6
    BALL_MAX_X_ACCELERATION = 1 - 1e-6
    BALL_MIN_Y_ACCELERATION = 1 - 1e-6
    BALL_MAX_Y_ACCELERATION = 1 - 1e-6

    TIME_PER_DRAW = 1.0
    OVERLAP_EPS = 1e-3
    HANDLE_COLLISIONS = True

    FPS = 120
    TARGET_FPS = 120

    BACKGROUND_COLOR = (0, 0, 0)

    FONT_NAME = 'arial'
    FONT_SIZE = WIDTH // 45
    FONT_COLOR = (255, 255, 255)

    @classmethod
    @property
    def random_radius(cls) -> float:
        return uniform(cls.BALL_MIN_RADIUS, cls.BALL_MAX_RADIUS)

    @classmethod
    @property
    def random_color(cls) -> tuple:
        return tuple(randint(0, 255) for _ in range(3))

    @classmethod
    def get_random_x_coord(cls, radius: float) -> float:
        return cls._get_random_coord(
            cls.BALL_MIN_X_COORD,
            cls.BALL_MAX_X_COORD,
            radius,
        )

    @classmethod
    def get_random_y_coord(cls, radius: float) -> float:
        return cls._get_random_coord(
            cls.BALL_MIN_Y_COORD,
            cls.BALL_MAX_Y_COORD,
            radius,
        )

    @staticmethod
    def _get_random_coord(min_coord: float, max_coord: float, radius: float) -> float:
        return uniform(
            min_coord + radius + 1,
            max_coord - radius - 1,
        )

    @classmethod
    @property
    def random_x_speed(cls) -> float:
        return cls._get_random_speed(
            cls.BALL_MIN_X_SPEED,
            cls.BALL_MAX_X_SPEED,
        )

    @classmethod
    @property
    def random_y_speed(cls) -> float:
        return cls._get_random_speed(
            cls.BALL_MIN_Y_SPEED,
            cls.BALL_MAX_Y_SPEED,
        )

    @staticmethod
    def _get_random_speed(min_speed: float, max_speed: float) -> float:
        direction = (-1) ** randint(0, 1)
        return direction * uniform(
            min_speed,
            max_speed,
        )

    @classmethod
    @property
    def random_x_acceleration(cls) -> float:
        return uniform(
            cls.BALL_MIN_X_ACCELERATION,
            cls.BALL_MAX_X_ACCELERATION,
        )

    @classmethod
    @property
    def random_y_acceleration(cls) -> float:
        return uniform(
            cls.BALL_MIN_Y_ACCELERATION,
            cls.BALL_MAX_Y_ACCELERATION,
        )

    @staticmethod
    def _get_random_acceleration(min_acceleration: float, max_acceleration: float) -> float:
        return uniform(
            min_acceleration,
            max_acceleration,
        )
