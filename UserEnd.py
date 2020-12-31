#-------------------------------------------------------------------------------
# Name:        UserEnd
# Purpose:     User can provide the records to be created,deleted, or read from file
#
# Author:      Karthikeyan
#
# Created:     30-12-2020
# Copyright:   (c) Karthikeyan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import FileStorage

if(__name__=='__main__'):
    print('welcome')
    file_object = open('C:/PythonProject/EmployeeDetails.txt','a')
    file_path ='C:/PythonProject/EmployeeDetails.txt'
    d=dict(line.strip().split('=',1) for line in open("C:/PythonProject/EmployeeDetails.txt"))

    #1:
    #Below is the call for create defintion to create a records at file

    #Sample:
    #FileStorage.create(key,value,dictionary,file_object,timeout)

    Createcall=FileStorage.create('ttttt','{ "nickname":"ilaks", "age":28, "car":innova }',d,file_object,120)
    print('Create Call response: '+ str(Createcall))



    #2:
    #Below is the call for read defintion to read a records at file

    #Sample:
    #FileStorage.read(key,dictionary)

    Readcall=FileStorage.read('eee',d)
    print('Read Call response: '+ str(Readcall))

    #3:

    #Below is the call for read defintion to read a records at file

    #Sample:
    #FileStorage.delete(key,dictionary,file_path)

    Deletecall=FileStorage.delete('eee',d,file_path)
    print('Delete Call response: '+ str(Deletecall))



    file_object.close()