"""This class defines Vms and the corresponding links between those vms without the configParser file."""

class VM:
    #def __init__(self, csp, location):
    #def __init__(self, id, cpu, memory, csp, location, processingtime):
    #def __init__(self, id, cpu, memory, hourrate, csp, location, processingtime):
    #def __init__(self, id=None, cpu=None, memory=None, hourrate=None, location=None, csp=None):
    def __init__(self, id=None, cpu=None, memory=None, hourrate=None, location=None, csp=None, processingtime=None):
    
        self.id = id
        self.cpu = cpu
        self.memory = memory
        self.hourrate = hourrate
        self.location = location
        self.csp = csp
        self.processingtime=processingtime
        self.links = {}
   

    def add_link(self, vm, data_rate):
        self.links[vm] = data_rate

   

    """def add_link(self, vm, data_rate):
        self.links.append((vm, data_rate))"""

    
    