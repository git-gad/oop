class Agent:
    count = 0
    
    def __init__(self, code_name, clearance_level):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.count += 1
        
    def report(self):
        print(f'Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}')
        
    def get_clearance_level(self):
        print(self._clearance_level)
        
    def set_clerance_level(self, level):
        if 1 <= level <= 10:    
            self._clearance_level = level
            
    @classmethod
    def get_total_agents(cls):
        return cls.count
        
class Mission:
    def __init__(self, mission_name, target_location, assigned_agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent
        
    def brief(self):
        print(f'Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.assigned_agent.code_name}')
        
class FieldAgent(Agent):
    def __init__(self, code_name, clearance_level, region):
        super().__init__(code_name, clearance_level)
        self.region = region
        
    def report(self):
        print(f'Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}. Region: {self.region}')
        
class CyberAgent(Agent):
    def __init__(self, code_name, clearance_level, specialty):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty
        
    def report(self):
        print(f'Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}. Specialty: {self.specialty}')

ag1 = Agent('gad', 1)
ag2 = CyberAgent('dag', 2, 'cs1.6')
ag3 = FieldAgent('avi', 3, 'Russia')

agents_list = [ag1, ag2, ag3]
 
class AgencyDirector:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name):
        self.name = name
        
ad1 = AgencyDirector('gad')
ad2 = AgencyDirector('dag')

print(ad1 is ad2)