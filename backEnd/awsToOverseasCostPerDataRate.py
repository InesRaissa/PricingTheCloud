from vmClass import VM
from operator import mul


"""This function retrieve the cost per data rate for a link between two vms, one belonging to aws 
and the other belonging to another provider. 
The costs per data rate considered are taken from real aws costs dataset (April 2023).
The following zones have not been represented: SKT(Daejeon and seoul), India(Dehli and Kolkata), 
Taiwan, Lagos, USA(minneapolis, )
vma is the egress vm (the one that initiates the trafic) and vmb is the ingress traffic"""



#VMaws is the vm which initiates the traffic on the link (egress vm)
def get_aws_toOverseas_costPerDataRate(VMaws, DRout):

    DRout_a= int(DRout)
    Cegress=-1

    # From asia pacific(Hong Kong and Singapore)
    if VMaws.location=="ap-east-1" or VMaws.location=="ap-southeast-1":

        #for trafic between 0GB and 10 TB 
        if 0 < DRout_a <=10240:
            Cegress=0.12
        
        #for trafic between 10TB and 50TB (the next 40 TB)
        elif 10240 < DRout_a <=51200:
            Cegress=0.085

        #for trafic between 50TB and 150TB (the next 100TB)
        elif 51200 < DRout_a <=153600:
            Cegress=0.0082

        #for trafic more than 150TB
        elif DRout_a >153600:
            Cegress=0.08

    # for egress trafics from europe(all), us(all)
    elif VMaws.location=="eu-west-1" or VMaws.location== "eu-west-2" or VMaws.location== "eu-west-3" or VMaws.location== "eu-south-1" or VMaws.location== "eu-south-2" or VMaws.location== "eu-north-1" or VMaws.location=="us-west-1" or VMaws.location== "us-west-2" or VMaws.location== "us-east-1" or VMaws.location== "us-east-2" or VMaws.location== "eu-central-1" or VMaws.location== "eu-central-2" or VMaws.location== "ca-central-1":
        
        #between 0GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.09
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.085
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.07

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.05
    
    # for egress trafics in Asia pacific_hyderabad, mumbai and not represented: india(dehli; kolkata), mexico(queretaro)
    elif VMaws.location=="ap-south-2"or VMaws.location=="ap-south-1":
        
        #between 100GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.1093
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.085
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.082

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.08

    # for egress trafics in Asia pacific_seoul
    elif VMaws.location=="ap-northeast-2":
        
        #between 100GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.126
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.122
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.117

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.108

    # for egress trafics from middle east (Bahrain)  
    elif VMaws.location=="me-south-1":
        
        #between 100GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.117
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.1105
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.091

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.065

    # for egress trafics from Africa_south africa
    elif VMaws.location=="af-south-1":
        
        #between 100GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.154
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.147
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.126

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.112

    # for egress trafics FROM Jakarta
    elif VMaws.location=="ap-southeast-3":
        
        #between 100GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.132
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.01
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.095

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.09

    # for egress trafics from melbourne or sydney
    elif VMaws.location=="ap-southeast-4" or VMaws.location=="ap-southeast-2":
        
        #between 0GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.114
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.098
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.094

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.092

    # for egress trafics from 
    elif VMaws.location=="ap-southeast-3":
        
        #between 0GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.132
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.1
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.095

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.09
    
    # for egress trafics from melbourne or sydney
    elif VMaws.location=="ap-northeast-3":
        
        #between 0GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.114
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.089
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.086

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.084

    # for egress trafics from melbourne or sydney
    elif VMaws.location=="me-central-1":
        
        #between 0GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.11
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.085
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.077

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.055

    # for egress trafics from melbourne or sydney
    elif VMaws.location=="sa-east-1":
        
        #between 0GB and 10TB
        if 0 < DRout_a <=10240:
            Cegress=0.15
        
        #between 10TB and 50TB
        elif 10240 < DRout_a <=51200:
            Cegress=0.138
       
        #between 50TB and 150TB
        elif 51200 < DRout_a <=153600:
            Cegress=0.126

        #more than 150TB
        elif DRout_a >153600:
            Cegress=0.114
            
    else:
        Cegress=0
        print('Sorry we do not recognise the aws vm location you entered for trafic overseas through aws ntwk (OTP)')

    
    return Cegress
    #print(f'Network cost: {NtwkC_DP}')


dataRate1=34
dataRate2=560
"""vm1 = VM(cpu=4, memory=8, csp='aws', location='me-central-1', processingtime=10 )
vm2 = VM(cpu=2, memory=4, csp='azur', location='us-east-2', processingtime=36)"""


"""vm1 = VM( csp='aws', location='me-central-1' )
vm2 = VM( csp='azur', location='eu-south-1')

cp1 = get_aws_toOverseas_costPerDataRate(vm2, dataRate1)
cp2 = get_aws_toOverseas_costPerDataRate(vm1, dataRate1)

print(cp1)
print(cp2)"""












