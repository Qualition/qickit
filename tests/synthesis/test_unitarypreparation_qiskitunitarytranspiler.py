# Copyright 2023-2024 Qualition Computing LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://github.com/Qualition/QICKIT/blob/main/LICENSE
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

__all__ = ["TestQiskitUnitaryTranspiler"]

from numpy.testing import assert_almost_equal
from scipy.stats import unitary_group

from qickit.circuit import QiskitCircuit
from qickit.primitives import Operator
from qickit.synthesis.unitarypreparation import QiskitUnitaryTranspiler
from tests.synthesis import UnitaryPreparationTemplate

# Define the test data
unitary_matrix = unitary_group.rvs(8)


class TestQiskitUnitaryTranspiler(UnitaryPreparationTemplate):
    """ `tests.synthesis.test_unitarypreparation_qiskitunitarytranspiler.TestQiskitUnitaryTranspiler` is the tester class
    for `qickit.synthesis.unitarypreparation.QiskitUnitaryTranspiler` class.
    """
    def test_init(self) -> None:
        qiskit_transpiler = QiskitUnitaryTranspiler(QiskitCircuit)

    def test_prepare_unitary_ndarray(self) -> None:
        # Initialize the Qiskit transpiler
        qiskit_transpiler = QiskitUnitaryTranspiler(QiskitCircuit)

        # Prepare the unitary matrix
        circuit = qiskit_transpiler.prepare_unitary(unitary_matrix) # type: ignore

        # Get the unitary matrix of the circuit
        unitary = circuit.get_unitary()

        # Ensure that the unitary matrix is close enough to the expected unitary matrix
        assert_almost_equal(unitary, unitary_matrix, decimal=8)

    def test_prepare_unitary_operator(self) -> None:
        # Initialize the Qiskit transpiler
        qiskit_transpiler = QiskitUnitaryTranspiler(QiskitCircuit)

        # Prepare the unitary matrix
        circuit = qiskit_transpiler.prepare_unitary(Operator(unitary_matrix)) # type: ignore

        # Get the unitary matrix of the circuit
        unitary = circuit.get_unitary()

        # Ensure that the unitary matrix is close enough to the expected unitary matrix
        assert_almost_equal(unitary, unitary_matrix, decimal=8)