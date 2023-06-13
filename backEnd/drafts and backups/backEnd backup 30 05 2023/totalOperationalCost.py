from vmClass import VM
from operator import mul
#there should be an import here that gives us the list of dbs after search


def get_total_operational_cost(vm_list):
    
    #vm_list= get_vm_afterDbSearch()

    #opcost_vm
    total_operational_cost=0

    # Compute total link cost for AWS links
    print('\n')
    print('Generating operational costs for each vm of your architecture...')
    for vm in vm_list:
        
        opcost_vm= mul(float(vm.hourrate), float(vm.processingtime))

        print(f" operational cost for {vm.id}: ${opcost_vm:.2f}")

        #computing and printing the total operational cost
        total_operational_cost+= opcost_vm
        
    #print(f'\n')
    #print(f'The final (total) operational cost: ${total_operational_cost:.2f}')
     

    return total_operational_cost




#print(f"The Overall Total Network Cost: $ {get_total_network_cost(vm_list):.2f}")  