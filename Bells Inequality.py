import cirq
import matplotlib.pyplot as plt


qubits = cirq.LineQubit.range(2)
angle = -1.0

for i in range(200):
    def CEntang():
        global qubits
        yield cirq.X(qubits[0])**0.5, cirq.X(qubits[1])
        yield cirq.CX(qubits[0], qubits[1])
        yield cirq.X(qubits[0]), cirq.X(qubits[1])**(angle)
        yield cirq.Moment(cirq.measure(qubits[0], key="q1"), cirq.measure(qubits[1], key="q2"))


    circuit = cirq.Circuit()
    circuit.append(CEntang())
    print(circuit)
    simulate = cirq.Simulator()
    result = simulate.run(circuit, repetitions=1000)
    print(result.multi_measurement_histogram(keys=["q1", "q2"]))





    angle =  angle + 0.01
    print(angle*360)
    cirq.reset(qubits[0])
    cirq.reset(qubits[1])
    #print(result)


    #cirq.plot_state_histogram(result)



