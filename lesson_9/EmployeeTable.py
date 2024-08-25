from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanyTable:
    __scripts = {
        "insert new": text("insert into company(\"name\", description) values (:new_name, :new_description)"),
        "get max id": "select MAX(\"id\") from company where deleted_at is null",
        "delete by id": text("delete from employee where id =:id_to_delete")
    }

    def __init__(self, connection_string: str):
        """
        Функция-конструктор, создает экземпляр класса
        """
        self.db = create_engine(connection_string)
        

    def create_company(self, name: str, description: str):
        """
        Функция добавляет новую компанию в базу данных с помощью sql-запроса, в параметрах указываются 
        название и описание создаваемой компании
        """
        self.db.execute(self.__scripts["insert new"], new_name = name, new_description = description)

    def get_max_id(self) -> int:
        """
        Функция запрашивает максимальный существующий id в списке компаний
        (по логике это будет id последней добавленной в базу данных компании)
        """
        return self.db.execute(self.__scripts["get max id"]).fetchall()[0][0]

    def delete_company(self, id: int):
        """
        Функция удаляет компанию по id (указывается как параметр)
        """        
        self.db.execute(self.__scripts["delete by id"], id_to_delete = id)



class EmployeeTable:
    __scripts = {
        "delete by id": text("delete from employee where id =:id_to_delete")
    }

    def __init__(self, connection_string: str):
        """
        Функция-конструктор, создает экземпляр класса 
        """        
        self.db = create_engine(connection_string)

    def get_employees(self, id: int) -> list:
        """
        Функция запрашивает список сотрудников определенной компании
        (её id указывается в параметре)
        """  
        sql = text("select * from employee where company_id = :company_id")
        rows = self.db.execute(sql, company_id = id).fetchall()
        return rows
    
    def delete_employee(self, id: int):
        """
        Функция удаляет сотрудника по id (указывается как параметр)
        """          
        self.db.execute(self.__scripts["delete by id"], id_to_delete = id)

    