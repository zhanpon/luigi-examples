import luigi
from luigi import LocalTarget

from hello_world import HelloWorld


class ToUpper(luigi.Task):
    def requires(self):
        return HelloWorld()

    def output(self):
        return LocalTarget("data/to_upper.txt")

    def run(self):
        with self.input().open("r") as i, self.output().open("w") as o:
            for line in i:
                o.write(line.upper())
