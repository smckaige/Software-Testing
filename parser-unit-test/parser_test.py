import unittest
from parser import parse

class Parser_TestCase(unittest.TestCase):
    def test_000_parser_function_exists(self):
        parse("3")

    def test_001_parser_returns_None_for_nonsense(self):
        assert parse("slfdkjs;lged") == None
        assert parse("") == None
        assert parse(None) == None
        assert parse(23425) == None

    def test_002_parser_can_parse_one_digit_numbers(self):
        assert parse("0") == 0
        assert parse("1") == 1
        assert parse("9") == 9
        assert parse("x") == None
        assert parse(".") == None

    def test_003_parser_can_parse_multiple_digit_numbers(self):
        assert parse("00") == 0
        assert parse("01") == 1
        assert parse("10") == 10
        assert parse("9999") == 9999
        assert parse("123456789") == 123456789

    def test_004_parser_can_parse_negative_multiple_digit_numbers(self):
        assert parse("-00") == -0
        assert parse("-01") == -1
        assert parse("-10") == -10
        assert parse("-9999") == -9999
        assert parse("-123456789") == -123456789
        assert parse("--9999") == 9999

    def test_005_parser_can_parse_decimal_numbers(self):
        assert parse("0.0") == 0.0
        assert parse("0.1") == 0.1
        assert parse("1.0") == 1.0
        assert parse("9.999") == 9.999
        assert parse("123.4567") == 123.4567
        assert parse(".999") == .999
        assert parse("999.") == 999.0

    def test_006_parser_can_parse_negative_decimal_numbers(self):
        assert parse("-0.0") == -0.0
        assert parse("-0.1") == -0.1
        assert parse("-1.0") == -1.0
        assert parse("-9.999") == -9.999
        assert parse("-123.4567") == -123.4567
        assert parse("-.999") == -.999
        assert parse("-999.") == -999.0
        assert parse("--999.") == 999.0

    def test_007_parser_can_add_numbers(self):
        assert parse("1+2+3+4") == 10
        assert parse("1+2+3+NOTHING") == None

    def test_008_parser_can_parse_single_positive_sccientfic_noteation(self):
        assert parse("0e0") == 0
        assert parse("0E0") == 0
        assert parse("5e10") == 5e10
        assert parse("3.5E15") == 3.5E15
        assert parse("e") == None
        assert parse("E") == None

    def test_009_parser_can_parse_single_negative_sccientfic_noteation(self):
        assert parse("0e-0") == 0
        assert parse("0E-0") == 0
        assert parse("5e-10") == 5e-10
        assert parse("3.5E-15") == 3.5E-15

    def test_010_parser_can_add_scientfic_noteation(self):
        assert parse("1e5+3.6E4") == 136000.0
        assert parse("1.34e-5+19E-6") == 3.24e-05
        assert parse("3.14e1+31.4e-1") == 34.54

		
if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
