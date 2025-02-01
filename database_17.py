from abc import ABC, abstractmethod


class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self,data):
        pass

    @abstractmethod
    def update(self,id,data):
        pass

    @abstractmethod
    def delete(self,id):
        pass


class SQLDatabase(IDatabaseOperations):
    def insert(self,data):
        print(f"Insert data into SQL database: {data}\n")

    def update(self,id,data):
        print(f"Update data with ID {id} in SQL database with data: {data}\n")

    def delete(self,id):
        print(f"Delete record with ID {id} from SQL database\n")


class NoSQLDatabase(IDatabaseOperations):
    def insert(self,data):
        print(f"Insert data into NoSQL database: {data}\n")

    def update(self,id,data):
        print(f"Update data with ID {id} in NoSQL database with data: {data}\n")

    def delete(self, id):
        print(f"Delete data with ID {id} from NoSQL database\n")


sql_db=SQLDatabase()
sql_db.insert({"name":"sri","age":30})
sql_db.update(1,{"name":"srij","age":30})
sql_db.delete(4)

nosql_db = NoSQLDatabase()
nosql_db.insert({"name":"pri","age":25})
nosql_db.update(2,{"name":"pri4","age":25})
nosql_db.delete(6)
