from din6885 import *

def test_1():
    assert din6885_1.Passfeder(140, 100, din6885_1.Passfeder.Form.A).b == 36
    
    assert din6885_1.Passfeder(45, 20, din6885_1.Passfeder.Form.B).h == 9
    
    assert din6885_1.Passfeder(70, 50, din6885_1.Passfeder.Form.AB).t_1 == 7.5

def test_2():
    assert din6885_2.Passfeder(140, 100, din6885_2.Passfeder.Form.A).b == 36
    
    assert din6885_2.Passfeder(45, 20, din6885_2.Passfeder.Form.C).h == 9
    
    assert din6885_2.Passfeder(70, 50, din6885_2.Passfeder.Form.E1).t_1 == 7.5

def test_3():
    assert din6885_3.Passfeder(140, 100, din6885_3.Passfeder.Form.A).b == 36
    
    assert din6885_3.Passfeder(45, 20, din6885_3.Passfeder.Form.B).h == 9
    
    assert din6885_3.Passfeder(70, 50, din6885_3.Passfeder.Form.E).t_1 == 7.5
