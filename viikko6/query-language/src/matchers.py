class Pino:
    def __init__(self):
        self.alkiot = []

    def push(self, alkio):
        self.alkiot.append(alkio)

    def pop(self):
        return self.alkiot.pop()

    def empty(self):
        return len(self.alkiot) == 0

class QueryBuilder:
    def __init__(self, pino=None):
        self.pino_olio = pino if pino else Pino()

    def plays_in(self, team):
        PlaysIn(self.pino_olio, team)
        return self

    def has_at_least(self, value, attr):
        HasAtLeast(self.pino_olio, value, attr)
        return self

    def has_fewer_than(self, value, attr):
        HasFewerThan(self.pino_olio, value, attr)
        return self
    
    def one_of(self, *matchers):
        Or(self.pino_olio, *matchers)
        return self
        
    def build(self):
        return And(*self.pino_olio.alkiot)

class PlaysIn:
    def __init__(self, pino, team):
        self._team = team
        pino.push(self)

    def test(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, pino, value, attr):
        self._value = value
        self._attr = attr
        pino.push(self)

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value >= self._value

class HasFewerThan:
    def __init__(self, pino, value, attr):
        self._value = value
        self._attr = attr
        pino.push(self)

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value

class All:
    def __init__(self):
        pass

    def test(self, player):
        return player

class Not:
    def __init__(self, negation):
        self._negation = negation
    
    def test(self, player):
        return not self._negation.test(player)

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, pino, *matchers):
        self._matchers = matchers
        pino.push(self)

    def test(self, player): 
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        
        return False