import requests
from player import Player
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def main():
    console.print("[bold blue]NHL statistics by nationality[/bold blue]")

    season = Prompt.ask("Select season(e.g., 2023-24)")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationality = Prompt.ask("Select nationality (e.g., FIN)")
    players = stats.top_scorers_by_nationality(nationality)

    console.print(f"[bold magenta]Top scorers of {nationality} season {season} :[/bold magenta]")
    
    for player in players:
        print(player)

class PlayerReader:
    def __init__(self, url) -> None:
        self.url = url
    
    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(player_dict) for player_dict in response]

class PlayerStats:
    def __init__(self, players) -> None:
        self.players = players.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        toplist = []
        for player in self.players:
            if player.nationality == nationality:
                toplist.append(player)
        return sorted(toplist, key=lambda player: player.points, reverse=True)

if __name__ == "__main__":
    main()
