#!/usr/bin/env python3

import sys
import os
import argparse
import json

scriptpath = os.path.realpath(__file__)
scriptdir = os.path.dirname(scriptpath)
translatordir = os.path.join(scriptdir, "translators")

def translate(inputtext, translatorname):
    translatorjson = os.path.join(translatordir, 
        "{}.json".format(translatorname))
    fh = open(translatorjson, 'r')
    translator = json.load(fh, encoding="utf8")
    fh.close()

    output = ""
    for c in list(inputtext):
        if c in translator:
            output += translator[c]
        else:
            output += c

    return output

def main(*args):
    h= "Perform some stupid unicoed tricks"
    argparser = argparse.ArgumentParser(description=h)

    h="Text to translate"
    argparser.add_argument('inputtext', help=h, action='store')

    h="Translator to use"
    argparser.add_argument('translatorname', help=h, action='store')

    pargs = argparser.parse_args()
    print(translate(pargs.inputtext, pargs.translatorname))

if __name__ == '__main__':
    sys.exit(main(*sys.argv))


