# Starting with a func approach? Needs global state of game.


ACTIONS = {
    'ATTACK': 1,
    'PEACE': 0
}


RULES = {
        'player_count': 2,
        'type': 'turn_based_strategy',
        'victory': ('player.score > 0', 'player.score > opponent.sore'),
        'stop': ()
        }

class Game(object):
  def __init__(self, players=None, actions=ACTIONS, state=None,)
