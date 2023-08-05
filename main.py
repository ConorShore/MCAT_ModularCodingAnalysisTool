
from prettytable import PrettyTable
from pycparser import c_parser, c_ast, parse_file
import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])

# Test code
text = r"""
    typedef int Node, Hash;

    void HashPrint(Hash* hash, void (*PrintFunc)(char*, char*))
    {
        unsigned int i;

        if (hash == NULL || hash->heads == NULL)
            return;

        for (i = 0; i < hash->table_size; ++i)
        {
            Node* temp = hash->heads[i];

            while (temp != NULL)
            {
                PrintFunc(temp->entry->key, temp->entry->value);
                SomeOtherFunc();
                temp = temp->next;
            }
        }
    }
    void AnotherFunc(void) {
        print("Hello");
    }
"""

# Create the parser and ask to parse the text. parse() will throw
# a ParseError if there's an error in the code
#
parser = c_parser.CParser()
ast = parser.parse(text, filename='<none>')

# A generic extractor class for getting infomation from AST


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

    def __repr__(self):
        table = PrettyTable()
        table.field_names = [self.getDataType(), "Line Number"]

        for entries in self.__ExtractorList:
            table.add_row([entries[0],str(entries[1].line)])

        return self.getDataType() + " Table\n" + str(table)


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

FuncCallExtract = FuncCallExtractor(ast)
print(FuncCallExtract)

FuncDefExtract = FuncDefExtractor(ast)
print(FuncDefExtract)

# v = FuncCallVisitor()
# v.visit(ast)
# x = FuncDefVisitor()
# x.visit(ast)
