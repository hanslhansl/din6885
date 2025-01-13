import din6885

class Passfeder(din6885._Passfeder):
    """Hohe Form für Werkzeugmaschinen"""

    def __init__(self, d_1 : float, l : float, form : din6885._Passfeder.Form):
        assert self.form in (Passfeder.Form.A, Passfeder.Form.C, Passfeder.Form.E1, Passfeder.Form.E2)
