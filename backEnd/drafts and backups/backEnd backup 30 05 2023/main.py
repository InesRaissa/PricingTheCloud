#import psycopg2
from vmClass import VM
#from operator import mul
from totalOperationalCost import get_total_operational_cost
from FindTheBestVmFromDb import find_TheBestVm_in_db
from totalNetworkCost import get_total_network_cost


#This is the main function (vm_list entered by the end user and vm_list after the selection)  

def main():
    
    num_vms = int(input("Enter the number of VMs you want to create: "))
    vmList_beforeDbSearch = []
    vmList_afterDbSearch=[]
    opcost_vm=0
    total_operational_cost=0
    total_network_cost=0
    total_cost=0

    
    for i in range(num_vms):
        
        print(f"\nCreating VM {i+1}:")
        id = None
        cpu = input("Enter the CPU for the VM: ")
        memory = input("Enter the memory for the VM: ")
        hourrate=None
        location = input("Enter the location for the VM: ")
        csp = input("Enter the CSP for the VM: ")
        processtime = input("Enter the processing time of the VM: ")
        

        #recuperation des valeurs de vms entrés par l'utilisateur
        #vm = VM(cpu, memory, csp, location, processtime)
        #vm = VM(id, cpu, memory, location, csp, processtime)
        vm = VM(id, cpu, memory, hourrate, location, csp, processtime)
        
        print("Printing vm parameters: \n")
        print(f"vm id: {vm.id}")
        print(f"cpu: {vm.cpu}")
        print(f"memory: {vm.memory}")
        print(f"hour rate: {vm.hourrate}")
        print(f"location: {vm.location}")
        print(f"csp: {vm.csp}")
        print(f"processing time: {vm.processingtime}")
        
        print(f"\n")
        

        vm_afterDb=find_TheBestVm_in_db(cpu=vm.cpu, memory=vm.memory, csp=vm.csp)
        """print(f"new vm id: {vm_afterDb.id}")
        print(f"new cpu: {vm_afterDb.cpu}")
        print(f"new memory: {vm_afterDb.memory}")
        print(f"new hour rate: {vm_afterDb.hourrate}")
        print(f"new location: {vm_afterDb.location}")
        print(f"new csp: {vm_afterDb.csp}")
        print(f"new processing time: {vm_afterDb.processingtime}")
        print(f"\n")"""

        #assign the user entered processing time to the new vm
        vm_afterDb.processingtime= processtime
        print('\n')
        print('Characteristics of the chosen vm')
        print(f"chosen vm id: {vm_afterDb.id}")
        print(f"chosen cpu: {vm_afterDb.cpu}")
        print(f"chosen memory: {vm_afterDb.memory}")
        print(f"chosen hour rate: {vm_afterDb.hourrate}")
        print(f"chosen location: {vm_afterDb.location}")
        print(f"chosen csp: {vm_afterDb.csp}")
        print(f"chosen processing time: {vm_afterDb.processingtime}")
        print(f"\n")

        
        #computing operational cost
        #opcost_vm= mul(float(vm_afterDb.hourrate), float(vm_afterDb.processingtime))

        #print(f" Operational cost for vm {vm_afterDb.id}: $ {opcost_vm: .2f}\n")


        #computing the final operational cost
        #total_operational_cost+= opcost_vm
        #print(f'\n')
        #print(f'The final (total) operational cost: $ {final_opcost: .2f}\n')
        #print('\n')
        #print(type(vm_afterDb))
        #print(vm_afterDb)
        
        
        #vm = VM(csp, location)
        #printing the vm list before user's choice
        vmList_beforeDbSearch.append(vm)
        
        # The vm list after user's choice
        vmList_afterDbSearch.append(vm_afterDb)
        
        

    # Ask user to establish links between VMs
    for i, vm in enumerate(vmList_afterDbSearch):
        print(f"\nCreating links for VM {i+1}:")
            
        for j, linked_vm in enumerate(vmList_afterDbSearch):
            if i != j:
                data_rate = input(f"Enter the volume of trafic between VM {i+1} and VM {j+1} (Gbps): ")
                vm.add_link(linked_vm, data_rate)

    

    # Recap of the chosen vms
    print("\n Recap of the chosen vms for your architecture:")
    for i, vm_afterDb in enumerate(vmList_afterDbSearch):
                #print(f"{i+1}. {vm.id}:  ({vm.hourrate}/hour)")
                print(f"{i+1}. vm id: {vm_afterDb.id}")
                print(f"cpu: {vm_afterDb.cpu}")
                print(f"memory: {vm_afterDb.memory}")
                print(f"hour rate: {vm_afterDb.hourrate}")
                print(f"location: {vm_afterDb.location}")
                print(f"csp: {vm_afterDb.csp}")
                print(f"processing time: {vm_afterDb.processingtime}")
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

 
    










   


       