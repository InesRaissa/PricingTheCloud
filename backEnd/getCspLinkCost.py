#from vmClass import VM
from AzurToAzurCostPerDataRate import get_Azur_to_azur_costPerDataRate
from awsToAwsCostPerDataRate import get_Aws_to_aws_costPerDataRate
from awsToOverseasLinkCost import get_aws_toOverseas_link_cost
from AzurToOverseasLinkCost import get_AzurToOverseas_throwInternet_linkcost


def get_aws_link_cost(vm_list):
   
    print("\n Aws links connexion costs...")
    aws_vms = [vm for vm in vm_list if vm.csp == "aws"]
    aws_link_cost = 0
    
    for vm in aws_vms:
        for linked_vm, data_rate in vm.links.items():
            
            if linked_vm.csp == "aws":
                link_cost = float(data_rate) * get_Aws_to_aws_costPerDataRate(vm, linked_vm)
                aws_link_cost +=link_cost 
                print(f" Outgoing trafic from '{vm.id}' at {vm.location} to '{linked_vm.id}' at {linked_vm.location}: $ {link_cost:.2f}")
                #aws_link_cost += 2

            else:
                #vm is the one that initiates the traffic (egress vm)
                #costPerDataRateOverseas= get_aws_toOverseas_costPerDataRate(vm, data_rate)
                #link_cost =float(data_rate) * costPerDataRateOverseas
                link_cost= get_aws_toOverseas_link_cost(vm, data_rate)
                aws_link_cost +=link_cost 
                print(f" Outgoing trafic from '{vm.id}' at {vm.location} to '{linked_vm.id}' at {linked_vm.location}: $ {link_cost:.2f}") 

    return aws_link_cost


#I've written the function. There remain the verification step
def get_azur_link_cost(vm_list):
    azur_vms = [vm for vm in vm_list if vm.csp == "azur"]
    #print("\n ")
    print("\n Azur links connexion costs...")
    azur_link_cost = 0
    for vm in azur_vms:
        for linked_vm, data_rate in vm.links.items():
            
            #case azur to azur interAD within region (There is however a risk that the two are in the same AD)
            if linked_vm.csp == "azur":

                if vm.location ==linked_vm.location:
                    link_cost = float(data_rate) * 0.01
                    azur_link_cost += link_cost
                    print(f"Outgoing trafic from '{vm.id}' at {vm.location} to '{linked_vm.id}' at {linked_vm.location}: $ {link_cost:.2f}")

                else:
                    
                    link_cost = float(data_rate) * get_Azur_to_azur_costPerDataRate(vm, linked_vm)
                    azur_link_cost += link_cost
                    print(f" Outgoing trafic from '{vm.id}' at {vm.location} to '{linked_vm.id}' at {linked_vm.location}: $ {link_cost:.2f}")

            #case azur to overseas (we only consider the overseas throw ISP). We don't know how represent throw azurntwk yet
            else:
                #link_cost = float(data_rate) * get_AzurToOverseas_throwInternet_costPerDataRate(vm, data_rate)
                link_cost= get_AzurToOverseas_throwInternet_linkcost(vm, data_rate)
                azur_link_cost += link_cost
                print(f" Outgoing trafic from '{linked_vm.id}' at {vm.location} to '{linked_vm.id}' at {linked_vm.location}: $ {link_cost:.2f}")

    return azur_link_cost

