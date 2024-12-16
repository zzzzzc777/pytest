import pytest

class TestDemo:
    @pytest.mark.demo
    def test_demo(self):
        a = 5
        b = -1
        assert a != b
        print("我的第一个测试用例")

    @pytest.mark.smoke
    def test_two(self):
        a = 2
        # 假设您想设置 b 为 -1 的相反数，即 1
        # 如果不是，请替换为正确的值
        b = -(-1)  # 或者简单地 b = 1
        assert a != b
        print("我的第二个测试用例")