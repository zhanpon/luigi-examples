from luigi.mock import MockTarget

from hello_world import HelloWorld

mock_target = MockTarget("test")


class IsolatedHelloWorld(HelloWorld):
    def output(self):
        return mock_target


def test_output():
    task = IsolatedHelloWorld()
    task.run()
    with mock_target.open("r") as i:
        result = i.readlines()
        assert result == ["Hello, World\n", "Salut !\n"]


def test_addition():
    n = 1 + 1
    assert n == 1