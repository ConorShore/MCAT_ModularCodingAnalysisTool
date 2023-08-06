#!/usr/bin/python3


from re import T
import sys
import glob
import os
import argparse



from C_Extractors import CLangParser

argparser = argparse.ArgumentParser(
    prog='MCAT',
    description='Modular Coding Analysis Tool',
    epilog='Text at the bottom of help')

filename =""

# The key is the language name, the value is a list, first entry in the parse function,
# the second entry is file extensions assosiated with this language
# the third entry is the "nice" way of displaying the language i.e Python
supportedLanguages = {
    "c" : [CLangParser,[".c"],"C"]
}


# TODO - make this not a required thing, if not specific check files types to determine 
# TODO - add some way to pass language specific options down to parser
argparser.add_argument('--files', '-f',
                       help="File to analyse", required=True)
argparser.add_argument('--language', '-l',
                       help="Language to analyse", required=True)
argparser.add_argument('-v', '--verbose',
                       action='store_true')  # on/off flag

args = argparser.parse_args()
lowercaseTargetLang = str(args.language).lower()



if lowercaseTargetLang not in supportedLanguages:
    print("Language not supported")
    print("Supported languages are:")
    for lang in supportedLanguages.values():
        print(lang[2])
        exit()

        
# TODO - Test ideas for this
# relative path with no ./
# relative with with ./
# full path

# TODO - test file is exists and is readable

TargetFileList = []
for fileExtension in supportedLanguages[lowercaseTargetLang][1]:

    # glob returns a list of files, but we want to flatten that out seen as 
    # we could be running through this loop more than once
    foundFiles = glob.glob(str(args.files) + "/**/*" + fileExtension, recursive=True)
    for file in foundFiles:
        TargetFileList.append(file)

for file in TargetFileList:

    funcs = supportedLanguages[lowercaseTargetLang][0](file)
    print(repr(funcs))