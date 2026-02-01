import pytest
import cirq
import numpy as np
from classical_algos.eigensolver import ClassicalEigensolver

def test_single_qubit_z():
    """Test H = Z. Ground state energy should be -1."""
    q = cirq.GridQubit(0, 0)
    hamiltonian = cirq.Z(q)
    solver = ClassicalEigensolver(hamiltonian)
    energy = solver.compute_ground_state_energy()
    assert np.isclose(energy, -1.0)

def test_single_qubit_x():
    """Test H = X. Ground state energy should be -1."""
    q = cirq.GridQubit(0, 0)
    hamiltonian = cirq.X(q)
    solver = ClassicalEigensolver(hamiltonian)
    energy = solver.compute_ground_state_energy()
    assert np.isclose(energy, -1.0)

def test_two_qubit_z_sum():
    """Test H = Z0 + Z1. Ground state |11> energy -1 + -1 = -2."""
    q0, q1 = cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)
    hamiltonian = cirq.Z(q0) + cirq.Z(q1)
    solver = ClassicalEigensolver(hamiltonian)
    energy = solver.compute_ground_state_energy()
    assert np.isclose(energy, -2.0)

def test_two_qubit_z_product():
    """Test H = Z0 * Z1. Ground states |01>, |10> with energy -1."""
    q0, q1 = cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)
    hamiltonian = cirq.Z(q0) * cirq.Z(q1)
    solver = ClassicalEigensolver(hamiltonian)
    energy = solver.compute_ground_state_energy()
    assert np.isclose(energy, -1.0)

def test_complex_hamiltonian():
    """Test H = -1.0*Z0*Z1 - 1.0*X0. Same as VQE demo."""
    q0, q1 = cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)
    hamiltonian = -1.0 * cirq.Z(q0) * cirq.Z(q1) - 1.0 * cirq.X(q0)
    solver = ClassicalEigensolver(hamiltonian)
    energy = solver.compute_ground_state_energy()
    # Eigenvalues of this matrix are approx +/- 1.414...
    assert np.isclose(energy, -np.sqrt(2), atol=1e-5)

def test_three_qubit_hamiltonian():
    """Test H = Z0 + Z1 + Z2. Ground state |111> energy -3."""
    q0, q1, q2 = cirq.GridQubit(0, 0), cirq.GridQubit(0, 1), cirq.GridQubit(0, 2)
    hamiltonian = cirq.Z(q0) + cirq.Z(q1) + cirq.Z(q2)
    solver = ClassicalEigensolver(hamiltonian)
    energy = solver.compute_ground_state_energy()
    assert np.isclose(energy, -3.0)
