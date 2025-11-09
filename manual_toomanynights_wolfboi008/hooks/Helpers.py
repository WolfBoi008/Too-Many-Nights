from typing import Optional, TYPE_CHECKING
from BaseClasses import MultiWorld, Item, Location

if TYPE_CHECKING:
    from ..Items import ManualItem
    from ..Locations import ManualLocation

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    if category_name == "Challenges - Easy":
        return ("Easy" in multiworld.worlds[player].options.difficultyselect.value)
    if category_name == "Challenges - Normal":
        return ("Normal" in multiworld.worlds[player].options.difficultyselect.value)
    if category_name == "Challenges - Hard":
        return ("Hard" in multiworld.worlds[player].options.difficultyselect.value)
    if category_name == "Challenges - Insane":
        return ("Insane" in multiworld.worlds[player].options.difficultyselect.value)
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: "ManualItem") -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: "ManualLocation") -> Optional[bool]:
    return None
