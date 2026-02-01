# My Cirq Playground

This is a personal playground for experimenting with quantum algorithms using the [Cirq](https://quantumai.google/cirq) library.

## Environment Setup

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install the package in editable mode (with dev dependencies):**
    ```bash
    pip install -e ".[dev]"
    ```
    This installs `cirq`, `numpy`, `scipy`, `typing-extensions`, `pytest`, and `ruff`.

## Running Tests

Run tests using pytest:
```bash
pytest
```

## Basic Usage

You can import the package in your scripts:
```python
import quantum_algos
import cirq
```
