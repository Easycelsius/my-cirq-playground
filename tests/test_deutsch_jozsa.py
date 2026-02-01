import pytest
from quantum_algos.deutsch_jozsa import DeutschJozsa
from quantum_algos.errors import OracleValueError, QubitCountError

def test_constant_oracle_zero():
    """Test DJ with constant oracle f(x) = 0."""
    n = 3
    oracle = DeutschJozsa.create_constant_oracle(0)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Constant"

def test_constant_oracle_one():
    """Test DJ with constant oracle f(x) = 1."""
    n = 3
    oracle = DeutschJozsa.create_constant_oracle(1)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Constant"

def test_balanced_oracle():
    """Test DJ with balanced oracle."""
    n = 3
    oracle = DeutschJozsa.create_balanced_oracle()
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_balanced_oracle_2_qubits():
    """Test DJ with balanced oracle with different qubit count."""
    n = 2
    oracle = DeutschJozsa.create_balanced_oracle()
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_balanced_1():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [1, 1, 0, 0]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_balanced_2():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [0, 1, 1, 0]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_balanced_3():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [0, 0, 1, 1]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_balanced_4():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [1, 0, 0, 1]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_unbalanced_1():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [1, 1, 1, 0]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_unbalanced_2():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [1, 1, 0, 1]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_unbalanced_3():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [1, 0, 1, 1]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_unbalanced_4():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [0, 1, 1, 1]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_unbalanced_5():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [0, 0, 0, 1]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_unbalanced_6():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [0, 0, 1, 0]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_unbalanced_7():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [0, 1, 0, 0]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_unbalanced_8():
    """Test DJ with custom balanced oracle."""
    n = 4
    seq = [1, 0, 0, 0]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Balanced"

def test_custom_oracle_constant_zeros():
    """Test DJ with custom constant oracle (all zeros)."""
    n = 4
    seq = [0, 0, 0, 0]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Constant"

def test_custom_oracle_all_ones():
    """Test DJ with custom oracle (all ones)."""
    n = 2
    seq = [1, 1]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Constant"

def test_error_qubit_count_mismatch():
    """Test that QubitCountError is raised when lengths mismatch."""
    n = 3
    seq = [1, 0] # Length 2
    with pytest.raises(QubitCountError):
        DeutschJozsa.create_my_oracle(n, seq)

def test_custom_oracle_constant_one():
    """Test DJ with custom constant oracle (constant_one=True)."""
    n = 3
    seq = [1, 1, 1]
    oracle = DeutschJozsa.create_my_oracle(n, seq)
    dj = DeutschJozsa(n, oracle)
    result = dj.run()
    assert result == "Constant"