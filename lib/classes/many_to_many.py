from statistics import mean

class Game:
    all = []  # Class variable to store all instances of Game

    def __init__(self, title):
        self.title = title  # Setting the title of the game
        Game.all.append(self)  # Appending the current instance to the list of all games

    @property
    def title(self):
        return self._title  # Getter method for the title property to read the attribute
    
    @title.setter
    def title(self, title):
        # Setter method for the title property, ensuring it's a non-empty string
        if isinstance(title, str) and not hasattr(self, "_title") and title: # Checking if the title is a string of appropriate length and if it's not already set
            self._title = title  # Setting the title if conditions are met

    # # BEN's SOLUTION
    # @title.setter
    # def title(self, title):
    #     if isinstance(title, str) and len(title) > 0 and hasattr(self, '_title') # hasattr() first object as 'self' and a second attribute of _title. If the second attribute is not set, then the second attribute is set to an empty string.
    #         self._title = title  
    def results(self):
        # Returns a list of results associated with this game
        game_results = [] # Creating a list to store the results
        for result_obj in Result.all: # Instances = Result
            if result_obj.game is self: # Checking if the result is associated with this game 
                game_results.append(result_obj) # Appending the result to the list of results
        return game_results # Returning the list of results associated with this game 

    def players(self):
        # Returns a list of players who played this game
        player_counts = {} # Creating a dictionary to store the number of games played by each player
        for result in Result.all: # Instances = Result 
            if result.game is self: # Checking if the result is associated with this game 
                player_counts[result.player] = 1  # Adding each unique player who played the game to the dictionary, with a placeholder value of 1
        return list(player_counts.keys()) # Returning the list of players who played this game

    def average_score(self, player):
        # Calculates the average score of a player for this game
        scores = [] # Creating a list to store the scores
        results = player.results() # Getting the results associated with the player
        for result in results: # Instances = Result
            if result.game is self: # Checking if the result is associated with this game 
                scores.append(result.score) # Add the score to the list of scores
        if len(scores) > 0: # Checking if there are scores 
            return mean(scores)  # Calculating the mean of scores
        else:
            return 0  # Returning 0 if there are no scores

    def __repr__(self):
        return f"Game Title: {self.title}"  # Representation of the game object

class Player:
    all = []  # Class variable to store all instances of Player

    def __init__(self, username):
        self.username = username  # Setting the username
        Player.all.append(self)  # Appending the current instance to the list of all players

    @property
    def username(self):
        return self._username  # Getter method for the username property
    
    @username.setter
    def username(self, username):
        # Setter method for the username property, ensuring it's a string of appropriate length
        if isinstance(username, str) and 2 <= len(username) <= 16: # checking is username is a string between 2 and 16 characters long
            self._username = username  # Setting the username if conditions are met

    def results(self):
        # Returns a list of results associated with this player
        result_list = [] # Creating a list to store the results
        for result_obj in Result.all: # for the player object in Result.all 
            if result_obj.player is self: # Checking if the result is associated with this player object
                result_list.append(result_obj) # Appending the result to the list of results
        return result_list # Returning the list of results associated with this player 

    def games_played(self): 
        # Returns a list of games played by this player
        indvidual_games = set() # Creating a set to store the games played by this player
        for result in Result.all: # Instances = Result
            if result.player is self: # Checking if the result is associated with this player 
                indvidual_games.add(result.game) # Appending the game to the set of games played by this player
        return list(indvidual_games) # Returning the list of games played by this player 

    def played_game(self, game):
        # Checks if the player has played a specific game
        return game in self.games_played() 

    def num_times_played(self, game):
        # Returns the number of times the player has played a specific game
        games_played = [result.game for result in self.results()] # Getting the games played by this player 
        return games_played.count(game) #

    @classmethod
    def highest_scored(cls, game):
        # Returns the player with the highest average score for a given game
        averages = [(game.average_score(player), player) for player in cls.all] 
        if not averages: 
            return None # Returning None if there are no players with scores in the database 
        highest_record_tuple = max(averages, key=lambda tup: tup[0]) # Finding the tuple with the highest average score by comparing the first element of each tuple (the average score) in the list of averages. Then, retrieving the corresponding player from the tuple (list)
        return highest_record_tuple[1]  # Returning the player with the highest average score

class Result:
    all = []  # Class variable to store all instances of Result

    def __init__(self, player, game, score):
        self.player = player  # Setting the player associated with the result
        self.game = game  # Setting the game associated with the result
        self.score = score  # Setting the score of the result
        Result.all.append(self)  # add this object to Result.all, which is a list of all instances of Result.

    @property
    def score(self):
        return self._score  # Getter method for the score property
    
    @score.setter
    def score(self, score):
        # Setter method for the score property, ensuring it's an integer within a certain range
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000: # checking if the score is an integer within a range of 1 and 5000
            self._score = score  # Setting the score if conditions are met

    @property
    def player(self):
        return self._player  # Getter method for the player property
    
    @player.setter
    def player(self, player):
        # Setter method for the player property, ensuring it's an instance of Player
        if isinstance(player, Player): # checking if the player is an instance of Player
            self._player = player # setting the player if conditions are met

    def __repr__(self):
        return f"Result: {self.player.username}, Game: {self.game}, Score: {self.score}"


game_1 = Game("Risk of Rain")
player_1 = Player("GingerJoo")
result_game_played_1 = Result(player_1, game_1, 1455)
result_game_played_2 = Result(player_1, game_1, 2567)



player_2 = Player("Scurffy Panda")
game_2 = Game("Baldurs Gate")
score_2 = 5000
result_game_played_3 = Result(player_2, game_2, score_2)
result_game_played_4 = Result(player_2, game_2, 4300)

game_4 = Game("") # line 17 with no argument will crash the code. will reutrn Null, becuase it is empty and there is nothing there. 'and not hasattr(self, "title") and title:'



# print(game_1.title)
# print(game_1.results())
# print(game_1.average_score(player_1))
print(player_2.games_played())