import allure, pytest

class Test_001_01:

    @pytest.allure.severtity(pytest.allure.servrity_level.BLOCKER)
    @allure.step(title="第一个测试")
    def test_001(self):
        allure.attach('这是一个描述内容')
        assert 0

