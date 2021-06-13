import random

player_list = []
player_score = []



snakes_and_ladderlist = [4 ,7, 15, 30, 36, 61, 66, 90, 39, 55, 70, 79, 96, 98, 100] #list of bottom of ladders, top of snakes and the winning square
square_change_list=[23, 12, 72, 52, 41, 82, 77, 93, 18, 45, 49, 56, 33, 60, 100]# where each square will take you

number_of_players = int(input('How may players are there?  ')) #how may player do you start with
range(number_of_players) ## the range of players goes from 0 to number of players -1 so 3 players would be 0 1 2
player_list = list(range(number_of_players)) #player list is a list of players in the range of the number of players
for i in range(number_of_players):              
	player_list[i] = input('player name: ') ##for each player in the list put a name in which will replace the number in the list
	player_score.append(0) #gives each player a starting score of 0
                
print('Lets play') #something to let you know the first part is done
curent_player = 0 #sets the starting player to the first on the list
while True:
    try:
        roll = random.randint(1,6) #picks a random number between one and 6
        player_score[curent_player] = player_score[curent_player] + roll #adds random number to players score
        print(player_list[curent_player], 'has rolled a ', roll, 'moves to ',player_score[curent_player]) #prints where they are moving to
        
        if player_score[curent_player] >= 101: #if player rolls greater then 100 they have to go back
            move_back = player_score[curent_player]-100
            player_score[curent_player] = 100 - move_back #if you roll a number that makes your total greater than 100, how many spaces you have to then go back
            print('Too far go back ', move_back, ' spaces!')
            print('now on square ', player_score[curent_player])
              
        try:
            index = snakes_and_ladderlist.index(player_score[curent_player]) #checks the snakes_and_laderslist to see if there is a change in their square or if they have won
            if square_change_list[index] == 100: #winning the game
                print(player_list[curent_player], 'has won! congratulations')
                break
            if square_change_list[index] >= player_score[curent_player]: #if score is greater then their orignal score they move up a ladder
                player_score[curent_player] = square_change_list[index]
                print('ladder!')
                print('player' , player_list[curent_player], " move to square", player_score[curent_player])
                curent_player = curent_player + 1
            else:
                player_score[curent_player] <= square_change_list[index] #if score is less than their orignal score they move down a snake
                player_score[curent_player] = square_change_list[index]
                print('snake!')
                print('player' , player_list[curent_player], " move to square", player_score[curent_player])
                curent_player = curent_player + 1
        except(ValueError):
            print(player_list[curent_player], ' is on square ', player_score[curent_player])  #if none of the above then notheing happens
            curent_player = curent_player + 1
    except(IndexError):
            curent_player = 0 #if the player is more then in the list reset to the first

print('Game over')

