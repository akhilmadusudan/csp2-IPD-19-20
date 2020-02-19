####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
 
team_name = 'E0'
strategy_name = 'Collude_Betray'
'''This strategey colludes once, then betrays 3 times to counter'''
def move(my_history, their_history, my_score, their_score):
 if len(my_history) % 4 == 0:
   return 'c'
 else:
   return 'b'
