from app.operations import add, subtract

def test_add_positive_numbers():
    # Arrange: inputs and an independently known answer.
    first, second = 2, 3
    expected = 5
    # Act: exercise the function.
    result = add(first, second)
    # Assert: verify the result.
    assert result == expected

def test_add_zero():
    # Arrange: inputs and an independently known answer.
    first, second = 5, 0
    expected = 5
    # Act: exercise the function.
    result = add(first, second)
    # Assert: verify the result.
    assert result == expected

def test_add_negative_numbers():
    # Arrange: inputs and an independently known answer.
    first, second = -2, -3
    expected = -5
    # Act: exercise the function.
    result = add(first, second)
    # Assert: verify the result.
    assert result == expected

def test_subtract_positive_numbers():
    # Arrange: inputs and an independently known answer.
    first, second = 5, 3
    expected = 2
    # Act: exercise the function.
    result = subtract(first, second)
    # Assert: verify the result.
    assert result == expected

def test_subtract_negative_numbers():
    # Arrange: inputs and an independently known answer.
    first, second = -5, -3
    expected = -2
    # Act: exercise the function.
    result = subtract(first, second)
    # Assert: verify the result.
    assert result == expected

def test_subtract_zero():
    # Arrange: inputs and an independently known answer.
    first, second = 5, 0
    expected = 5
    # Act: exercise the function.
    result = subtract(first, second)
    # Assert: verify the result.
    assert result == expected