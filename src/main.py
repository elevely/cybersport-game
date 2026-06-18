import sys

from models.player import Player
from models.coach import Coach
from models.team import Team
from models.match import Match
from models.world import World
from models.tournament import Tournament
from models.manager import Manager
from models.organization import Organization
from models.game_date import GameDate

from data.tournaments import TOURNAMENTS
from data.organizations import organization_names, ORGANIZATIONS

from services.match_simulator import MatchSimulator
from services.tournament_simulator import TournamentSimulator

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

    for i, organization_name in enumerate(organization_names, start=1):
        print(f"{i}. {organization_name}")

    choice = int(input("> "))

    selected_organization = ORGANIZATIONS[choice - 1]

    manager = Manager(
        name = manager_name
    )

    organization = selected_organization

    world = World(
        manager=manager,
        organization=organization,
        organizations=ORGANIZATIONS,
        tournaments=TOURNAMENTS,
        date=GameDate(
            day=1,
            month=1,
            year=2026
        )
    )

    print(
        f"\nВы стали менеджером "
        f"{organization.name}"
    )

    return manager, organization, world

def general_info():
    print('')
    print(f'====================')
    print(f'Дата: {world.date.day}.{world.date.month}.{world.date.year}')
    print('')
    print(f'Менеджер: {manager.name}')
    print(f'Организация: {organization.name}')
    print(f'Баланс: {organization.money}')
    print(f'====================')

def play_tournament(today_tournament):

    TournamentSimulator.play(today_tournament)

    print('')


def action_selection():

    flag_today_tournament, today_tournament = world.flag_tournament()

    print('')
    if flag_today_tournament == True:
        print(f'===== НАЧАЛСЯ {today_tournament.name} =====')
        print('')
    print('Выберите действие:')
    print('1. Общая информация')
    print('2. Посмотреть состав')
    print('3. Турниры')
    print('4. Следующий день')
    if flag_today_tournament == True:
        print('5. Начать турнир')
        print('6. Выход')
    else:
        print('5. Выход')

    choice = input('> ')
 
    if choice == '1':
        general_info()

    if choice == '2':
        pass

    if choice == '3':
        world.next_tournament()

    if choice == "4":
        print('')
        world.advance_day()

        print(
            f"\nНаступило "
            f"{world.date.day:02d}."
            f"{world.date.month:02d}."
            f"{world.date.year}"
        )
    
    if flag_today_tournament == True:
        if choice == '5':
            play_tournament(today_tournament)
            world.advance_day()
            print(
            f"\nНаступило "
            f"{world.date.day:02d}."
            f"{world.date.month:02d}."
            f"{world.date.year}"
            )

        if choice == '6':
            sys.exit()
    else:
        if choice == '5':
            sys.exit()



manager, organization, world = start_game()
general_info()

while True:
    action_selection()