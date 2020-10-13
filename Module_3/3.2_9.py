def test_substring(full_string, substring):
    assert str(substring) in str(full_string), f"expected '{substring}', to be substring of '{full_string}'"

# тестовык данные для отладки
# full_string = "fulltext"
# substring = "some_value"
# test_substring(full_string, substring)
