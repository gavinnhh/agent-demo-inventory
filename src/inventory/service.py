"""In-memory inventory reservation helper.

``config`` is initialized with a default demo API key so reserve() can run.
"""

from inventory.config import Config


class InventoryService:
    def __init__(self) -> None:
        self.config: Config = Config("demo-api-key")

    def reserve(self, sku: str, quantity: int) -> int:
        if not sku or quantity <= 0:
            return 400
        if not self.config.api_key:
            return 500
        return 200
