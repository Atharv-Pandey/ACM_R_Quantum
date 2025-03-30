#Used AI implementation
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def oracle(circuit):
    circuit.cz(0, 1) 

def diffusion_operator(circuit):
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.h(1)
    circuit.cz(0, 1)
    circuit.h(1)
    circuit.x([0, 1])
    circuit.h([0, 1])


grover_circuit = QuantumCircuit(2, 2)

grover_circuit.h([0, 1])

oracle(grover_circuit)

diffusion_operator(grover_circuit)

grover_circuit.measure([0, 1], [0, 1])

simulator = AerSimulator()
job = simulator.run(grover_circuit)
result = job.result()

counts = result.get_counts()
print("Measurement Results:", counts)
plot_histogram(counts)
