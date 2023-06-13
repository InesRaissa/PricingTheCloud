from vmClass import VM
import json


"""This function retrieves vm objects, their parameters and their associated links from a .ini config file."""
# Retrieving elements from configuration file

# Extracting VM objects from config file
def get_vms_from_jsonConfigFile(config):
    vms = []
    for vm_data in config["vms"]:
        id=None
        cpu = vm_data["cpu"]
        memory = vm_data["memory"]
        hourrate=None
        location = vm_data["location"]
        csp = vm_data["csp"]
        processingtime = vm_data["processing_time"]
        vm = VM(id, cpu, memory, hourrate, location, csp, processingtime)
        vms.append(vm)
    return vms

# Extracting established links between VMs from config file
def get_establish_links_from_jsonConfigFile(vms, config):
    for i, vm in enumerate(vms):
        for link_data in config["vms"][i]["links"]:
            link_vm_num = link_data["vm"]
            data_rate = link_data["data_rate"]
            linked_vm = vms[link_vm_num - 1]
            vm.add_link(linked_vm, data_rate)




#the main



























"""This class encompasses the parser class and more elaborated vms"""

"""e.g. of config file.json

{
  "vms": [
    {
      "cpu": 2,
      "memory": 4,
      "csp": "aws",
      "location": "us-west-1",
      "links": [
        {
          "vm": 2,
          "data_rate": 100
        },
        {
          "vm": 3,
          "data_rate": 50
        }
      ]
    },
    {
      "cpu": 4,
      "memory": 8,
      "csp": "aws",
      "location": "us-east-1",
      "links": [
        {
          "vm": 1,
          "data_rate": 100
        },
        {
          "vm": 4,
          "data_rate": 75
        }
      ]
    },
    {
      "cpu": 4,
      "memory": 16,
      "csp": "azure",
      "location": "westus",
      "links": [
        {
          "vm": 1,
          "data_rate": 50
        }
      ]
    },
    {
      "cpu": 8,
      "memory": 32,
      "csp": "azure",
      "location": "eastus",
      "links": [
        {
          "vm": 2,
          "data_rate": 75
        }
      ]
    }
  ]
}









"""





    
    