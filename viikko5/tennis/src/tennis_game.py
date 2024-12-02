class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score += 1
        elif player_name == self.player2_name:
            self.p2_score += 1

    def get_score(self):
        if self.p1_score == self.p2_score:
            return self.equal_score()    
        elif self.p1_score >= 4 or self.p2_score >= 4:
            return self.endgame()
        else:
            return self.gamescore()

    def equal_score(self):
        score = ""
        if self.p1_score == 0:
            score = "Love-All"
        elif self.p1_score == 1:
            score = "Fifteen-All"
        elif self.p1_score == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score

    def endgame(self):
        score = ""
        minus_result = self.p1_score - self.p2_score

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def gamescore(self):
        score = ""
        temp_score = 0
        for i in range(2):
            if i == 0:
                temp_score = self.p1_score
            else:
                score = score + "-"
                temp_score = self.p2_score

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score