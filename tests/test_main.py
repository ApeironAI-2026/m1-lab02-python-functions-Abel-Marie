import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import calculate_area

def test_calculate_area():
    assert calculate_area(5, 10) == 50, "Failed input (5, 10)"
    assert calculate_area(7, 3) == 21, "Failed input (7, 3)"
    print("All tests passed!")