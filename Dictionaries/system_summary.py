import platform

my_comp_info = {}

# Add OS info
pc_info = platform.uname()
my_comp_info['OS'] = pc_info.system + ' ' + pc_info.version
my_comp_info['CPU'] = pc_info.processor + ' ' + pc_info.machine
my_comp_info['System Name'] = pc_info.node



print(my_comp_info)