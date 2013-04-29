class Person:

    def __init__(self, name, birth_year, gender,
                 father=None, mother=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.father = father
        self.mother = mother
        self._children = []
        if father:
            father.add_child(self)
        if mother:
            mother.add_child(self)

    def add_brother(self, brother):
        self.brothers.append(brother)

    def add_sister(self, sister):
        self.sisters.append(sister)

    def get_sisters(self):
        return list((set(self.father.children('F')) | set(self.mother.children('F'))) - {self})

    def get_brothers(self):
        return list((set(self.father.children('M')) | set(self.mother.children('M'))) - {self})

    def add_child(self, child):
        self._children.append(child)

    def children(self, gender=None):
        if gender:
            return [child for child in self._children if child.gender == gender]
        return self._children

    def is_direct_successor(self, other):
        return other in self._children
