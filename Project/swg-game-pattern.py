import random
user_input= input("Enter your choice : ").lower()
# print(type(user_input))
user = {"snake":-1 , "water":0, "gun":1}
user_move = user[user_input]

reverse_user = {-1:"snake", 0:"water", 1:"gun"}
computer_move = random.choice(list(reverse_user.keys()))
computer_value=reverse_user[computer_move]
print(computer_value)

if user_move == computer_move:
  print("Draw as you both selected : ",user_input)
elif (user_move-computer_move)in (-1,2):
  print("You won as you choose",user_input," which beats what computer chose which is ",computer_value)
else:
  print("You loose")