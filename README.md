# Metadata

#### Project Name: Monte Carlo Game Simulator

#### Author: Sydney Mathiason


# Synopsis

#### Install
```
pip install -e .
```

#### Import
```
from montecarlo.montecarlo import Die, Game, Analyzer
```

#### Use

##### Die
```
die = Die(np.array([1,2,3,4,5,6]))
die.change_weight(6, 5)
die.show_state()
```

##### Game
```
rolls = 10000
game = Game([die, die, die])
game.play(rolls)
game.show_result()
```

##### Analyzer
```
A = Analyzer(game)
A.jackpot()
A.face_counts()
A.combo_count()
A.permutation_count()
```


# API Documentation

### Classes

1. Die

Methods:

- __init__
- change_weight
- roll_die

Attributes:

- faces


2. Game

Methods:

- __init__
- play
- show_results

Attributes:



3. Analyzer

Methods:

- __init__
- jackpot
- face_counts
- combo_count
- permutation_count

Attributes:





