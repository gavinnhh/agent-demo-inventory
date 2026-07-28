# Golden fix — Bug A

## Problem

`InventoryService.config` is never initialized. `reserve()` accesses `self.config.api_key` and raises `AttributeError: 'NoneType' object has no attribute 'api_key'`.

## Fix

In `src/inventory/service.py`, initialize config in `__init__`:

```python
def __init__(self) -> None:
    self.config = Config("demo-api-key")
```

## Verify

```bash
make build
make test
```

Expected: one passing test, `test_reserve_returns_200_when_ok`.
