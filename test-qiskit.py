from qiskit import *
from qiskit.circuit.library import *
from qiskit_aer import AerSimulator
import sys

sim = AerSimulator(method='statevector')
#sim_gpu = AerSimulator(method='tensor_network', device='CPU')
print(sim.status)

shots = 100
depth=10
qubits = 10
block_bits = 10

circuit = transpile(QuantumVolume(qubits, depth, seed=0),
                    backend=sim,
                    optimization_level=0)
circuit.measure_all()

new_circuit = transpile(circuit, sim)
#result_base = sim.run(new_circuit)

from qiskit.primitives import BackendSampler

sampler = BackendSampler(sim)
result_base = sampler.run(circuit)

#result_base = execute(circuit,sim,shots=shots,seed_simulator=12345).result()

#print(result_base)
#if result_base.to_dict()['metadata']['mpi_rank'] == 0:
print(result_base)
print(f" > Status: {result_base.status()}")
#print(result_base.status().to_dict()['backend_name'])
print(result_base.result())
#print(sorted(result_base.to_dict()['results'][0]['data']['counts'].items(),key=lambda x:x[0]))
