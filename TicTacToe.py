playing = True
plays = []
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def fillTicTacToe(player):
  x = int(input(f"Player {plays[-1]} please input row (1-3): "))
  if x > 3 or x < 1:
    return "Wrong input, please input a number in range of 1 to 3."
  y = int(input(f"Player {plays[-1]} please input col (1-3): "))
  if y > 3 or y < 1:
    return "Wrong input, please input a number in range of 1 to 3."
  if board[x-1][y-1] != "":
    return "This field is already filled in."
  board[x-1][y-1] = player
  if len(plays) == 0:
    plays.append("x")
  elif plays[-1] == "x":
    plays.append("o")
  elif plays[-1] == "o":
    plays.append("x")
  return f"{board[0]}\n{board[1]}\n{board[2]}"

while playing:
  if len(plays) == 0:
    plays.append("x")
  result = fillTicTacToe(plays[-1])
  print(result)
  if (board[0][0] == board[0][1] and board[0][0] == board[0][2]) and board[0][0] != '' and board[0][1] != '' and board[0][2] != '':
    print(f"Player {board[0][0]} win!")
    playing = False
  elif (board[0][0] == board[1][1] and board[0][0] == board[2][2]) and board[0][0] != '' and board[1][1] != '' and board[2][2] != '':
    print(f"Player {board[0][0]} win!")
    playing = False
  elif (board[0][2] == board[1][1] and board[0][2] == board[2][2]) and board[0][2] != '' and board[1][1] != '' and board[2][2] != '':
    print(f"Player {board[0][0]} win!")
    playing = False
  elif (board[1][0] == board[1][1] and board[1][0] == board[1][2]) and board[1][0] != '' and board[1][1] != '' and board[1][2] != '':
    print(f"Player {board[0][0]} win!")
    playing = False
  elif (board[2][0] == board[2][1] and board[2][0] == board[2][2]) and board[2][0] != '' and board[2][1] != '' and board[2][2] != '':
    print(f"Player {board[0][0]} win!")
    playing = False
  elif len(plays) == 10:
    print("No one win")
    playing = False
