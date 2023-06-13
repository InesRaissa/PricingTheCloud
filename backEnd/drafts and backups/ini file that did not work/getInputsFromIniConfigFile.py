from vmClassForConfigFile import VM
import configparser

"""This function retrieves vm objects, their parameters and their associated links from a .ini config file."""


# Extracting VM objects from .ini config file
def get_vms_from_iniConfigFile(config):
    vm_list = []
    vm_count = config.getint('General', 'VMCount')

    print("Printing vm parameters before VM research (optional):")

    for i in range(1, vm_count + 1):
        section_name = 'VM{}'.format(i)
        id=None
        cpu = config.get(section_name, 'CPU')
        memory = config.get(section_name, 'Memory')
        hourrate=None
        location = config.get(section_name, 'Location')
        csp = config.get(section_name, 'CSP')
        processtime = config.get(section_name, 'Processing time')

        vm = VM(id, cpu, memory, hourrate, location, csp, processtime)
        vm_list.append(vm)

        # Printing VM parameters before database research
        """print(f"vm id: {vm.id}")
        print(f"cpu: {vm.cpu}")
        print(f"memory: {vm.memory}")
        print(f"hour rate: {vm.hourrate}")
        print(f"location: {vm.location}")
        print(f"csp: {vm.csp}")
        print(f"processing time: {vm.processingtime}")
        
        print(f"\n")"""

    return vm_list

# Extracting established links between VMs from .ini config file
def get_correspondingLinks_from_iniConfigFile(vm_list, config):
    
    config = configparser.ConfigParser()
    for i, vm in enumerate(vm_list):
        section_name = 'VM{}'.format(i + 1)
        links = config.get(section_name, 'Links').split(',')
        for link in links:
            link_vm_num, data_rate = link.strip().split(':')
            link_vm_num = int(link_vm_num)
            linked_vm = vm_list[link_vm_num - 1]
            vm.add_link(linked_vm, data_rate)



#testing these functions here

 # Read configuration from file
    
#config = configparser.ConfigParser()
config = configparser.ConfigParser()
config.read('config.ini')

# Create VMs based on the configuration
vm_list = get_vms_from_iniConfigFile(config)

print("Printing vm parameters")
for i, vm in enumerate(vm_list):
    print(f"vm id: {vm.id}")
    print(f"cpu: {vm.cpu}")
    print(f"memory: {vm.memory}")
    print(f"hour rate: {vm.hourrate}")
    print(f"location: {vm.location}")
    print(f"csp: {vm.csp}")
    print(f"processing time: {vm.processingtime}")
        
    print(f"\n")

# Establish links between VMs
print("establishing vm list with corresponding lists...\n")
get_correspondingLinks_from_iniConfigFile(config, vm_list)

for i, vm in enumerate(vm_list):
    print(f"new vm id: {vm.id}")
    print(f"new cpu: {vm.cpu}")
    print(f"new memory: {vm.memory}")
    print(f"new hour rate: {vm.hourrate}")
    print(f"new location: {vm.location}")
    print(f"new csp: {vm.csp}")
    print(f"new processing time: {vm.processingtime}")
        
    print(f"\n")

























"""e.g. of config file.ini

[General]
VMCount = 4

[VM1]
CPU = 2
Memory = 4
CSP = aws
Location = us-west-1
Links = 2:100, 3:50

[VM2]
CPU = 4
Memory = 8
CSP = aws
Location = us-east-1
Links = 1:100, 4:75

[VM3]
CPU = 4
Memory = 16
CSP = azure
Location = westus
Links = 1:50

[VM4]
CPU = 8
Memory = 32
CSP = azure
Location = eastus
Links = 2:75



"""





    
    