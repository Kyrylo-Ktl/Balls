from random import randint, uniform


class Config:
    """"""

    WIDTH = 1000
    HEIGHT = 600

    N_BALLS = 15

    BALL_MIN_X_COORD = 0
    BALL_MAX_X_COORD = WIDTH

    BALL_MIN_Y_COORD = 0
    BALL_MAX_Y_COORD = HEIGHT

    BALL_MIN_X_SPEED = 0
    BALL_MAX_X_SPEED = 3

    BALL_MIN_Y_SPEED = 0
    BALL_MAX_Y_SPEED = 3

    BALL_MIN_RADIUS = 20
    BALL_MAX_RADIUS = 35

    BALL_X_ACCELERATION = 1 - 1e-5
    BALL_Y_ACCELERATION = 1 - 1e-5

    TIME_PER_DRAW = 1.0
    OVERLAP_EPS = 1e-3
    HANDLE_COLLISIONS = True

    FPS = 120
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
        return direction * uniform(min_speed, max_speed)

    @classmethod
    def get_random_x_coord(cls, radius: float) -> float:
        return cls._get_random_coord(cls.BALL_MIN_X_COORD, cls.BALL_MAX_X_COORD, radius)

    @classmethod
    def get_random_y_coord(cls, radius: float) -> float:
        return cls._get_random_coord(cls.BALL_MIN_Y_COORD, cls.BALL_MAX_Y_COORD, radius)

    @staticmethod
    def _get_random_coord(min_coord: float, max_coord: float, radius: float) -> float:
        return uniform(
            min_coord + radius + 1,
            max_coord - radius - 1,
        )
