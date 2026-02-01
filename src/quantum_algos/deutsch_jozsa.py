from typing import List, Callable, Dict
import cirq
from quantum_algos.errors import OracleValueError, QubitCountError

class DeutschJozsa:
    """Class to run the Deutsch-Jozsa algorithm using Cirq."""

    def __init__(self, n_qubits: int, oracle: Callable[[List[cirq.Qid], cirq.Qid], cirq.OP_TREE]):
        """
        Args:
            n_qubits: Number of input qubits (not including the helper qubit).
            oracle: A function that takes a list of input qubits and a helper qubit,
                    and yields operations representing the oracle U_f.
        """
        self.n = n_qubits
        self.oracle = oracle
        self.input_qubits = cirq.LineQubit.range(n_qubits)
        self.helper_qubit = cirq.LineQubit(n_qubits)
        self.circuit = self._create_circuit()

    def _create_circuit(self) -> cirq.Circuit:
        """Creates the Deutsch-Jozsa circuit."""
        c = cirq.Circuit()

        # 1. Initialize helper qubit to |-> state
        c.append(cirq.X(self.helper_qubit))
        c.append(cirq.H(self.helper_qubit))

        # 2. Apply Hadamard to all input qubits
        c.append(cirq.H.on_each(self.input_qubits))

        # 3. Apply Oracle
        c.append(self.oracle(self.input_qubits, self.helper_qubit))

        # 4. Apply Hadamard to input qubits again
        c.append(cirq.H.on_each(self.input_qubits))

        # 5. Measure input qubits
        c.append(cirq.measure(*self.input_qubits, key='result'))

        return c

    def run(self, repetitions: int = 1) -> str:
        """
        Runs the algorithm simulation.

        Returns:
            "Constant" if measurement is all 0s.
            "Balanced" if measurement is 1 for half of the elements, 0 for the other half.
        """
        simulator = cirq.Simulator()
        result = simulator.run(self.circuit, repetitions=repetitions)
        measurements = result.measurements['result'][0] # Check the first run
        print("Measurements:", measurements)

        # If all input bits are 0, it's constant. Otherwise, balanced.
        if sum(measurements) == 0:
            return "Constant"
        else:
            return "Balanced"

    @staticmethod
    def create_constant_oracle(value: int) -> Callable[[List[cirq.Qid], cirq.Qid], cirq.OP_TREE]:
        """
        Creates a constant oracle where f(x) = value.
        If value is 0, oracle is Identity.
        If value is 1, oracle is X on the helper qubit.
        """
        def oracle(input_qubits: List[cirq.Qid], helper_qubit: cirq.Qid):
            if value == 1:
                yield cirq.X(helper_qubit)
        return oracle

    @staticmethod
    def create_balanced_oracle() -> Callable[[List[cirq.Qid], cirq.Qid], cirq.OP_TREE]:
        """
        Creates a balanced oracle. 
        Example: f(x) = x_0 (CNOT from first qubit to helper).
        This is balanced because x_0 is 0 for half inputs and 1 for half inputs.
        """
        def oracle(input_qubits: List[cirq.Qid], helper_qubit: cirq.Qid):
            # Implement CNOT(x_0, y)
            yield cirq.CNOT(input_qubits[0], helper_qubit)
        return oracle

    @staticmethod
    def create_my_oracle(n_qubits: int, input_values: List[int]) -> Callable[[List[cirq.Qid], cirq.Qid], cirq.OP_TREE]:
        """
        Create a custom oracle.
        
        Args:
            n_qubits: Number of input qubits.
            input_values: List of 0s and 1s. 
                          If input_values[i] == 1, apply CNOT(input[i], helper).
                          This creates a Balanced function (Bernstein-Vazirani style)
                          UNLESS input_values is all zeros.
        """
        
        if len(input_values) != n_qubits:
             raise QubitCountError(f"Length ({len(input_values)}) must match n_qubits ({n_qubits})")

        def oracle(input_qubits: List[cirq.Qid], helper_qubit: cirq.Qid):
            # Case A: Constant Function f(x) = 1
            if n_qubits == sum(input_values):
                yield cirq.X(helper_qubit)
                return

            # Case B: Balanced Function (or f(x)=0 if all zeros): f(x) = (x & input_values)
            for i, val in enumerate(input_values):
                if val == 1:
                    yield cirq.CNOT(input_qubits[i], helper_qubit)
        
        return oracle