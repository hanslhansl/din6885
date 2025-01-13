from dataclasses import dataclass
from enum import IntEnum, auto

import din6885

@dataclass
class Passfeder(din6885._Passfeder):
    """Hohe Form für Werkzeugmaschinen"""

    class Form(IntEnum):
        A = auto()
        """rundstirnig"""
        C = auto()
        """rundstirnig (ab 8x7 mit Bohrung für eine Halteschraube über der Stufenlinie)"""
        E1 = auto()
        """rundstirnig, 8x7 und 10x8 (mit Bohrungen für zwei Halteschrauben unter der Stufenlinie)"""
        E2 = auto()
        """rundstirnig (mit Bohrungen für zwei Halteschrauben unter der Stufenlinie ab 12x8 zusätzlich mit Gewindebohrung für eine oder zwei Abdrückschrauben)"""
        
    form : Form


    def __post_init__(self):
        pass
