#from vmClass import VM
from operator import mul


"""This function retrieve the cost per data rate for a link between two vms belonging to aws 
knowing the location of the 2 vms
The costs per data rate considered are taken from real aws costs dataset (April 2023)
vma is the egress vm (the one that initiates the trafic) and vmb is the ingress traffic"""

def get_Aws_to_aws_costPerDataRate(vma, vmb):
    
    #retrieving the location of the egress vm
    dicoAllAwsRegions=['us-east-1','us-east-2','us-west-1','us-west-2','us-gov-east-1','us-gov-west-1',
                       'ap-east-1','ap-south-2','ap-southeast-3','ap-southeast-4','ap-south-1',
                       'ap-northeast-3', 'ap-northeast-2', 'ap-southeast-1','ap-southeast-2', 'ap-northeast-1',
                       'eu-central-1', 'eu-central-2','eu-west-1','eu-west-2','eu-west-3',
                        'eu-south-1', 'eu-south-2','eu-north-1','me-south-1', 'me-central-1',
                        'ca-central-1','af-south-1']
    
    aws_to_aws_CostPerDR=-1

    # for egress trafics from Asia pacific (mumbai, Hyderabad), and not represented:india (dehli, kolkata)
    if vma.location=="ap-south-2" and vmb.location in dicoAllAwsRegions or vma.location=="ap-south-1" and vmb.location in dicoAllAwsRegions:
        aws_to_aws_CostPerDR=0.086
    
    # for egress trafics from Asia pacific (Hong Kong, singapore, osaka), and not represented:KDDI (osaka, Tokyo)
    elif vma.location=="ap-east-1"and vmb.location in dicoAllAwsRegions or vma.location== "ap-southeast-1" and vmb.location in dicoAllAwsRegions or vma.location== "ap-northeast-3"and vmb.location in dicoAllAwsRegions or vma.location== "ap-northeast-1"and vmb.location in dicoAllAwsRegions:
        aws_to_aws_CostPerDR=0.09

    # for egress trafics from Asia pacific sydney to melbourne et vice-versa
    elif vma.location== "ap-southeast-2" and vmb.location== "ap-southeast-4":
        aws_to_aws_CostPerDR=0.08

    # for egress trafics from Asia pacific sydney to all other aws regions except melbourne
    elif vma.location== "ap-southeast-2" and vmb.location in list(set(dicoAllAwsRegions) - set(["ap-southeast-4"])):
        aws_to_aws_CostPerDR=0.098

    # for egress trafics from Asia pacific (seoul, ), and not represented:SKT (seoul, Daejeon,
    elif vma.location== "ap-northeast-2" and vmb.location in dicoAllAwsRegions:
        aws_to_aws_CostPerDR=0.08

    # for egress trafics from all Europe (ireland, London, Paris, Milan, Spain, Stokholm, zurich) usa (california, oregon,)
    
   # elif vma.location=="eu-west-1"and vmb.location in dicoAllAwsRegions or vma.location== "eu-west-2"and vmb.location in dicoAllAwsRegions or vma.location== "eu-west-3"and vmb.location in dicoAllAwsRegions or vma.location== "eu-south-1"and vmb.location in dicoAllAwsRegions or vma.location== "eu-south-2"and vmb.location in dicoAllAwsRegions or vma.location== "eu-north-1"and vmb.location in dicoAllAwsRegions or vma.location=="us-west-1" or vma.location== "us-west-2"and vmb.location in dicoAllAwsRegions or vma.location== "eu-central-1"and vmb.location in dicoAllAwsRegions or vma.location== "eu-central-2"and vmb.location in dicoAllAwsRegions:
    elif vma.location in ["eu-west-1","eu-west-2", "eu-west-3", "eu-south-1", "eu-south-2", "eu-north-1", "us-west-1", "us-west-2", "eu-central-1", "eu-central-2"] and vmb.location in dicoAllAwsRegions:   
        aws_to_aws_CostPerDR=0.02

    # for egress trafics between ohio and N virginia
    elif vma.location=="us-east-1" and vmb.location== "us-east-2" or vma.location== "us-east-2" and vmb.location== "us-east-1":
        aws_to_aws_CostPerDR=0.01

    # for egress trafics from ohio and N virginia to other regions
    elif vma.location=="us-east-1" and vmb.location!= "us-east-2" or vma.location== "us-east-2" and vmb.location!= "us-east-1":
        aws_to_aws_CostPerDR=0.02
    
    # for egress trafics from Middle East (Bahrain to other regions
    elif vma.location=="me-south-1" and vmb.location in dicoAllAwsRegions:
        aws_to_aws_CostPerDR=0.1105

    # for egress trafics from us gov (east and west) to other regions
    elif vma.location=="us-gov-east-1" and vmb.location in dicoAllAwsRegions or vma.location=="us-gov-west-1" and vmb.location in dicoAllAwsRegions:
        aws_to_aws_CostPerDR=0.03

    # for egress trafics from south africa to other regions
    elif vma.location=="af-south-1" and vmb.location in dicoAllAwsRegions:
        aws_to_aws_CostPerDR=0.147

    # for egress trafics from south africa to other regions
    elif vma.location=="ap-southeast-4" and vmb.location=="ap-southeast-2":
        aws_to_aws_CostPerDR=0.08

    # for egress trafics from melbourne to Bahrain
    elif vma.location=="ap-southeast-4" and vmb.location=="me-south-1":
        aws_to_aws_CostPerDR=0.14

    # for egress trafics from melbourne to UAE
    elif vma.location=="ap-southeast-4" and vmb.location=="me-central-1":
        aws_to_aws_CostPerDR=0.14

    # for egress trafics from melbourne to other regions
    elif vma.location=="ap-southeast-4" and vmb.location in list(set(dicoAllAwsRegions) - set(["ap-southeast-2", "me-south-1", "me-central-1"])):
        aws_to_aws_CostPerDR=0.1

     # for egress trafics from melbourne to UAE
    elif vma.location=="ap-southeast-3" and vmb.location in dicoAllAwsRegions:
        aws_to_aws_CostPerDR=0.1

    # for egress trafics from melbourne to other regions
    elif vma.location=="me-central-1" and vmb.location in dicoAllAwsRegions:
        aws_to_aws_CostPerDR=0.085

    # for egress trafics from melbourne to other regions
    elif vma.location=="sa-east-1" and vmb.location in dicoAllAwsRegions:
        aws_to_aws_CostPerDR=0.138

    else:
         print('no such region in inter aws regions dictionnary')
         aws_to_aws_CostPerDR=0


    return aws_to_aws_CostPerDR
    

          
