class Team():
    #itialise Team
    def __init__(self,x,y):
        self.locs = [] #holds the locations of members
        self.bound = {"min":{"x":x,"y":y},"max":{"x":x,"y":y}} #holds boundaries of members
        self.count = 1 #number of members in team

    #checks if person is adjacent to team 
    def isInTeam(self, x,y): 
        if (((
            self.bound["max"]["x"]+1 > x > self.bound["min"]["x"]-1
            )and(
            self.bound["max"]["y"] > y > self.bound["min"]["y"]
            ))
            )or(
            ((
            self.bound["max"]["x"] > x > self.bound["min"]["x"]
            )and(
            self.bound["max"]["y"]+1 > y > self.bound["min"]["y"]-1
            ))):

            print("Adding person in location ", [x,y], "to team")
            self.locs.append([x,y])

            if y > self.bound["max"]["y"]: #Redo y boundary
                self.bound["max"]["y"] = y
            if y < self.bound["min"]["y"]:
                self.bound["min"]["y"] = y

            if x > self.bound["max"]["x"]: #Redo x boundary
                self.bound["max"]["x"] = x
            if x < self.bound["min"]["x"]:
                self.bound["min"]["x"] = x

            return True
        else:
            print([x,y], " does not belong in this team")
            return False


