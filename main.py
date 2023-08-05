#!/usr/bin/python3


from re import T
import sys
import glob
import os
import argparse

from pycparser import c_parser, parse_file, preprocess_file

from Extractors import FuncCallExtractor, FuncDefExtractor

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
argparser = argparse.ArgumentParser(
    prog='MCAT',
    description='Modular Coding Analysis Tool',
    epilog='Text at the bottom of help')

filename =""

argparser.add_argument('--filename', '-f',
                       help="File to analyse", required=True)     # positional argument
argparser.add_argument('-v', '--verbose',
                       action='store_true')  # on/off flag
argparser.add_argument('--parser', '-p',
                       help="Path to C parser, use if it is not in PATH")     # positional argument


args = argparser.parse_args()

print(args.filename)

# TODO - Test ideas for this
# relative path with no ./
# relative with with ./
# full path

TargetFileList = glob.iglob(str(args.filename) + "/**/*.c", recursive=True)

for name in TargetFileList:
    cparser = c_parser.CParser()

    # test file is exists and is readable
    
    file=open(name,"r")

    # TODO -  Add support for customer cpp path
    # TODO -  Add passable cpp_args

    ast = parse_file(name,use_cpp=True,
    cpp_args=r'-I./pycparser/utils/fake_libc_include')

    FuncCallExtract = FuncCallExtractor(ast)
    print(repr(FuncCallExtract))

    FuncDefExtract = FuncDefExtractor(ast)
    print(repr(FuncDefExtract))
