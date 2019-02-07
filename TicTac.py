game = [[0,0,0],[0,0,0],[0,0,0]] #list of lists  

def game_board(game_map,player=0, row=0, column=0,just_display=False):
	#takes multiple parameters
	try:
		print ("   0  1  2")
		## header for row select
		if not just_display:
			game_map[row][column] = player
		# if just display is false then it will use this function
		# and this block makes the actual modification to the map
		for count, rows in enumerate(game_map):
			print (count , rows)
		# this for loop will just display the actual gameboard 
			if count == 2 :
				print()
			# prints an empty line when the board is finished printing for readability
		return game_map ## returns the modified map
	except IndexError as e:
		print("You didnt enter your row/column as 0 1 or 2")
	except Exception as e:
		print("A serious fault occured")

game=game_board(game, just_display = True)
#sets the game variable to the new modified map
#without the need for a global variable
game=game_board(game, player=1,row=2, column=1)

game=game_board(game,just_display = True)


