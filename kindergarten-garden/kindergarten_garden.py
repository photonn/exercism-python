class Garden:
    
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", 
    "Eve", "Fred", "Ginny", "Harriet",
    "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.students = students
        self.diagram = diagram.split("\n")
    
    def plants(self, string):
        plantsdict = {"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}
        result = []
        for window in self.diagram:
            result.append(plantsdict[window[self.students.index(string)*2]])
            result.append(plantsdict[window[self.students.index(string)*2+1]])
        return result