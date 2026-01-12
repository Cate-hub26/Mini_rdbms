class Table:
    def __init__(self, name, schema, primary_key=None):
        """
        name: table name (string)
        schema: dict of column_name -> type (e.g., {"id": int, "name": str})
        primary_key: column name to enforce uniqueness
        """
        self.name = name
        self.schema = schema
        self.primary_key = primary_key
        self.rows = []

    def insert(self, row):
        # Validate schema
        for col, col_type in self.schema.items():
            if col not in row:
                raise ValueError(f"Missing column : {col}")
            if not isinstance(row[col], col_type):
                raise TypeError(f"Column {col} must be {col_type.__name__}")
            
        # Enforce primary key uniqueness
        
        if self.primary_key:
            for r in self.rows:
                if r[self.primary_key] == row[self.primary_key]:
                    raise ValueError("Duplicate Primary key")
        self.rows.append(row)
            
