"""Implementation of DIN 6885 - Drive type fastenings without taper action, parallel keys, keyways.

see https://github.com/hanslhansl/din6885."""


from dataclasses import dataclass
from enum import IntEnum, auto


@dataclass
class _Passfeder:
    """Implementation"""

    class Form(IntEnum):
        A = auto()
        """rundstirnig"""
        B = auto()
        """geradstirnig"""
        AB = auto()
        """rund-geradstirnig"""
        C = auto()
        """rundstirnig (ab 8x7 mit Bohrung für eine Halteschraube über der Stufenlinie)"""
        D = auto()
        """geradstirnig (ab 8x7 mit Bohrung für eine Halteschraube über der Stufenlinie)"""
        E1 = auto()
        """rundstirnig, 8x7 und 10x8 (mit Bohrungen für zwei Halteschrauben unter der Stufenlinie)"""
        E2 = auto()
        """rundstirnig (mit Bohrungen für zwei Halteschrauben unter der Stufenlinie ab 12x8 zusätzlich mit Gewindebohrung für eine oder zwei Abdrückschrauben)"""
        F1 = auto()
        """geradstirnig, 8x7 und 10x8 (mit Bohrungen für zwei Halteschrauben unter der Stufenlinie)"""
        F2 = auto()
        """geradstirnig (mit Bohrungen für zwei Halteschrauben unter der Stufenlinie ab 12x8 zusätzlich mit Gewindebohrung für eine oder zwei Abdrückschrauben)"""
        G = auto()
        """geradstirnig mit Schrägung und Bohrung für eine Halteschraube"""
        H = auto()
        """geradstirnig mit Schrägung und Bohrungen für zwei Halteschrauben"""
        J = auto()
        """geradstirnig mit Schrägung und Bohrung für eine Spannhülse"""

    d_1 : float
    l : float
    form : Form

    b : float
    h : float
    t_1 : float


from . import din6885_1
from . import din6885_2
from . import din6885_3


