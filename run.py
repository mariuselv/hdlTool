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

from hdl_tool import Hdl_tool as Ht

def main():

    ht = Ht()

    # Create VIP UART collection
    uart_col = ht.collection()
    uart_col.set_library("bitvis_vip_uart")
    uart_col.add_files("test/bitvis_vip_uart/*.vhd")
    uart_col.organize_collection()

    # Create VIP SBI collection
    sbi_col = ht.collection()
    sbi_col.set_library("bitvis_vip_sbi")
    sbi_col.add_files("test/bitvis_vip_sbi/*.vhd")
    sbi_col.organize_collection()

    # Create VIP Scoreboard collection
    sb_col = ht.collection()
    sb_col.set_library("bitvis_vip_scoreboard")
    sb_col.add_files("test/bitvis_vip_scoreboard/*.vhd")
    sb_col.organize_collection()

    # Create Util collection
    util_col = ht.collection()
    util_col.set_library("uvvm_util")
    util_col.add_files("test/uvvm_util/*.vhd")
    util_col.organize_collection()

    # Create VVC Framework collection
    fw_col = ht.collection()
    fw_col.set_library("uvvm_vvc_framework")
    fw_col.add_files("test/uvvm_vvc_framework/src/*.vhd")
    fw_col.add_files("test/uvvm_vvc_framework/src_target_dependent/*.vhd")
    fw_col.organize_collection()


    # List compile order in each collection
    #uart_col.list_compile_order()
    #sbi_col.list_compile_order()
    #sb_col.list_compile_order()
    #util_col.list_compile_order()
    #fw_col.list_compile_order()

    # Add all collections to HDL Tool
    ht.add_collection(sb_col)
    ht.add_collection(sbi_col)
    ht.add_collection(fw_col)
    ht.add_collection(util_col)
    ht.add_collection(uart_col)

    # Sort collections in required compile order
    ht.organize_collection()

    # List required library compiled order
    ht.list_compile_order()


    ht.compile_collection()





if __name__ == "__main__":
    main()

