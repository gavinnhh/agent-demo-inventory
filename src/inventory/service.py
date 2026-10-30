"""In-memory inventory reservation helper."""

import os

from inventory.config import Config

DEFAULT_API_KEY = "local-dev"


class InventoryService:
    def __init__(self, config: Config | None = None) -> None:
        self.config: Config = config or Config(
            api_key=os.environ.get("INVENTORY_API_KEY", DEFAULT_API_KEY)
        )

    def reserve(self, sku: str, quantity: int) -> int:
        if not sku or quantity <= 0:
            return 400
        if not self.config.api_key:
            return 500
        return 200
