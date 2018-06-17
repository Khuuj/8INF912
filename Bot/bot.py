class game:

    def __init__(self):
        #LOAD VALUES OF LEARNER
        self._actions = 
        self._values =
        self._policies =

    def new_game(self, bot, opponent):
        self._bot = player(bot)
        self._opponent = player(opponent)


class player:

    heroClasses = {
        "Hero_01":"Warrior",
        "Hero_02":"",
        "Hero_03":"Rogue",
        "Hero_04":"",
        "Hero_05":"",
        "Hero_06":"Druid",
        "Hero_07":"Warlock",
        "Hero_08":"",
        "Hero_09":"Priest",
    }

    def __init__(self, heroId):
        self._hero_class = self.heroClasses[heroId]
        self._hero_power = hero_power(self._hero_class)
        

class hero_power:
    
    heroPowersName = {
        "Rogue": "Dagger Mastery",
        "Warrior": "Armor up",
        "Mage": "Fireblast",
        "Priest": "Lesser Heal",
        "Hunter": "Steady shot",
        "Paladin": "Reinforce",
        "Druid": "Shapeshift",
        "Warlock": "Lifetap",
        "Shaman": "Totemic call"
    }

    heroPowersValue = {
        "Dagger Mastery": (1,2),
        "Armor up": 2,
        "Fireblast": 1,
        "Lesser Heal": 2,
        "Steady shot": 2,
        "Reinforce": (1,1),
        "Shapeshift": (1,1),
        "Lifetap": 2,
        "Totemic call": ,
    }

    heroPowersTarget = {
        "Dagger Mastery": "self,
        "Armor up":"self",
        "Fireblast":"any",
        "Lesser Heal":"any",
        "Steady shot":"opponent",
        "Reinforce":"board",
        "Shapeshift":"self",
        "Lifetap":"self",
        "Totemic call":"board",
    }


    def __init__(self, hero_class):
        self._hero_power_name = self.heroPowersName[hero_class]
        self._exhausted = False
        self._upgraded = False
        self._base_cost = 2
        self._cost = 2
        set_hero_power_base_value(self, self._hero_power_name)
        ##################################################


    def use_hero_power(self, target = None):
        #choose target
        possible_target = heroPowersTarget(self._hero_power_name)
        if target == None:
            if possible_target == "self":
                #################################
        self._exhausted = True

    def reset_hero_power(self):
        self._exhausted = False

    def set_hero_power_cost(self, cost):
        self._cost = cost

    def set_hero_power_base_value(self, _hero_power_name):
        
        if self._hero_power_name in heroPowersValue:
            self._base_value = heroPowersValue[self._hero_power_name]
            self._value = heroPowersValue[self._hero_power_name]
        else:
            self._base_value = 0
            self._value = 0

    def set_hero_power_value(self, dalue):
        self._value = value