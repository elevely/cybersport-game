from models.tournament import Tournament
from models.match import Match

from services.match_simulator import MatchSimulator

class TournamentSimulator:
    
    @staticmethod
    def play_round(teams):
        team_winners = []
        
        for i in range(0, len(teams), 2):
            team_a = teams[i]
            team_b = teams[i+1]

            match = Match(team_a, team_b)
            winner = MatchSimulator.simulate(match)

            print(f'{team_a.name} vs {team_b.name}')
            print(f'Winner: {winner.name}')

            team_winners.append(winner)

        return team_winners
    
    @staticmethod
    def play(tournament):

        print("=== Quarterfinals ===")

        quarterfinal_winners = TournamentSimulator.play_round(
            tournament.teams
        )

        print("\n=== Semifinals ===")

        semifinal_winners = TournamentSimulator.play_round(
            quarterfinal_winners
        )

        print("\n=== Final ===")

        final_winner = TournamentSimulator.play_round(
            semifinal_winners
        )

        champion = final_winner[0]

        print(f"\nChampion: {champion.name}")

        return champion
        
