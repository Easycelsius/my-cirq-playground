import cirq
import matplotlib.pyplot as plt

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)

print("Circuit:")
print(circuit)

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

# Visualize with matplotlib
cirq.plot_state_histogram(histogram, plt.subplot())
plt.title("Qubit Measurement Results")
plt.xlabel("State")
plt.ylabel("Count")
plt.savefig("hello_qubit_histogram.png")
print("\nHistogram saved to 'hello_qubit_histogram.png'")
