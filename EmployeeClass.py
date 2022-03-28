class EmployeeClass:
    def __init__(self, EmployeeId , EmployeeLocation , EmployeeName , EmployeeSalary):  
        self.EmployeeId = EmployeeId    
        self.EmployeeLocation = EmployeeLocation
        self.EmployeeName = EmployeeName
        self.EmployeeSalary = EmployeeSalary

    def GetEmployee(self):
         
        print("      " + str(self.EmployeeId)+ "       " + str(self.EmployeeLocation) + "                   "+(self.EmployeeName)+ "                 " + str(self.EmployeeSalary))
        

