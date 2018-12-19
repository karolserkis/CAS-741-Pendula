import pytest
import numpy as np
import unittest
#import sim

# -------------------------------
# Test cases
# -------------------------------

#@pytest.mark.parametrize("test_case", test_cases)

#def test_input_argparse(cmdopt):
#    if links > 5:
#        print("Too many pendula for display")
#    elif links < 1:
#        print("Number of pendula must be positive integer")
#    assert 0  # to see what was printed

#if __name__ == '__main__':
#    unittest.main()

import argparse

#def test_required_unknown(capsys):
def test_required_unknown():
    """ Try to perform sweep on something that isn't an option. """
    parser=argparse.ArgumentParser()
    parser.add_argument(
        '--nlinks', metavar='N',
        type=int,
        default=1,
        required=True)
    args = ["--nlinks", "NADA"]

    with pytest.raises(SystemExit):
        parser.parse_args(args)

@pytest.fixture
def nlinks(request):
    return request.config.getoption("--nlinks")

import time


def test_funcfast():
    time.sleep(0.1)


def test_funcslow1():
    time.sleep(0.2)


def test_funcslow2():
    time.sleep(0.3)

@pytest.mark.parametrize('test_input,expected', [
    ('3+5', 8),
    pytest.param('1+7', 8,
                 marks=pytest.mark.basic),
    pytest.param('2+4', 6,
                 marks=pytest.mark.basic,
                 id='basic_2+4'),
    pytest.param('6*9', 42,
                 marks=[pytest.mark.basic, pytest.mark.xfail],
                 id='basic_6*9'),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

#    stderr = capsys.readouterr().err
#    assert 'invalid choice' in stderr

##def pytest_addoption(parser):
#def test_funcfast():
#    time.sleep(0.1)

#def test_funcslow1():
#    time.sleep(0.2)

#def test_funcslow2():
#    time.sleep(0.3)
