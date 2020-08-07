import sys

sys.path.append('../src')

import pytest
from vhd import VHD

def setup_function():
    global vhd
    vhd = VHD("my_vhd_file.vhd")

def tear_down_function():
    pass


def test_get_filename():
    filename = vhd.get_filename()
    assert filename == "my_vhd_file.vhd", "Expecting init filename"
