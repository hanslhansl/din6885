"""Implementation of DIN 6885 - Drive type fastenings without taper action, parallel keys, keyways.

see https://github.com/hanslhansl/din6885."""


from dataclasses import dataclass


@dataclass
class _Passfeder:
    """Implementation"""

    d_1 : float
    l : float


from . import din6885_1
from . import din6885_2
from . import din6885_3


