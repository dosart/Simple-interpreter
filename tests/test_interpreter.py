# # -*- coding:utf-8 -*-

# """Interpreter representation tests."""

# import pytest

# from interpreter.intereter import interpret
# from interpreter.visitor import _GLOBAL_SCOPE


# @pytest.mark.parametrize(
#     "test_input",
#     ["BEGIN x := 10+11 END.", " BEGIN x:=10 + 11 END. ", " BEGIN x:=10 + 11   END."],
# )
# def test_apply_plus_or_minus1(test_input):
#     """Check a simple expression.

#     Args:
#         test_input: data for test
#     """

#     interpret(test_input)
#     assert _GLOBAL_SCOPE["x"] == 21


# # @pytest.mark.parametrize(
# #     "test_input",
# #     ["10+11+11", "10 + 11 + 11 ", " 10 + 11   + 11"],
# # )
# # def test_apply_plus_or_minus2(test_input):
# #     """Check a simple expression.

# #     Args:
# #         test_input: data for test
# #     """
# #     assert interpret(test_input) == 32


# # @pytest.mark.parametrize(
# #     "test_input",
# #     ["10", "10 ", " 10 "],
# # )
# # def test_apply_plus_or_minus3(test_input):
# #     """Check a simple expression.

# #     Args:
# #         test_input: data for test
# #     """
# #     assert interpret(test_input) == 10


# # @pytest.mark.parametrize(
# #     "test_input",
# #     ["10-5", "10 - 5 ", " 10 - 5   "],
# # )
# # def test_apply_plus_or_minus4(test_input):
# #     """Check a simple expression.

# #     Args:
# #         test_input: data for test
# #     """
# #     assert interpret(test_input) == 5


# # @pytest.mark.parametrize(
# #     "test_input",
# #     ["10-5-2", "10 - 5 -2 ", " 10 - 5 - 2  "],
# # )
# # def test_apply_plus_or_minus5(test_input):
# #     """Check a simple expression.

# #     Args:
# #         test_input: data for test
# #     """
# #     assert interpret(test_input) == 3


# # @pytest.mark.parametrize(
# #     "test_input",
# #     ["10-5+2", "10 - 5 +2 ", " 10 - 5 + 2  "],
# # )
# # def test_apply_plus_or_minus6(test_input):
# #     """Check a simple expression.

# #     Args:
# #         test_input: data for test
# #     """
# #     assert interpret(test_input) == 7


# # @pytest.mark.parametrize(
# #     "test_input",
# #     ["10-2-5+2", "10 -2 - 5 +2 ", " 10-2 - 5 + 2  "],
# # )
# # def test_apply_plus_or_minus7(test_input):
# #     """Check a simple expression.

# #     Args:
# #         test_input: data for test
# #     """
# #     assert interpret(test_input) == 5
