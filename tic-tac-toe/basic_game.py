from __future__ import print_function

import random
import numpy as np

symbol_choices = ('X', 'x', 'O', 'o')


class Player(object):
  def __init__(self, symbol, name='Player', verbose=False):
    if symbol not in symbol_choices:
      raise ValueError('Invalid symbol given for player.')
    self.symbol = symbol
    self.name = name
    self.verbose = verbose

  def play(self):
    raise NotImplementedError()


from ipdb import set_trace
class HumanPlayer(Player):
  def play(self, available_positions):
    print(self.name + '\'s turn!')
    if self.verbose:
      print('Available positions: ', available_positions)
    while True:
      coords = raw_input('Enter board coords where you wish to place mark:')
      separator = ',' if ',' in coords else ' '
      try:
        int_coords = tuple(map(int, coords.strip().split(separator)))
        assert len(int_coords) == 2
        if int_coords not in available_positions:
          print('That position is not available, choose another one...')
          continue
        return int_coords
      except (ValueError, AssertionError) as e:
        set_trace()
        print('Invalid inputs, try again...')
        continue


class Board(object):
  def __init__(self, verbose=False):
    self.board = np.zeros((3, 3), dtype=np.character)

  def play(self, position, symbol):
    if self.board[position] != '':
      # Should be a custom exc.
      raise ValueError('That position is not available')
    self.board[position] = symbol

  def get_coords(self, symbol):
    return zip(*np.where(self.board==symbol))

  def get_available_positions(self):
    return zip(*np.where(self.board==''))


def is_won(board, symbol, positions, latest_move):
  # One way is to check all possible 3-combinations, but inefficient.
  x, y = latest_move
  positions = set(positions)
  if positions.issuperset([(x, i) for i in range(3)]):
    return True
  if positions.issuperset([(i, y) for i in range(3)]):
    return True
  if x == y and positions.issuperset([(i, i) for i in range(3)]):
    return True
  # Generic: size = N ==> range(N), below x + y == N - 1
  if x + y == 2 and positions.issuperset([(i, 2 - i) for i in range(3)]):
    return True
  return False


def game_loop(players, board):
  first, second = players
  while board.get_available_positions():
    # for player in players:
    move = first.play(board.get_available_positions())
    board.play(move, first.symbol)  # MOA/pub-sub.
    positions = board.get_coords(first.symbol)
    if is_won(board, first.symbol, positions, move):
      print('Winner: ' + first.name)
      return first

    if not board.get_available_positions():
      break

    move = second.play(board.get_available_positions())
    board.play(move, second.symbol)
    positions = board.get_coords(second.symbol)
    if is_won(board, second.symbol, positions, move):
      print('Winner: ' + second.name)
      return second

  print('Match drawn!')
  return None


def main():
  # Get options like verbosity, board size, player names, symbols as cmdline
  # arg/option inputs, click package!
  # players = map(HumanPlayer, [('X', 'p1', True), ('O', 'p2', True)])
  players = HumanPlayer('X', 'p1', True), HumanPlayer('O', 'p2', True)
  # Toss
  # first = players[random.randint()]
  index_subtractor = random.randint(0, 1)
  first, second = players[0 - index_subtractor], players[1 - index_subtractor]
  game_loop((first, second), board=Board())


if __name__ == '__main__':
  main()

# Idea is to try keeping the board as passive object as possible, here focus is
# on the game logic/loop. Players will be moved out. Board is just to keep the
# current positions marked by the players, with no logic. The is_won can be
# kept inside it but that would mean putting more logic in board.
