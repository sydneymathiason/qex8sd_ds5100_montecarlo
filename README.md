# Monte Carlo Game Simulator

## Author: Sydney Mathiason


# Synopsis

#### Install

After downloading git repository to your computer, 

```python
pip install -e .
```

#### Import
```python
from montecarlo.montecarlo import Die, Game, Analyzer
```

#### Use

##### Die
```python
die = Die(np.array([1,2,3,4,5,6])) #create die with array of faces
die.change_weight(6, 5) #change weight of a face by specifying face and weight
die.roll(5) #roll die a give number of times
die.show_state() #show current state of die with 
```

##### Game
```python
game = Game([die, die, die]) #create game with list of Die objects
game.play(1000) #play game by specifying number of rolls
game.show_result() #show results of most recent game play in a data frame
```

##### Analyzer
```python
A = Analyzer(game) #create analyzer with a game object
A.jackpot() #get number of jackpots in the game
A.face_counts() #get face counts for all rolls in the game
A.combo_count() #get combination counts for game
A.permutation_count() #get permutation counts for game
```


# API Documentation

```
NAME
    montecarlo.montecarlo

CLASSES
    builtins.object
        Analyzer
        Die
        Game
    
    class Analyzer(builtins.object)
     |  Analyzer(game)
     |  
     |  Represents an Analyzer class for analyzing results from a Game object.
     |  
     |  Attributes:
     |      game (Game): The Game object to analyze.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, game)
     |      Create an Analyzer object with a Game object.
     |      
     |      Parameters
     |      ----------
     |      game : Game
     |          The Game object to be analyzed.
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If the input is not a valid Game object.
     |  
     |  combo_count(self)
     |      Return the combination counts of faces in the game results.
     |      
     |      Returns
     |      -------
     |      pandas.DataFrame
     |          A DataFrame containing combination counts.
     |  
     |  face_counts(self)
     |      Return the face counts for all rolls in the game results.
     |      
     |      Returns
     |      -------
     |      pandas.DataFrame
     |          A DataFrame containing face counts for each roll.
     |  
     |  jackpot(self)
     |      Return the number of jackpots in the game results.
     |      
     |      Returns
     |      -------
     |      int
     |          The count of jackpots.
     |  
     |  permutation_count(self)
     |      Return the permutation counts of combinations in the game results.
     |      
     |      Returns
     |      -------
     |      pandas.DataFrame
     |          A DataFrame containing permutation counts.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Die(builtins.object)
     |  Die(faces)
     |  
     |  Represents a Die object that simulates a fair or weighted die.
     |  
     |  Attributes
     |  ----------
     |  faces : numpy.ndarray
     |      An array representing the possible faces of the die.
     |  
     |  Raises
     |  ------
     |  TypeError
     |      If the faces parameter is not a NumPy array.
     |  ValueError
     |      If the faces are not all unique.
     |  
     |  Note
     |  ----
     |  The Die object starts with equal weights for all faces.
     |  
     |  Attributes:
     |      faces (numpy.ndarray): An array representing the possible faces of the die.
     |  
     |  Raises:
     |      TypeError: If the faces parameter is not a NumPy array.
     |      ValueError: If the faces are not all unique.
     |  
     |  Note:
     |      The Die object starts with equal weights for all faces.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, faces)
     |      Create a Die object with specified faces and equal weights.
     |      
     |      Parameters
     |      ----------
     |      faces : numpy.ndarray
     |          An array representing the possible faces of the die.
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If the faces parameter is not a NumPy array.
     |      ValueError
     |          If the faces are not all unique.
     |  
     |  change_weight(self, face, new_weight)
     |      Change the weight of a specific die face.
     |      
     |      Parameters
     |      ----------
     |      face : int
     |          The face whose weight needs to be changed.
     |      new_weight : int or float
     |          The new weight for the specified face.
     |      
     |      Raises
     |      ------
     |      IndexError
     |          If the specified face is not a valid face of the die.
     |      TypeError
     |          If the new_weight parameter is not an int or float.
     |  
     |  roll_die(self, rolls=1)
     |      Roll the die a given number of times and return the results in a list.
     |      
     |      Parameters
     |      ----------
     |      rolls : int, optional
     |          The number of times to roll the die. Default is 1.
     |      
     |      Returns
     |      -------
     |      list
     |          A list of outcomes obtained from rolling the die.
     |  
     |  show_state(self)
     |      Show the current faces and weights of the die object.
     |      
     |      Returns
     |      -------
     |      pandas.DataFrame
     |          A DataFrame containing the faces and their corresponding weights.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Game(builtins.object)
     |  Game(list_of_die)
     |  
     |  Represents a game involving one or multiple dice.
     |  
     |  Parameters
     |  ----------
     |  list_of_die : list
     |      A list of Die objects used in the game.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, list_of_die)
     |      Initialize a game object with a list of Die objects.
     |      
     |      Parameters
     |      ----------
     |      list_of_die : list
     |          A list of Die objects used in the game.
     |  
     |  play(self, times)
     |      Simulate playing the game by rolling the dice a given number of times.
     |      
     |      Parameters
     |      ----------
     |      times : int
     |          The number of times to roll the dice.
     |  
     |  show_result(self, dftype='wide')
     |      Return the results from playing the game in a specified format.
     |      
     |      Parameters
     |      ----------
     |      dftype : str, optional
     |          The format of the results. Options: "wide" (default) or "narrow".
     |      
     |      Returns
     |      -------
     |      pandas.DataFrame
     |          The results in the specified format.
     |      
     |      Raises
     |      ------
     |      ValueError
     |          If dftype is not "narrow" or "wide".
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

```


