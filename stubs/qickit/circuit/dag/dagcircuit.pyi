from qickit.circuit.dag import DAGNode
__all__ = ["DAGCircuit"]

class DAGCircuit:
    num_qubits: int
    qubits: dict[str, DAGNode]
    def __init__(self, num_qubits: int) -> None: ...
    def add_operation(self, operation: dict) -> None: ...
    def get_depth(self) -> int: ...
    def draw(self) -> None: ...