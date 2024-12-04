from statistics import Statistics
from player_reader import PlayerReader
from matchers import QueryBuilder
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    
    reader = [
        Player("Player1", "PHI", 10, 15),
        Player("Player2", "NYR", 15, 23),
        Player("Player3", "EDM", 25, 3),
        Player("Player4", "CHI", 19, 55),
    ]
    stats = Statistics(reader)
    query = QueryBuilder()
    matcher1 = query.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()
    m1 = QueryBuilder().plays_in("PHI").has_at_least(10, "goals").build()
    m2 = QueryBuilder().plays_in("EDM").has_fewer_than(5, "assists").build()
    matcher2 = QueryBuilder().one_of(m1, m2).build()
    print("test1")
    for player in stats.matches(matcher1):
        print(player)
    print("test2")
    for player in stats.matches(matcher2):
        print(player)

if __name__ == "__main__":
    main()
