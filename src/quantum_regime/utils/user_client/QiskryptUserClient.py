"""

Copyrights:\n
- © Qiskrypt, 2022 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum cryptography, quantum communication and
  other protocols/algorithms, built using the IBM's Qiskit.

College(s):\n
- NOVA School of Science and Technology, NOVA University of Lisbon, Portugal.
- Faculty of Sciences, University of Lisbon, Portugal.
- Tecnico Lisboa, University of Lisbon, Portugal.
- School of Engineering, University of Connecticut, United States of America.

Other Institution(s):\n
- Instituto de Telecomunicacoes, Portugal.
- SQIG, Portugal.
- LASIGE, Portugal.
- UT Austin Program, Portugal.

Author(s):\n
- Ruben Barreiro (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

Acknowledgement(s):\n
- Prof. Andre Souto (Faculty of Sciences, University of Lisbon, Portugal).
- Prof. Paulo Mateus (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Nikola Paunkovic (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Walter Krawec (School of Engineering, University of Connecticut, United States of America).
- Prof. Antonio Ravara (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

"""

"""
Import required Libraries and Packages.
"""

from uuid import UUID

"""
Import the general UUID (Universally Unique IDentifier).
"""

from uuid import uuid1

"""
Import the general UUID (Universally Unique IDentifier) version 1.
"""

from uuid import uuid3

"""
Import the general UUID (Universally Unique IDentifier) version 3.
"""

from uuid import uuid4

"""
Import the general UUID (Universally Unique IDentifier) version 4.
"""

from uuid import uuid5

"""
Import the general UUID (Universally Unique IDentifier) version 5.
"""

from src.quantum_regime.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister

"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.QiskryptAncillaQuantumRegister \
    import QiskryptAncillaQuantumRegister

"""
Import the Qiskrypt's Ancilla Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.fully_quantum.QiskryptFullyQuantumRegister \
    import QiskryptFullyQuantumRegister

"""
Import the Qiskrypt's Fully-Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.fully_quantum.QiskryptAncillaFullyQuantumRegister \
    import QiskryptAncillaFullyQuantumRegister

"""
Import the Qiskrypt's Ancilla Fully-Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.semi_quantum.QiskryptSemiQuantumRegister \
    import QiskryptSemiQuantumRegister

"""
Import the Qiskrypt's Semi-Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.semi_quantum.QiskryptAncillaSemiQuantumRegister \
    import QiskryptAncillaSemiQuantumRegister

"""
Import the Qiskrypt's Ancilla Semi-Quantum Register.
"""

from src.quantum_regime.circuit.registers.classical.QiskryptClassicalRegister \
    import QiskryptClassicalRegister

"""
Import the Qiskrypt's Classical Register.
"""

from src.quantum_regime.utils.parties_and_agents.QiskryptParty \
    import QiskryptParty

"""
Import the Qiskrypt's Party.
"""

from src.quantum_regime.utils.parties_and_agents.quantum.QiskryptQuantumParty \
    import QiskryptQuantumParty

"""
Import the Qiskrypt's Quantum Party.
"""

from src.quantum_regime.utils.parties_and_agents.quantum.fully_quantum.QiskryptFullyQuantumParty \
    import QiskryptFullyQuantumParty

"""
Import the Qiskrypt's Fully-Quantum Party.
"""

from src.quantum_regime.utils.parties_and_agents.quantum.semi_quantum.QiskryptSemiQuantumParty \
    import QiskryptSemiQuantumParty

"""
Import the Qiskrypt's Semi-Quantum Party.
"""

from src.quantum_regime.utils.parties_and_agents.classical.QiskryptClassicalParty \
    import QiskryptClassicalParty

"""
Import the Qiskrypt's Classical Party.
"""

from src.quantum_regime.true_random.random_generator.binary.QiskryptQuantumRandomBinaryGenerator \
    import QiskryptQuantumRandomBinaryGenerator

"""
Import the Qiskrypt's Quantum Random Binary Generator.
"""

from src.quantum_regime.utils.parties_and_agents.QiskryptParty \
    import POSSIBLE_PARTY_CONTEXTS

"""
Import the available Party contexts for the Qiskrypt's Parties.
"""

from src.classical_regime.common.QiskryptClassicalUtilities \
    import QiskryptClassicalUtilities

"""
Import the Qiskrypt's Classical Utilities.
"""

from src.classical_regime.common.QiskryptClassicalUtilities \
    import SIZE_BYTE_IN_NUM_BITS

"""
Import the size of a byte in number of bits.
"""

"""
Definition of Constants and Enumerations.
"""

NUM_BYTES_FOR_UUID = 16
"""
The number of bytes to be used in an UUID (Universally Unique IDentifier)
for the Qiskrypt's User Client.
"""


class QiskryptUserClient:
    """
    Object class for the Qiskrypt's User Client.
    """

    def __init__(self, party: QiskryptParty,
                 uuid_version=0, uuid_bytes=None, uuid_node=None,
                 uuid_clock_sequence=None, uuid_name=None, uuid_namespace=None):
        """
        Constructor of the Qiskrypt's User Client.

        :param party: the Qiskrypt's Party for the Qiskrypt's User Client.
        :param uuid_version: the version of the UUID (Universally Unique IDentifier)
                             for the Qiskrypt's User Client.
        :param uuid_bytes: the bytes to build the UUID (Universally Unique IDentifier)
                           for the Qiskrypt's User Client.
        :param uuid_node: the node to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's User Client.
        :param uuid_clock_sequence: the clock sequence to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's User Client.
        :param uuid_name: the name to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's User Client.
        :param uuid_namespace: the namespace to build the UUID (Universally Unique IDentifier)
                               for the Qiskrypt's User Client.
        """

        if uuid_version == 0:
            """
            If the Qiskrypt's User Client is configured with
            general UUID (Universally Unique IDentifier).
            """

            if uuid_bytes is None:
                """
                If was given specific bytes for the UUID (Universally Unique IDentifier).
                """

                quantum_random_binary_generator = \
                    QiskryptQuantumRandomBinaryGenerator("qu_rng_binary")
                """
                Create a Qiskrypt's Quantum Random Binary Generator.
                """

                quantum_random_binary_generator.initiate((NUM_BYTES_FOR_UUID * SIZE_BYTE_IN_NUM_BITS))
                """
                Initiate the Qiskrypt's Quantum Random Binary Generator, for 128 bits (16 bytes).
                """

                random_binary_string_bits = \
                    quantum_random_binary_generator.generate_binary_string()
                """
                Generate a random binary string in bits, with 128 bits (16 bytes).
                """

                random_binary_string_bytes = \
                    QiskryptClassicalUtilities.convert_binary_string_to_bytes(random_binary_string_bits)
                """
                Convert the random binary string in bits to a random binary string in bytes,
                with 128 bits (16 bytes).
                """

                self.uuid = UUID(bytes=random_binary_string_bytes)
                """
                Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
                """

            else:
                """
                If was not given specific bytes for the UUID (Universally Unique IDentifier).
                """

                self.uuid = UUID(bytes=uuid_bytes)
                """
                Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
                """

        if uuid_version == 1:
            """
            If the Qiskrypt's User Client is configured with
            UUID (Universally Unique IDentifier) version 1.
            """

            self.uuid = uuid1(uuid_node, uuid_clock_sequence)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
            """

        elif uuid_version == 3:
            """
            If the Qiskrypt's User Client is configured with
            UUID (Universally Unique IDentifier) version 3.
            """

            self.uuid = uuid3(uuid_namespace, uuid_name)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
            """

        elif uuid_version == 4:
            """
            If the Qiskrypt's User Client is configured with
            UUID (Universally Unique IDentifier) version 4.
            """

            self.uuid = uuid4()
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
            """

        elif uuid_version == 5:
            """
            If the Qiskrypt's User Client is configured with
            UUID (Universally Unique IDentifier) version 5.
            """

            self.uuid = uuid5(uuid_namespace, uuid_name)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
            """

        else:
            """
            If the Qiskrypt's User Client is configured with an invalid version.
            """

            # TODO Throw - Exception

        self.party = party
        """
        Set the Qiskrypt's Party for the Qiskrypt's User Client.
        """

        self.registers = []
        """
        Set the Qiskrypt's Registers for the Qiskrypt's User Client, as an initially empty list.
        """

    def get_uuid(self) -> UUID:
        """
        Return the UUID (Universally Unique IDentifier) of
        the Qiskrypt's User Client.

        :return self.uuid: the UUID (Universally Unique IDentifier) of
                           the Qiskrypt's User Client.
        """

        """
        Return the UUID (Universally Unique IDentifier) of
        the Qiskrypt's User Client.
        """
        return self.uuid

    def get_party(self) -> QiskryptParty:
        """
        Return the Qiskrypt's Party of the Qiskrypt's User Client.

        :return self.party: the Qiskrypt's Party of the Qiskrypt's User Client.
        """

        """
        Return the Qiskrypt's Party of the Qiskrypt's User Client.
        """
        return self.party

    def get_registers(self) -> list:
        """
        Return the Qiskrypt's Registers of the Qiskrypt's User Client.

        :return self.registers: the Qiskrypt's Registers of the Qiskrypt's User Client.
        """

        """
        Return the Qiskrypt's Registers of the Qiskrypt's User Client.
        """
        return self.registers

    def get_num_registers(self) -> int:
        """
        Return the number of Qiskrypt's Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's User Client.

        :return len(self.registers): the number of Qiskrypt's Registers in
                                     the list of Qiskrypt's Registers of
                                     the Qiskrypt's User Client.
        """

        """
        Return the number of Qiskrypt's Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's User Client.
        """
        return len(self.registers)

    def add_quantum_register(self, quantum_register: QiskryptQuantumRegister):
        """
        Adds a given Qiskrypt's Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's User Client.

        :param quantum_register: the Qiskrypt's Quantum Register to be added
                                 to the list of Qiskrypt's Registers of
                                 the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[0]) and \
                (isinstance(self.get_party(), QiskryptQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Quantum Party and belongs
            to a Quantum Context.
            """

            self.registers.append(quantum_register)
            """
            Adds the given Qiskrypt's Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's User Client.
            """

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Quantum Party or does not
            belongs to a Quantum Context.
            """

            # TODO Throw - Exception

    def remove_quantum_register_by_name(self, quantum_register_name: str):
        """
        Removes a Qiskrypt's Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its name.

        :param quantum_register_name: the name of a Qiskrypt's Quantum Register to be removed
                                      from the list of Qiskrypt's Registers of
                                      the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[0]) and \
                (isinstance(self.get_party(), QiskryptQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Quantum Party and belongs
            to a Quantum Context.
            """

            for current_register_index in range(len(self.registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's User Client. 
                """

                current_register = self.registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if current_register.get_name() == quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is a Qiskrypt's Quantum Register.
                        """

                        self.registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is not a Qiskrypt's Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Quantum Party or does not
            belongs to a Quantum Context.
            """

            # TODO Throw - Exception

    def remove_quantum_register_by_index(self, quantum_register_index: int):
        """
        Removes a Qiskrypt's Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its index.

        :param quantum_register_index: the index of a Qiskrypt's Quantum Register to be removed
                                       from the list of Qiskrypt's Registers of
                                       the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[0]) and \
                (isinstance(self.get_party(), QiskryptQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Quantum Party and belongs
            to a Quantum Context.
            """

            if quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is valid.
                """

                current_register = self.registers[quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if isinstance(current_register, QiskryptQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is a Qiskrypt's Quantum Register.
                    """

                    self.registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is not a Qiskrypt's Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Quantum Party or does not
            belongs to a Quantum Context.
            """

            # TODO Throw - Exception

    def add_ancilla_quantum_register(self, ancilla_quantum_register: QiskryptAncillaQuantumRegister):
        """
        Adds a given Qiskrypt's Ancilla Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's User Client.

        :param ancilla_quantum_register: the Qiskrypt's Ancilla Quantum Register to be added
                                         to the list of Qiskrypt's Registers of
                                         the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[0]) and \
                (isinstance(self.get_party(), QiskryptQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Quantum Party and belongs
            to a Quantum Context.
            """

            self.registers.append(ancilla_quantum_register)
            """
            Adds the given Qiskrypt's Ancilla Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's User Client.
            """

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Quantum Party or does not belongs
            to a Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_quantum_register_by_name(self, ancilla_quantum_register_name: str):
        """
        Removes a Qiskrypt's Ancilla Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its name.

        :param ancilla_quantum_register_name: the name of a Qiskrypt's Ancilla Quantum Register to be removed
                                              from the list of Qiskrypt's Registers of
                                              the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[0]) and \
                (isinstance(self.get_party(), QiskryptQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Quantum Party and belongs
            to a Quantum Context.
            """

            for current_register_index in range(len(self.registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's User Client. 
                """

                current_register = self.registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if current_register.get_name() == ancilla_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptAncillaQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is a Qiskrypt's Ancilla Quantum Register.
                        """

                        self.registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is not a Qiskrypt's Ancilla Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Quantum Party or does not
            belongs to a Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_quantum_register_by_index(self, ancilla_quantum_register_index: int):
        """
        Removes a Qiskrypt's Ancilla Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its index.

        :param ancilla_quantum_register_index: the index of a Qiskrypt's Ancilla Quantum Register to be removed
                                               from the list of Qiskrypt's Registers of
                                               the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[0]) and \
                (isinstance(self.get_party(), QiskryptQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Quantum Party and belongs
            to a Quantum Context.
            """

            if ancilla_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Ancilla Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is valid.
                """

                current_register = self.registers[ancilla_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if isinstance(current_register, QiskryptAncillaQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is a Qiskrypt's Ancilla Quantum Register.
                    """

                    self.registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is not a Qiskrypt's Ancilla Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Ancilla Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Quantum Party or does not
            belongs to a Quantum Context.
            """

            # TODO Throw - Exception

    def add_fully_quantum_register(self, fully_quantum_register: QiskryptFullyQuantumRegister):
        """
        Adds a given Qiskrypt's Fully-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's User Client.

        :param fully_quantum_register: the Qiskrypt's Fully-Quantum Register to be added
                                       to the list of Qiskrypt's Registers of
                                       the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[1]) and \
                (isinstance(self.get_party(), QiskryptFullyQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Fully-Quantum Party and belongs
            to a Fully-Quantum Context.
            """

            self.registers.append(fully_quantum_register)
            """
            Adds the given Qiskrypt's Fully-Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's User Client.
            """

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Fully-Quantum Party or does not belongs
            to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_fully_quantum_register_by_name(self, fully_quantum_register_name: str):
        """
        Removes a Qiskrypt's Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its name.

        :param fully_quantum_register_name: the name of a Qiskrypt's Fully-Quantum Register to be removed
                                            from the list of Qiskrypt's Registers of
                                            the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[1]) and \
                (isinstance(self.get_party(), QiskryptFullyQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Fully-Quantum Party and belongs
            to a Fully-Quantum Context.
            """

            for current_register_index in range(len(self.registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's User Client. 
                """

                current_register = self.registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if current_register.get_name() == fully_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptFullyQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is a Qiskrypt's Fully-Quantum Register.
                        """

                        self.registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is not a Qiskrypt's Fully-Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Fully-Quantum Party or does not
            belongs to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_fully_quantum_register_by_index(self, fully_quantum_register_index: int):
        """
        Removes a Qiskrypt's Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its index.

        :param fully_quantum_register_index: the index of a Qiskrypt's Fully-Quantum Register to be removed
                                             from the list of Qiskrypt's Registers of
                                             the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[1]) and \
                (isinstance(self.get_party(), QiskryptFullyQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Fully-Quantum Party and belongs
            to a Fully-Quantum Context.
            """

            if fully_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Fully-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is valid.
                """

                current_register = self.registers[fully_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if isinstance(current_register, QiskryptFullyQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is a Qiskrypt's Fully-Quantum Register.
                    """

                    self.registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is not a Qiskrypt's Fully-Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Fully-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Fully-Quantum Party or does not
            belongs to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def add_ancilla_fully_quantum_register(self, ancilla_fully_quantum_register: QiskryptAncillaFullyQuantumRegister):
        """
        Adds a given Qiskrypt's Ancilla Fully-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's User Client.

        :param ancilla_fully_quantum_register: the Qiskrypt's Ancilla Fully-Quantum Register to be added
                                               to the list of Qiskrypt's Registers of
                                               the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[1]) and \
                (isinstance(self.get_party(), QiskryptFullyQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Fully-Quantum Party and belongs
            to a Fully-Quantum Context.
            """

            self.registers.append(ancilla_fully_quantum_register)
            """
            Adds the given Qiskrypt's Ancilla Fully-Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's User Client.
            """

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Quantum Party or does not belongs
            to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_fully_quantum_register_by_name(self, ancilla_fully_quantum_register_name: str):
        """
        Removes a Qiskrypt's Ancilla Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its name.

        :param ancilla_fully_quantum_register_name: the name of a Qiskrypt's Ancilla Fully-Quantum Register
                                                    to be removed from the list of Qiskrypt's Registers of
                                                    the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[1]) and \
                (isinstance(self.get_party(), QiskryptFullyQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Fully-Quantum Party and belongs
            to a Fully-Quantum Context.
            """

            for current_register_index in range(len(self.registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's User Client. 
                """

                current_register = self.registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if current_register.get_name() == ancilla_fully_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptAncillaFullyQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is a Qiskrypt's Ancilla Fully-Quantum Register.
                        """

                        self.registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is not a Qiskrypt's Ancilla Fully-Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Fully-Quantum Party or does not
            belongs to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_fully_quantum_register_by_index(self, ancilla_fully_quantum_register_index: int):
        """
        Removes a Qiskrypt's Ancilla Fully-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its index.

        :param ancilla_fully_quantum_register_index: the index of a Qiskrypt's Ancilla Fully-Quantum Register
                                                     to be removed from the list of Qiskrypt's Registers of
                                                     the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[1]) and \
                (isinstance(self.get_party(), QiskryptFullyQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Fully-Quantum Party and belongs
            to a Fully-Quantum Context.
            """

            if ancilla_fully_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Ancilla Fully-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is valid.
                """

                current_register = self.registers[ancilla_fully_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if isinstance(current_register, QiskryptAncillaFullyQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is a Qiskrypt's Ancilla Fully-Quantum Register.
                    """

                    self.registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is not a Qiskrypt's Ancilla Fully-Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Ancilla Fully-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Fully-Quantum Party or does not
            belongs to a Fully-Quantum Context.
            """

            # TODO Throw - Exception

    def add_semi_quantum_register(self, semi_quantum_register: QiskryptSemiQuantumRegister):
        """
        Adds a given Qiskrypt's Semi-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's User Client.

        :param semi_quantum_register: the Qiskrypt's Semi-Quantum Register to be added
                                      to the list of Qiskrypt's Registers of
                                      the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[2]) and \
                (isinstance(self.get_party(), QiskryptSemiQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Semi-Quantum Party and belongs
            to a Semi-Quantum Context.
            """

            self.registers.append(semi_quantum_register)
            """
            Adds the given Qiskrypt's Semi-Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's User Client.
            """

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Semi-Quantum Party or does not belongs
            to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_semi_quantum_register_by_name(self, semi_quantum_register_name: str):
        """
        Removes a Qiskrypt's Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its name.

        :param semi_quantum_register_name: the name of a Qiskrypt's Semi-Quantum Register
                                           to be removed from the list of Qiskrypt's Registers of
                                           the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[2]) and \
                (isinstance(self.get_party(), QiskryptSemiQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Semi-Quantum Party and belongs
            to a Semi-Quantum Context.
            """

            for current_register_index in range(len(self.registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's User Client. 
                """

                current_register = self.registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if current_register.get_name() == semi_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptSemiQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is a Qiskrypt's Semi-Quantum Register.
                        """

                        self.registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is not a Qiskrypt's Semi-Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Semi-Quantum Party or does not
            belongs to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_semi_quantum_register_by_index(self, semi_quantum_register_index: int):
        """
        Removes a Qiskrypt's Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its index.

        :param semi_quantum_register_index: the index of a Qiskrypt's Semi-Quantum Register
                                            to be removed from the list of Qiskrypt's Registers of
                                            the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[2]) and \
                (isinstance(self.get_party(), QiskryptSemiQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Semi-Quantum Party and belongs
            to a Semi-Quantum Context.
            """

            if semi_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Semi-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is valid.
                """

                current_register = self.registers[semi_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if isinstance(current_register, QiskryptSemiQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is a Qiskrypt's Semi-Quantum Register.
                    """

                    self.registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is not a Qiskrypt's Semi-Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Semi-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Semi-Quantum Party or does not
            belongs to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def add_ancilla_semi_quantum_register(self, ancilla_semi_quantum_register: QiskryptAncillaSemiQuantumRegister):
        """
        Adds a given Qiskrypt's Ancilla Semi-Quantum Register to
        the list of Qiskrypt's Registers of the Qiskrypt's User Client.

        :param ancilla_semi_quantum_register: the Qiskrypt's Ancilla Semi-Quantum Register to be added
                                              to the list of Qiskrypt's Registers of
                                              the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[2]) and \
                (isinstance(self.get_party(), QiskryptSemiQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Semi-Quantum Party and belongs
            to a Semi-Quantum Context.
            """

            self.registers.append(ancilla_semi_quantum_register)
            """
            Adds the given Qiskrypt's Ancilla Semi-Quantum Register to
            the list of Qiskrypt's Registers of the Qiskrypt's User Client.
            """

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Semi-Quantum Party or does not belongs
            to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_semi_quantum_register_by_name(self, ancilla_semi_quantum_register_name: str):
        """
        Removes a Qiskrypt's Ancilla Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its name.

        :param ancilla_semi_quantum_register_name: the name of a Qiskrypt's Ancilla Semi-Quantum Register
                                                   to be removed from the list of Qiskrypt's Registers of
                                                   the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[2]) and \
                (isinstance(self.get_party(), QiskryptSemiQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Semi-Quantum Party and belongs
            to a Semi-Quantum Context.
            """

            for current_register_index in range(len(self.registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's User Client. 
                """

                current_register = self.registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if current_register.get_name() == ancilla_semi_quantum_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptAncillaSemiQuantumRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is a Qiskrypt's Ancilla Semi-Quantum Register.
                        """

                        self.registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is not a Qiskrypt's Ancilla Semi-Quantum Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Semi-Quantum Party or does not
            belongs to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def remove_ancilla_semi_quantum_register_by_index(self, ancilla_semi_quantum_register_index: int):
        """
        Removes a Qiskrypt's Ancilla Semi-Quantum Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its index.

        :param ancilla_semi_quantum_register_index: the index of a Qiskrypt's Ancilla Semi-Quantum Register
                                                    to be removed from the list of Qiskrypt's Registers of
                                                    the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[2]) and \
                (isinstance(self.get_party(), QiskryptSemiQuantumParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Semi-Quantum Party and belongs
            to a Semi-Quantum Context.
            """

            if ancilla_semi_quantum_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Ancilla Semi-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is valid.
                """

                current_register = self.registers[ancilla_semi_quantum_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if isinstance(current_register, QiskryptAncillaSemiQuantumRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is a Qiskrypt's Ancilla Semi-Quantum Register.
                    """

                    self.registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is not a Qiskrypt's Ancilla Semi-Quantum Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Ancilla Semi-Quantum Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Semi-Quantum Party or does not
            belongs to a Semi-Quantum Context.
            """

            # TODO Throw - Exception

    def add_classical_register(self, classical_register: QiskryptClassicalRegister):
        """
        Adds a given Qiskrypt's Classical Register to
        the list of Qiskrypt's Registers of the Qiskrypt's User Client.

        :param classical_register: the Qiskrypt's Classical Register to be added
                                   to the list of Qiskrypt's Registers of
                                   the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[3]) and \
                (isinstance(self.get_party(), QiskryptClassicalParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Classical Party and belongs
            to a Classical Context.
            """

            self.registers.append(classical_register)
            """
            Adds the given Qiskrypt's Classical Register to
            the list of Qiskrypt's Registers of the Qiskrypt's User Client.
            """

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Classical Party or does not belongs
            to a Classical Context.
            """

            # TODO Throw - Exception

    def remove_classical_register_by_name(self, classical_register_name: str):
        """
        Removes a Qiskrypt's Classical Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its name.

        :param classical_register_name: the name of a Qiskrypt's Classical Register
                                        to be removed from the list of Qiskrypt's Registers of
                                        the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[3]) and \
                (isinstance(self.get_party(), QiskryptClassicalParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Classical Party and belongs
            to a Classical Context.
            """

            for current_register_index in range(len(self.registers)):
                """
                For each Qiskrypt's Register in the list of
                Qiskrypt's Registers of the Qiskrypt's User Client. 
                """

                current_register = self.registers[current_register_index]
                """
                Retrieve the current Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if current_register.get_name() == classical_register_name:
                    """
                    If it was found a Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client,
                    with the given name.
                    """

                    if isinstance(current_register, QiskryptClassicalRegister):
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is a Qiskrypt's Classical Register.
                        """

                        self.registers.remove(current_register)
                        """
                        Removes the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                        """

                    else:
                        """
                        If the current Qiskrypt's Register in
                        the list of Qiskrypt's Registers of the Qiskrypt's User Client
                        is not a Qiskrypt's Classical Register.
                        """

                        # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Classical Party or does not
            belongs to a Classical Context.
            """

            # TODO Throw - Exception

    def remove_classical_register_by_index(self, classical_register_index: int):
        """
        Removes a Qiskrypt's Classical Register from
        the list of Qiskrypt's Registers of the Qiskrypt's User Client,
        given its index.

        :param classical_register_index: the index of a Qiskrypt's Ancilla Semi-Quantum Register
                                         to be removed from the list of Qiskrypt's Registers of
                                         the Qiskrypt's User Client.
        """

        if (self.party.get_context() == POSSIBLE_PARTY_CONTEXTS[3]) and \
                (isinstance(self.get_party(), QiskryptClassicalParty)):
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is a Qiskrypt's Classical Party and belongs
            to a Classical Context.
            """

            if classical_register_index < self.get_num_registers():
                """
                If the given index of a Qiskrypt's Classical Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is valid.
                """

                current_register = self.registers[classical_register_index]
                """
                Retrieve the respective Qiskrypt's Register in
                the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                """

                if isinstance(current_register, QiskryptClassicalRegister):
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is a Qiskrypt's Classical Register.
                    """

                    self.registers.remove(current_register)
                    """
                    Removes the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client.
                    """

                else:
                    """
                    If the current Qiskrypt's Register in
                    the list of Qiskrypt's Registers of the Qiskrypt's User Client
                    is not a Qiskrypt's Classical Register.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the given index of a Qiskrypt's Classical Register to be removed
                from the list of Qiskrypt's Registers of the Qiskrypt's User Client is not valid.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Party of the Qiskrypt's User Client
            is not a Qiskrypt's Classical Party or does not
            belongs to a Classical Context.
            """

            # TODO Throw - Exception
