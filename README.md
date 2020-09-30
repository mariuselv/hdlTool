HDLTool is a program that will help running VHDL simulations:

- [X] Automatic dependency detection
- [X] Compiling 
- [X] Configuring tests
- [X] Running simulations
- [ ] Advanced testbench generics

**NOTE** not all features are implemented yet

**WARNING** this project is in development


**Demo setup:**
```python
import sys
sys.path.insert(0, 'src')
  
from hdlTool import HdlTool as Ht

def main():

    ht = Ht()
  
    # Create VIP UART collection
    uart_col = ht.collection()
    uart_col.set_library("bitvis_vip_uart")
    uart_col.add_files("demo/bitvis_vip_uart/*.vhd")
    uart_col.add_files("demo/uvvm_vvc_framework/src_target_dependent/*.vhd")
    uart_col.organize_collection()
  
    # Create VIP SBI collection
    sbi_col = ht.collection()
    sbi_col.set_library("bitvis_vip_sbi")
    sbi_col.add_files("demo/bitvis_vip_sbi/*.vhd")
    sbi_col.add_files("demo/uvvm_vvc_framework/src_target_dependent/*.vhd")
    sbi_col.organize_collection()
  
    # Create VIP Scoreboard collection
    sb_col = ht.collection()
    sb_col.set_library("bitvis_vip_scoreboard")
    sb_col.add_files("demo/bitvis_vip_scoreboard/*.vhd")
    sb_col.organize_collection()
  
    # Create Util collection
    util_col = ht.collection()
    util_col.set_library("uvvm_util")
    util_col.add_files("demo/uvvm_util/*.vhd")
    util_col.organize_collection()
  
    # Create VVC Framework collection
    fw_col = ht.collection()
    fw_col.set_library("uvvm_vvc_framework")
    fw_col.add_files("demo/uvvm_vvc_framework/src/*.vhd")
    fw_col.organize_collection()
  
    # List compile order in each collection
    uart_col.list_compile_order()
    sbi_col.list_compile_order()
    sb_col.list_compile_order()
    util_col.list_compile_order()
    fw_col.list_compile_order()
  
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
```



**Demo output:**
```console
√ hdlTool % py ht.py 

================================ bitvis_vip_uart ================================
[1] File: demo/bitvis_vip_uart/uart_bfm_pkg.vhd (PACKAGE: uart_bfm_pkg)
[2] File: demo/bitvis_vip_uart/transaction_pkg.vhd (PACKAGE: transaction_pkg)
[3] File: demo/bitvis_vip_uart/vvc_cmd_pkg.vhd (PACKAGE: vvc_cmd_pkg)
[4] File: demo/bitvis_vip_uart/monitor_cmd_pkg.vhd (PACKAGE: monitor_cmd_pkg)
[5] File: demo/uvvm_vvc_framework/src_target_dependent/td_target_support_pkg.vhd (PACKAGE: td_target_support_pkg)
[6] File: demo/uvvm_vvc_framework/src_target_dependent/td_queue_pkg.vhd (PACKAGE: td_cmd_queue_pkg)
[7] File: demo/bitvis_vip_uart/vvc_methods_pkg.vhd (PACKAGE: vvc_methods_pkg)
[8] File: demo/bitvis_vip_uart/uart_monitor.vhd (ENTITY: uart_monitor)
[9] File: demo/uvvm_vvc_framework/src_target_dependent/td_vvc_framework_common_methods_pkg.vhd (PACKAGE: td_vvc_framework_common_methods_pkg)
[10] File: demo/uvvm_vvc_framework/src_target_dependent/td_vvc_entity_support_pkg.vhd (PACKAGE: td_vvc_entity_support_pkg)
[11] File: demo/bitvis_vip_uart/uart_rx_vvc.vhd (ENTITY: uart_rx_vvc)
[12] File: demo/bitvis_vip_uart/vvc_context.vhd (CONTEXT: vvc_context)
[13] File: demo/bitvis_vip_uart/uart_tx_vvc.vhd (ENTITY: uart_tx_vvc)
[14] File: demo/bitvis_vip_uart/uart_vvc.vhd (ENTITY: uart_vvc)

================================ bitvis_vip_sbi ================================
[1] File: demo/bitvis_vip_sbi/sbi_bfm_pkg.vhd (PACKAGE: sbi_bfm_pkg)
[2] File: demo/bitvis_vip_sbi/transaction_pkg.vhd (PACKAGE: transaction_pkg)
[3] File: demo/bitvis_vip_sbi/vvc_cmd_pkg.vhd (PACKAGE: vvc_cmd_pkg)
[4] File: demo/uvvm_vvc_framework/src_target_dependent/td_target_support_pkg.vhd (PACKAGE: td_target_support_pkg)
[5] File: demo/uvvm_vvc_framework/src_target_dependent/td_vvc_framework_common_methods_pkg.vhd (PACKAGE: td_vvc_framework_common_methods_pkg)
[6] File: demo/uvvm_vvc_framework/src_target_dependent/td_queue_pkg.vhd (PACKAGE: td_cmd_queue_pkg)
[7] File: demo/bitvis_vip_sbi/vvc_methods_pkg.vhd (PACKAGE: vvc_methods_pkg)
[8] File: demo/bitvis_vip_sbi/vvc_context.vhd (CONTEXT: vvc_context)
[9] File: demo/uvvm_vvc_framework/src_target_dependent/td_vvc_entity_support_pkg.vhd (PACKAGE: td_vvc_entity_support_pkg)
[10] File: demo/bitvis_vip_sbi/sbi_vvc.vhd (ENTITY: sbi_vvc)

================================ bitvis_vip_scoreboard ================================
[1] File: demo/bitvis_vip_scoreboard/generic_sb_support_pkg.vhd (PACKAGE: generic_sb_support_pkg)
[2] File: demo/bitvis_vip_scoreboard/generic_sb_pkg.vhd (PACKAGE: generic_sb_pkg)
[3] File: demo/bitvis_vip_scoreboard/predefined_sb.vhd (PACKAGE: local_pkg)

================================ uvvm_util ================================
[1] File: demo/uvvm_util/types_pkg.vhd (PACKAGE: types_pkg)
[2] File: demo/uvvm_util/adaptations_pkg.vhd (PACKAGE: adaptations_pkg)
[3] File: demo/uvvm_util/string_methods_pkg.vhd (PACKAGE: string_methods_pkg)
[4] File: demo/uvvm_util/protected_types_pkg.vhd (PACKAGE: protected_types_pkg)
[5] File: demo/uvvm_util/global_signals_and_shared_variables_pkg.vhd (PACKAGE: global_signals_and_shared_variables_pkg)
[6] File: demo/uvvm_util/hierarchy_linked_list_pkg.vhd (PACKAGE: hierarchy_linked_list_pkg)
[7] File: demo/uvvm_util/license_pkg.vhd (PACKAGE: license_pkg)
[8] File: demo/uvvm_util/alert_hierarchy_pkg.vhd (PACKAGE: alert_hierarchy_pkg)
[9] File: demo/uvvm_util/methods_pkg.vhd (PACKAGE: methods_pkg)
[10] File: demo/uvvm_util/bfm_common_pkg.vhd (PACKAGE: bfm_common_pkg)
[11] File: demo/uvvm_util/uvvm_util_context.vhd (CONTEXT: uvvm_util_context)

================================ uvvm_vvc_framework ================================
[1] File: demo/uvvm_vvc_framework/src/ti_data_queue_pkg.vhd (PACKAGE: ti_data_queue_pkg)
[2] File: demo/uvvm_vvc_framework/src/ti_protected_types_pkg.vhd (PACKAGE: ti_protected_types_pkg)
[3] File: demo/uvvm_vvc_framework/src/ti_data_fifo_pkg.vhd (PACKAGE: ti_data_fifo_pkg)
[4] File: demo/uvvm_vvc_framework/src/ti_vvc_framework_support_pkg.vhd (PACKAGE: ti_vvc_framework_support_pkg)
[5] File: demo/uvvm_vvc_framework/src/ti_uvvm_engine.vhd (ENTITY: ti_uvvm_engine)
[6] File: demo/uvvm_vvc_framework/src/ti_generic_queue_pkg.vhd (PACKAGE: ti_generic_queue_pkg)
[7] File: demo/uvvm_vvc_framework/src/ti_data_stack_pkg.vhd (PACKAGE: ti_data_stack_pkg)

================================ HDL Tool ================================
[1] Lib: uvvm_util
[2] Lib: uvvm_vvc_framework
[3] Lib: bitvis_vip_scoreboard
[4] Lib: bitvis_vip_sbi
[5] Lib: bitvis_vip_uart

Generating: sim/compiler.do
```
