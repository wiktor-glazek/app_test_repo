from  stepikApp.py import sumInts

def test_sumInts():
    assert sumInts(5,5) == 10
    assert sumInts(0,0) == 0
    assert sumInts(-5,5) == 0
