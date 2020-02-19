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
    uart_col.add_files("test/uvvm_vvc_framework/src_target_dependent/*.vhd")
    uart_col.organize_collection()

    # Create VIP SBI collection
    sbi_col = ht.collection()
    sbi_col.set_library("bitvis_vip_sbi")
    sbi_col.add_files("test/bitvis_vip_sbi/*.vhd")
    sbi_col.add_files("test/uvvm_vvc_framework/src_target_dependent/*.vhd")
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
    #fw_col.add_files("test/uvvm_vvc_framework/src_target_dependent/*.vhd")
    fw_col.organize_collection()
    
    # Create VIP clock generator collection
    cg_col = ht.collection()
    cg_col.set_library("bitvis_vip_clock_generator")
    cg_col.add_files("test/bitvis_vip_clock_generator/*.vhd")
    cg_col.add_files("test/uvvm_vvc_framework/src_target_dependent/*.vhd")
    cg_col.organize_collection()

    # Create UART DUT collection
    uart_dut = ht.collection()
    uart_dut.set_library("bitvis_uart")
    uart_dut.add_files("test/bitvis_uart/*.vhd")
    uart_dut.organize_collection()

    # List compile order in each collection
    uart_col.list_compile_order()
    sbi_col.list_compile_order()
    sb_col.list_compile_order()
    util_col.list_compile_order()
    fw_col.list_compile_order()
    cg_col.list_compile_order()
    uart_dut.list_compile_order()

    # Add all collections to HDL Tool
    ht.add_collection(sb_col)
    ht.add_collection(sbi_col)
    ht.add_collection(fw_col)
    ht.add_collection(util_col)
    ht.add_collection(uart_col)
    ht.add_collection(cg_col)
    ht.add_collection(uart_dut)

    # Sort collections in required compile order
    ht.organize_collection()

    # List required library compiled order
    ht.list_compile_order()


    ht.compile_collection()


    # Defining testbench
    tb = ht.add_testbench("tb/demo_tb.vhd", verbose=True)
    tb.set_harness("tb/demo_th.vhd")
    tb.set_library("bitvis_vip_uart")
    tb.set_entity("demo_tb")
    tb.add_generic("GC_TEST", "test_error_injection")
    tb.add_generic("GC_TEST", "test_randomise")
    tb.add_generic("GC_TEST", "test_protocol_checker")
    tb.add_generic("GC_TEST", "test_activity_watchdog")
    tb.add_generic("GC_TEST", "test_simple_watchdog")
    
    tb.run_testbench()


if __name__ == "__main__":
    main()

