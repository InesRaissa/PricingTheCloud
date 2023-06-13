from totalNetworkCost import get_total_network_cost
from totalOperationalCost import get_total_operational_cost


def get_total_costs(vm_list):
    
    total_cost=0
    total_network_cost=get_total_network_cost(vm_list)
    total_operational_cost=get_total_operational_cost(vm_list)

    
    total_cost = total_operational_cost+total_network_cost

    #Printing Results
    print(f'The total cost of this transaction is ${total_cost:.2f}')


    return total_cost