from vmClass import VM
import pandas as pd
#this is a test of a function that has nothing to do with backEnd development I am doing

class Solution(object):
#nums=[]
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        for i in range (len(nums)):
            for j  in range (len(nums)):
                if nums[i]+nums[j]==target:
                    rtype=[i,j]
                    break

        #print(rtype)
                #else:
                #   print ('error')


#sol= Solution()
#sol.twoSum([1,4,9,3], 7)

#Testing exceptions in lists
suits = ["h", "c", "d", "s", "g", "a", "r"]
noclubs = list(set(suits) - set(["c", "h", "a"]))
"""print(f'{noclubs}')
print(type(noclubs))"""


#testing VM objects sorting

"""vm1 = VM(cpu=4, memory=8, csp='azur', location='uksouth', processingtime=23)
vm2 = VM(cpu=2, memory=4, csp='azur', location="easus", processingtime=20.76)
vm3 = VM(cpu=5, memory=25, csp='aws', location='ap-southeast-1', processingtime=298)
vm4 = VM(cpu=6, memory=67, csp='aws', location="eu-north-1", processingtime=223)
vm5 = VM(cpu=8, memory=23, csp='azur', location="us-east-1", processingtime=2376)


vmlist=[vm1,vm3,vm5]"""
"""azur_vms=[]
aws_vms=[]"""

"""for vm in vmlist:
    #print(vm.csp)
    azur_vms1 = [vm for vm in vmlist if vm.csp == "azur"]
    aws_vms1 = [vm for vm in vmlist if vm.csp == "aws"]

print(azur_vms1)
print(aws_vms1)


for i, vm in enumerate(vmlist):
    print(f"\nCreating links for VM {i+1}:")
    for j, linked_vm in enumerate(vmlist):
        if i != j:
            data_rate = input(f"Enter the data rate between VM {i+1} and VM {j+1} (Mbps): ")
            vm.add_link(linked_vm, data_rate)


#azur_link_cost = 0
for vm in azur_vms1:
    for linked_vm, data_rate in vm.links.items():
        print(f"vm_azur: {vm}-->linkedVm: {linked_vm}:{data_rate}\n")

#azur_link_cost = 0
for vm in aws_vms1:
    for linked_vm, data_rate in vm.links.items():
        print(f"vm_aws: {vm}-->linkedVm: {linked_vm}:{data_rate}\n")"""
        



#representing intervals


def testInterval(nber):
    interval1= pd.Interval (10,30)
    interval2 = pd.Interval(30, 70)

    if nber in interval1:
        print(f'This nber ({nber}) belongs to {interval1}')
    elif nber in interval2:
        print(f' This nber ({nber}) belongs to {interval2}')
    else:
        print(f' This number ({nber}) neither belong to {interval1} nor to {interval2}')


#print("Interval1...\n",interval1)
#print("Interval2...\n",interval2)

nber= 17

testInterval(nber)
