from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, file_dt: str=None, **kwargs):
        self.spark = None
        self.update(file_dt)

    def update(self, file_dt: str="2025-01-09", **kwargs):
        prophecy_spark = self.spark
        self.file_dt = file_dt
        pass
