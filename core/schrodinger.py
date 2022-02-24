import numpy as np
import scipy.linalg as la
from core.utils import parse_gate


def time_evolution(opsH, hs, dt, Nt, img=True):
    n_ops = len(opsH)
    n_qubits = len(opsH[0])
    Hamiltonian = hs[0]*parse_gate(opsH[0])
    U = np.zeros((2**n_qubits, 2**n_qubits, Nt), dtype="complex")
    for j in range(1, n_ops):
        Hamiltonian += hs[j]*parse_gate(opsH[j])
    for n in range(Nt):
        if img==True:
            U[:, :, n] = la.expm(-1j*dt*n*Hamiltonian)
        elif img==False:
            U[:, :, n] = la.expm(dt*n*Hamiltonian)
    return U


def state_evoluted(initial_state, opsH, hs, dt, Nt, img=True):
    n_qubits = len(opsH[0])
    state_evoluted = np.zeros((2**n_qubits, Nt), dtype="complex")
    U = time_evolution(opsH, hs, dt, Nt, img=True)
    for n in range(Nt):
        state_evoluted[:, n] = np.dot(U[:, :, n], initial_state)
    return state_evoluted