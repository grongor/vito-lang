#!venv/bin/python

import sys
import os
import collections
import re
import tempfile
import subprocess

__author__ = 'jakub.chabek@heureka.cz'

lang_definition = collections.OrderedDict()
lang_definition['print'] = ['A to si piš']
lang_definition['exit'] = ['Seru na to', 'Drž hubu']
lang_definition['True'] = ['Možná', 'Asi']
lang_definition['False'] = ['Je neni']
lang_definition['and'] = ['a další věc', 'a ještě taky']
lang_definition['or'] = ['nebo taky možná', 'a když to nepůjde tak']
lang_definition['not'] = ['jakoby opak', 'to přesně vopačný']
lang_definition['if \\1'] = ['Hele, a co kdyby jsme jakoby (.+?)', 'No když bude (.+?)']
lang_definition['elif'] = ['Nebo teda tohle', 'Tak tyvole třeba']
lang_definition['else'] = ['Tak když nic jinýho', 'Nasrat, bude to', 'Jinak prostě']
lang_definition['=='] = ['plus mínus stejný jako', 'stejný jako', 'cca']
lang_definition['!='] = ['je jinačí než', 'není vůbec podobný', 'trochu jiný než']
lang_definition['\\1 = '] = ['do (.+?) teď narvu', 'tak (.+?) bude třeba', '(.+?) teď bude', '(.+?) bude přesně jako']
lang_definition['with'] = ['bezpečnost nadevše, takže', 'tady bacha, ']
lang_definition['open'] = ['otevři mi tuten soubor', 'načti mi tohle']
lang_definition['as'] = ['a budem tomu říkat', 'a.k.a.']
lang_definition['try'] = ['Hele agilně', 'Prostě to zkusíme']
lang_definition['except'] = ['Kozy? Tak když ti to hodí', 'Ty vole do prdele co s tím']
lang_definition['finally'] = ['No a nakonec prostě', 'Hele v každym případě']
lang_definition['function'] = ['Týhle části budem říkat', 'Takže poslouchej']
lang_definition['class'] = ['Kravina s názvem', 'Nevim co je']
lang_definition['for \\1 in \\2'] = ['Kdybych dostal (.+?) za každou (.+?) tak bych',
                                     'Tak vezmu všechny (.+?) z toho (.+?) a prostě']
lang_definition['while'] = ['Dokuď je', 'Hele prostě tohle dělej dokuď']
lang_definition['8'] = ['O.S.M.', 'otočený nekonečno']

whitespace = ['vole', 'kurva', 'do prdele', 'čůrák', 'čůráci', 'zasranej kokot', 'zasraný kokoti', 'tvoje máma',
              'tvoje bába']

if len(sys.argv) != 2:
    print('You must pass exactly one parameter - path to the .nohy script')
    sys.exit(1)

file = sys.argv[1]
""" :type file: string """
if not os.path.isfile(file):
    print('File "{0}" was not found. Please supply path to the existing .nohy script'.format(file))
    sys.exit(1)

if not file.endswith('.nohy'):
    print('File "{0}" has an invalid extension. VitoLang scripts must end with .nohy'.format(file))
    sys.exit(1)

with open(file, 'r') as file:
    contents = file.read()
    for command, aliases in lang_definition.items():
        if command in contents:
            print(contents)
            print('Unknown command "{0}" used. This is not a VitoLang construct.'.format(command))
            exit(1)

        for alias in aliases:
            regexp = re.compile(alias)
            contents = regexp.sub(command, contents)

with tempfile.NamedTemporaryFile('w+b', 0) as file:
    file.write(contents.encode())

    process = subprocess.Popen(['{0}/venv/bin/python'.format(os.curdir), file.name],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = process.communicate()

    if errors:
        print(errors.decode())
        exit(1)

    print(output.decode().strip())
