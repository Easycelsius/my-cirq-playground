class QuantumAlgoError(Exception):
    """Base class for exceptions in this module."""
    pass

class OracleError(QuantumAlgoError):
    """Exception raised for errors in the oracle."""
    pass

class OracleValueError(OracleError):
    """Exception raised when oracle values are invalid (e.g., not balanced/constant)."""
    pass

class QubitCountError(QuantumAlgoError):
    """Exception raised when there is a mismatch in qubit counts."""
    pass

class CircuitError(QuantumAlgoError):
    """Exception raised for errors during circuit construction."""
    pass
