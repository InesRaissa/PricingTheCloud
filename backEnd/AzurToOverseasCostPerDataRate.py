#import vmUserInput
#import edgeUserInput
from operator import mul
from vmClass import VM


#dictionnaries definition

dicoRegionNorthAmerica=['easus','easus_II','northcentralus','westcentralus','westus','westus_II','westus_III','canadacentral','canadaeast']
dicoRegionSouthAmerica=['brazilsouth','southcentralus']
dicoRegionEurope=['francecentral','francesouth','germancentral', 'northeurope', 'switzerlandnorth', 'switzerlandwest', 'switzerlandcentral', 'norwayeast', 'norwaywest', 'uksouth', 'ukwest', 'westeurope']
dicoRegionAsia=['east_asia','japan_east', 'japan_west', 'koreacentral', 'koreasouth', 'koreacentral', 'southeast_asia', 'southindia', 'westindia',  'jioindiawest']
dicoRegionAfrica=['southafricannorth','southafricawest']
dicoRegionMiddleEast=['uaecentral', 'uanorth','quatarcentral']
dicoRegionOceania=['australiacentral','australiacentral_II', 'australiaeast', 'australiasoutheast']

#OTI= overseas throw ISP(internet)
def get_AzurToOverseas_throwInternet_costPerDataRate(VMazur, DRout_az):

    #Give a default Cegress value
    Cegress=-1
    DRout_azur=int(DRout_az)

    #From North America and Europe to overseas throw internet    
    if VMazur.location in dicoRegionNorthAmerica or VMazur.location in dicoRegionEurope:
        
        #for trafic between 100GB and 10100 (next 10TB)
        if 0 < DRout_azur <=10100:
            Cegress=0.08
            
        #for trafic between 10100 and 50100 (next 40TB)
        elif 10100 < DRout_azur <=50100:
            Cegress=0.065

        #for trafic between 50100 and 150100 (next 100TB)
        elif 50100 < DRout_azur <=150100:
            Cegress=0.06

        #for trafic between 150100 and 500100 (next 350TB)
        elif 150100 < DRout_azur <=500100:
            Cegress=0.04
        
        #for trafic more than 500TB
        elif DRout_azur >500100:
            Cegress=0.04
        
    # From azur vms Asia, oceania, and middle east to overseas throw internet
    elif VMazur.location in dicoRegionAsia or VMazur.location in dicoRegionOceania or VMazur.location in dicoRegionMiddleEast:
        
        #for trafic between 100GB and 10100 (next 10TB)
        if 0 < DRout_azur <=10100:
            Cegress=0.11
            
        #for trafic between 10100 and 50100 (next 40TB)
        elif 10100 < DRout_azur <=50100:
            Cegress=0.075

        #for trafic between 50100 and 150100 (next 100TB)
        elif 50100 < DRout_azur <=150100:
            Cegress=0.07

        #for trafic between 150100 and 500100 (next 350TB)
        elif 150100 < DRout_azur <=500100:
            Cegress=0.06
        
        #for trafic more than 500TB
        elif DRout_azur >500100:
            Cegress=0.06
    
    #from azur south america to other providers throw internet (ISP)
    elif VMazur.location in dicoRegionSouthAmerica:
        
        #for trafic between 100GB and 10100 (next 10TB)
        if 0 < DRout_azur <=10100:
            Cegress=0.12
            
        #for trafic between 10100 and 50100 (next 40TB)
        elif 10100 < DRout_azur <=50100:
            Cegress=0.085

        #for trafic between 50100 and 150100 (next 100TB)
        elif 50100 < DRout_azur <=150100:
            Cegress=0.08

        #for trafic between 150100 and 500100 (next 350TB)
        elif 150100 < DRout_azur <=500100:
            Cegress=0.075
        
        #for trafic more than 500TB
        elif DRout_azur >500000:
            Cegress=0.075
        
    else:
        Cegress=0
        print('Sorry. There is no trafic from this azur vm to overseas throw ISP network') 


    return Cegress




#cost per data rate for overseas throw azur provider
def get_AzurToOverseas_throwAzurNtwk_costPerdataRate(VMazur, DRout_az):

    #Give a default Cegress value
    Cegress=-1
    DRout_azur=int(DRout_az)
    
    if VMazur.location in dicoRegionNorthAmerica or VMazur.location in dicoRegionEurope:
        
        #for trafic between 0GB and 10100 (next 10TB)
        if 0 < DRout_azur <=10100:
            Cegress=0.087
            
        #for trafic between 10100 and 50100 (next 40TB)
        elif 10100 < DRout_azur <=50100:
            Cegress=0.083

        #for trafic between 50100 and 150100 (next 100TB)
        elif 50100 < DRout_azur <=150100:
            Cegress=0.07

        #for trafic between 150100 and 500100 (next 350TB)
        elif 150100 < DRout_azur <=500100:
            Cegress=0.05
        
        #for trafic more than 500TB
        elif DRout_azur >500000:
            Cegress=0.05

    elif VMazur.location in dicoRegionAsia or VMazur.location in dicoRegionOceania or VMazur.location in dicoRegionNorthAmerica or VMazur.location in dicoRegionMiddleEast:
          
        #for trafic between 100GB and 10100 (next 10TB)
        if 0 < DRout_azur <=10100:
            Cegress=0.12
            
        #for trafic between 10100 and 50100 (next 40TB)
        elif 10100 < DRout_azur <=50100:
            Cegress=0.085

        #for trafic between 50100 and 150100 (next 100TB)
        elif 50100 < DRout_azur <=150100:
            Cegress=0.082

        #for trafic between 150100 and 500100 (next 350TB)
        elif 150100 < DRout_azur <=500100:
            Cegress=0.08
        
        #for trafic more than 500TB
        elif DRout_azur >500000:
            Cegress=0.08
    
    #from azur south america to other providers throw aur premium network
    elif VMazur.location in dicoRegionSouthAmerica:
        
        #for trafic between 100GB and 10100 (next 10TB)
        if 0 < DRout_azur <=10100:
            Cegress=0.181
            
        #for trafic between 10100 and 50100 (next 40TB)
        elif 10100 < DRout_azur <=50100:
            Cegress=0.175

        #for trafic between 50100 and 150100 (next 100TB)
        elif 50100 < DRout_azur <=150100:
            Cegress=0.17

        #for trafic between 150100 and 500100 (next 350TB)
        elif 150100 < DRout_azur <=500100:
            Cegress=0.16
        
        elif DRout_azur >500000:
            Cegress=0.16

    else:
        Cegress=0
        print('Sorry. There is no trafic from this azur vm to overseas throw azur premium network') 

    return Cegress
   

















#a simple main
    
"""dataRate=600
vm1 = VM(cpu=4, memory=8, csp='AZUR', location='uksouth', processingtime=23)
vm2 = VM(cpu=2, memory=4, csp='AZUR', location="uanorth", processingtime=20.76)
#cpu, memory, csp, continent, region, ad

print(get_AzurToOverseas_throwAzurNtwk_costPerdataRate(vm1,dataRate))
print(get_AzurToOverseas_throwInternet_costPerDataRate(vm1,dataRate))

print(get_AzurToOverseas_throwAzurNtwk_costPerdataRate(vm2,dataRate))
print(get_AzurToOverseas_throwInternet_costPerDataRate(vm2,dataRate))"""


"""print("\n test azur inter regions within continent\n")
print (f"location of vm2: {vm2.location} ")
print (f"location of vm1: {vm1.location} ")
print(f" {azur_costPerDataRate_InterContinentsVms(vm1,vm2)} ")
print(f" {NtwkCost_InterAzurRegions_withinContinent(vm1,vm2,dataRate)} ")"""




#testing USA vm location
#bestVMDico1={"apiName": "a1.2xlarge", "VMName": "A1 Double Extra Large", "cpu": 8, "memory": 16.0, "storage": "EBS only", "hourRate": 0.204, "location": "use1-az2, use1-az4, use1-az6", "networkPerformance": "Up to 10 Gigabit"}
bestVMDico1={'apiName': 'Standard_D8pls_v5', 'cpu': 8, 'memory': '16', 'hourRate':'0.17', 'location': 'centralindia', 'csp': 'azur'}
bestVMDico2={'apiName': 'Standard_B2s', 'cpu': 2, 'memory':'4', 'hourRate': '0.0416', 'location': 'eastus', 'csp': 'azur'}






