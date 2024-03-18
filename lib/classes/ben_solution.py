class Game:
    def __init__(self, title):
        self.title = title

    # @property
    def get_title(self):
        return self._title
    
    # @title.setter
    def set_title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0 and not hasattr(self, '_title'):
            self._title = new_title  # success case
        else:
            print(f'invalid title: {new_title}')
            # pass

    title = property(get_title, set_title)

    def results(self):
        result_list = []
        for result_obj in Result.all:
            if result_obj.game is self:
                result_list.append(result_obj)
        return result_list

    # def players(self):
    #     player_list = []
    #     for result_obj in self.results():  # a list of result objects for this game
    #         player_list.append(result_obj.player)
    #     return list(set(player_list))

    def players(self):
        player_list = []
        for result_obj in self.results():  # a list of result objects for this game
            if result_obj.player not in player_list:  # check if this player has been added yet
                player_list.append(result_obj.player)
        return player_list

    def average_score(self, player):
        total = 0
        count = 0
        for result_obj in self.results():
            if result_obj.player is player:
                total += result_obj.score
                count += 1
        return total / count


    def __repr__(self) -> str:
        return f"<Game {self.title}>"

class Player:
    def __init__(self, username):
        self.username = username
    
    def get_username(self):
        return self._username
    
    def set_username(self, new_username):
        # if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
        if isinstance(new_username, str) and len(new_username) <= 16 and len(new_username) >= 2:
            self._username = new_username
        else:
            print(f'invalid username: {new_username}')

    username = property(get_username, set_username)

    def results(self):
        # loop through Results.all
        # find every result for this player
        # return **new** list of results
        result_list = []
        for result_obj in Result.all:
            if result_obj.player is self:
                result_list.append(result_obj)
        return result_list
        # return [result_obj for result_obj in Result.all if result_obj.player is self]

    def games_played(self):
        games_list = []
        for result_obj in self.results():
            if result_obj.game not in games_list:
                games_list.append(result_obj.game)
        return games_list

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        count = 0
        for result in self.results():
            if result.game is game:
                count += 1
        return count
        # return len([result for result in self.results() if result.game is game])

    def __repr__(self) -> str:
        return f"<Player {self.username}>"

class Result:
    all = []  # store all result objects here

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)  # add this object to Results.all
    
    def get_player(self):
        return self._player
    
    def set_player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            print('invalid player')
    
    player = property(get_player, set_player)

    def __repr__(self) -> str:
        return f"<Result {self.player.username} {self.game.title} {self.score}>"



pacman = Game('pacman')
galaga = Game('galaga')
anne = Player('anne123')
joe = Player('joe456')


r1 = Result(anne, pacman, 500)
r2 = Result(anne, pacman, 750)
r3 = Result(joe, pacman, 456)
r3 = Result(joe, galaga, 456)

print(pacman.average_score(anne))