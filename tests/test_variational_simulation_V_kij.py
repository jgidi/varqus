import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, assemble
from qiskit.circuit import Gate
from qiskit.extensions import HamiltonianGate
from qiskit.circuit.library.standard_gates import *
from qiskit.quantum_info.operators import Operator, Pauli
from core.variational_simulation_with_v import A_kqij, V_kij
from core.utils import test_A_kqij


# n_qubits = 3
# J = 1j*1/2
# B = 1j*1/2
# fs = [[-J, -J, -J], [-B, -B, -B]]
# params = np.array([1.0, 1.0])
# ops = [["ZZI", "IZZ", "ZIZ"], ["XII", "IXI", "IIX"]]
# # ops = [["IZZ", "ZZI", "ZIZ"], ["IIX", "IXI", "XII"]]
# k, q, i, j = 0, 1, 1, 0
# vector = np.array([ 0.35355339,  0.35355339,
#         0.35355339, -0.35355339,
#         0.35355339, -0.35355339,
#        -0.35355339, -0.35355339]).reshape(8, 1) +1j*0
# a_kqij = A_kqij(params, fs, ops, n_qubits, k, q, i, j)
# a_kqij_test = test_A_kqij(params, fs, ops, n_qubits, k, q, i, j, vector)
#
# a_kqij, a_kqij_test

n_qubits = 2
J = 1/2
B = 1/2
fs = [[-1j*J], [-1j*B, -1j*B]]
params = np.array([1.0, 1.0])
ops = [["ZZ"], ["XI", "IX"]]
# ops = [["IZZ", "ZZI", "ZIZ"], ["IIX", "IXI", "XII"]]

hs = [-2.0*J, -B, -B]
opsH = ["ZZ", "XI", "IX"]


k_a, q_a, i_a, j_a = 1, 1, 0, 0
vector = np.array([0.5, 0.5, 0.5, 0.5]).reshape(4, 1) +1j*0
# a_kqij = A_kqij(params, fs, ops, n_qubits, k_a, q_a, i_a, j_a)
# a_kqij_test = test_A_kqij(params, fs, ops, n_qubits, k_a, q_a, i_a, j_a, vector)

# print(a_kqij, a_kqij_test)


k_v, i_v, j_v = 1,1,2
vector = np.array([0.5, 0.5, 0.5, 0.5]).reshape(4, 1) +1j*0
v_kij = V_kij(params, fs, hs, ops, opsH, n_qubits, k_v, i_v, j_v)

print(v_kij)
