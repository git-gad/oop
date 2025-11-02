class Agent:
    def __init__(self, code_name, unit, clearance_level):
        self.code_name = code_name
        self.unit = unit
        self.__clearance_level = clearance_level
        
    def get_clearance_level(self):
        return self.__clearance_level
    
    def set_clearance_level(self, level: int):
        if 1 <= level <= 5:    
            self.__clearance_level = level
        
    def report(self):
        print(f'Agent {self.code_name} reporting. Clearance level: {self.get_clearance_level()}')

class Mission:
    def __init__(self, name, location, agent):
        self.mission_name = name
        self.target_location = location
        self.assigned_agent = agent
        
    def brief(self):
        print(f"Mission: {self.mission_name}, Traget: {self.target_location}, Agent: {self.assigned_agent.code_name}")

class IntelTools:
    @staticmethod
    def encrypt_message(msg: str):
        return msg[::-1]
    
    @classmethod
    def log_transmission(cls, agent_name: str, message: str):
        print(f'{agent_name} sent encrypted message: {IntelTools.encrypt_message(message)}')
            
class Report:
    def __init__(self, summary, urgency_level, agent: Agent):
        self.summary = summary
        self.urgency_level = urgency_level
        self.agent = agent
        
class MissionControl:
    @classmethod
    def analyze_report(cls, r: Report):
        if r.urgency_level >= 4:
            print("Immediate response required.")
        elif r.urgency_level == 3: 
            print("High priority. Monitor closely.")
        else:
            print("Routine analysis.")
    

agent_007 = Agent('bond', '8200', 1)

report = Report('gad is terrorist', 5, agent_007)

MissionControl.analyze_report(report)

IntelTools.log_transmission(agent_007.code_name, report.summary)