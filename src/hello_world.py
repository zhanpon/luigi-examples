import luigi
from luigi import LocalTarget


class HelloWorld(luigi.Task):
    def requires(self):
        pass

    def output(self):
        return LocalTarget("data/hello_world.txt")

    def run(self):
        with self.output().open("w") as o:
            o.write("Hello, World\n")
            o.write("Salut !\n")
