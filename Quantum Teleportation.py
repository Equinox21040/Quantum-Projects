import cirq




qubits = cirq.LineQubit.range(3)


for i in range(200):
    def CEntang():
        global qubits
        yield cirq.H(qubits[1]) , cirq.X(qubits[0])
        yield cirq.CX(qubits[1],qubits[2])
        yield cirq.CX(qubits[0],qubits[1])
        yield cirq.CX(qubits[1],qubits[2])
        yield cirq.Moment(cirq.measure(qubits[0], key="q1"), cirq.measure(qubits[2], key="q2"))


    circuit = cirq.Circuit()
    circuit.append(CEntang())
    print(circuit)
    simulate = cirq.Simulator()
    result = simulate.run(circuit, repetitions=1000)
    print(result.multi_measurement_histogram(keys=["q1", "q2"]))






    cirq.reset(qubits[0])
    cirq.reset(qubits[1])
    print(result)


    #cirq.plot_state_histogram(result)
