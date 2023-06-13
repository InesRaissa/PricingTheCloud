from vmClass import VM
from operator import mul
import pandas as pd
import math


"""This function retrieve the cost per data rate for a link between two vms, one belonging to aws 
and the other belonging to another provider. 
The costs per data rate considered are taken from real aws costs dataset (April 2023).
The following zones have not been represented: SKT(Daejeon and seoul), India(Dehli and Kolkata), 
Taiwan, Lagos, USA(minneapolis, )
vma is the egress vm (the one that initiates the trafic) and vmb is the ingress traffic"""



#VMaws is the vm which initiates the traffic on the link (egress vm)
def get_aws_toOverseas_link_cost(VMaws, DRout):

    #initialising the parameters
    DRout_a= int(DRout)
    #Cegress=-1
    aws_toOverseas_link_cost = -1


    #defining the different intervals to use
    lowerbound_interval_0_to_10TB=0
    upperbound_interval_0_to_10TB=10240
    upperbound_interval_next_40TB=51200
    upperbound_interval_next_100TB=153600


    interval_0_to_10TB=pd.Interval(lowerbound_interval_0_to_10TB, upperbound_interval_0_to_10TB)
    interval_next_40TB=pd.Interval(upperbound_interval_0_to_10TB, upperbound_interval_next_40TB)
    interval_next_100TB=pd.Interval(upperbound_interval_next_40TB, upperbound_interval_next_100TB)
    interval_morethan_150TB=pd.Interval(upperbound_interval_next_100TB, math.inf)

    



    # From asia pacific(Hong Kong and Singapore)
    if VMaws.location=="ap-east-1" or VMaws.location=="ap-southeast-1":

        #for trafic between 0GB and 10 TB 
        if DRout_a in interval_0_to_10TB:
            Cegress=0.12
            aws_toOverseas_link_cost = DRout_a * Cegress

        
        #for trafic between 10TB and 50TB (the next 40 TB)
        elif DRout_a in interval_next_40TB:
            Cegress=0.085
            aws_toOverseas_link_cost= (0.12 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)

        #for trafic between 50TB and 150TB (the next 100TB)
        elif DRout_a in interval_next_100TB:
            Cegress=0.0082
            aws_toOverseas_link_cost= (0.12 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.085 *(upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)
            

        #for trafic more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.08
            aws_toOverseas_link_cost= (0.12 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.085 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.082 * (upperbound_interval_next_100TB- upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)


    # for egress trafics from europe(all), us(all)
    elif VMaws.location=="eu-west-1" or VMaws.location== "eu-west-2" or VMaws.location== "eu-west-3" or VMaws.location== "eu-south-1" or VMaws.location== "eu-south-2" or VMaws.location== "eu-north-1" or VMaws.location=="us-west-1" or VMaws.location== "us-west-2" or VMaws.location== "us-east-1" or VMaws.location== "us-east-2" or VMaws.location== "eu-central-1" or VMaws.location== "eu-central-2"or VMaws.location== "ca-central-1":
        
        #between 0GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.09
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB
        elif DRout_a in interval_next_40TB:
            Cegress=0.085
            aws_toOverseas_link_cost= (0.09 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)
            #a= 0.09 x 10240 + (DRout_a-10240)Cegress

        #between 50TB and 150TB
        elif DRout_a in interval_next_100TB:
            Cegress=0.07
            aws_toOverseas_link_cost= (0.09 * (upperbound_interval_0_to_10TB- lowerbound_interval_0_to_10TB)) + (0.085 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)

        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.05
            aws_toOverseas_link_cost= (0.09 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.085 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.07 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)
    
    # for egress trafics in Asia pacific_hyderabad, mumbai and not represented: india(dehli; kolkata), mexico(queretaro)
    elif VMaws.location=="ap-south-2"or VMaws.location=="ap-south-1":
        # (0.1093, 0.085,0.082, 0.08 )
        
        #between 100GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.1093
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB
        elif DRout_a in interval_next_40TB:
            Cegress=0.085
            aws_toOverseas_link_cost= (0.1093 * (upperbound_interval_0_to_10TB -lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)
       
        #between 50TB and 150TB
        elif DRout_a in interval_next_100TB:
            Cegress=0.082
            aws_toOverseas_link_cost= (0.1093 * (upperbound_interval_0_to_10TB-lowerbound_interval_0_to_10TB)) + (0.085 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)



        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.08
            aws_toOverseas_link_cost= (0.1093 * (upperbound_interval_0_to_10TB -lowerbound_interval_0_to_10TB)) + (0.085 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.082 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)

    # for egress trafics in Asia pacific_seoul
    elif VMaws.location=="ap-northeast-2":
        # (0.126, 0.122, 0.117, 0.108 )
        
        #between 100GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.126
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB (next 40TB)
        elif DRout_a in interval_next_40TB :
            Cegress=0.122
            aws_toOverseas_link_cost= (0.126 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)
       
        #between 50TB and 150TB
        elif DRout_a in interval_next_100TB:
            Cegress=0.117
            aws_toOverseas_link_cost= (0.126 * (upperbound_interval_0_to_10TB- lowerbound_interval_0_to_10TB)) + (0.122 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)


        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.108
            aws_toOverseas_link_cost= (0.126 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.122 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.117 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)

    # for egress trafics from middle east (Bahrain)  
    elif VMaws.location=="me-south-1":
        # (0.117, 0.1105, 0.091, 0.065 )
        
        #between 100GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.117
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB (next 40)
        elif DRout_a in interval_next_40TB:
            Cegress=0.1105
            aws_toOverseas_link_cost= (0.117 * (upperbound_interval_0_to_10TB-lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)

       
        #between 50TB and 150TB (next 100)
        elif DRout_a in interval_next_100TB:
            Cegress=0.091
            aws_toOverseas_link_cost= (0.117 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.1105 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)
            

        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.065
            aws_toOverseas_link_cost= (0.117 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.1105 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.091 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)


    # for egress trafics from Africa_south africa
    elif VMaws.location=="af-south-1":
        # (0.154, 0.147, 0.126, 0.112 )
        
        #between 100GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.154
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB (next 40)
        elif DRout_a in interval_next_40TB:
            Cegress=0.147
            aws_toOverseas_link_cost= (0.154 * (upperbound_interval_0_to_10TB- lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)

       
        #between 50TB and 150TB (next 100)
        elif DRout_a in interval_next_100TB:
            Cegress=0.126
            aws_toOverseas_link_cost= (0.154 * (upperbound_interval_0_to_10TB- lowerbound_interval_0_to_10TB)) + (0.147 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)
            

        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.112
            aws_toOverseas_link_cost= (0.154 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.147 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.126 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)


    # for egress trafics FROM Jakarta
    elif VMaws.location=="ap-southeast-3":
        
        #between 100GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.132
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB
        elif DRout_a in interval_next_40TB:
            Cegress=0.01
            aws_toOverseas_link_cost= (0.132 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)

       
        #between 50TB and 150TB (next 100TB)
        elif DRout_a in interval_next_100TB:
            Cegress=0.095
            aws_toOverseas_link_cost= (0.132 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.01 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)
            

        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.09
            aws_toOverseas_link_cost= (0.132 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.01 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.095 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)


    # for egress trafics from melbourne or sydney
    elif VMaws.location=="ap-southeast-4" or VMaws.location=="ap-southeast-2":
        
        #between 0GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.114
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB
        elif DRout_a in interval_next_40TB:
            Cegress=0.098
            aws_toOverseas_link_cost= (0.114 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)

       
        #between 50TB and 150TB
        elif DRout_a in interval_next_100TB:
            Cegress=0.094
            aws_toOverseas_link_cost= (0.114 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.098 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)
            

        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.092
            aws_toOverseas_link_cost= (0.114 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.098 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.094 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)


    # for egress trafics from 
    elif VMaws.location=="ap-southeast-3":
        
        #between 0GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.132
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB
        elif DRout_a in interval_next_40TB:
            Cegress=0.1
            aws_toOverseas_link_cost= (0.132 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)

       
        #between 50TB and 150TB
        elif DRout_a in interval_next_100TB:
            Cegress=0.095
            aws_toOverseas_link_cost= (0.132 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.1 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)
            

        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.09
            aws_toOverseas_link_cost= (0.132 * (upperbound_interval_0_to_10TB- lowerbound_interval_0_to_10TB)) + (0.1 * (upperbound_interval_next_40TB- upperbound_interval_0_to_10TB))+ (0.095 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)

    
    # for egress trafics from melbourne or sydney
    elif VMaws.location=="ap-northeast-1" or VMaws.location=="ap-northeast-3":
        
        #between 0GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.114
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB
        elif DRout_a in interval_next_40TB:
            Cegress=0.089
            aws_toOverseas_link_cost= (0.114 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)

       
        #between 50TB and 150TB
        elif DRout_a in interval_next_100TB:
            Cegress=0.086
            aws_toOverseas_link_cost= (0.114 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.089 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)
            

        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.084
            aws_toOverseas_link_cost= (0.114 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.089 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.086 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)


    # for egress trafics from melbourne or sydney
    elif VMaws.location=="me-central-1":
        
        #between 0GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.11
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB
        elif DRout_a in interval_next_40TB:
            Cegress=0.085
            aws_toOverseas_link_cost= (0.11 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)

       
        #between 50TB and 150TB
        elif DRout_a in interval_next_100TB:
            Cegress=0.077
            aws_toOverseas_link_cost= (0.11 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.085 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)
            

        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.055
            aws_toOverseas_link_cost= (0.11 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.085 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.077 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)


    # for egress trafics from melbourne or sydney
    elif VMaws.location=="sa-east-1":
        
        #between 0GB and 10TB
        if DRout_a in interval_0_to_10TB:
            Cegress=0.15
            aws_toOverseas_link_cost= DRout_a * Cegress
        
        #between 10TB and 50TB
        elif DRout_a in interval_next_40TB:
            Cegress=0.138
            aws_toOverseas_link_cost= (0.15 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_0_to_10TB)*Cegress)

       
        #between 50TB and 150TB
        elif DRout_a in interval_next_100TB:
            Cegress=0.126
            aws_toOverseas_link_cost= (0.15 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.138 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB)) + ((DRout_a - upperbound_interval_next_40TB)*Cegress)
            

        #more than 150TB
        elif DRout_a in interval_morethan_150TB:
            Cegress=0.114
            aws_toOverseas_link_cost= (0.15 * (upperbound_interval_0_to_10TB - lowerbound_interval_0_to_10TB)) + (0.138 * (upperbound_interval_next_40TB - upperbound_interval_0_to_10TB))+ (0.126 * (upperbound_interval_next_100TB - upperbound_interval_next_40TB)) + ((DRout_a - upperbound_interval_next_100TB)*Cegress)

            
    else:
        Cegress=0
        aws_toOverseas_link_cost=0
        print('Sorry we do not recognise the aws vm location you entered for trafic overseas through aws ntwk (OTP)')

    
    return aws_toOverseas_link_cost
    #print(f'Network cost: {NtwkC_DP}')


"""dataRate1=87000
#dataRate2=560
vm1 = VM(cpu=4, memory=8, csp='aws', location='me-central-1', processingtime=10 )
vm2 = VM(cpu=2, memory=4, csp='azur', location='eu-west-2', processingtime=36)


#vm1 = VM( csp='aws', location='me-central-1' )
#vm2 = VM( csp='azur', location='"eu-west-2"')

cp1 = get_aws_toOverseas_link_cost(vm2, dataRate1)
cp2 = get_aws_toOverseas_link_cost(vm1, dataRate1)

print(cp1)
print(cp2)"""












