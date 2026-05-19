# Python pytest Assignment Test Report

This repository contains the completed tasks for four assignments testing various systems (`Calculator`, `GradeBook`, `ShoppingCart`, and `UserAuth`).

## Summary of All Tests Run

All 47 tests passed successfully (including 1 skipped test and 1 expected pass/xpassed lockout test):

```
================== 45 passed, 1 skipped, 1 xpassed in 0.28s ===================
```

### Detailed Test Session Output

```
============================= test session starts =============================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\hi\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: F:\PYTEST
plugins: cov-7.1.0
collecting ... collected 47 items

test_auth.py::TestUserAuth::test_auth_weak_passwords[short1] PASSED      [  2%]
test_auth.py::TestUserAuth::test_auth_weak_passwords[noumbershere] PASSED [  4%]
test_auth.py::TestUserAuth::test_auth_weak_passwords[12345] PASSED       [  6%]
test_auth.py::TestUserAuth::test_auth_weak_passwords[] PASSED            [  8%]
test_auth.py::TestUserAuth::test_auth_successful_registration_and_login PASSED [ 10%]
test_auth.py::TestUserAuth::test_auth_lockout_policy XPASS (Lockout ...) [ 12%]
test_auth.py::TestUserAuth::test_auth_reset_attempts PASSED              [ 14%]
test_calculator.py::test_add[10-5-15] PASSED                             [ 17%]
test_calculator.py::test_add[-2-8-6] PASSED                              [ 19%]
test_calculator.py::test_add[0-0-0] PASSED                               [ 21%]
test_calculator.py::test_subtract[10-5-5] PASSED                         [ 23%]
test_calculator.py::test_subtract[-2-8--10] PASSED                       [ 25%]
test_calculator.py::test_subtract[0-0-0] PASSED                          [ 27%]
test_calculator.py::test_multiply[10-5-50] PASSED                        [ 29%]
test_calculator.py::test_multiply[-2-8--16] PASSED                       [ 31%]
test_calculator.py::test_multiply[0-100-0] PASSED                        [ 34%]
test_calculator.py::test_divide[10-5-2.0] PASSED                         [ 36%]
test_calculator.py::test_divide[5-2-2.5] PASSED                          [ 38%]
test_calculator.py::test_divide[1-3-expected2] PASSED                    [ 40%]
test_calculator.py::test_divide_by_zero PASSED                           [ 42%]
test_cart.py::test_add_item PASSED                                       [ 44%]
test_cart.py::test_remove_item PASSED                                    [ 46%]
test_cart.py::test_module_cart_total PASSED                              [ 48%]
test_cart.py::test_apply_discount[0-100.0] PASSED                        [ 51%]
test_cart.py::test_apply_discount[10-90.0] PASSED                        [ 53%]
test_cart.py::test_apply_discount[25-75.0] PASSED                        [ 55%]
test_cart.py::test_apply_discount[50-50.0] PASSED                        [ 57%]
test_cart.py::test_apply_discount[100-0.0] PASSED                        [ 59%]
test_cart.py::test_apply_discount[33.33-66.67] PASSED                    [ 61%]
test_cart.py::test_apply_discount_invalid PASSED                         [ 63%]
test_cart.py::test_slow_operation PASSED                                 [ 65%]
test_cart.py::test_apply_coupon SKIPPED (not implemented)                [ 68%]
test_gradebook.py::TestGradeBook::test_average PASSED                    [ 70%]
test_gradebook.py::TestGradeBook::test_highest PASSED                    [ 72%]
test_gradebook.py::TestGradeBook::test_lowest PASSED                     [ 74%]
test_gradebook.py::TestGradeBook::test_letter_grade[100-A] PASSED        [ 76%]
test_gradebook.py::TestGradeBook::test_letter_grade[90-A] PASSED         [ 78%]
test_gradebook.py::TestGradeBook::test_letter_grade[89.9-B] PASSED       [ 80%]
test_gradebook.py::TestGradeBook::test_letter_grade[80-B] PASSED         [ 82%]
test_gradebook.py::TestGradeBook::test_letter_grade[79.9-C] PASSED       [ 85%]
test_gradebook.py::TestGradeBook::test_letter_grade[70-C] PASSED         [ 87%]
test_gradebook.py::TestGradeBook::test_letter_grade[69.9-D] PASSED       [ 89%]
test_gradebook.py::TestGradeBook::test_letter_grade[60-D] PASSED         [ 91%]
test_gradebook.py::TestGradeBook::test_letter_grade[59.9-F] PASSED       [ 93%]
test_gradebook.py::TestGradeBook::test_letter_grade[0-F] PASSED          [ 95%]
test_gradebook.py::TestGradeBook::test_add_score_out_of_range PASSED     [ 97%]
test_gradebook.py::TestGradeBook::test_letter_grade_out_of_range PASSED  [100%]
```

## Assignment Summaries

### Assignment 1: Calculator
- **Source**: `calculator.py`
- **Tests**: `test_calculator.py`
- **Features Tested**: Addition, subtraction, multiplication, division (raises `ZeroDivisionError` on division by zero). Included multiple input pairs with `@pytest.mark.parametrize` and float-approximations with `pytest.approx`.

### Assignment 2: Student GradeBook
- **Source**: `gradebook.py`
- **Tests**: `test_gradebook.py`
- **Features Tested**: Score tracking (0-100), average, highest, lowest score, and grade mapping boundary checks (A/B/C/D/F). Integrates a shared fixture in `conftest.py` across tests.

### Assignment 3: Shopping Cart System
- **Source**: `cart.py`
- **Tests**: `test_cart.py`
- **Features Tested**: Adding/removing items, total computation, discount application, and a skipped coupon feature. Utilizes module and function fixtures, a custom registered `slow` mark, and 95% test coverage enforcement.

### Assignment 4: User Authentication System
- **Source**: `auth.py`
- **Tests**: `test_auth.py`
- **Features Tested**: Registration, password complexity validation, login state with a 3-attempt lockout policy (4th fails), and attempts resetting. Utilizes class setup/teardown methods.
