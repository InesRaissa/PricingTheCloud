#import psycopg2
from vmClassForConfigFile import VM
#from operator import mul
import json
from totalOperationalCost import get_total_operational_cost
from FindTheBestVmFromDbConfigF import find_TheBestVm_in_db
from totalNetworkCost import get_total_network_cost
from getInputsFromJsonConfigFile import get_vms_from_jsonConfigFile
from getInputsFromJsonConfigFile import get_establish_links_from_jsonConfigFile


#This is the main function (vm_list entered by the end user and vm_list after the selection)  

def main():
    
   #initialising all the variables 
    vmList_beforeDbSearch = []
    vmList_afterDbSearch=[]
    #opcost_vm=0
    total_operational_cost=0
    total_network_cost=0
    total_cost=0

    
        # Read configuration from file
    with open('configFile.json') as config_file:
        config = json.load(config_file)

    # Extracting VMs (without their links) and their parameters from the json configuration file and return them in a list
    vmList_beforeDbSearch = get_vms_from_jsonConfigFile(config)

    for i, vm in enumerate(vmList_beforeDbSearch):

        #Looking for corresponding vms in the database...
        vm_afterDb=find_TheBestVm_in_db(vm)

        #assigning corresponding processing times values to the vms chosen from the db
        vm_afterDb.processingtime= vm.processingtime
        

        vmList_afterDbSearch.append(vm_afterDb)

    print("Printing vmList after DB search with good processing time")

    for i, vm in enumerate(vmList_beforeDbSearch):

        print(f"  afterDbSearch vm id: {vm.id}")
        print(f" cpu: {vm.cpu}")
        print(f" memory: {vm.memory}")
        print(f" hour rate: {vm.hourrate}")
        print(f" location: {vm.location}")
        print(f" csp: {vm.csp}")
        print(f" processing time: {vm.processingtime}")
        print(f" links: {vm.links}")
        print(f"\n")

        
        
        

    # Adding Established links between VMs from Json config file
    get_establish_links_from_jsonConfigFile(vmList_afterDbSearch, config)

    
    # printing prarameters of the final vm list to be used (vmList after DB search with good processing time and corresponding links)
    # Recap of the chosen vms
    print("\n Recap of the chosen vms for your architecture:")
    for i, vm_afterDb in enumerate(vmList_afterDbSearch):
        print(f"{i+1}. vm id: {vm_afterDb.id}")
        print(f"cpu: {vm_afterDb.cpu}")
        print(f"memory: {vm_afterDb.memory}")
        print(f"hour rate: {vm_afterDb.hourrate}")
        print(f"location: {vm_afterDb.location}")
        print(f"csp: {vm_afterDb.csp}")
        print(f"processing time: {vm_afterDb.processingtime}")
        print(f"links: {vm_afterDb.links}")
        print("\n")

    #Retrieving the operational cost
    total_operational_cost= get_total_operational_cost(vmList_afterDbSearch)
    
    #Retrieving the network cost
    total_network_cost= get_total_network_cost(vmList_afterDbSearch)

    #Computing the overall total cost
    total_cost= total_operational_cost+total_network_cost


    #Generate the overall results 
    print('\n')
    print('Generating the Overall total costs of your architecture...')
    
    print(f'Total operational costs: $ {total_operational_cost:.2f}')
    print(f'Total Network costs: $ {total_network_cost:.2f}')
    print(f'Final Total cost of your architecture: $ {total_cost:.2f}')

    
    
    
    
    
    
    
    
    
    
    #make a search for each vm in the vm list
    
    #for vm in enumerate(vmList_beforeDb):
        #manage exception if the research does not return anything
        #try:
        #print(find_TheBestVm_in_db(cpu=vm.cpu, memory=vm.memory, csp=vm.csp))
        #print(type(find_TheBestVm_in_db(cpu=vm.cpu, memory=vm.memory, csp=vm.csp)))
        #vmList_afterDbSearch[i+1].append(vm_afterDbSearch)
        #except:
         #   raise Exception("error when filling in the new vm list")

    
    #afficher le nouveau dictionnaire de vms
    """for new_vm in enumerate(vmList_afterDbSearch):
        print(f"{i+1}. vm id: {new_vm.id}")
        print(f"cpu: {new_vm.cpu}")
        print(f"memory: {new_vm.memory}")
        print(f"hour rate: {new_vm.hourrate}")
        print(f"csp: {new_vm.csp}")
        print(f"location: {new_vm.location}")
        print(f"\n")"""


if __name__ == "__main__":
    main()  

 
    










   


       