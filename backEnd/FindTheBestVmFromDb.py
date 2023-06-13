import psycopg2
from vmClass import VM



"""This function finds vms in the database according to user entered parameters, 
and let the user choose the best vm from the results of the research, and returns that unique best vm"""

#def find_corresponding_vms_in_db(id=None, cpu=None, memory=None, hourrate=None, csp=None, location=None):
#def find_corresponding_vms_in_db(cpu=None, memory=None, csp=None, location=None):

def find_TheBestVm_in_db(cpu=None, memory=None, csp=None):    
    
    try:
        
        conn = psycopg2.connect(database="cspvm",
                                host="localhost",
                                user="postgres",
                                password="postgres",
                                port="5432")

        cursor = conn.cursor()

        # Building the query based on the provided parameters
        #query = "SELECT * FROM realazuraws WHERE"
        query = "SELECT * FROM finalrealazurawsdb WHERE"
        conditions = []
        values = []

        if cpu is not None:
            conditions.append("cpu_vm = %s")
            values.append(cpu)
        if memory is not None:
            #int(memory)
            conditions.append("memory_vm = %s")
            values.append(memory)
        if csp is not None:
            conditions.append("csp_vm = %s")
            values.append(csp)
        """if location is not None:
            conditions.append("location_vm = %s")
            values.append(location)"""

        if len(conditions) == 0:
            # No conditions provided, return all VMs
            query += " 1"
        else:
            query += " " + " AND ".join(conditions)

        # Adding an "ORDER BY" clause to sort by hourrate in ascending order
        query += " ORDER BY hourrate_vm ASC"

        # Execute the query and fetch the results
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        results = cursor.fetchall()

        #initialising the chosen vm value
        chosen_vm=None

        #managing exception where no result is returned
        if len(results)==0:
            chosen_vm=None
            raise Exception(f"Sorry, no vms with {cpu} GB cpu and {memory} GB memory in {csp}'s data bases")
        else:

            # Create VM objects from the results and return them as a list
            vms = []
            for row in results:
                vm = VM(*row)
                vms.append(vm)
        
            # Print the list of matching VMs with their hour rates
            """for i, vm in enumerate(vms):
            print(f"{i+1}. {vm} ({vm.hourrate}/hour)")"""
        
            # Print the list of matching VMs with their parameters
            for i, vm in enumerate(vms):
                #print(f"{i+1}. {vm.id}:  ({vm.hourrate}/hour)")
                print(f"{i+1}. vm id: {vm.id}")
                print(f"cpu: {vm.cpu}")
                print(f"memory: {vm.memory}")
                print(f"hour rate: {vm.hourrate}")
                print(f"csp: {vm.csp}")
                print(f"location: {vm.location}")
                print(f"\n")


            # Ask the user to choose a VM from the list
            choice = input("Choose a VM from the above list (enter a number): ")
            print(f"\n")
            vm_index = int(choice) - 1


            # Get the chosen VM and store its parameters in variables
            chosen_vm = vms[vm_index]
            chosen_cpu = chosen_vm.cpu
            chosen_memory = chosen_vm.memory
            chosen_hourrate = chosen_vm.hourrate
            chosen_csp = chosen_vm.csp
            chosen_location = chosen_vm.location


            # Display the chosen VM's parameters
            print("Chosen VM parameters:")
            print(f"CPU: {chosen_cpu}")
            print(f"Memory: {chosen_memory}")
            print(f"Hour rate: {chosen_hourrate}")
            print(f"CSP: {chosen_csp}")
            print(f"Location: {chosen_location}")




        # closing database connection.
        conn.close()

            
    except (Exception, psycopg2.Error) as error:
        #print("Failed to research in data base AAA and in table xxx: ", error)
        print(error)

        
    #return vms
    return chosen_vm



#find_corresponding_vms_in_db(cpu=4, memory=8, csp='aws', location='us-east-1')
#find_TheBestVm_in_db(cpu=4, memory=8, csp='aws')       