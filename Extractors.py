from typing import TypeVar
from prettytable import PrettyTable
from dataclasses import dataclass
from typing import List

# This is a simple data container with whatever data of interest you want, and where it is


class GenericInterestObject():
    def __init__(self, data: str = "", lineNumber: int = -1, columnNumber: int = -1) -> None:
        self.__dict = {
            "data": data,
            "lineNumber": lineNumber,
            "columnNumber": columnNumber
        }

    def set(self, data: str, lineNumber: int, columnNumber: int) -> None:
        self.__dict[data] = data
        self.__dict[lineNumber] = lineNumber
        self.__dict[columnNumber] = columnNumber

    def getData(self) -> dict:
        return self.__dict

    def getValues(self) -> list:
        return self.__dict.values()

    def getKeys(self) -> list:
        return self.__dict.keys()

    def __repr__(self) -> str:
        table = PrettyTable()
        table.field_names = self.getKeys()
        table.add_row(self.getValues())
        return repr(table) + "\n"

    def __str__(self) -> str:
        returnstr = ""
        for values in self.__dict.values():
            returnstr += str(values)

        return returnstr + "\n"

# A Generic Interest List is a list of GenericInterestObjects with a datatype header


class GenericInterestList():
    # TODO, specific that the list passed should be a list of GenericInterestObject
    def __init__(self, dataType: str = "Generic", listin: List[GenericInterestObject] = []) -> None:
        self.__dataType = dataType
        self.__list = listin

    def __repr__(self) -> str:
        table = PrettyTable()
        if type(self.__list[0]) == type(GenericInterestObject()):
            table.field_names = self.__list[0].getKeys()
        else:
            exit()

        for entries in self.__list:
            table.add_row(entries.getValues())

        return str(self.__dataType) + " Table \n" + str(table) + "\n"

# TODO - this should be more generic, and actually work
    def __str__(self) -> str:
        returnstr = ""
        for entries in self.__list:
            returnstr += entries[0] + "," + str(entries[1].line) + "\n"

        return returnstr

    def append(self, objectToAdd: GenericInterestObject) -> None:
        self.__list.append(objectToAdd)

    def setDataType(self, dataType: str) -> None:
        self.__dataType = dataType

    def getList(self) -> list:
        return self.__list

    def getDataType(self) -> str:
        return self.__dataType

    def reset(self) -> None:
        self.__list = []

# A generic extractor class for getting a list of particular types from and AST

class GenericExtractor():
    def __init__(self) -> None:
        
        self.__ExtractorList = GenericInterestList()
        self.__ExtractorList.reset()

    # Used to add items to the object's function list
    def _appendList(self, dataToAppend: str, LineNumToAppend: int, columnToAppend: int) -> None:
        self.__ExtractorList.append(
            GenericInterestObject(dataToAppend, LineNumToAppend, columnToAppend))

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
    def __init__(self, funcDefList: list, funcCallList: list, filename: str) -> None:
        self.__filename = filename
        self.__funcDefList = GenericInterestList(
            "Function Definition", funcDefList)
        self.__funcCallList = GenericInterestList(
            "Function Call", funcCallList)

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
