VitoLang
========

Hello there, welcome! Thank you for your interest in VitoLang!

What is it?
-----------

VitoLang is a modern language inspired by a need for more native programming language. A language that anyone
can use to write great applications in a very easy and intuitive way.

VitoLang makes use of a lot of aliases for certain construct to make the work with it easier.
If you for example forget how to write a condition then there is probably another way (another expression)
which you can use - just use your common language. It will grow on you very soon.

How to start?
-------------

Well there is a `Makefile` to make the first steps very easy! All you need to do is clone this repository
and issue `make` command. `Makefile` will take care of all the rest.

My first program
----------------

All programs written in VitoLang are stored in `.nohy` files. You can start by creating your first
file: `touch main.nohy`

To run a VitoLang program you must use the automatically installed interpreter `chci`. So just give it a try and run
your newly created VitoLang program using the command: `chci main.nohy`

There should be no output - of course, your program is empty. It is time to create a standard "HelloWorld!" program.
Put this in your `main.nohy` file: `A to si piš('HelloWorld!')`

If you execute the program again it should output "HelloWorld!", great, isn't it? :-)

To learn more about VitoLang, please visit the next section **Language constructs**

Language constructs
-------------------

VitoLang inspired in Python a lot so there are many familiar constructs. You surround your function calls with
parenthesis, indent blocks with 4 spaces, end conditions, cycles etc with colon, use dot to interface object
methods and properties etc. You can also import any Python library and use them inside VitoLang program.

**Import libraries:**
- `Budeme používat`, `No radši mi načti`, `Tohle se bude hodit`

**Output:**
- To output some text you can use commands: `A to si piš`, `Vypiš tohle`, `Někam to zapiš`, `Volám Čuprovi`

**Boolean logic:**
- There are boolean values True represented by `Možná` or `Asi` and False by `Je neni`
- For logical product (AND, &&) you can use `a další věc` or `a ještě taky`
- For logical sum (OR, ||) there are `nebo taky možná`, `a když to nepůjde tak`
- For logical negation (NOT, ~) use either `jakoby opak` or `to přesně vopačný`

**Conditions:**
- First condition (IF) is represented by `Hele, a co kdyby jsme jakoby {CONDITION}`, `No když bude {CONDITION}`
- Other conditional branches (ELSEIF, ELIF) can be expressesd by `Nebo teda tohle`, `Tak tyvole třeba`
- Last unconditional branch (ELSE) may be written using `Tak když nic jinýho`, `Nasrat, bude to`, `Jinak prostě`

**Variables and comparison:**
- To assign value to a variable (=, :=) use `do {VARIABLE} teď narvu`, `tak {VARIABLE} bude třeba`,
  `{VARIABLE} teď bude`, `{VARIABLE} bude přesně jako`
- To check whether two expressions are same (==, eq) you can use `plus mínus stejný jako`, `stejný jako`, `cca`
- To check whether two expressions are different (!=, ne) you can use `je jinačí než`, `není vůbec podobný`,
  `trochu jiný než`

**Safe work with files and other things:**
- If you are familiar with the Python construction `with open('file.txt') as file_handle:`, then you will be happy
  that we managed to incorporate that into VitoLang too! Use the following expressions:
    - with: `bezpečnost nadevše, takže`, `tady bacha, `
    - open: `otevři mi tuten soubor`, `načti mi tohle`
    - as: `a budem tomu říkat`, `a.k.a.`

**Exceptions handling:**
- To surround a block of code with exception-handling code, use expressions `Hele agilně`, `Prostě to zkusíme`
- To catch an exception, use any of those `Kozy? Tak když ti to hodí`, `Ty vole do prdele co s tím`
- And to perform final cleaning (the block will execute with or without exception), use one of `No a nakonec prostě`,
  `Hele v každym případě`

**Classes and functions:**
- Of course you can define classes, use any of those `Kravina s názvem`, `Nevim co je`
- For defining a function there are those constructs `Týhle části budem říkat`, `Takže poslouchej`
- To return a value from function use `Tady mám prachy na dobírku`, `Chci prostě to`, `Vybleju`

**Cycles:**
- To iterate over a collection use `Kdybych dostal {ITEM} za každou {COLLECTIOn} tak bych`,
  `Tak vezmu všechny {ITEM} z toho {COLLECTION} a prostě`
- For a simple conditional cycle there are `Dokuď je`, `Hele prostě tohle dělej dokuď`
- To skip a cycle iteration use `Hele jdi dál`, `Ok tohle skipneme`
- To break the cycle use one of `Nemá cenu, srát na to`, `Hele prcáme to`

**Exit the program:**
- There is a few functions to exit the program: `Seru na to`, `Drž hubu`

**Numbers:**
- All numbers are the same as in Python. There had to be a single exception and that is a number 8. To express
  the number 8 you must use either `O.S.M.` or `otočený nekonečno`

**Whitespace:**
- We understand the need to express yourself. You are creative person after all. If you feel like you need to add
  some more constructs you add those before or after any command as you feel like: `vole`, `kurva`, `do prdele`,
  `čůrák`, `čůráci`, `zasranej kokot`, `zasraný kokoti`, `tvoje máma`, `tvoje bába`

**Other:**
- If you need a placeholder block without any real function then use `nechci` or `zbytečný` to pass over it
- To remove a variable use `jdi do prdele`, `to už nechci`
- To assert a condition in your program use `Ne, já prostě chci, aby`, `Tohle bude takhle jinak prostě ne`

Simple example to get you started
---------------------------------

If you are confused by all the abilities of VitoLang then fear not. You will get into it very soon!
Here is an example of VitoLang and it's Python equivalent (just so you see how simple VitoLang really is):

```
tak abc bude třeba 'string'
No když bude Možná cca Je neni nebo taky možná jakoby opak (Je neni plus mínus stejný jako Asi):
    A to si piš('Hello there!')
Nebo teda tohle abc stejný jako 'rofl':
    kurva vole Vypiš tohle do piče('foobar')
Tak tyvole třeba Asi:
    zbytečný
Tak když nic jinýho debilní kokoti:
    A to si piš('no' + 'thing to see there')

items bude přesně jako (1, 2, 3)
Kdybych dostal item za každou items tak bych do piče:
    Někam to zapiš(item)

do a teď narvu 0
Hele prostě tohle dělej dokuď tvoje máma to přesně vopačný (a cca 2):
    Vypiš tohle(a)
    a += 1

Seru na to
```

```
abc = 'string'
if True == False or not (False == True):
    print('Hello there!')
elif abc == 'rofl':
      print('foobar')
elif True:
    pass
else :
    print('no' + 'thing to see there')

items = (1, 2, 3)
for item in items :
    print(item)

a = 0
while not (a == 2):
    print(a)
    a += 1

exit
```

Minor negatives
---------------

Well nothing is without a bad side. VitoLang's bad side is that you sometimes might be forced to split string
literals into multiple strings as the interpreter will confuse them with language constructs. An example is word
`'nothing'` which parser will confuse with an internal function `not`. You can bypass this little thing with string
concatenation `'no' + 'thing'`
