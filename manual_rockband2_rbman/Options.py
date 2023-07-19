from Options import FreeText, OptionSet, Option, Range
from BaseClasses import MultiWorld
from typing import Union, Dict


class ExcludeInstruments(OptionSet):
    """
    Excludes instruments from holding progression. Valid options are ["Bass", "Drums", "Guitar", "Vocals"]
    """
    display_name = "Exclude Instruments"
    valid_keys = frozenset([
        "Bass", "Drums", "Guitar", "Vocals"
    ])

class StartingSongs(Range):
    """
    Select an amount of random Tier 0 songs to start with.
    """
    display_name = "Starting Songs"
    range_start = 1
    range_end = 12
    default = 3


manual_options: Dict[str, Option] = {
    "exclude_instruments": ExcludeInstruments,
    "starting_songs": StartingSongs
}


def is_option_enabled(world: MultiWorld, player: int, name: str) -> bool:
    return get_option_value(world, player, name) > 0


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, dict]:
    option = getattr(world, name, None)
    if option == None:
        return 0

    return option[player].value
