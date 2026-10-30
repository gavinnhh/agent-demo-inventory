"""In-memory inventory reservation helper."""

import os

from inventory.config import Config

DEFAULT_API_KEY = "local-dev-key"


class InventoryService:
    def __init__(self, config: Config | None = None) -> None:
        if config is None:
            config = Config(api_key=os.environ.get("INVENTORY_API_KEY", DEFAULT_API_KEY))
        self.config: Config = config

    def reserve(self, sku: str, quantity: int) -> int:
        if not sku or quantity <= 0:
            return 400
        if self.config is None or not self.config.api_key:
            return 500
        return 200
