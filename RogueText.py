#Class used to define the general parent of many hero types and skills
class Hero:
    #these three change variables are going to be used during combat(temporary buffs or debuffs)
    attackChange = 0
    defenseChange = 0
    speedChange = 0
    skillSet = []

    def __init__(self,name,health,attack,defense,speed) -> None:
        self.health = health
        self.currentHealth = self.health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
    
    def addSkill(self,skill):
        if(len(self.skillSet)<5):
            self.skillSet.append(skill)
        else:
            self.removeSkill()
    #TODO: complete selectSkill to allow all other parts of the Hero class to use it
    def selectSkill(self):
        pass

    def removeSkill(self):
        self.displaySkills()
        removeSkill = int(input("Enter the number you want to delete"))
        self.skillSet.pop(removeSkill-1)

    def applySkill(self,skill):
        self.currentHealth += skill.hpChange
        self.attackChange = skill.atkChange
        self.defenseChange = skill.defChange
        self.speedChange = skill.spdChange

    def displayHero(self):
        print(f"Hero Name: {self.name}\tHP: {self.currentHealth}/{self.health}\tAttack: {self.attack-self.attackChange}\tDefense: {self.defense-self.defenseChange}\tSpeed: {self.speed-self.speedChange}")

    def displaySkills(self):
        for skill in self.skillSet:
            skill.displaySkill(self)

#Children classes of heroes with set names and not set stats(this can be changed in the future)
class Crusader(Hero):
    def __init__(self, health, attack, defense, speed) -> None:
        super().__init__("Crusader", health, attack, defense, speed)

    def displayHero(self):
        super().displayHero()


class Ranger(Hero):
    def __init__(self, health, attack, defense, speed) -> None:
        super().__init__("Ranger",health, attack, defense, speed)

    def displayHero(self):
        super().displayHero()



#Class used to be used as a generic parent for many children to use as a base ground for skills
class Skill:
    def __init__(self,name,dmg,hpChange,atkChange,defChange,spdChange) -> None:
        self.name = name
        self.dmg = dmg
        self.hpChange = hpChange
        self.atkChange = atkChange
        self.defChange = defChange
        self.spdChange = spdChange
    
    def displaySkill(self):
        print(self.name + ": ",end= "")

class Strike(Skill):
    def __init__(self) -> None:
        super().__init__("Strike", 6, 0, 0, 0, 0)

    def displaySkill(self,hero):
        super().displaySkill()
        print(f"Deals {self.dmg + hero.attack} damage")

class DoubleEdgeStrike(Skill):
    def __init__(selfe) -> None:
        super().__init__("Double Edged Strike", 10, -2, 0, 0, 0)

    def displaySkill(self,hero):
        super().displaySkill()
        print(f"Deals {self.dmg + hero.attack} damage. Take {self.hpChange} damage.")


x = Crusader(50,25,20,15)
x.addSkill(Strike())
x.addSkill(DoubleEdgeStrike())
x.displayHero()
x.displaySkills()
x.applySkill(x.skillSet[1])
x.displayHero()
