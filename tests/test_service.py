from inventory.service import InventoryService


def test_reserve_returns_200_when_ok():
    service = InventoryService()
    assert service.reserve("SKU-001", 3) == 200
