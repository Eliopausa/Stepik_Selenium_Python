def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

    # Решение ниже работает только с числами, оно было расценено как не верное, хотя тут дело в
    # двусмысленности задания + примеры решения
    # assert int(expected_result) - int(actual_result) == 0, f"expected {expected_result}, got {actual_result}"


# Ниже входные данные для теста
# expected_result = 9
# actual_result = 8
# test_input_text(expected_result, actual_result)
