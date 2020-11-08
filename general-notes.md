# Congklak: built with pygame

### Overview
* what is the idea?
    * to simulate the traditional game congklak using pygame with minimalistic design
* How is congklak played?
    * resource: https://www.youtube.com/watch?v=pxT4BbsdybY
    * steps
        * each board contain 2 base and 14 hole
        * at start:
            *empty base and fill all hole with 7 seedss each
            * each player is assigned 7 hole at his side, and 1 base to the left of him
            * the goal is to get as many seedss to your base
        * at each turn:
            * pick one hole of yours and take all the seedss in it
            * move clockwise and drop one seeds at each hole and your base, skip opponent's base
            * last drop cases
                * hole not empty
                    * pick all the seedss in the hole and keep moving
                * empty
                    * in your side: take the seeds at the hole and accross it and drop it on your base, then switch turn
                    * in opponent's side:
                        * switch turn
                * your base:
                    * you can pick any one of your hole and basically restart your turn
* General steps in development
    * Develop logic of the game: write text-based version of it
    * Develop visual of the game: create minimalist representation using pygame

### Pure logic: text-based implementation
* board reprsentation
    * option 1
        * with two array of length 8, one for each player
        * the first element is the base
    * option 2
        * with one big array the first 8 is for first player, the last 8 for second player
* seeds movement
    * let n be the value for the chosen hole
    * move left n times, skip opponents base
    * if it lands on non-empty, take the value of that hole and continue
    * if it lands on empty opponent's hole
        * finish
    * if it lands on empty player's hole
        * add value of adjacent opponent's hole + 1 to your base
    * if it lands on your base:
        * finish, no switch
    * additional rule:
        * if there's no seed in player's side, then switch turn
* skipping opponents base
    * if it's opponent's base
        * do not add the seed
        * do not decrease the seed in the original hole
        * extend the range
* game play process
    1. player 1 starts
    2. player 1 continue or switch
    3. keep playing until base is bigger than half of total seeds

### Visual development
* general style
    * simple geometry
    * beage/pastel color
    * calming music
    * sound effect
* basic shape
    * congklak board: ellipse
    * hole: circle
* movement
    * selected circle is colored dark color
* seed illustration
    * number inside the circle
    * user the circle global coordinate

### Improvement
* ideas
    * reorganized text
    * highlighting for last hole 
    * sound
    * highlighting for p1 and p2 hole
* bugs:
    * in message ("please enter valid" ironically not valid) [fixed]
    * empty game, then switch [fixed]
    * index error [fixed]