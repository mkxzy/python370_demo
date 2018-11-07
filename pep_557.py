from dataclasses import dataclass, field


@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float = field(repr=True, default=5.0)
    quantity_on_hand: int = 2

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


item = InventoryItem("a")
print(item.total_cost())
