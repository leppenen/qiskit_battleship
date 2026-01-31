import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import DiagonalGate


def _validate_targets(targets: list[str]) -> int:
    if not targets:
        raise ValueError("targets must be a non-empty list of bitstrings")

    num_qubits = len(targets[0])
    if num_qubits == 0:
        raise ValueError("targets must contain non-empty bitstrings")

    if any(len(t) != num_qubits for t in targets):
        raise ValueError("all target bitstrings must have the same length")

    if any(set(t) - {"0", "1"} for t in targets):
        raise ValueError("targets must be binary strings containing only 0/1")

    return num_qubits


def create_multi_target_oracle(targets: list[str]) -> QuantumCircuit:
    """Create an oracle that flips the phase of multiple target bitstrings.
    In a battle ship game, these targets represent the positions of the ships.
    """
    num_qubits = _validate_targets(targets)
    qc = QuantumCircuit(num_qubits)

    oracle_matrix = np.ones(2**num_qubits, dtype=float)
    for target in targets:
        idx = int(target, 2)
        oracle_matrix[idx] = -1.0

    qc.append(DiagonalGate(oracle_matrix.tolist()), range(num_qubits))
    return qc


def create_multi_target_oracle_gate(targets: list[str]) -> QuantumCircuit:
    """Create a gate-based oracle that flips phase for each target bitstring.
    """
    num_qubits = _validate_targets(targets)
    qc = QuantumCircuit(num_qubits)

    for target in targets:
        # Qiskit uses little-endian qubit order: q0 is the rightmost bit.
        # Map target state to |11..1> using X on 0-bits (rightmost bit -> qubit 0).
        zero_indices = [i for i, bit in enumerate(reversed(target)) if bit == "0"]
        if zero_indices:
            qc.x(zero_indices)

        if num_qubits == 1:
            qc.z(0)
        else:
            # Multi-controlled Z implemented via H + MCX + H on last qubit.
            qc.h(num_qubits - 1)
            qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
            qc.h(num_qubits - 1)

        # Undo X gates to restore original basis states.
        if zero_indices:
            qc.x(zero_indices)

    return qc

