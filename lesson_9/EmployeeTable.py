from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanyTable:
    __scripts = {
        "insert new": text("insert into company(\"name\", description) values (:new_name, :new_description)"),
        "get max id": "select MAX(\"id\") from company where deleted_at is null",
        "delete by id": text("delete from employee where id =:id_to_delete")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def create_company(self, name, description):
        self.__db.execute(self.__scripts["insert new"], new_name = name, new_description = description)

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]

    def delete_company(self, id):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)



class EmployeeTable:
    __scripts = {
        "delete by id": text("delete from employee where id =:id_to_delete")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_employees(self, id):
        sql = text("select * from employee where company_id = :company_id")
        rows = self.db.execute(sql, company_id = id).fetchall()
        return rows
    
    def delete_employee(self, id):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)

    