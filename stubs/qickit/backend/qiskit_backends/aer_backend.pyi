import numpy as np
from numpy.typing import NDArray
from qickit.backend import NoisyBackend
from qickit.circuit import Circuit

__all__ = ['AerBackend']

class AerBackend(NoisyBackend):
    def __init__(self, single_qubit_error: float = 0.0, two_qubit_error: float = 0.0, device: str = 'CPU') -> None: ...
    def get_statevector(self, circuit: Circuit) -> NDArray[np.complex128]: ...
    def get_operator(self, circuit: Circuit) -> NDArray[np.complex128]: ...
    def get_counts(self, circuit: Circuit, num_shots: int) -> dict[str, int]: ...