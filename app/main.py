from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(concert_elves: list) -> None:
    for elf in concert_elves:
        Elf.play_elf_song(elf)


def feast_of_the_dwarves(dwarf_list: list) -> None:
    for eat in dwarf_list:
        Dwarf.eat_favourite_dish(eat)
