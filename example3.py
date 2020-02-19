####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
 
team_name = 'E3'
strategy_name = 'Collude, then check.'
strategy_description = '''Collude in the first three rounds, then check if your opponent has been betraying in their previous three turns. If yes, then betray. If no, then collude. '''
  
def move(my_history, their_history, my_score, their_score):
 def collude():
   return 'c'
 new_history = their_history[len(their_history)-3:]
 if 'b' in new_history:
   return 'b'
 else:
   collude()
