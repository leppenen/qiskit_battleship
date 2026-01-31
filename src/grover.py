import numpy as np
from qiskit import QuantumCircuit

def grover_operator_custom(oracle: QuantumCircuit):
  n_q = oracle.num_qubits
  q_list = list(range(n_q))
  qc = QuantumCircuit(n_q)
  # S_f
  qc.compose(oracle, inplace=True)
  # H
  qc.h(q_list)
  # Zero reflection, S_0
  qc.x(q_list) # 000 -> 111 | 111 -> 000
  qc.h(n_q - 1) # 111 -> 110 - 111 | 000 -> 000 + 001 = 00 (0 + 1)
  qc.mcx(list(range(n_q - 1)), n_q - 1) # 110 - 111 -> 111 - 110 = 11 (1 - 0) | 00 (0 + 1) -> 00 (0 + 1)
  qc.h(n_q - 1) # 11 (1 - 0) -> -111 | 00 (0 + 1) -> 000
  qc.x(q_list) # -000 | 111
  # H
  qc.h(q_list)

  return qc
