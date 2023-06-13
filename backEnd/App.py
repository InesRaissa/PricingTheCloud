from vmClassForConfigFile import VM
from totalOperationalCost import get_total_operational_cost
from FindTheBestVmFromDbConfigF import find_TheBestVm_in_db
from totalNetworkCost import get_total_network_cost
from totalCost import get_total_costs

from flask import Flask, render_template, request, jsonify

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    #user='ines'
    if request.method=='POST':
        num_vms = int(request.form['num_vms'])
        vmList_beforeDbSearch= []
        vmList_afterDbSearch= []

        for i in range(num_vms):
            """id = None
            cpu = int(request.form[f'cpu{i}'])
            memory = float(request.form[f'memory{i}'])
            hourrate=None
            location = request.form[f'location{i}']
            csp = request.form[f'csp{i}']
            processtime = float(request.form[f'processtime{i}'])
            
            vm = VM(id, cpu, memory, hourrate, location, csp, processtime)
            vmList_beforeDbSearch.append(vm)"""

            vm = {
                'id': None,
                'cpu': int(request.form['cpu{}'.format(i)]),
                'memory': int(request.form['memory{}'.format(i)]),
                'hourrate': None,
                'location': request.form['location{}'.format(i)],
                'csp': request.form['csp{}'.format(i)],
                'processtime': float(request.form['processtime{}'.format(i)]),
                
            }
            
            vmList_beforeDbSearch.append(vm)

           # vm_afterDb=find_TheBestVm_in_db(vm)
            #vm_afterDb.processingtime= processtime
            
        
            # The vm list after user's choice
            #vmList_afterDbSearch.append(vm_afterDb)
            #vms.append(vm)"""

        #retrieving the data rates? Hopefully the logic will be the same
        for i in range(num_vms):
            for j in range(num_vms):
                if i != j:
                    data_rate = float(request.form[f'data_rate{i}_{j}'])
                    vmList_beforeDbSearch[i].add_link(vmList_beforeDbSearch[j], data_rate)


        for vm in vmList_beforeDbSearch:
            chosen_vm = find_TheBestVm_in_db(vm)
            vm.id = chosen_vm.id
            vm.cpu = chosen_vm.cpu
            vm.memory = chosen_vm.memory
            vm.hourrate=chosen_vm.hourrate
            vm.location = chosen_vm.location
            vm.csp = chosen_vm.csp
            
            #The processing time remains the one entered by the end user
            vm.processtime = processtime
            vmList_afterDbSearch.append(vm)
        

        #Retrieving the costs
        #Retrieving the operational cost
        total_operational_cost= get_total_operational_cost(vmList_afterDbSearch)
    
        #Retrieving the network cost
        total_network_cost= get_total_network_cost(vmList_afterDbSearch)

        #Computing the overall total cost
        total_costs= get_total_costs(vmList_afterDbSearch)

        return render_template('index.html', show_form=False, show_results=True,
                               operational_cost=total_operational_cost, network_cost=total_network_cost,
                               total_cost=total_costs)
    
    
    return render_template('index.html', show_form=True, show_results=False)


@app.route('/search_vm', methods=['POST'])
def search_vm():
    vm_data = request.get.json

    cpu = vm_data['cpu']
    memory = vm_data['memory']
    hourrate = vm_data['hourrate']
    location = vm_data['location']
    csp = vm_data['csp']
    
    vm = VM(id,cpu, memory, hourrate, location, csp)
    chosen_vm = find_TheBestVm_in_db(vm)

    response = {
        'id': 'VM001',
        'cpu': 4,
        'memory': 16,
        'hourrate': 0.5,
        'location': 'us-west-2',
        'csp': 'aws',
        
    }

    return jsonify(response)

    """if chosen_vm:
        return jsonify(id=chosen_vm.id, cpu=chosen_vm.cpu, memory=chosen_vm.memory, hourrate=chosen_vm.hourrate, location=chosen_vm.location, csp=chosen_vm.csp)
    else:
        return jsonify(error="No suitable VM found")"""

if __name__ == '__main__':
    app.run()



