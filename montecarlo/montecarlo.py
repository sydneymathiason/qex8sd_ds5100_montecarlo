import numpy as np
import pandas as pd

class Die:
    """
    Represents a Die object that simulates a fair or weighted die.

    Attributes
    ----------
    faces : numpy.ndarray
        An array representing the possible faces of the die.

    Raises
    ------
    TypeError
        If the faces parameter is not a NumPy array.
    ValueError
        If the faces are not all unique.

    Note
    ----
    The Die object starts with equal weights for all faces.

    Attributes:
        faces (numpy.ndarray): An array representing the possible faces of the die.

    Raises:
        TypeError: If the faces parameter is not a NumPy array.
        ValueError: If the faces are not all unique.

    Note:
        The Die object starts with equal weights for all faces.
    """
    def __init__(self, faces):
        """
        Create a Die object with specified faces and equal weights.

        Parameters
        ----------
        faces : numpy.ndarray
            An array representing the possible faces of the die.

        Raises
        ------
        TypeError
            If the faces parameter is not a NumPy array.
        ValueError
            If the faces are not all unique.
        """
        self.faces = faces
        if not isinstance(self.faces, np.ndarray):
            raise TypeError("The faces parameter must be a NumPy array.")
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces are not all unique")
        
        self._die_state = pd.DataFrame({"weights": [1] * len(faces)}, index=faces)
        
    def change_weight(self, face, new_weight):
        """
        Change the weight of a specific die face.

        Parameters
        ----------
        face : int
            The face whose weight needs to be changed.
        new_weight : int or float
            The new weight for the specified face.

        Raises
        ------
        IndexError
            If the specified face is not a valid face of the die.
        TypeError
            If the new_weight parameter is not an int or float.
        """
        if face not in self._die_state.index:
            raise IndexError("Invalid face value.")
            
        if not isinstance(new_weight, (int, float)):
            raise TypeError("Invalid weight type.")
        
        self._die_state.at[face, "weights"] = new_weight
        
    def roll_die(self, rolls=1):
        """
        Roll the die a given number of times and return the results in a list.

        Parameters
        ----------
        rolls : int, optional
            The number of times to roll the die. Default is 1.

        Returns
        -------
        list
            A list of outcomes obtained from rolling the die.
        """
        outcomes = np.random.choice(self._die_state.index, rolls, p=self._die_state["weights"] / sum(self._die_state["weights"]))
        return outcomes.tolist()
    
    def show_state(self):
        """
        Show the current faces and weights of the die object.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing the faces and their corresponding weights.
        """
        return self._die_state.copy()

        

class Game:
    """
    Represents a game involving one or multiple dice.

    Parameters
    ----------
    list_of_die : list
        A list of Die objects used in the game.

    """

    def __init__(self, list_of_die):
        """
        Initialize a game object with a list of Die objects.

        Parameters
        ----------
        list_of_die : list
            A list of Die objects used in the game.
        """
        self._dice = list_of_die
        self._play_data = None
        
    def play(self, times):
        """
        Simulate playing the game by rolling the dice a given number of times.

        Parameters
        ----------
        times : int
            The number of times to roll the dice.
        """
        play_results = {i: die.roll_die(times) for i, die in enumerate(self._dice)}
        self._play_data = pd.DataFrame(play_results)
        self._play_data.index.name = "roll_number"
        
    def show_result(self, dftype="wide"):
        """
        Return the results from playing the game in a specified format.

        Parameters
        ----------
        dftype : str, optional
            The format of the results. Options: "wide" (default) or "narrow".

        Returns
        -------
        pandas.DataFrame
            The results in the specified format.

        Raises
        ------
        ValueError
            If dftype is not "narrow" or "wide".
        """
        if dftype == "wide":
            out = self._play_data.copy()
        elif dftype == "narrow":
            out = pd.DataFrame(self._play_data.copy().stack())
        else:
            raise ValueError("dftype needs to be narrow or wide")
            
        return out


class Analyzer:
    """
    Represents an Analyzer class for analyzing results from a Game object.

    Attributes:
        game (Game): The Game object to analyze.

    """

    def __init__(self, game):
        """
        Create an Analyzer object with a Game object.

        Parameters
        ----------
        game : Game
            The Game object to be analyzed.

        Raises
        ------
        ValueError
            If the input is not a valid Game object.
        """
        if not isinstance(game, Game):
            raise ValueError("The input must be a Game object")
        self._game = game
        
    def jackpot(self):
        """
        Return the number of jackpots in the game results.

        Returns
        -------
        int
            The count of jackpots.
        """
        return pd.DataFrame(self._game.show_result().eq(self._game.show_result().iloc[:, 0], axis=0
                                                       ).all(1).astype(int)).sum().item()
        
    def face_counts(self):
        """
        Return the face counts for all rolls in the game results.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing face counts for each roll.
        """
        return self._game.show_result().apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)

    def combo_count(self):
        """
        Return the combination counts of faces in the game results.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing combination counts.
        """
        df1 = self.face_counts()
        cols = df1.columns.to_list()
        mylist = []
        for i in range(len(df1)):
            newlist = []
            for col in cols:
                if df1.iloc[i][col] > 0:
                    for x in range(df1.iloc[i][col]):
                        newlist.append(col)

            mylist.append(newlist)
        return pd.DataFrame(pd.DataFrame(mylist, columns=range(len(self._game._dice))
                                        ).groupby(list(range(len(self._game._dice)))).value_counts()).rename(columns={0: 'count'})

    def permutation_count(self):
        """
        Return the permutation counts of combinations in the game results.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing permutation counts.
        """
        permutations = self._game.show_result().groupby(list(range(len(self._game._dice))))
        permutation_counts = permutations.value_counts()
        return pd.DataFrame({"count": permutation_counts})

