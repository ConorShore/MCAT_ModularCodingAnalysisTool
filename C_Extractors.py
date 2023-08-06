from pycparser import c_parser, parse_file, c_ast
from Extractors import GenericExtractor, GenericParseObject

#TODO - this currently doesn't handle header files. figure it out

# A class to extract all function call from a give AST

class FuncCallExtractor(GenericExtractor,c_ast.NodeVisitor):

    def visit_FuncCall(self, node) -> None:
        self._appendList(node.name.name, node.name.coord.line,node.name.coord.column )

        # Visit args in case they contain more func calls.
        if node.args:
            self.visit(node.args)

    # when instantiating the class, also analyse the AST
    def __init__(self, input_ast, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.visit(input_ast)
        self.__DataType="FuncCall"
    
    def getDataType(self) -> None:
        return str(self.__DataType)

# A class to extract all function definitions from a give AST

class FuncDefExtractor(GenericExtractor,c_ast.NodeVisitor):

    def visit_FuncDef(self, node) -> None:
        self._appendList(node.decl.name, node.decl.coord.line, node.decl.coord.column)

    # when instantiating the class, also analyse the AST
    def __init__(self, input_ast, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.visit(input_ast)
        self.__DataType="FuncDef"

    def getDataType(self) -> str:
        return str(self.__DataType)


def CLangParser(file) -> GenericParseObject:
   
    # TODO -  Add support for customer cpp path
    # TODO -  Add passable cpp_args

    ast = parse_file(file,use_cpp=True,
    cpp_args=r'-I./pycparser/utils/fake_libc_include')

    FuncDefExtract = FuncDefExtractor(ast)

    FuncCallExtract = FuncCallExtractor(ast)

    ParseObj = GenericParseObject(FuncDefExtract._getList(),FuncCallExtract._getList(),str(file))
    
    return ParseObj