import cirq
import sympy
import numpy as np
import time
from quantum_algos.vqe import VQE
from classical_algos.eigensolver import ClassicalEigensolver
from quantum_algos.visualization import save_circuit_svg

def two_qubit_demo():
    # 1. Define Qubits
    q0 = cirq.GridQubit(0, 0)
    q1 = cirq.GridQubit(0, 1)
    qubits = [q0, q1]

    # 2. Define Hamiltonian
    # Example: Transverse-field Ising model H = -1.0 * Z0*Z1 - 1.0 * X0
    # Ground state needs to align spins but also superposition from X.
    hamiltonian = -1.0 * cirq.Z(q0) * cirq.Z(q1) - 1.0 * cirq.X(q0)
    """
    [[-1.  0. -1.  0.]
     [ 0.  1.  0. -1.]
     [-1.  0.  1.  0.]
     [ 0. -1.  0. -1.]]
    """
    print(f"Hamiltonian: {hamiltonian}")

    # 3. Define Ansatz
    # Simple Hardware Efficient Ansatz
    theta0 = sympy.Symbol('theta0')
    theta1 = sympy.Symbol('theta1')
    theta2 = sympy.Symbol('theta2')
    symbols = [theta0, theta1, theta2]

    def ansatz(qs, syms):
        c = cirq.Circuit()
        c.append(cirq.ry(syms[0]).on(qs[0]))
        c.append(cirq.ry(syms[1]).on(qs[1]))
        c.append(cirq.CNOT(qs[0], qs[1]))
        c.append(cirq.ry(syms[2]).on(qs[0]))
        return c

    # Visualize Ansatz (using random params for drawing)
    dummy_circuit = ansatz(qubits, symbols)
    print("two_qubit_demo ansatz:")
    print(dummy_circuit)
    save_circuit_svg(dummy_circuit, "vqe_ansatz_circuit.svg")

    # 4. Run VQE
    vqe = VQE(qubits, ansatz, hamiltonian)
    
    initial_params = list(np.random.random(len(symbols)))
    print(f"Initial Parameters: {initial_params}")
    
    start_time = time.time()
    result = vqe.minimize(initial_params, symbols, method='COBYLA')
    vqe_time = time.time() - start_time
    
    print("\n--- VQE Results ---")
    print(f"Optimal Value (Energy): {result.fun:.6f}")
    print(f"Optimal Parameters: {result.x}")
    print(f"Iterations: {result.nfev}")
    print(f"Execution Time: {vqe_time:.4f} sec")

    # 5. Run Classical Eigensolver
    classical_solver = ClassicalEigensolver(hamiltonian)
    
    start_time = time.time()
    exact_energy = classical_solver.compute_ground_state_energy()
    classical_time = time.time() - start_time
    
    print("\n--- Classical Results ---")
    print(f"Exact Energy: {exact_energy:.6f}")
    print(f"Execution Time: {classical_time:.4f} sec")

    # 6. Comparison
    print("\n--- Comparison ---")
    print(f"Energy Difference: {abs(result.fun - exact_energy):.6f}")
    
    # 7. Plot Convergence
    vqe.plot_history(filename="vqe_convergence.png")

def three_qubit_demo():
    # 1. Define Qubits
    q0 = cirq.GridQubit(0, 0)
    q1 = cirq.GridQubit(0, 1)
    q2 = cirq.GridQubit(0, 2)
    qubits = [q0, q1, q2]

    # 2. Define Hamiltonian
    # Example: Transverse-field Ising model H = -1.0 * Z0*Z1 - 1.0 * X0
    # Ground state needs to align spins but also superposition from X.
    # hamiltonian = -1.0 * cirq.Z(q0) * cirq.Z(q1) - 1.0 * cirq.X(q0)
    hamiltonian = -1.0 * cirq.Z(q0) * cirq.Z(q1) \
              -1.0 * cirq.Z(q1) * cirq.Z(q2) \
              -1.0 * cirq.X(q0)
    print(f"Hamiltonian: {hamiltonian.matrix}")

    # 3. Define Ansatz
    # Simple Hardware Efficient Ansatz
    theta0 = sympy.Symbol('theta0')
    theta1 = sympy.Symbol('theta1')
    theta2 = sympy.Symbol('theta2')
    theta3 = sympy.Symbol('theta3')
    theta4 = sympy.Symbol('theta4')
    theta5 = sympy.Symbol('theta5')
    symbols = [theta0, theta1, theta2, theta3, theta4, theta5]

    def ansatz(qs, syms):
        c = cirq.Circuit()
        c.append(cirq.ry(syms[0]).on(qs[0]))
        c.append(cirq.ry(syms[1]).on(qs[1]))
        c.append(cirq.CNOT(qs[0], qs[1]))
        c.append(cirq.ry(syms[2]).on(qs[0]))
        c.append(cirq.CNOT(qs[1], qs[2]))
        c.append(cirq.ry(syms[3]).on(qs[0]))
        c.append(cirq.ry(syms[4]).on(qs[1]))
        c.append(cirq.ry(syms[5]).on(qs[2]))
        return c

    # Visualize Ansatz (using random params for drawing)
    dummy_circuit = ansatz(qubits, symbols)
    print("three_qubit_demo ansatz:")
    print(dummy_circuit)
    save_circuit_svg(dummy_circuit, "vqe_ansatz_circuit.svg")

    # 4. Run VQE
    vqe = VQE(qubits, ansatz, hamiltonian)
    
    initial_params = list(np.random.random(len(symbols)))
    print(f"Initial Parameters: {initial_params}")
    
    start_time = time.time()
    result = vqe.minimize(initial_params, symbols, method='COBYLA')
    vqe_time = time.time() - start_time
    
    print("\n--- VQE Results ---")
    print(f"Optimal Value (Energy): {result.fun:.6f}")
    print(f"Optimal Parameters: {result.x}")
    print(f"Iterations: {result.nfev}")
    print(f"Execution Time: {vqe_time:.4f} sec")

    # 5. Run Classical Eigensolver
    classical_solver = ClassicalEigensolver(hamiltonian)
    
    start_time = time.time()
    exact_energy = classical_solver.compute_ground_state_energy()
    classical_time = time.time() - start_time
    
    print("\n--- Classical Results ---")
    print(f"Exact Energy: {exact_energy:.6f}")
    print(f"Execution Time: {classical_time:.4f} sec")

    # 6. Comparison
    print("\n--- Comparison ---")
    print(f"Energy Difference: {abs(result.fun - exact_energy):.6f}")
    
    # 7. Plot Convergence
    vqe.plot_history(filename="vqe_convergence.png")

if __name__ == "__main__":
    print("###############################")
    two_qubit_demo()
    print("###############################")
    three_qubit_demo()