import json
import psycopg2

class VM:
    def __init__(self, cpu, memory, csp, location):
        self.cpu = cpu
        self.memory = memory
        self.csp = csp
        self.location = location
        self.links = []

    def add_link(self, vm, data_rate):
        self.links.append((vm, data_rate))

# Function to create VM objects
def create_vms(config):
    vms = []
    for vm_data in config["vms"]:
        cpu = vm_data["cpu"]
        memory = vm_data["memory"]
        csp = vm_data["csp"]
        location = vm_data["location"]
        vm = VM(cpu, memory, csp, location)
        vms.append(vm)
    return vms

# Function to establish links between VMs
def establish_links(vms, config):
    for i, vm in enumerate(vms):
        for link_data in config["vms"][i]["links"]:
            link_vm_num = link_data["vm"]
            data_rate = link_data["data_rate"]
            linked_vm = vms[link_vm_num - 1]
            vm.add_link(linked_vm, data_rate)

# Function to compute total cost for nodes with CSP "aws"
def compute_aws_cost(vms):
    total_cost = 0
    for vm in vms:
        if vm.csp == "aws":
            # Compute cost for AWS node based on CPU, memory, or other factors
            # Add the cost to the total_cost variable
            total_cost += 1  # Placeholder cost value, replace with actual calculation
    return total_cost

# Function to compute total cost for nodes with CSP "azure"
def compute_azure_cost(vms):
    total_cost = 0
    for vm in vms:
        if vm.csp == "azure":
            # Compute cost for Azure node based on CPU, memory, or other factors
            # Add the cost to the total_cost variable
            total_cost += 1  # Placeholder cost value, replace with actual calculation
    return total_cost

# Function to compute total cost for links between "aws" and "azure" nodes
def compute_aws_azure_link_cost(vms):
    total_cost = 0
    for vm in vms:
        for linked_vm, data_rate in vm.links:
            if vm.csp == "aws" and linked_vm.csp == "azure":
                # Compute cost for AWS to Azure link based on data rate or other factors
                # Add the cost to the total_cost variable
                total_cost += 1  # Placeholder cost value, replace with actual calculation
    return total_cost

# Function to compute total cost for links between "azure" and "aws" nodes
def compute_azure_aws_link_cost(vms):
    total_cost = 0
    for vm in vms:
        for linked_vm, data_rate in vm.links:
            if vm.csp == "azure" and linked_vm.csp == "aws":
                # Compute cost for Azure to AWS link based on data rate or other factors
                # Add the cost to the total_cost variable
                total_cost += 1  # Placeholder cost value, replace with actual calculation
    return total_cost

# Function to compute the overall cost
def compute_overall_cost(vms):
    aws_cost = compute_aws_cost(vms)
    azure_cost = compute_azure_cost(vms)
    aws_azure_link_cost = compute_aws_azure_link_cost(vms)
    azure_aws_link_cost = compute_azure_aws_link_cost(vms)

    total_cost = aws_cost + azure_cost + aws_azure_link_cost + azure_aws_link_cost
    return total_cost

# Function to look for corresponding VMs in the database
def lookup_vms_in_database(vms):
    conn = psycopg2.connect(database="your_database", user="your_user", password="your_password", host="your_host", port="your_port")
    cursor = conn.cursor()

    for vm in vms:
        query = f"SELECT * FROM vms_table WHERE cpu={vm.cpu} AND memory={vm.memory} AND csp='{vm.csp}' AND location='{vm.location}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            vm_id = result[0]  # Assuming the first column is the VM ID
            print(f"VM found in the database with ID: {vm_id}")
        else:
            print("VM not found in the database")

    cursor.close()
    conn.close()

# Read configuration from file
with open('config.json') as config_file:
    config = json.load(config_file)

# Create VMs based on the configuration
vms_list = create_vms(config)

# Look for corresponding VMs in the database
lookup_vms_in_database(vms_list)

# Establish links between VMs
establish_links(vms_list, config)

# Compute the costs
aws_cost = compute_aws_cost(vms_list)
azure_cost = compute_azure_cost(vms_list)
aws_azure_link_cost = compute_aws_azure_link_cost(vms_list)
azure_aws_link_cost = compute_azure_aws_link_cost(vms_list)
overall_cost = compute_overall_cost(vms_list)

# Print the costs
print("AWS Node Cost:", aws_cost)
print("Azure Node Cost:", azure_cost)
print("AWS to Azure Link Cost:", aws_azure_link_cost)
print("Azure to AWS Link Cost:", azure_aws_link_cost)
print("Overall Cost:", overall_cost)
