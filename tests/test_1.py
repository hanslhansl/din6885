import din6885

def test_1():
    assert din6885.PassfederHoheForm(140, 100, din6885.Passfeder.Form.A).b == 36
    
    assert din6885.PassfederHoheForm(45, 20, din6885.Passfeder.Form.B).h == 9
    
    assert din6885.PassfederHoheForm(70, 50, din6885.Passfeder.Form.AB).t_1 == 7.5

def test_2():
    assert din6885.PassfederHoheFormFürWerkzeugmaschinen(140, 100, din6885.Passfeder.Form.A).b == 36
    
    assert din6885.PassfederHoheFormFürWerkzeugmaschinen(45, 20, din6885.Passfeder.Form.C).h == 9
    
    assert din6885.PassfederHoheFormFürWerkzeugmaschinen(70, 50, din6885.Passfeder.Form.E1).t_1 == 7.5

def test_3():
    assert din6885.PassfederNiedrigeForm(140, 100, din6885.Passfeder.Form.A).b == 36
    
    assert din6885.PassfederNiedrigeForm(45, 20, din6885.Passfeder.Form.B).h == 9
    
    assert din6885.PassfederNiedrigeForm(70, 50, din6885.Passfeder.Form.E).t_1 == 7.5
