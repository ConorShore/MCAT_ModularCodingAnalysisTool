from prettytable import PrettyTable
from dataclasses import dataclass

# This is a simple data container with whatever data of interest you want, and where it is

class GenericInterestObject():
    def __init__(self,data = "",linenumber = 0):
        self.__data = data
        self.__lineNumber = linenumber

    def set(self, Datain: str, LineNumberin: int):
        self.__data = Datain
        self.__lineNumber = LineNumberin

    def getData(self) -> list:
        return self.__data

    def getLineNumber(self) -> int:
        return self.__lineNumber

    def __repr__(self) -> str:
        table = PrettyTable()
        table.field_names = ["Data", "Line Number"]
        table.add_row([self.__data, self.__lineNumber])
        return table

    def __str__(self) -> str:
        return str(self.__data) + "," + str(self.__lineNumber) + "\n"

# A Generic Interest List is a list of GenericInterestObjects with a datatype header

class GenericInterestList():

    def __init__(self, dataType="Generic", list = []):
        self.__dataType = dataType
        self.__list = list

    def __repr__(self) -> str:
        table = PrettyTable()
        table.field_names = [self.__dataType, "Line Number"]

        for entries in self.__list:
            table.add_row([str(entries[0]), str(entries[1])])


        return str(self.__dataType) + " Table\n" + str(table) + "\n"

    def __str__(self) -> str:
        returnstr = ""
        returnstr += self.__dataType + "\n"
        for entries in self.__list:
            returnstr += entries[0] + "," + str(entries[1].line) + "\n"

        return returnstr

    def append(self, objectToAdd: GenericInterestObject):
        self.__list.append([objectToAdd.getData(), objectToAdd.getLineNumber()])

    def setDataType(self, dataType: str):
        self.__dataType = dataType

    def getList(self) -> list:
        return self.__list

    def getDataType(self) -> str:
        return self.__dataType

# A generic extractor class for getting a list of particular types from and AST


class GenericExtractor():
    def __init__(self):
        self.__ExtractorList = GenericInterestList()

    # Used to add items to the object's function list
    def _appendList(self, dataToAppend, LineNumToAppend):
        self.__ExtractorList.append(GenericInterestObject(dataToAppend, LineNumToAppend))

    # Returns the items in the function list
    def _getList(self) -> list:
        return self.__ExtractorList.getList()

    def _getDataType(self) -> str:
        return self.__ExtractorList.__dataType

    # Repr prints a nice table :)
    def __repr__(self) -> str:
        return repr(self.__ExtractorList)

    # returns the data as a CSV. Comma between data and newline between entries
    def __str__(self) -> str:
        return str(self.__ExtractorList)




# This should take in a file name and contain 2 GenericInterestsLists, 1 for Function Definitions
# and 1 for function calls along with the filename

class GenericParseObject():
    def __init__(self, funcDefList : list, funcCallList : list, filename : str):
        self.__filename = filename
        self.__funcDefList = GenericInterestList("Function Definition",funcDefList)
        self.__funcCallList = GenericInterestList("Function Call",funcCallList)
    
    def getFuncDefList(self) -> list:
        return self.__funcDefList

    def getFuncCallList(self) -> list:
        return self.__funcCallList

    def getFileName(self) -> str:
        return self.__filename

    def __repr__(self) -> str:
        returnstr = self.__filename + "\n"
        returnstr += repr(self.__funcDefList)
        returnstr += repr(self.__funcCallList)
        return returnstr

    def __str__(self) -> str:
        returnstr = self.__filename + "\n"
        returnstr += str(self.__funcDefList)
        returnstr += str(self.__funcCallList)
        return returnstr


