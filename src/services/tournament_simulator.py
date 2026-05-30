from models.tournament import Tournament
from models.match import Match

from services.match_simulator import MatchSimulator

class TournamentSimulator:
    
    @staticmethod
    def play_round(teams, place_teams):
        team_winners = []
        
        for i in range(0, len(teams), 2):
            team_a = teams[i]
            team_b = teams[i+1]

            match = Match(team_a, team_b)
            winner, loser = MatchSimulator.simulate(match)
            
            place_teams.append(loser)

            print(f'{team_a.name} vs {team_b.name}')
            print(f'Winner: {winner.name}')

            team_winners.append(winner)
        

        return team_winners
    
    @staticmethod
    def play(tournament):

        place_teams = []

        print("=== Quarterfinals ===")

        quarterfinal_winners = TournamentSimulator.play_round(
            tournament.teams,
            place_teams
        )

        print("\n=== Semifinals ===")

        semifinal_winners = TournamentSimulator.play_round(
            quarterfinal_winners,
            place_teams
        )

        print("\n=== Final ===")

        final_winner = TournamentSimulator.play_round(
            semifinal_winners,
            place_teams
        )

        champion = final_winner[0]
        place_teams.append(champion)

        second_place = place_teams[-2]

        third_fourth = [
            place_teams[-4],
            place_teams[-5]
        ]

        fifth_eighth = [
            place_teams[0],
            place_teams[1],
            place_teams[2],
            place_teams[3]
        ]

        TournamentSimulator.distribute_prize_money(
            champion,
            second_place,
            third_fourth,
            fifth_eighth
        )

        print(f"\nChampion: {champion.name}")
        print(f'2 место: {second_place.name}')
        print(f'3-4 место: {third_fourth[0].name}, {third_fourth[1].name}')
        print(f'5-8 место: {fifth_eighth[0].name}, {fifth_eighth[1].name}, {fifth_eighth[2].name}, {fifth_eighth[3].name}')

        return champion
    
    @staticmethod
    def distribute_prize_money(champion, second_place, third_fourth, fifth_eighth):    
        prize_pool = Tournament.prize_pool
        champion.money += prize_pool * 0.51
        second_place.money += prize_pool * 0.25
        for team in third_fourth:
            team.money += prize_pool * 0.1
        for team in fifth_eighth:
            team.money += prize_pool * 0.01
                
