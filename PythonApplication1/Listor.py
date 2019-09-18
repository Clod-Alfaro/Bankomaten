class Player:    
    Namn = ""           
    JerseyNumber = 0
    SkoStorlek = 0
    ScoresThisSeason = 4
    HasHair = False


listOfPlayers = []

player1 = Player()    
player1.Namn = "Peter Forsberg" 
player1.JerseyNumber = 13 
player1.SkoStorlek = 44
player1.ScoresThisSeason = 12
player1.HasHair = True 
listOfPlayers.append(player1)

player2 = Player()   
player2.Namn = "Mats Sundin"
player2.JerseyNumber = 21
player2.SkoStorlek = 43
player2.ScoresThisSeason = 4
player2.HasHair = False
listOfPlayers.append(player2)

player3 = Player()   
player3.Namn = "Niklas Lindström"
player3.JerseyNumber = 5
player3.SkoStorlek = 45
player3.ScoresThisSeason = 1
player3.HasHair = False
listOfPlayers.append(player3)

for player in listOfPlayers:
    
    print(f"{player.Namn} in jersey number {player.JerseyNumber}")
    print(f"{player.Namn} in sko storlek {player.SkoStorlek}")
    print(f"{player.Namn} in scores this season {player.ScoresThisSeason}")
    print(f"{player.Namn} in has hair {player.HasHair}")
   

