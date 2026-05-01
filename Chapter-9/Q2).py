import random
def game():
  random_number = random.randint(1,50)
  return random_number
try:
  with open("./game.txt","r") as f:
        old_score=f.read().strip()
        if old_score == "":
            hi_score = 0
        else:
            hi_score = int(old_score)
           
except FileNotFoundError:
       hi_score = 0
 
       
        # print(type(hi_score))
print("High score in file : ",hi_score)

# new_score has the random computer generated number
new_score = game()
print("New score generated : ",new_score)
if new_score > hi_score:
      with open("game.txt","w") as f:
             f.write(str(new_score))
             print("you win!! High Score updated")
else:
        print("you loose")


# This is the correct solution         
# import random

# def game():
#     return random.randint(1, 50)

# # Step 1: Read old score safely
# try:
#     with open("game.txt", "r") as f:
#         content = f.read().strip()
#         if content == "":
#             hi_score = 0
#         else:
#             hi_score = int(content)
# except FileNotFoundError:
#     hi_score = 0

# print("High score in file:", hi_score)

# # Step 2: Generate new score
# new_score = game()
# print("New score generated:", new_score)

# # Step 3: Compare and update
# if new_score > hi_score:
#     with open("game.txt", "w") as f:
#         f.write(str(new_score))
#     print("New High Score! Updated.")
# else:
#     print("No update. You lose.")
        
        
      





