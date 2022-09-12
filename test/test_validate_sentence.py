import pytest
from src.validate_sentence import is_sentence_valid, get_csv_data


# This method is to initiate the testing for all the contents present in the file
@pytest.mark.parametrize("tc", get_csv_data(r"C:\Users\jaswa\PycharmProjects\test\input\input_string.csv"))
def test_validate_sentences(tc):
    sentence, is_valid = tc
    result, message = is_sentence_valid(sentence)
    assert str(result).upper() == is_valid, message
