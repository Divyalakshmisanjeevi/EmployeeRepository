from EmployeeClass import *

Ram = EmployeeClass(1001,"Delhi","Ram",15000)
Joshi = EmployeeClass(1002,"Banglore","Joshi",20000)
Peter = EmployeeClass(1003,"Lucknow","Peter",25000)
Ashna = EmployeeClass(1004,"chennai","Ashna",20000)
Ragahv = EmployeeClass(1005,"kolkatha","Ragahv",25000)

print("------------------------------------------------------------------------")
print("Employee id"+"\t"+"Employee location" +"\t" + "Employee name"+"\t"+"Employee salary")
print("------------------------------------------------------------------------")

Ram.GetEmployee()
Joshi.GetEmployee()
Peter.GetEmployee()
Ashna.GetEmployee()
Ragahv.GetEmployee()

