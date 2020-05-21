
class Item(object):
    """
    An item object enables developers to add usable/interactable that the player
    can pickup, drop, and use.

    @author Nausher Rao (SherRao#8509)
    """

    def __init__(self, id: int, name: str, description: str):
        """
        @param id The internal integer ID to refer to this item by
        @param name The display name of this item
        @param description The description of the item to display inside the inventory.
        """
        self.id = id
        self.name = name
        self.description = description