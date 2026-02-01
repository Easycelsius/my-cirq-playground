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

## Development Guide

### Project Structure
- **`src/quantum_algos/`**: This is where the core logic and algorithms reside. Implement your new quantum classes and functions here.
- **`tests/`**: Contains unit tests. When you add a new feature, please add a corresponding test file here (e.g., `test_my_feature.py`).
- **`examples/`**: Scripts demonstrating how to use the library concepts.

### Running Tests
We use `pytest` for ensuring code quality.
To run all tests:
```bash
pytest
```
To run a specific test file:
```bash
pytest tests/test_deutsch_jozsa.py
```

## Basic Usage

You can import the package in your scripts:
```python
import quantum_algos
import cirq
```

## Algorithms

### Deutsch-Jozsa Algorithm

Determines if a function (oracle) is constant (returns same value for all inputs) or balanced (returns 0 for half of inputs and 1 for the other half).

```python
from quantum_algos.deutsch_jozsa import DeutschJozsa

# 1. Define inputs
n_qubits = 3

# 2. Create an oracle (e.g., Balanced)
oracle = DeutschJozsa.create_balanced_oracle()

# 3. Run the algorithm
dj = DeutschJozsa(n_qubits, oracle)
result = dj.run()

print(f"The oracle is: {result}")
# Output: The oracle is: Balanced
```
