import status_check

#test status_check.mp_elig
#test status_check.senator_elig

def test_mp_elig():
    assert status_check.mp_elig(True, 20)
    assert not status_check.mp_elig(False, 70)
    assert not status_check.mp_elig(True, 17)



def test_senator_elig():
    assert False