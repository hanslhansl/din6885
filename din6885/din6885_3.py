from dataclasses import dataclass
from enum import IntEnum, auto

import din6885

@dataclass
class Passfeder(din6885._Passfeder):
    """Niedrige Form"""

    class Form(IntEnum):
        A = auto()
        """rundstirnig"""
        B = auto()
        """geradstirnig"""
        C = auto()
        """rundstirnig (ab 8x5 mit Bohrung für eine Halteschraube über der Stufenlinie)"""
        E = auto()
        """rundstirnig (mit Bohrungen für zwei Halteschrauben und 1 oder 2 Abdrückschrauben)"""
        
    form : Form

    def __post_init__(self):
        pass
