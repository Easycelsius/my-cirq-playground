import matplotlib.pyplot as plt
import cirq
from cirq.contrib.svg import SVGCircuit
from typing import Dict, List, Any

def plot_histogram(data: Any, title: str = "Qubit Measurement Results", filename: str = "histogram.png"):
    """
    Plots a histogram of measurement results.
    
    Args:
        data: The histogram data (e.g., from result.histogram()).
        title: Title of the plot.
        filename: Output filename to save the plot.
    """
    plt.figure()
    cirq.plot_state_histogram(data, plt.subplot())
    plt.title(title)
    plt.xlabel("State")
    plt.ylabel("Count")
    plt.savefig(filename)
    print(f"\nHistogram saved to '{filename}'")
    plt.close()

def plot_convergence(history: List[float], title: str = "Optimization Convergence", filename: str = "convergence.png"):
    """
    Plots the convergence of an optimization process (e.g., VQE cost function).
    
    Args:
        history: List of cost values per iteration.
        title: Title of the plot.
        filename: Output filename to save the plot.
    """
    plt.figure()
    plt.plot(history, marker='o')
    plt.title(title)
    plt.xlabel("Iteration")
    plt.ylabel("Cost Value")
    plt.grid(True)
    plt.savefig(filename)
    print(f"\nConvergence plot saved to '{filename}'")
    plt.close()

def save_circuit_svg(circuit: cirq.Circuit, filename: str = "circuit.svg"):
    """
    Saves the quantum circuit as an SVG file.
    
    Args:
        circuit: The Cirq circuit to visualize.
        filename: Output filename (should end in .svg).
    """
    svg_string = SVGCircuit(circuit)._repr_svg_()
    with open(filename, 'w') as f:
        f.write(svg_string)
    print(f"\nCircuit SVG saved to '{filename}'")
