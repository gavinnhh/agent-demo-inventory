"""In-memory inventory reservation helper.

``config`` defaults to a demo API key so reserve() works out of the box.
"""

from inventory.config import Config


class InventoryService:
    def __init__(self, config: Config | None = None) -> None:
        self.config: Config = config if config is not None else Config("demo-api-key")

    def reserve(self, sku: str, quantity: int) -> int:
        if not sku or quantity <= 0:
            return 400
        if not self.config.api_key:
            return 500
        return 200
