from luigi.mock import MockTarget

from to_upper import ToUpper

mock_input = MockTarget("in")
mock_output = MockTarget("out")


class IsolatedToUpper(ToUpper):
    def input(self):
        return mock_input

    def output(self):
        return mock_output


def test_to_upper():
    with mock_input.open("w") as i:
        i.write("this is a test\n")
        i.write("see you soon\n")

    task = IsolatedToUpper()
    task.run()

    with mock_output.open("r") as o:
        result = o.readlines()
        assert result == ["THIS IS A TEST\n", "SEE YOU SOON\n"]
