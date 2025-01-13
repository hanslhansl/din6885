"""Implementation of DIN 6885 - Drive type fastenings without taper action, parallel keys, keyways.

see https://github.com/hanslhansl/din6885."""


from dataclasses import dataclass
from enum import IntEnum, auto


@dataclass
class Passfeder:
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

class PassfederHoheForm(Passfeder):
    """Hohe Form"""

    def __init__(self, d_1 : float, l : float, form : Passfeder.Form):
        if 6 < d_1 <= 8:
            b = 2.
            h = 2.
            t_1 = 1.2
        elif d_1 <= 10:
            b = 3.
            h = 3.
            t_1 = 1.8
        elif d_1 <= 12:
            b = 4.
            h = 4.
            t_1 = 2.5
        elif d_1 <= 17:
            b = 5.
            h = 5.
            t_1 = 3.
        elif d_1 <= 22:
            b = 6.
            h = 6.
            t_1 = 3.5
        elif d_1 <= 30:
            b = 8.
            h = 7.
            t_1 = 4.
        elif d_1 <= 38:
            b = 10.
            h = 8.
            t_1 = 5.
        elif d_1 <= 44:
            b = 12.
            h = 8.
            t_1 = 5.
        elif d_1 <= 50:
            b = 14.
            h = 9.
            t_1 = 5.5
        elif d_1 <= 58:
            b = 16.
            h = 10.
            t_1 = 6.
        elif d_1 <= 65:
            b = 18.
            h = 11.
            t_1 = 7.
        elif d_1 <= 75:
            b = 20.
            h = 12.
            t_1 = 7.5
        elif d_1 <= 85:
            b = 22.
            h = 14.
            t_1 = 9.
        elif d_1 <= 95:
            b = 25.
            h = 14.
            t_1 = 9.
        elif d_1 <= 110:
            b = 28.
            h = 16.
            t_1 = 10.
        elif d_1 <= 130:
            b = 32.
            h = 18.
            t_1 = 11.
        elif d_1 <= 150:
            b = 36.
            h = 20.
            t_1 = 12.
        elif d_1 <= 170:
            b = 40.
            h = 22.
            t_1 = 13.
        elif d_1 <= 200:
            b = 45.
            h = 25.
            t_1 = 15.
        elif d_1 <= 230:
            b = 50.
            h = 28.
            t_1 = 17.
        elif d_1 <= 260:
            b = 56.
            h = 32.
            t_1 = 20.
        elif d_1 <= 290:
            b = 63.
            h = 32.
            t_1 = 20.
        elif d_1 <= 330:
            b = 70.
            h = 36.
            t_1 = 22.
        elif d_1 <= 380:
            b = 80.
            h = 40.
            t_1 = 25.
        elif d_1 <= 440:
            b = 90.
            h = 45.
            t_1 = 28.
        elif d_1 <= 500:
            b = 100.
            h = 50.
            t_1 = 31.
        else:
            raise ValueError("d_1 out of range")

        super().__init__(d_1, l, form, b, h, t_1)

class PassfederHoheFormFürWerkzeugmaschinen(Passfeder):
    """Hohe Form für Werkzeugmaschinen"""

    def __init__(self, d_1 : float, l : float, form : Passfeder.Form):
        assert self.form in (Passfeder.Form.A, Passfeder.Form.C, Passfeder.Form.E1, Passfeder.Form.E2)

        raise NotImplementedError

class PassfederNiedrigeForm(Passfeder):
    """Niedrige Form"""

    def __init__(self, d_1 : float, l : float, form : Passfeder.Form):
        assert self.form in (Passfeder.Form.A, Passfeder.Form.B, Passfeder.Form.C, Passfeder.Form.E1, Passfeder.Form.E2)

        raise NotImplementedError

class PassfederFoo:
    pass