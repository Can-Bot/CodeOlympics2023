from Team import Team

def HeadCounter(map):
    teams = []
    headcount = 0
    #Traverse through map
    for y in range(len(map)):
        for x in range(len(map[y])):
            #check if person is present
            if map[y][x] == 1:
                headcount += 1 #increase person count

                #make new team if no teams
                if len(teams) == 0:
                    teams.append(Team(x,y))
                else:
                    #check if in the limits for present teams
                    inTeam =  False
                    teamIndex = 0
                    while not inTeam and teamIndex < len(teams):
                        #print("Checking team with bounds: ", teams[teamIndex].bound)
                        inTeam = teams[teamIndex].isInTeam(x,y)
                        teamIndex += 1

                    #new team if it doesnt qualify
                    if not inTeam:
                        #print("Making new team")
                        teams.append(Team(x,y))
    return teams, headcount

if __name__ == "__main__":
    inputMap = [[1,1,0,0,0,0,1,1], [1,1,0,1,1,0,1,1],[0,0,0,1,1,0,0,0], [1,1,0,1,1,0,1,1], [1,1,0,0,0,0,1,1]]
    print("The 2D map to be counted: \n",inputMap)

    teams, headcount = HeadCounter(inputMap)
    print(len(teams), " teams with ", sorted(team.count for team in teams), " people, totalling ", headcount)


