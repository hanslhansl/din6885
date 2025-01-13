from dataclasses import dataclass
from enum import IntEnum, auto

import din6885

@dataclass
class Passfeder(din6885._Passfeder):
    """Hohe Form"""

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
        
    form : Form

    def __post_init__(self):
        if 6 < self.d_1 <= 8:
            self.b = 2.
            self.h = 2.
            self.t_1 = 1.2
        elif self.d_1 <= 10:
            self.b = 3.
            self.h = 3.
            self.t_1 = 1.8
        elif self.d_1 <= 12:
            self.b = 4.
            self.h = 4.
            self.t_1 = 2.5
        elif self.d_1 <= 17:
            self.b = 5.
            self.h = 5.
            self.t_1 = 3.
        elif self.d_1 <= 22:
            self.b = 6.
            self.h = 6.
            self.t_1 = 3.5
        elif self.d_1 <= 30:
            self.b = 8.
            self.h = 7.
            self.t_1 = 4.
        elif self.d_1 <= 38:
            self.b = 10.
            self.h = 8.
            self.t_1 = 5.
        elif self.d_1 <= 44:
            self.b = 12.
            self.h = 8.
            self.t_1 = 5.
        elif self.d_1 <= 50:
            self.b = 14.
            self.h = 9.
            self.t_1 = 5.5
        elif self.d_1 <= 58:
            self.b = 16.
            self.h = 10.
            self.t_1 = 6.
        elif self.d_1 <= 65:
            self.b = 18.
            self.h = 11.
            self.t_1 = 7.
        elif self.d_1 <= 75:
            self.b = 20.
            self.h = 12.
            self.t_1 = 7.5
        elif self.d_1 <= 85:
            self.b = 22.
            self.h = 14.
            self.t_1 = 9.
        elif self.d_1 <= 95:
            self.b = 25.
            self.h = 14.
            self.t_1 = 9.
        elif self.d_1 <= 110:
            self.b = 28.
            self.h = 16.
            self.t_1 = 10.
        elif self.d_1 <= 130:
            self.b = 32.
            self.h = 18.
            self.t_1 = 11.
        elif self.d_1 <= 150:
            self.b = 36.
            self.h = 20.
            self.t_1 = 12.
        elif self.d_1 <= 170:
            self.b = 40.
            self.h = 22.
            self.t_1 = 13.
        elif self.d_1 <= 200:
            self.b = 45.
            self.h = 25.
            self.t_1 = 15.
        elif self.d_1 <= 230:
            self.b = 50.
            self.h = 28.
            self.t_1 = 17.
        elif self.d_1 <= 260:
            self.b = 56.
            self.h = 32.
            self.t_1 = 20.
        elif self.d_1 <= 290:
            self.b = 63.
            self.h = 32.
            self.t_1 = 20.
        elif self.d_1 <= 330:
            self.b = 70.
            self.h = 36.
            self.t_1 = 22.
        elif self.d_1 <= 380:
            self.b = 80.
            self.h = 40.
            self.t_1 = 25.
        elif self.d_1 <= 440:
            self.b = 90.
            self.h = 45.
            self.t_1 = 28.
        elif self.d_1 <= 500:
            self.b = 100.
            self.h = 50.
            self.t_1 = 31.
        else:
            raise ValueError("d_1 out of range")

    pass
