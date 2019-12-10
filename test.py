"""
========================================================
    Filename: hdl_tool.py
    Author: Marius Elvegård
    Description:

    (c) 2019 Marius Elvegård
========================================================
"""

import sys
sys.path.insert(0, 'src')

from hdl_tool import Hdl_tool

def main():

    tool = Hdl_tool()

    # Create a collection and add to list
    collection = tool.collection()
    collection.set_library("bitvis_vip_uart")
    collection.add_files("test/bitvis_vip_uart/*.vhd")
    collection.organize()
    collection.list_compile_order()

    tool.add_collection(collection)

    collection = tool.collection()
    collection.set_library("bitvis_vip_sbi")
    collection.add_files("test/bitvis_vip_sbi/*.vhd")
    collection.organize()
    collection.list_compile_order()

    tool.add_collection(collection)

    collection = tool.collection()
    collection.set_library("bitvis_vip_scoreboard")
    collection.add_files("test/bitvis_vip_scoreboard/*.vhd")
    collection.organize()
    collection.list_compile_order()

    tool.add_collection(collection)

    collection = tool.collection()
    collection.set_library("uvvm_util")
    collection.add_files("test/uvvm_util/*.vhd")
    collection.organize()
    collection.list_compile_order()

    tool.add_collection(collection)

    collection = tool.collection()
    collection.set_library("uvvm_vvc_framework")
    collection.add_files("test/uvvm_vvc_framework/src/*.vhd")
    collection.add_files("test/uvvm_vvc_framework/src_target_dependent/*.vhd")
    collection.organize()
    collection.list_compile_order()

    tool.add_collection(collection)


    tool.organize()
    tool.list_compile_order()


if __name__ == "__main__":
    main()