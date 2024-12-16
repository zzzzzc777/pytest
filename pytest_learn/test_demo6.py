import pytest

def add_function(a, b):
    return a + b

# 修正了参数化测试中的参数列表格式和负数的表示方法
@pytest.mark.parametrize("a, b, expected",
                         [(3, 5, 8),
                          (-1, -2, -3),  # 修正了负数的表示方法
                          (100, 200, 300)],
                         ids=["int_sum", "minus_sum", "bigint_sum"])  # 修正了ids中的字符串，使其更具描述性
def test_add(a, b, expected):
    assert add_function(a, b) == expected