import cirq
import numpy as np
from scipy.sparse.linalg import eigsh

class ClassicalEigensolver:
    """Calculates exact eigenvalues classically."""

    def __init__(self, hamiltonian: cirq.PauliSum):
        self.hamiltonian = hamiltonian

    def compute_ground_state_energy(self) -> float:
        """
        Computes the minimum eigenvalue (ground state energy) of the Hamiltonian.
        """
        # Convert PauliSum to sparse matrix
        matrix = self.hamiltonian.matrix()
        
        # If matrix is small, use numpy.linalg.eigh (returns all eigenvalues)
        if matrix.shape[0] <= 1024: # 10 qubits
             eigenvalues = np.linalg.eigvalsh(matrix)
             return float(np.min(eigenvalues))
        else:
             # Use scipy.sparse.linalg.eigsh for larger sparse matrices
             # k=1 returns 1 eigenvalue, which='SA' means Smallest Algebraic
             eigenvalues, _ = eigsh(matrix, k=1, which='SA')
             return float(eigenvalues[0])
