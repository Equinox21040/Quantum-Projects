import cirq

qubits = cirq.LineQubit.range(2)


def Q1Circuit():

    yield cirq.X(qubits[0])
    yield cirq.X(qubits[0])**0.5
# yield cirq.X(qubits[0])**0.25
# yield cirq.X(qubits[0])**0.75
    yield cirq.X(qubits[0])**(-1)
    yield cirq.measure(qubits[0] , key = "q1")




circuit = cirq.Circuit()
circuit.append(Q1Circuit())
print(circuit)

simulate = cirq.Simulator()
results1 = simulate.run(circuit , repetitions= 1000)
print(results1)
print(results1.histogram(key = "q1"))
cirq.plot_state_histogram(results1)

print()
print()
print()



def Q2Circuit():
    yield cirq.X(qubits[1])
    yield cirq.X(qubits[1])**(-1)
    yield cirq.measure(qubits[1], key="q2")

circuit = cirq.Circuit()
circuit.append(Q2Circuit())
print(circuit)

simulate = cirq.Simulator()
results2 = simulate.run(circuit , repetitions= 1000)
print(results2)
print(results2.histogram(key = "q2"))
cirq.plot_state_histogram(results2)