import cirq
from quantum_algos.visualization import plot_histogram, save_circuit_svg

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)

print("Circuit:")
print(circuit)
save_circuit_svg(circuit, "hello_qubit_circuit.svg")

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)

print("\nResults:")
print(result)

# Get the histogram
histogram = result.histogram(key='m')

# Plot the histogram
print("\nHistogram:")
print(histogram)

# Visualize using utility
plot_histogram(histogram, filename="hello_qubit_histogram.png")
