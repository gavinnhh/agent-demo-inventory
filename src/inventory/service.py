"""In-memory inventory reservation helper.

Bug A on main: ``config`` is never initialized — reserve() raises when CI runs make test.
"""

from inventory.config import Config


class InventoryService:
    def __init__(self) -> None:
        self.config: Config | None = None

    def reserve(self, sku: str, quantity: int) -> int:
        if not sku or quantity <= 0:
            return 400
        # BUG A: config is None → AttributeError on next line
        if not self.config.api_key:
            return 500
        return 200
