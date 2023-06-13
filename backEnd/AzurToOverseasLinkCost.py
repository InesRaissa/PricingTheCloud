#import vmUserInput
#import edgeUserInput
from operator import mul
from vmClass import VM
import pandas as pd
import math


#dictionnaries definition
dicoRegionNorthAmerica=['eastus','eastus_II','northcentralus','westcentralus','westus','westus_II','westus_III','canadacentral','canadaeast']
dicoRegionEurope=['francecentral','francesouth','germancentral', 'northeurope', 'switzerlandnorth', 'switzerlandwest', 'switzerlandcentral', 'norwayeast', 'norwaywest', 'uksouth', 'ukwest', 'westeurope', 'swedencentral']

dicoRegionAsia=['east_asia','japan_east', 'japan_west', 'koreacentral', 'koreasouth', 'koreacentral', 'southeast_asia', 'southindia', 'westindia',  'jioindiawest']
dicoRegionMiddleEast=['uaecentral', 'uanorth','quatarcentral']
dicoRegionOceania=['australiacentral','australiacentral_II', 'australiaeast', 'australiasoutheast']

dicoRegionSouthAmerica=['brazilsouth','southcentralus', 'brazilsoutheast']

dicoRegionAfrica=['southafricannorth','southafricawest']



#OTI= overseas throw ISP(internet)
def get_AzurToOverseas_throwInternet_linkcost(VMazur, DRout_az):

    #Give a default Cegress value
    #Cegress=-1
    DRout_azur=int(DRout_az)
    azur_toOverseas_link_cost = -1


    #defining the different intervals to use
    lowerbound_interval_0_to_10TB=0
    upperbound_interval_0_to_10TB=10100
    upperbound_interval_next_40TB=50100
    upperbound_interval_next_100TB=150100
    upperbound_interval_next_350TB=500100


    interval_0_to_10TB=pd.Interval(lowerbound_interval_0_to_10TB, upperbound_interval_0_to_10TB)
    interval_next_40TB=pd.Interval(upperbound_interval_0_to_10TB, upperbound_interval_next_40TB)
    interval_next_100TB=pd.Interval(upperbound_interval_next_40TB, upperbound_interval_next_100TB)
    interval_next_350TB=pd.Interval(upperbound_interval_next_100TB, upperbound_interval_next_350TB)
    interval_morethan_350TB=pd.Interval(upperbound_interval_next_350TB, math.inf)


    #From North America and Europe to overseas throw internet    
    if VMazur.location in dicoRegionNorthAmerica or VMazur.location in dicoRegionEurope:
        
        #for trafic between 100GB and 10100 (next 10TB)
        if DRout_azur in interval_0_to_10TB:
            Cegress=0.08
            azur_toOverseas_link_cost = DRout_azur * Cegress
            
        #for trafic between 10100 and 50100 (next 40TB)
        elif DRout_azur in interval_next_40TB:
            Cegress=0.065
            azur_toOverseas_link_cost= (0.08 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_azur - upperbound_interval_0_to_10TB)*Cegress)


        #for trafic between 50100 and 150100 (next 100TB)
        elif DRout_azur in interval_next_100TB:
            Cegress=0.06
            azur_toOverseas_link_cost= (0.08 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.065 *(upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_azur - upperbound_interval_next_40TB)*Cegress)
            

        #for trafic between 150100 and 500100 (next 350TB)
        elif DRout_azur in interval_next_350TB:
            Cegress=0.04
            azur_toOverseas_link_cost= (0.08 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.065 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.06 * (upperbound_interval_next_100TB- upperbound_interval_next_40TB)) + ((DRout_azur - upperbound_interval_next_100TB)*Cegress)

        
        #for trafic more than 500TB
        elif DRout_azur in interval_morethan_350TB:
            Cegress=0.04
            azur_toOverseas_link_cost= (0.08 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.065 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.06 * (upperbound_interval_next_100TB- upperbound_interval_next_40TB))+ (Cegress * (upperbound_interval_next_350TB- upperbound_interval_next_100TB)) + ((DRout_azur - upperbound_interval_next_350TB)*Cegress)

            print("For trafic volumes >500100 GB, You should contact Azur for a better offer. For now, you're charged as if the trafic volume was between 150100 GB and 500100GB")
        
    # From azur vms Asia, oceania, and middle east to overseas throw internet
    elif VMazur.location in dicoRegionAsia or VMazur.location in dicoRegionOceania or VMazur.location in dicoRegionMiddleEast:
        
        #for trafic between 100GB and 10100 (next 10TB)
        if DRout_azur in interval_0_to_10TB:
            Cegress=0.11
            azur_toOverseas_link_cost = DRout_azur * Cegress
            
            
        #for trafic between 10100 and 50100 (next 40TB)
        elif DRout_azur in interval_next_40TB:
            Cegress=0.075
            azur_toOverseas_link_cost= (0.11 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_azur - upperbound_interval_0_to_10TB)*Cegress)


        #for trafic between 50100 and 150100 (next 100TB)
        elif DRout_azur in interval_next_100TB:
            Cegress=0.07
            azur_toOverseas_link_cost= (0.11 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.075 *(upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_azur - upperbound_interval_next_40TB)*Cegress)
            


        #for trafic between 150100 and 500100 (next 350TB)
        elif DRout_azur in interval_next_350TB:
            Cegress=0.06
            azur_toOverseas_link_cost= (0.11 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.075 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.07 * (upperbound_interval_next_100TB- upperbound_interval_next_40TB)) + ((DRout_azur - upperbound_interval_next_100TB)*Cegress)


        
        #for trafic more than 500TB
        elif DRout_azur in interval_morethan_350TB:
            Cegress=0.06
            azur_toOverseas_link_cost= (0.11 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.075 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + (0.07 * (upperbound_interval_next_100TB- upperbound_interval_next_40TB)) + (Cegress * (upperbound_interval_next_350TB- upperbound_interval_next_100TB)) + ((DRout_azur - upperbound_interval_next_350TB)*Cegress)

            print("For trafic volumes >500100 GB, You should contact Azur for a better offer. For now, you're charged as if the trafic volume was between 150100 GB and 500100GB")
        
    
    #from azur south america to other providers throw internet (ISP)
    elif VMazur.location in dicoRegionSouthAmerica:
        
        #for trafic between 100GB and 10100 (next 10TB)
        if DRout_azur in interval_0_to_10TB:
            Cegress=0.12
            azur_toOverseas_link_cost = DRout_azur * Cegress
            
        #for trafic between 10100 and 50100 (next 40TB)
        elif  DRout_azur in interval_next_40TB:
            Cegress=0.085
            azur_toOverseas_link_cost= (0.12 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_azur - upperbound_interval_0_to_10TB)*Cegress)



        #for trafic between 50100 and 150100 (next 100TB)
        elif DRout_azur in interval_next_100TB:
            Cegress=0.08
            azur_toOverseas_link_cost= (0.12 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.085 *(upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_azur - upperbound_interval_next_40TB)*Cegress)
            

        #for trafic between 150100 and 500100 (next 350TB)
        elif DRout_azur in interval_next_350TB:
            Cegress=0.075
            azur_toOverseas_link_cost= (0.12 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.085 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.08 * (upperbound_interval_next_100TB- upperbound_interval_next_40TB)) + ((DRout_azur - upperbound_interval_next_100TB)*Cegress)

        
        #for trafic more than 500TB
        elif DRout_azur in interval_morethan_350TB:
            Cegress=0.075
            azur_toOverseas_link_cost= (0.12 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.085 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.08 * (upperbound_interval_next_100TB- upperbound_interval_next_40TB)) + (Cegress * (upperbound_interval_next_350TB- upperbound_interval_next_100TB)) +((DRout_azur - upperbound_interval_next_350TB)*Cegress)
            print("For trafic volumes >500100 GB, You should contact Azur for a better offer. For now, you're charged as if the trafic volume was between 150100 GB and 500100GB")
        
        
    else:
        Cegress=0
        azur_toOverseas_link_cost=0
        print('Sorry. There is no trafic from this azur vm to overseas throw ISP network') 


    return azur_toOverseas_link_cost




#cost per data rate for overseas throw azur provider
"""def get_AzurToOverseas_throwAzurNtwk_costPerdataRate(VMazur, DRout_az):

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

    return Cegress"""
   

















#a simple main
    
"""dataRate=56500
vm1 = VM(cpu=4, memory=8, csp='AZUR', location='uksouth', processingtime=23)
vm2 = VM(cpu=2, memory=4, csp='AZUR', location="uanorth", processingtime=20.76)

vm1 = VM(csp='AZUR', location='easus_II')
vm2 = VM(csp='AZUR', location="brazilsouth")
vm3 = VM(csp='AZUR', location="uanorth")
cpu, memory, csp, continent, region, ad

print(get_AzurToOverseas_throwAzurNtwk_costPerdataRate(vm1,dataRate))
print('result for ')
print(get_AzurToOverseas_throwInternet_linkcost(vm1,dataRate))

print(get_AzurToOverseas_throwAzurNtwk_costPerdataRate(vm2,dataRate))
print(get_AzurToOverseas_throwInternet_linkcost(vm2,dataRate))
print(get_AzurToOverseas_throwInternet_linkcost(vm3,dataRate))"""


"""print("\n test azur inter regions within continent\n")
print (f"location of vm2: {vm2.location} ")
print (f"location of vm1: {vm1.location} ")
print(f" {azur_costPerDataRate_InterContinentsVms(vm1,vm2)} ")
print(f" {NtwkCost_InterAzurRegions_withinContinent(vm1,vm2,dataRate)} ")"""




#testing USA vm location
#bestVMDico1={"apiName": "a1.2xlarge", "VMName": "A1 Double Extra Large", "cpu": 8, "memory": 16.0, "storage": "EBS only", "hourRate": 0.204, "location": "use1-az2, use1-az4, use1-az6", "networkPerformance": "Up to 10 Gigabit"}
#bestVMDico1={'apiName': 'Standard_D8pls_v5', 'cpu': 8, 'memory': '16', 'hourRate':'0.17', 'location': 'centralindia', 'csp': 'azur'}
#bestVMDico2={'apiName': 'Standard_B2s', 'cpu': 2, 'memory':'4', 'hourRate': '0.0416', 'location': 'eastus', 'csp': 'azur'}






