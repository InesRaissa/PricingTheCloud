from vmClass import VM

from getCspLinkCost import get_aws_link_cost
from getCspLinkCost import get_azur_link_cost


def get_total_network_cost(vm_list):
    
    # Compute total link cost for AWS links
    print('\n')
    print('Generating network costs per csp for your architecture...')
    aws_link_cost = get_aws_link_cost(vm_list)
    
    
    # Compute total link cost for non-AWS links
    azur_link_cost = get_azur_link_cost(vm_list)
    
    # Compute total cost
    total_network_cost = aws_link_cost + azur_link_cost
    
    # Print results
    print(f"\nTotal network cost for AWS links: ${aws_link_cost:.2f}")
    print(f"Total network cost for Azur links: ${azur_link_cost:.2f}")

    return total_network_cost




#print(f"The Overall Total Network Cost: $ {get_total_network_cost(vm_list):.2f}")  