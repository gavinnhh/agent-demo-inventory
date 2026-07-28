# agent-demo-inventory

Small Python inventory demo for the **ci-remediation** capstone — second repo example using **Make**, not Maven.

- **`main`** intentionally contains **Bug A**: `InventoryService` never initializes `config`, so `make test` fails.
- Use alongside [`agent-demo-payments`](../agent-demo-payments) (Java + `mvn -B test`) to show gate discovery from different GitHub Actions workflows.
- Mentor answer key: [`docs/GOLDEN_FIX.md`](docs/GOLDEN_FIX.md)

## Local run

```bash
make build   # install deps + compile
make test    # fails on main (expected)
```

Requires Python 3.11+, `make`, and `pip`.

## CI

GitHub Actions [`.github/workflows/ci.yml`](.github/workflows/ci.yml) runs:

```bash
make build
make test
```

Gate discovery should return something like: `[["make","build"],["make","test"]]`

## Layout

```
Makefile
src/inventory/
  config.py
  service.py       # bug on main
tests/
  test_service.py
```
