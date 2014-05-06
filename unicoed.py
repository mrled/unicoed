#!/usr/bin/env python3

import sys
import os
import json
import importlib

#scriptpath = os.path.realpath(__file__)
#scriptdir = os.path.dirname(scriptpath)
#translatordir = os.path.join(scriptdir, "translators")

def translate_from_json(inputtext, translatorname):
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

def translate(inputtext, translatorname):
    transmod = importlib.import_module("translators.{}".format(translatorname))
    return transmod.translate(inputtext)

def main(*args):
    import argparse

    h= "Perform some stupid unicoed tricks"
    argparser = argparse.ArgumentParser(description=h)

    h="Text to translate"
    argparser.add_argument('inputtext', help=h, action='store')

    h="Translator to use"
    argparser.add_argument('translatorname', help=h, action='store')

    pargs = argparser.parse_args()
    print("\n\n\n\n{}\n\n\n\n".format(
        translate(pargs.inputtext, pargs.translatorname)))

if __name__ == '__main__':
    sys.exit(main(*sys.argv))


