# My Cirq Playground

This is a personal playground for experimenting with quantum algorithms using the [Cirq](https://quantumai.google/cirq) library.
**GitHub Repository:** [https://github.com/Easycelsius/my-cirq-playground](https://github.com/Easycelsius/my-cirq-playground)

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
- **`src/quantum_algos/`**: Core quantum algorithms (e.g., Deutsch-Jozsa, VQE).
- **`src/classical_algos/`**: Classical algorithms for benchmarking and verification (e.g., exact eigensolver).
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

### Variational Quantum Eigensolver (VQE)

Approximates the ground state energy of a Hamiltonian using a parameterized quantum circuit and classical optimization.

```python
import cirq
import sympy
from quantum_algos.vqe import VQE

# 1. Define Qubits & Hamiltonian (H = Z)
q0 = cirq.GridQubit(0, 0)
hamiltonian = cirq.Z(q0)

# 2. Define Ansatz (Ry rotation)
theta = sympy.Symbol('theta')
def ansatz(qubits, symbols):
    return cirq.Circuit(cirq.ry(symbols[0]).on(qubits[0]))

# 3. Run VQE
vqe = VQE([q0], ansatz, hamiltonian)
result = vqe.minimize(initial_params=[0.1], symbols=[theta])

print(f"Optimal Energy: {result.fun}")
# Output: Optimal Energy: -1.0 (approx)
```

### Classical Eigensolver

Used for verifying VQE results by computing eigenvalues classically.

```python
from classical_algos.eigensolver import ClassicalEigensolver

solver = ClassicalEigensolver(hamiltonian)
exact_energy = solver.compute_ground_state_energy()
print(f"Exact Energy: {exact_energy}")
```
