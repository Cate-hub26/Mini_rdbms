from .table import Table

class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, schema, primary_key=None):
        if name in self.tables:
            raise ValueError(f"Table {name} exists")
        self.tables[name] = Table(self, name, schema, primary_key)


    def get_table(self, name):
        if name not in self.tables:
            raise ValueError(f"Table {name} does not exist")
        return self.tables[name]

