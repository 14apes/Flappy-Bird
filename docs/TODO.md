# TODO
* Add pause functionality for single player mode
* Add pillar image instead of simple colors
* Add start screen to allow user to start game/choose game/edit settings and save in json file, edit profile, view best scores
* Import game configurations from json file [can be edited from settings option on start screen of game] and not config.py
* Add multiplayer option [You will need to create server, use a database for storing/transmitting data/game logs]
* Fix binary of linux [does not work if executable is run from outside repo folder]
* Create Windows executable as .exe using pyinstaller or pygame2exe or py2exe (have to explore)
* Fix all UNSOLVED [MAJOR] bugs in BUGS.md
* Segregate methods which are not exclusive to flappy bird, and can be used by other games as a PygameUtils library

# GO-WILD
* Use reinforcement learning from Open-AI mixed with Genetic Algorithms
* Add option for Computer(Model) vs Human
* Create themes [flappy bird(default), space, ocean(nemo), snow, deer escape(from top)]
* Explore use case of NEAT (Evolutionary Algorithm) in this case
* Enhance the security of program before creating an executable and encrypt it. Enhance the connection between server-client
* Move the application and executabe to Docker image for faster deployment and bootstrap time for new coders
* Write unit tests for game to test for corner case crashes, if any
* Integrate facebook (for friend circle) social media integration for multiplayer mode
* Add more similar games (Atari games/Super Mario) to this under main start screen (like Alphabet to Google)
* Enhance memory management [delete unused vars]
* Add music control from keys such as m for mute/unmute or +/- for volumne up/down, n for next song

# DONE
* Pass all global variables in configDict instead of func args
* Add background image
* Add levels in game and increase speed with each level
* Made pygame resizable [Needs to Test]