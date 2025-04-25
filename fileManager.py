import os 
import json

class DBTasks:

    def __init__(self):
        try:
            self.data = self.__parse_data()
        except Exception as e:
            self.data = {"tasks":[]}


    def get_data(self):
        try:
            self.data = self.__parse_data()
        except Exception as e:
            self.data = {"tasks":[]}
        return self.data


    def __parse_data(self):
        str_data:str = self.read()
        data = json.loads(str_data)
        return data


    def __openFile(self, permission:str):
        self.file = open("tasks.json",permission)


    def append(self, task:dict):
        print("tasks received:", task)
        self.data["tasks"].append(task)
        self.__openFile("w")
        self.file.write(json.dumps(self.data))
        self.__close()
        return True
    
    
    def update(self, n,task):
        self.data = self.__parse_data()
        self.data["tasks"][n] = task
        print("new status for the task", task)
        self.__openFile("w")
        self.file.write(json.dumps(self.data))
        self.__close()
        return True
    
    def delete(self,n):
        self.data["tasks"].pop(n)
        self.__openFile("w")
        self.file.write(json.dumps(self.data))
        self.__close()
        return True


    def read(self):
        self.__openFile("r")
        data = self.file.read()
        self.__close()
        return data


    def __close(self):
        self.file.close()
