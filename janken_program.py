import random

print('じゃんけんスタート')

print('あなたの手を入力してください')
my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
you_hand = random.randint(0, 2)

hand_diff = my_hand - you_hand

if hand_diff == 0:
  print('あいこ')
elif hand_diff == -1 or hand_diff == 2:
  print('勝ち')
elif hand_diff == -2 or hand_diff == 1:
  print('負け')
else:
  print('もう一度入力してください')
 
#
# if my_hand == 0:
#   if you_hand == 0:
#     print('あいこ') #=> 0-0= 0
#   elif you_hand == 1:
#     print('勝ち') #=> 0-1= -1
#   elif you_hand == 2:
#     print('負け')              #=> 0-2= -2
# elif my_hand == 1:
#   if you_hand == 0:
#     print('負け')              #=> 1-0= 1
#   elif you_hand == 1:
#     print('あいこ') #=> 1-1= 0
#   elif you_hand == 2:
#     print('勝ち') #=> 1-2= -1
# elif my_hand == 2:
#   if you_hand == 0:
#     print('勝ち') #=> 2-0= 2
#   elif you_hand == 1:
#     print('負け')              #=> 2-1= 1
#   elif you_hand == 2:
#     print('あいこ') #=> 2-2= 0
