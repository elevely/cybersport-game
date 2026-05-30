from models.player import Player
from models.coach import Coach
from models.team import Team
from models.match import Match
from models.world import World
from models.tournament import Tournament
from models.manager import Manager
from models.organization import Organization

from services.match_simulator import MatchSimulator
from services.world_sumulator import WorldSimulator
from services.team_factory import create_test_team
from services.tournament_simulator import TournamentSimulator

team_names = [
    "NAVI",
    "Spirit",
    "Vitality",
    "G2",
    "FaZe",
    "MOUZ",
    "Astralis",
    "Falcons",
    "Liquid",
    "The MongolZ"
]

teams = [
    create_test_team(name)
    for name in team_names
]

def start_game():

    print(
        f'===================='
        f'ESPORTS MANAGER'
        f'===================='
        f''
    )

    manager_name = input("Введите имя менеджера: ")

    print(f"\nДобро пожаловать, {manager_name}!")
    print(f'---------------------------------------------')
    print(f"Выберите команду, которую приведете к победам")

    for i, team_name in enumerate(team_names, start=1):
        print(f"{i}. {team_name}")

    choice = int(input("> "))

    selected_team = teams[choice - 1]

    manager = Manager(
        name = manager_name
    )

    organization = Organization(
        name=selected_team.name,
        money=100000,
        team=selected_team
    )

    print(
        f"\nВы стали менеджером "
        f"{organization.name}"
    )

    return manager, organization

def general_info():
    print('')
    print(f'====================')
    print(f'Дата: {World.current_day}.{World.current_month}.{World.current_year}')
    print('')
    print(f'Менеджер: {manager.name}')
    print(f'Организация: {organization.name}')
    print(f'Баланс: {organization.money}')
    print(f'====================')

def action_selection():
    print('')
    print('Выберите действие:')
    print('1. Посмотреть состав')
    print('2. Следующий день')
    print('3. Выход')

    choice = input('> ')

manager, organization = start_game()

while True:
    general_info()
    action_selection()
    break