class TeaLeaf:

    def __init__(self, age):
        self._age = age

    
    @property
    def age(self):
        """The Getter: Runs when you do 'print(tealeaf.age)'"""
        return self._age + 2
    
    @age.setter
    def age(self, age):
        """The Setter: Runs when you do 'tealeaf.age = 100'"""

        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea Leave, age must be between 1 and 5 years")


leaf = TeaLeaf(2)

print(leaf.age) # Call the getter
leaf.age = 6 #Calls the setter
print(leaf.age)

        