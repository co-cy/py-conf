from pyliteconf import Config as _Config
from time import time


class FuncArgConfig(_Config):
    """More parameters at this link..."""

    arg_1 = "1"
    arg_2 = "1"
    arg_3 = "1"

    arg_4 = str(123 + time())

    @classmethod
    def __new_arg_1__(cls):
        cls.arg_1 += '1'
