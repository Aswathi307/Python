print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
class Kangaroo:
    def __init__(self, name, pouch_contents=None):
        self.name = name
        if pouch_contents is None:
            self.pouch_contents = []
        else:
            self.pouch_contents = pouch_contents

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        contents = ''
        for item in self.pouch_contents:
            contents += f'  - {item}\n'
        return f"{self.name}'s pouch contains:\n{contents if contents else '  (empty)'}"
kanga = Kangaroo("Kanga")
roo = Kangaroo("Roo")

kanga.put_in_pouch("banana")
kanga.put_in_pouch("hat")
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
