from Packet_for_lesson5 import is_simple_number

def test_is_simple_number():
    assert is_simple_number(3)==True
    assert is_simple_number(4)==False
    assert is_simple_number(10)==False


from Packet_for_lesson5 import print_factors

def test_print_factors():
    assert print_factors(6)==[1,2,3,6]
    assert print_factors(7)==[1,7]

from Packet_for_lesson5 import max_divider

def test_max_divider():
    assert max_divider(8,44)==4
    assert max_divider(10,56)==2

