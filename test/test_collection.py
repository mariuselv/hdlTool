import sys

sys.path.append('../src')

import pytest
from collection import Collection

def setup_function():
    global collection
    collection = Collection()

def tear_down_function():
    pass


def test_library():
    collection.set_library("test_library")
    library = collection.get_library()
    assert library == "test_library", "Expecting test_library"


def test_add_file():
    result = collection.add_file("file.vhd")
    assert result == False, "Expecting file do not exist"

    result = collection.add_file("../demo/bitvis_vip_sbi/sbi_bfm_pkg.vhd")
    assert result == True, "Expecting file exist"

    result = collection.add_file("../demo/bitvis_vip_sbi/sbi_bfm_pkg.vhd")
    assert result == False, "Expecting file previously added"

    result = collection.add_file("../demo/bitvis_vip_sbi/vvc_cmd_pkg.vhd")
    assert result == True, "Expecting file not previously added"


def test_add_files():
    result = collection.add_files("../demo/bitvis_vip_sbi/*.vhd")
    assert result == True, "Expecting files not previously added"

    result = collection.add_files("../demo/bitvis_vip_sbi/*.vhd")
    assert result == False, "Expecting files previously added"