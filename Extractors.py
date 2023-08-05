from pycparser import c_ast
from prettytable import PrettyTable

# A generic extractor class for getting a list of particular types from and AST

class GenericExtractor(c_ast.NodeVisitor):
    def __init__(self):
        self.__ExtractorList = []
        self.__DataType = "Generic"

    # Used to add items to the object's function list
    def _appendList(self, dataToAppend, coordToAppend):
        x = [dataToAppend, coordToAppend]
        self.__ExtractorList.append(x)

    # Returns the items in the function list
    def getList(self):
        return self.__ExtractorList

    def getDataType(self):
        return "Generic"

    # Repr prints a nice table :)
    def __repr__(self):
        table = PrettyTable()
        table.field_names = [self.getDataType(), "Line Number"]

        for entries in self.__ExtractorList:
            table.add_row([entries[0],str(entries[1].line)])

        return self.getDataType() + " Table\n" + str(table)

    # returns the data as a CSV. Comma between data and newline between entries
    def __str__(self):
        returnstr = ""
        for entries in self.__ExtractorList:
            returnstr += entries[0] + "," + str(entries[1].line) + "\n"

        return returnstr


# A class to extract all function call from a give AST

class FuncCallExtractor(GenericExtractor):

    def visit_FuncCall(self, node):
        self._appendList(node.name.name, node.name.coord)

        # Visit args in case they contain more func calls.
        if node.args:
            self.visit(node.args)

    # when instantiating the class, also analyse the AST
    def __init__(self, input_ast, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.visit(input_ast)
        self.__DataType="FuncCall"
    
    def getDataType(self):
        return "FuncCall"

# A class to extract all function definitions from a give AST

class FuncDefExtractor(GenericExtractor):

    def visit_FuncDef(self, node):
        self._appendList(node.decl.name, node.decl.coord)

    # when instantiating the class, also analyse the AST
    def __init__(self, input_ast, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.visit(input_ast)
        self.__DataType="FuncDef"

    def getDataType(self):
        return "FuncDef"