#import vmUserInput
#import edgeUserInput
from operator import mul
from vmClass import VM



#dictionnaries definition

dicoRegionNorthAmerica=['easus','easus_II','northcentralus','westcentralus','westus','westus_II','westus_III','canadacentral','canadaeast']
dicoRegionSouthAmerica=['brazilsouth','southcentralus']
dicoRegionEurope=['francecentral','francesouth','germancentral', 'northeurope', 'switzerlandnorth', 'switzerlandwest', 'switzerlandcentral', 'norwayeast', 'norwaywest', 'uksouth', 'ukwest', 'westeurope']
dicoRegionAsia=['east_asia','japan_east', 'japan_west', 'koreacentral', 'koreasouth', 'koreacentral', 'southeast_asia','centralindia', 'southindia', 'westindia',  'jioindiawest']
dicoRegionAfrica=['southafricannorth','southafricawest']
dicoRegionMiddleEast=['uaecentral', 'uanorth','quatarcentral']
dicoRegionOceania=['australiacentral','australiacentral_II', 'australiaeast', 'australiasoutheast']


def get_Azur_to_azur_costPerDataRate(vma, vmb):
    #This cost encompasses azur to azur within region, inter-regions, and inter-continents.
    #due to the lack of dataset information, the interAD(within region) cost will not be considered
    
    #This code is for azur to azur within region. There should paramount be a condition that vma.location != vmb.location 
    azur_to_azur_CostPerDR =-1

    if vma.location in dicoRegionNorthAmerica and vmb.location in dicoRegionNorthAmerica:
        print(f"vma is in northamerica and vmb in nothamerica")
        azur_to_azur_CostPerDR=0.02
        
    elif vma.location in dicoRegionEurope and vmb.location in dicoRegionEurope:
        azur_to_azur_CostPerDR=0.02
        print(f"vma is in europe and vmb in europe")
    elif vma.location in dicoRegionAsia and vmb.location in dicoRegionAsia:
        azur_to_azur_CostPerDR=0.08
        print(f"vma is in asia and vmb in asia")
    elif vma.location in dicoRegionOceania and vmb.location in dicoRegionOceania:
        azur_to_azur_CostPerDR=0.08
        print(f"vma is in oceania and vmb in oceania")
    elif vma.location in dicoRegionAfrica and vmb.location in dicoRegionAfrica:
        azur_to_azur_CostPerDR=0.08
        print(f"vma is in africa and vmb in africa")
    elif vma.location in dicoRegionMiddleEast and vmb.location in dicoRegionMiddleEast:
        azur_to_azur_CostPerDR=0.08
        print(f"vma is in middle east and vmb in middle east")
    elif vma.location in dicoRegionSouthAmerica and vmb.location in dicoRegionSouthAmerica:
        azur_to_azur_CostPerDR=0.16   
        print(f"vma is in southamerica and vmb in southamerica") 

#this code is related to intercontinents
    elif vma.location in dicoRegionNorthAmerica and vmb.location not in dicoRegionNorthAmerica:
        azur_to_azur_CostPerDR=0.05
    
    elif vma.location in dicoRegionEurope and vmb.location not in dicoRegionEurope:
        azur_to_azur_CostPerDR=0.05
    
    elif vma.location in dicoRegionAsia and vmb.location not in dicoRegionAsia:
        azur_to_azur_CostPerDR=0.08
        
    elif vma.location in dicoRegionOceania and vmb.location not in dicoRegionOceania:
        azur_to_azur_CostPerDR=0.08
    
    elif vma.location in dicoRegionSouthAmerica and vmb.location not in dicoRegionSouthAmerica:
        azur_to_azur_CostPerDR=0.16

    elif vma.location in dicoRegionMiddleEast and vmb.location not in dicoRegionMiddleEast:
        azur_to_azur_CostPerDR=0
        print("Azur has not yet scheduled traffic from the middle east to other continents")

    elif vma.location in dicoRegionAfrica and vmb.location not in dicoRegionAfrica:
        azur_to_azur_CostPerDR=0.08
    
    else:
        azur_to_azur_CostPerDR=0
        print("The two vms do not belong to azur provider")
    
    return azur_to_azur_CostPerDR


   

















#a simple main
    
"""dataRate=600
vm1 = VM(cpu=4, memory=8, csp='azur', location='uksouth', processingtime=23)
vm2 = VM(cpu=2, memory=4, csp='azur', location="australiacentral", processingtime=20.76)
#cpu, memory, csp, continent, region, ad

print(float(dataRate)*get_Azur_to_azur_costPerDataRate(vm1,vm2))
print(float(dataRate)*get_Azur_to_azur_costPerDataRate(vm2,vm1))"""




#testing USA vm location
#bestVMDico1={"apiName": "a1.2xlarge", "VMName": "A1 Double Extra Large", "cpu": 8, "memory": 16.0, "storage": "EBS only", "hourRate": 0.204, "location": "use1-az2, use1-az4, use1-az6", "networkPerformance": "Up to 10 Gigabit"}
#bestVMDico1={'apiName': 'Standard_D8pls_v5', 'cpu': 8, 'memory': '16', 'hourRate':'0.17', 'location': 'centralindia', 'csp': 'azur'}
#bestVMDico2={'apiName': 'Standard_B2s', 'cpu': 2, 'memory':'4', 'hourRate': '0.0416', 'location': 'eastus', 'csp': 'azur'}

"""print("results for azur to azur within continent")
NtwkCost_InterAzurRegions_withinContinent(bestVMDico1,bestVMDico2,dataRate)
print('\n')

print("results for azur to overseas throw azur premium network")
#NtwkCost_FromAzurToOverseas_throwAzurNtwk(bestVMDico1,dataRate)
print('\n')

print("results for azur to overseas throw internet")
#NtwkCost_FromAzurToOverseas_throwInternet(bestVMDico1,dataRate)
print('\n')"""




