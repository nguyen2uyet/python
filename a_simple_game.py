def get_input():
  command =  input(" : ").split()
  if command[0] in verb_dict:
    verb = verb_dict[command[0]]
  else:
    print("Unknown verb {}".format(command[0]))
    return
  
  if len(command) >= 2:
    print(verb(command[1]))
  else:
    print(verb("nothing"))

class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self,name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + " : "+ self.name + "\n" + self.desc

class Goblin(GameObject):
    class_name = "goblin"
    desc = "A fool creature"

class Elf(GameObject):
    class_name = "elf"
    desc = "Very powerful"

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There no {}".format(noun)

def say(noun):
  return 'You said "{}"'.format(noun)

def listen(noun):
  return 'You listened "{}"'.format(noun)

verb_dict = {
  "say": say,
  "listen":listen,
  "examine":examine,
}


goblin = Goblin("Dobly")
elf = Elf("Negolas")

while True:
  get_input()