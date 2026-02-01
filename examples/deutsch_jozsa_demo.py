from quantum_algos.deutsch_jozsa import DeutschJozsa

# 1. Define inputs
my_oracle_sequence = [1, 1, 1, 1]
n_qubits = len(my_oracle_sequence)

# 2. Create an oracle (e.g., Balanced)
oracle = DeutschJozsa.create_my_oracle(n_qubits, my_oracle_sequence)

# 3. Run the algorithm
dj = DeutschJozsa(n_qubits, oracle)
print("Circuit:")
print(dj.circuit)
result = dj.run()

print(f"The oracle is: {result}")

