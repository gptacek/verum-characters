import dictionaries

# to help with character creation, will automatically give ability values/modifier
# and skill modifiers. will also calculate starting health 
#
# requires inputs for class, origin (and sub-origin), and race
# players can also choose a god for lip service (and possible church boon)
# also requires chosen proficiencies

class verum_char:
    def __init__(self):
        abilities = {"str": 10, "dex": 10, "con": 10, "int" : 10, "wis" : 10, "cha" : 10}
        skills = [0] * 19 #18 on default sheet, 19th being martial
        health = 0
        speed  = 0 #is walking speed, flying/swimming/climbing has to be saved somewhere else sorry ;w;

    #finish this helper
    def choose_ability(self, String: value):
        for key,value in self.abilities.items():
            print(key) #test

    #finish this helper
    def choose_skill(self, String: value):
        for x in range(len(self.skills)):
            print(x)

    # for choosing race
    def choose_race(self):
        print("Ok, you're gonna choose a race (and possible sub-race) now from the following list")
        print("For sub-categories, the names are abberviated to 3/4 characters")
        print("Please note that tritons and dragonborn are under the other category")
        races = dictionaries.races
        for key, value in races.items():
            print(key)
        chosen_cate = input("Enter your choice: ")
        print(races[chosen_cate])
        chosen_sub = input("Enter your choice: ")
        race_choice = chosen_cate
        race_choice += ": "
        race_choice += chosen_sub
        print(race_choice)
        for x in range(len(races[chosen_cate][chosen_sub])):
            self.choose_ability(races[chosen_cate][chosen_sub][x])
            self.choose_skill(races[chosen_cate][chosen_sub][x])
        
        

obj = verum_char()
obj.choose_race()