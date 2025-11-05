from abc import ABC, abstractmethod

class Weapon:
    total_weapons = 0
    
    def __init__(self, name, capacity, ammo):
        self.name = name
        self.capacity = capacity
        self.ammo = ammo
        self.serial_num = Weapon.total_weapons
        Weapon.total_weapons += 1
        
    def reload(self, ammo):
        if self.ammo + ammo <= self.capacity: 
            self.ammo += ammo
    
    
class Soldier:
    def __init__(self, name, rank, weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon
    
    def report(self):
        print(f'Name: {self.name} Rank: {self.rank} Weapon: {self.weapon.name}')
      
class Unit(ABC):
    def __init__(self, name, commander: Soldier, soldiers: list, equipment: list):
        self.name = name
        self.commander = commander
        self.soldiers = soldiers
        self.equipment = equipment
    
    def briefing(self):
        print(self.name)
        self.commander.report()
    
    @abstractmethod
    def attack(self):
        pass
    
class Infantry(Unit):
    def attack(self):
        print('infantry attack')
        
class TankUnit(Unit):
    def attack(self):
        print('tanks attack')  
        
class SniperUnit(Unit):
    def attack(self):
        print('sniper attack')
        
class StrikeOption:
    def __init__(self, name, ammo, range):
        self.name = name
        self.ammo = ammo
        self.range = range
        
    def strike(self):
        if self.ammo == 0:
            print('out of ammo')
        else:
            self.ammo -= 1
        
    
class Tank(StrikeOption):
    def strike(self):
        super().strike()
        print(f'tank boom in {self.range} range')

class Drone(StrikeOption):
    def strike(self):
        super().strike()
        print(f'drone boom in {self.range} range')
    
d1 = Drone('kamikaze', 1, 'long')
d1.strike()

m4 = Weapon('m4', 120, 30)
ak47 = Weapon('ak47', 120, 30)
galil = Weapon('galil', 120, 30)

s1 = Soldier('gad', 'lieutenant', ak47)
s2 = Soldier('dag', 'ensign', m4)
cap1 = Soldier('tag', 'general', galil)
s3 = Soldier('dan', 'lieutenant', ak47)
s4 = Soldier('ban', 'ensign', m4)
cap2 = Soldier('san', 'general', galil)
s5 = Soldier('pim', 'lieutenant', ak47)
s6 = Soldier('pum', 'ensign', m4)
cap3 = Soldier('pam', 'general', galil)
soldiers1 = [s1, s2]
soldiers2 = [s3, s4]
soldiers3 = [s5, s6]
tank1 = Tank('mercava', 10, 3)
tank2 = Tank('t34', 10, 3)
tank3 = Tank('panter', 10, 3)
drone1 = Drone('shahed', 1, 1)
drone2 = Drone('liutiy', 1, 1)
drone3 = Drone('harop', 1, 1)
equipment1 = [tank1, drone1]
equipment2 = [tank2, drone2]
equipment3 = [tank3, drone3]

unit1 = Infantry('navi', cap1, soldiers1, equipment1)     
unit2 = TankUnit('golani', cap2, soldiers2, equipment2)     
unit3 = SniperUnit('hashmonaim', cap3, soldiers3, equipment3)     
units = [unit1, unit2, unit3]
    
class Agent:
    def __init__(self, name, clearance):
        self.name = name
        self.clearance = clearance
    
class Mission:
    def __init__(self, name, target, assigned_agent, assigned_units: list, clearance):
        self.name = name
        self.target = target
        # if assigned_agent.clearance <= clearance:
        self.assigned_agent = assigned_agent
        # else:
        #     print('agent without sufficient clearance level')
        self.assigned_units = assigned_units
      
    def brief(self):
        print(f'Mission name: {self.name} Target: {self.target} Agent: {self.assigned_agent.name}'
              f' Units: {[unit.name for unit in self.assigned_units]}')
        
class MissionManager:
    def __init__(self, missions: list):
        self.missions = missions
        
    def add_mission(self, mission):
        self.missions.append(mission)
        
    def print_missions(self):
        for miss in self.missions:
            print(miss.name)
            
    def remove_mission(self, miss_name):
        for miss in self.missions:
            if miss.name == miss_name:
                self.missions.remove(miss)
    
    def accomplish(self):
        for miss in self.missions:
            miss.execute()
            
    def find_by_agent(self, agent_name):
        for miss in self.missions:
            if miss.assigned_agent.name == agent_name:
                print(miss.name)
    
ag1 = Agent('mati', 2)    
ag2 = Agent('dani', 1)    
ag3 = Agent('meni', 3)    
                
miss1 = Mission('haravot barzel', 'aza', ag1, [unit1], 1)
miss2 = Mission('blitzkrieg', 'moscow', ag2, [unit2], 2)
miss3 = Mission('barbarosa', 'ussr', ag3, [unit3], 3)

miss_list = [miss1, miss2, miss3]

mm = MissionManager(miss_list)

mm.find_by_agent('mati')

# miss1.brief()
# miss2.assigned_units[0].attack()

class Army:
    total_attacks = 0
    
    def __init__(self, units: list):
        self.units = units
        
    def attack_all(self):
        for unit in units:
            unit.attack()
            Army.total_attacks += 1
            
army1 = Army(units)

# army1.attack_all()

class Commander(Soldier):
    pass

commander = Commander('zxc', 'colonel', m4)

class ReconMission(Mission):
    def execute(self):
        for unit in self.assigned_units:
            unit.attack()

class StrikeMission(Mission):
    def execute(self):
        for unit in self.assigned_units:
            unit.attack()

class RescueMission(Mission):
    def execute(self):
        for unit in self.assigned_units:
            unit.attack()

recon_m = ReconMission('prikol', 'drugoy prikol', ag1, [unit1], 3)
s_m = StrikeMission('ewe prikol', 'kakoy prikol', ag2, [unit2], 2)
rescue_m = RescueMission('takoy prikol', 'zakon4ilis prikoli', ag3, [unit3], 1)

miss_list2 = [recon_m, s_m, rescue_m]

miss_man = MissionManager(miss_list2)

# miss_man.accomplish()

miss_man.find_by_agent('dani')