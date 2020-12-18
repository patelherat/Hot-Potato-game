# Hot-Potato-game
Players are arranged in a circle. The potato begins with one of the players. While music plays, the hot potato is passed from player to player, around the circle. Whoever is holding the potato when the music stops is out. The potato is handed to the next person, and the music starts up again. The game continues until only one player remains. That player is the winner.

Assume there is a file containing the following lines of text: <br />
Aaron <br />
Beth <br />
Cathy <br />
Duncan <br />
Emery <br /> <br />
Running your program should generate the following output: <br />
$python3 potato.py players.txt 10 <br />
Welcome to the Hot Potato Game! <br />
Reading from: players.txt <br />
Using random number generator seed: 10 <br />
Ready to play Hot Potato. Contestants are: <br />
Aaron, Beth, Cathy, Duncan, Emery <br />
The music starts (8): Aaron -> Beth -> Cathy -> Duncan -> Emery -> <br />
Aaron -> Beth -> Cathy -> Duncan is stuck holding the potato! <br />
The music starts (-7): Emery -> Cathy -> Beth -> Aaron -> <br />
Emery -> Cathy -> Beth -> Aaron is stuck holding the potato! <br />
The music starts (0): Emery is stuck holding the potato! <br />
The music starts (3): Beth -> Cathy -> Beth -> <br />
Cathy is stuck holding the potato! <br />
Beth is the winner! <br />
