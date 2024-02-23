import pytest
from extract_position import extract_position


def test_extract_position():
    position = extract_position(
        '|update| the positron location in the particle accelerator is x:21.432')
    assert position == '21.432'


def test_extract_position_error():
    position = extract_position(
        '|error| the positron location in the particle accelerator is x:21.432')
    assert position == None


def test_extract_position_debug():
    position = extract_position(
        '|debug| the positron location in the particle accelerator is x:21.432')
    assert position == None


def test_extract_position_no_pos():
    position = extract_position(
        '|update| the positron location in the particle accelerator is y:21.432')
    assert position == None
