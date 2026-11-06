"""In-memory inventory reservation helper.

``config`` defaults to a demo key when not supplied, so reserve() never sees ``None``.
"""

from inventory.config import Config

DEFAULT_API_KEY = "demo-api-key"


class InventoryService:
    def __init__(self, config: Config | None = None) -> None:
        self.config: Config = config if config is not None else Config(DEFAULT_API_KEY)

    def reserve(self, sku: str, quantity: int) -> int:
        if not sku or quantity <= 0:
            return 400
        if not self.config.api_key:
            return 500
        return 200
