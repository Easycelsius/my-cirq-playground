import cirq
import numpy as np
import sympy
from scipy.optimize import minimize
from typing import List, Callable, Tuple, Any
from quantum_algos.visualization import plot_convergence

class VQE:
    """Variational Quantum Eigensolver implementation."""

    def __init__(self, 
                 qubits: List[cirq.Qid], 
                 ansatz: Callable[[List[cirq.Qid], Any], cirq.Circuit],
                 hamiltonian: cirq.PauliSum):
        """
        Args:
            qubits: List of qubits used in the system.
            ansatz: Function that returns the parameterized circuit. 
                    Should accept (qubits, symbols).
            hamiltonian: The Hamiltonian operator to minimize expectation value for.
        """
        self.qubits = qubits
        self.ansatz = ansatz
        self.hamiltonian = hamiltonian
        self.simulator = cirq.Simulator()
        self.history = []

    def expectation_value(self, params: List[float], symbols: List[sympy.Symbol]) -> float:
        """Calculates the expectation value <H> for given parameters."""
        resolver = cirq.ParamResolver(dict(zip(symbols, params)))
        circuit = self.ansatz(self.qubits, symbols)
        
        # Simulate state
        # Note: For small systems, we can use simulate() to get the wave function
        # and calculate expectation value directly. For larger/real systems, 
        # we would sample. Here we use exact simulation for demonstration.
        result = self.simulator.simulate(circuit, param_resolver=resolver)
        
        # Calculate <psi|H|psi>
        # cirq.PauliSum.expectation_from_state_vector works efficiently
        expect = self.hamiltonian.expectation_from_state_vector(
            result.final_state_vector, 
            qubit_map={q: i for i, q in enumerate(self.qubits)}
        )
        return expect.real

    def minimize(self, initial_params: List[float], symbols: List[sympy.Symbol], method: str = 'COBYLA') -> Any:
        """
        Runs the classical optimization loop.
        
        Args:
            initial_params: Initial guess for parameters.
            symbols: List of sympy Symbols used in the ansatz.
            method: Scipy minimization method (default 'COBYLA').
            
        Returns:
            Optimization result object from scipy.
        """
        self.history = [] # Reset history

        def cost_function(params):
            val = self.expectation_value(params, symbols)
            self.history.append(val)
            return val

        result = minimize(cost_function, initial_params, method=method)
        return result

    def plot_history(self, filename: str = "vqe_convergence.png"):
        """Plots the convergence history."""
        plot_convergence(self.history, title="VQE Optimization Trace", filename=filename)
