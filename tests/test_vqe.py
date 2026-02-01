import pytest
import cirq
import sympy
import numpy as np
from quantum_algos.vqe import VQE
from classical_algos.eigensolver import ClassicalEigensolver

def test_vqe_single_qubit_z():
    """Test VQE on a single qubit Hamiltonian H = Z. Ground state overlap should maximize |1> (energy -1)."""
    qubit = cirq.GridQubit(0, 0)
    theta = sympy.Symbol('theta')
    
    # Ansatz: Ry(theta). 
    # If theta=pi, Ry(pi)|0> = |1>, <Z> = -1.
    # If theta=0, Ry(0)|0> = |0>, <Z> = 1.
    def ansatz(qubits, symbols):
        return cirq.Circuit(cirq.ry(symbols[0]).on(qubits[0]))

    hamiltonian = cirq.Z(qubit)
    
    vqe = VQE([qubit], ansatz, hamiltonian)
    
    # Run optimization
    initial_params = [0.1]
    result = vqe.minimize(initial_params, [theta], method='COBYLA')
    
    # Check convergence close to -1
    assert np.isclose(result.fun, -1.0, atol=0.1)

def test_vqe_simple_pauli_sum():
    """Test VQE on H = Z_0 + Z_1. Ground state |11>, energy -2."""
    q0, q1 = cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)
    a, b = sympy.Symbol('a'), sympy.Symbol('b')
    
    def ansatz(qubits, symbols):
        return cirq.Circuit(
            cirq.ry(symbols[0]).on(qubits[0]),
            cirq.ry(symbols[1]).on(qubits[1])
        )

    hamiltonian = cirq.Z(q0) + cirq.Z(q1)
    
    vqe = VQE([q0, q1], ansatz, hamiltonian)
    
    result = vqe.minimize([0.1, 0.1], [a, b], method='COBYLA')
    assert np.isclose(result.fun, -2.0, atol=0.1)

def test_vqe_vs_classical():
    """Verify VQE matches Classical Solver for a random Hamiltonian."""
    q0 = cirq.GridQubit(0, 0)
    theta = sympy.Symbol('theta')
    
    # H = X + Z
    # Eigenvalues of X+Z are +/- sqrt(2) approx +/- 1.414
    hamiltonian = cirq.X(q0) + cirq.Z(q0)
    
    def ansatz(qubits, symbols):
        return cirq.Circuit(cirq.ry(symbols[0]).on(qubits[0]))
    
    # Classical
    classical = ClassicalEigensolver(hamiltonian)
    exact_energy = classical.compute_ground_state_energy()
    
    # VQE
    vqe = VQE([q0], ansatz, hamiltonian)
    result = vqe.minimize([0.0], [theta], method='COBYLA')
    
    # Ground state energy should be -sqrt(2)
    assert np.isclose(exact_energy, -np.sqrt(2), atol=1e-5)
    
    # VQE should find it (Ry rotation can reach any superposition of 0 and 1, 
    # and the ground state of X+Z is a qubit state)
    assert np.isclose(result.fun, exact_energy, atol=0.1)
