from random import randrange

class Pet(object):
    boredom_threshold = 3
    hunger_threshold = 10
    sounds = ['moo']
    boredom_reduce = 3
    hunger_reduce = 2
    def __init__(self, name):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood_state(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood_state() + ". "
        return state
    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_reduce)
    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()
    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_reduce)
    def feed(self):
        self.reduce_hunger()

class Cat(Pet):
    sounds = ['Meow']

class Dog(Pet):
    sounds = ['Woof', 'Ruff']
    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

class Bird(Pet):
    sounds = ["chirp"]
    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])

class Lab(Dog):
    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None

pet_types = {'dog': Dog, 'lab': Lab,'cat': Cat, 'bird': Bird}
def whichtype(adopt_type="general pet"):

    return pet_types.get(adopt_type.lower(), Pet)

def play():
    animals = []
    base_prompt = """Adopt <pettype> -  dog, cat, lab, poodle, bird, or another unknown pet type\nGreet <petname>\nTeach <petname> <word>\nFeed  <petname>\nQuit\n\nEnter your Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit" or command=="quit" or command=="QUIT":
            print("Exiting...")
            return
        elif command == "Adopt" or command == "adopt" or command == "ADOPT" and len(words) > 1:
            try:
                if whichone(animals, words[1]):
                    feedback += "You already have a pet with that name\n"
                else:
                    if len(words) > 2:
                        new_pet = whichtype(words[2])
                    else:
                        new_pet = Pet
                    animals.append(new_pet(words[1]))
            except:
                print("enter the details correctly. ")

        elif command == "Greet" or command == "greet" or command == "GREET" and len(words) > 1:
            try:
                pet = whichone(animals, words[1])
                if not pet:
                    feedback += "Didn't understand. Please try again.\n"
                    print()
                else:
                    pet.hi()
            except:
                print("enter the details correctly. ")
        elif command == "Teach" or command == "teach" or command == "TEACH" and len(words) > 2:
            try:
                pet = whichone(animals, words[1])
                if not pet:
                    feedback += "Didn't understand. Please try again."
                else:
                    pet.teach(words[2])
            except:
                print("enter the details correctly. ")
        elif command == "Feed" or command == "FEED" or command == "feed" and len(words) > 1:
            try:
                pet = whichone(animals, words[1])
                if not pet:
                    feedback += "Didn't understand. Please try again."
                else:
                    pet.feed()
            except:
                print("enter the details correctly. ")
        else:
            feedback+= "Didn't understand. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()

play()
