import pytest
import math
from unittest.mock import patch
from calculate_grades import *


@patch('builtins.input', side_effect=['78', '89', '91', '68', '95'])
def test_user_input(mock_input):
    assert read_input() == [78, 89, 91, 68, 95]


def test_calculate_stat():
    grades = [78, 89, 91, 68]
    mean, sd = calculate_stat(grades)
    assert mean == 81.5
    assert math.isclose(sd, 9.2330927, abs_tol=1e-3)


@patch('builtins.input', side_effect=['78', '89', '91', '68', '95'])
def test_display_grade_stat(mock_input, capsys):
    display_grade_stat()
    output = capsys.readouterr()
    assert '****** Grade Statistics ******' in output.out
    assert "The grades's mean is: 84.2" in output.out
    assert "The population standard deviation of grades is:  9.867" in output.out
    assert "****** END ******" in output.out
