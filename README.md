# Game
A basic game with components fairly separated for future growth of their own.

This repo tries to combine my interests: AI, Machine learning, Neural Networks (& fuzzy logic), game, graph algorithms, algorithmic efficiency, statistics & statistical inference, concurrency (multiple players), go lang (for high computation maybe?) to some extent, testing and GUI. This should ideally be an example of reinforcement learning.

That's a huge list, so it will take time for them to show up (appear sufficiently). But the major weakness is I only think/plan & not to start anything, so I created this basic repo, with a simple enough topic & goal to start, so that there is actually some progress!
Many of these topics may and should evolve into their own projects/git submodules/git projects themselves, but let's just start!
JUST DO IT!

# Structure

lib.py(or lib): Basic lib for game, containing gameplay.  
rules: Rules of the game, victory condition, move definition etc. (json/pb2)  
player: AI implementation of a game player.  
stat: The stats for win/lose history, mostly for AI to use in ML.  
interface: Ways of launching game, AI battles, GUI, vs Human, api etc.  
db: Optional db. (stat maybe unified into db).  
