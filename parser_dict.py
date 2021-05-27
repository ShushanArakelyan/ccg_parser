POTENTIAL_FUTURE_PREDICATES = [
    'Number -> count',
    'Count -> count',
    'Edit',
    'Move',
    'Tuple',
    'Duplicate -> Check[EQ]',
    'Output',
    'that -> and',
]


# Everything that is defined in this dictionary MUST have corresponding rules in RAW_LEXICONE, or the parse will fail.
STRING2PREDICATE = {
    'dict': ['$Dict'],
    'dicts': ['$Dict'],
    'dictionary': ['$Dict'],
    'dictionaries': ['$Dict'],
    'int': ['$Int'],
    'integer': ['$Int'],
    'integers': ['$Int'],
    'array': ['$List'],
    'arrays': ['$List'],
    'list': ['$List'],
    'lists': ['$List'],
    'tuple': ['$Tuple'],
    'tuples': ['$Tuple'],
    'array': ['$List'],
    'string': ['$String'],
    'strings': ['$String'],
    'unicode string': ['$String'],
    'str': ['$String'],
    'file': ['$File'],
    'files': ['$File'],
    'loop': ['$Loop'],
    'for loop': ['$Loop'],
    'enum': ['$Enum'],
    'enumerate': ['$Enum'],
    'bool': ['$Bool'],
    'boolean': ['$Bool'],
    'char': ['$Char'],
    'character': ['$Char'],
    'characters': ['$Char'],
    'unicode': ['$Char'],
    'path': ['$Path'],
    'dir': ['$Path'],
    'directory': ['$Path'],
    'class': ['$Class'],
    'object': ['$Class'],
    'objects': ['$Class'],
    'member': ['$Class'],
    'func': ['$Func'],
    'function': ['$Func'],
    'method': ['$Func'],
    'index': ['$Index'],
    'id': ['$Index'],
    'regex': ['$Regex'],
    'column': ['$Column'],
    'columns': ['$Column'],
    'number': ['$Number'],
    'numbers': ['$Number'],
    'null': ['$Null'],
    'nulls': ['$Null'],
    'nan': ['$Null'],

    # det-s
    'the': ['$The'],
    'an': ['$The'],
    'a': ['$The'],

    # Action verbs
    # One problem with large string2predicate list is the fact that we lose the actual predicate/verb of
    'find': ['$Find'],
    'locate': ['$Find'],
    'calcuate': ['$Find'],
    'choose': ['$Find'],
    'search': ['$Find'],
    'filter': ['$Find'],
    'extract': ['$Find'],
    'lookup': ['$Find'],
    'retrieve': ['$Find'],
    # 'return': ['$Return'],
    # 'fallback': ['$Return'],
    # 'raise': ['$Return'],

    'merge': ['$Merge'],
    'join': ['$Merge'],
    'group': ['$Merge'],

    'round': ['$Round'],
    'limit': ['$Round'],
    'clamp': ['$Round'],

    'reset': ['$Convert'],
    'rename': ['$Convert'],
    'convert': ['$Convert'],
    'derive': ['$Convert'],
    'translate': ['$Convert'],
    'turn': ['$Convert'],
    'transform': ['$Convert'],
    'encode': ['$Convert'],
    'decode': ['$Convert'],
    'customize': ['$Convert'],
    'binarize': ['$Convert'],
    'inverse': ['$Convert'],
    'resize': ['$Convert'],
    'edit': ['$Convert'],
    'compress': ['$Convert'],
    'hash': ['$Convert'],
    'serialize': ['$Convert'],
    'wrap': ['$Convert'],

    'clear': ['$Remove'],
    'delete': ['$Remove'],
    'disable': ['$Remove'],
    'disallow': ['$Remove'],
    'drop': ['$Remove'],
    'erase': ['$Remove'],
    'strip': ['$Remove'],
    'reduce': ['$Remove'],
    'remove': ['$Remove'],
    'abort': ['$Remove'],
    'close': ['$Remove'],
    'escape': ['$Remove'],
    'ignore': ['$Remove'],
    'kill': ['$Remove'],
    'terminate': ['$Remove'],
    'exclude': ['$Remove'],

    'create': ['$Create'],
    'generate': ['$Create'],
    'initialize': ['$Create'],
    'duplicate': ['$Create'],
    'init': ['$Create'],
    'declare': ['$Create'],
    'define': ['$Create'],
    'copy': ['$Create'],
    'make': ['$Create'],
    'construct': ['$Create'],
    'produce': ['$Create'],
    'build': ['$Create'],
    'rebuild': ['$Create'],

    'load': ['$Load'],
    'read': ['$Load'],
    'download': ['$Load'],
    'input': ['$Load'],
    'import': ['$Load'],
    'open': ['$Load'],
    'receive': ['$Load'],
    'fetch': ['$Load'],

    'save': ['$Save'],
    'write': ['$Save'],
    'put': ['$Save'],
    'update': ['$Save'],
    'upload': ['$Save'],
    'store': ['$Save'],
    'export': ['$Save'],
    'keep': ['$Save'],
    'pickle': ['$Save'],

    'print': ['$Print'],

    'repeat': ['$Iterate'],
    'iterate': ['$Iterate'],
    'iter': ['$Iterate'],
    'iterator': ['$Iterate'],
    'iterators': ['$Iterate'],
    'loop': ['$Iterate'],
    'enumerate': ['$Iterate'],

    'extend': ['$Append'],
    'append': ['$Append'],
    'prepend': ['$Append'],
    'pad': ['$Append'],
    'scale': ['$Append'],
    'expand': ['$Append'],
    'pack': ['$Append'],

    'determine': ['$Compare'],
    'check': ['$Compare'],
    'see': ['$Compare'],
    'comp': ['$Compare'],
    'compare': ['$Compare'],
    'difference': ['$Compare'],

    'assign': ['$Assign'],
    'indexing': ['$Assign', '$Index'],

    'reorder': ['$Sort'],
    'order': ['$Sort'],
    'sort': ['$Sort'],

    'move': ['$Replace'],
    'change': ['$Replace'],
    'replace': ['$Replace'],
    'substitute': ['$Replace'],
    'fix': ['$Replace'],
    'swap': ['$Replace'],
    'rotate': ['$Replace'],
    'modify': ['$Replace'],
    'switch': ['$Replace'],
    'shift': ['$Replace'],
    'override': ['$Replace'],
    'shuffle': ['$Replace'],

    # Prepositions
    'as': ['$As'],
    'based on': ['$By'],
    'by': ['$By'],
    'for': ['$For'],
    'from': ['$From'],
    'in': ['$In'],
    'inside': ['$In'],
    'into': ['$Into'],
    'of': ['$Of'],
    'on': ['$On'],
    'over': ['$Over'],
    'through': ['$Through'],
    'to': ['$To'],
    'using': ['$With'],
    'within': ['$In'],
    'with': ['$With'],
    'with the help of': ['$With'],
}

WORD_NUMBERS = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
WORD2NUMBER = {elem: str(i) for i, elem in enumerate(WORD_NUMBERS)}


RAW_LEXICON = ''' :- S, NP, N, VP, PP
    Det :: NP/N
    Pro :: NP
    Modal :: S\\NP/VP

    TV :: VP/NP
    DTV :: TV/NP
    # PP :: (NP\\NP)/NP

    $The => N/N {\\x.x}
    $The => NP/NP {\\x.x}
    $The => N/VP {\\x.x}
    $The => NP/VP {\\x.x}

    $Dict => N {'Dict'}
    $Dict => NP {'Dict'}
    $Int => N {'Int'}
    $Int => NP {'Int'}
    $List => N {'List'}
    $List => NP {'List'}
    $List => NP/NP {\\x. '@Compose'('List', x)}
    $Tuple => N {'Tuple'}
    $Tuple => NP {'Tuple'}
    $String => N {'String'}
    $String => NP {'String'}
    $File => N {'File'}
    $File => NP {'File'}
    $Loop => N {'Loop'}
    $Loop => NP {'Loop'}
    $Enum => N {'Enum'}
    $Enum => NP {'Enum'}
    $Bool => N {'Bool'}
    $Bool => NP {'Bool'}
    $Char => N {'Char'}
    $Char => NP {'Char'}
    $Path => N {'Path'}
    $Path => NP {'Path'}
    $Set => N {'Set'}
    $Set => NP {'Set'}
    $Class => N {'Class'}
    $Class => NP {'Class'}
    $Func => N {'Func'}
    $Func => NP {'Func'}
    $Index => N {'Index'}
    $Index => NP {'Index'}
    $Regex => N {'Regex'}
    $Regex => NP {'Regex'}
    $Column => N {'Column'}
    $Column => NP {'Column'}
    $Null => N {'Null'}
    $Null => NP {'Null'}
    $Zero => N {'Null'}
    $Zero => NP {'Null'}
    $Number => N {'Number'}
    $Number => NP {'Number'}
    $Set => N {'Set'}
    $Set => NP {'Set'}

    # Prepositions
    $As => PP/NP {\\x. '@As'(x)}
    $As => PP/VP {\\x.'@As'(x)}
    $By => PP/NP {\\x.'@By'(x)}
    $By => S/S {\\x. x}
    $For => PP/NP {\\x.'@For'(x)}
    $For => PP/VP {\\x.'@For'(x)}
    $From => PP/NP {\\x.'@From'(x)}
    $From => PP/S {\\x.'@From'(x)}
    $From => PP/VP {\\x.'@From'(x)}
    $In => PP/NP {\\x.'@In'(x)}
    $Into => PP/NP {\\x.'@Into'(x)}
    $Into => PP/VP {\\x.'@Into'(x)}
    $Into => (PP/NP)/NP {\\y x.'@Into'(x, y)}
    $Of => (PP\\NP)/NP {\\y x. '@Of'(x, y)}
    $Of => (PP\\NP)/VP {\\y x. '@Of'(x, y)}
    $On => PP/NP {\\x. '@On'(x)}
    $On => PP/VP {\\x. '@On'(x)}
    $Over => PP/NP {\\x. '@Over'(x)}
    $Over => PP/VP {\\x. '@Over'(x)}
    $Through => PP/NP {\\x. '@Through'(x)}
    $Through => PP/VP {\\x. '@Through'(x)}
    $To_verb => S/S {\\x. x}
    $To_verb => VP/VP {\\x. x}
    $To => PP/NP {\\x. '@To'(x)}
    $To => PP/VP {\\x. '@To'(x)}
    $With => PP/NP {\\x.'@With'(x)}
    $With => PP/VP {\\x.'@With'(x)}

    # Action verbs
    $Find => S/NP {\\x.'@Action'('Find', x)}
    $Find => (S/NP)/PP {\\y x.'@Action'('Find', x, y)}
    $Find => (S/NP)/NP {\\y x.'@Action'('Find', x, y)}
    $Find => VP/NP {\\x.'@Action'('Find', x)}
    $Find => VP/PP {\\x.'@Action'('Find', x)}
    $Find => S/VP {\\x.'@Action'('Find', x)}
    $Find => (S/VP)/PP {\\y x.'@Action'(Find, x, y)}
    $Find => (VP/NP)/PP {\\y x.'@Action'(Find, x, y)}
    $Find => (VP/NP)/NP {\\y x.'@Action'(Find, x, y)}

    $Return => S/NP {\\x.'@Action'('Return', x)}
    $Return => (S/NP)/PP {\\y x.'@Action'('Return', x, y)}
    $Return => (S/NP)/NP {\\y x.'@Action'('Return', x, y)}
    $Return => VP/NP {\\x.'@Action'('Return', x)}
    $Return => S/VP {\\x.'@Action'('Return', x)}
    $Return => (S/VP)/PP {\\y x.'@Action'('Return', x, y)}
    $Return => (VP/NP)/PP {\\y x.'@Action'('Return', x, y)}
    $Return => (VP/NP)/NP {\\y x.'@Action'('Return', x, y)}
    
    $Merge => S/NP {\\x. '@Action'('Merge', x)}
    $Merge => S/PP {\\x. '@Action'('Merge', x)}
    $Merge => (S/NP)/PP {\\y x. '@Action'('Merge', x, y)}
    $Merge => VP/NP {\\x. '@Action'('Merge', x)}
    $Merge => VP/PP {\\x. '@Action'('Merge', x)}
    $Merge => (S/VP)/PP {\\y x. '@Action'('Merge', x, y)}
    $Merge => (VP/NP)/PP {\\y x. '@Action'('Merge', x, y)}

    $Iterate => S/PP {\\x. '@Action'('Iterate', x)}
    $Iterate => (S/NP)/PP {\\y x. '@Action'('Iterate', x, y)}
    $Iterate => (S/NP)/NP {\\y x. '@Action'('Iterate', x, y)}
    $Iterate => S/VP {\\x. '@Action'('Iterate', x)}
    $Iterate => (S/VP)/PP {\\y x. '@Action'('Iterate', x, y)}
    $Iterate => (S/VP)/NP {\\y x. '@Action'('Iterate', x, y)}
    $Iterate => VP/PP {\\x. '@Action'('Iterate', x)}
    $Iterate => (VP/NP)/PP {\\y x. '@Action'('Iterate', x, y)}
    $Iterate => (VP/NP)/NP {\\y x. '@Action'('Iterate', x, y)}

    $Sort => S/NP {\\x. '@Action'('Sort', x)}
    $Sort => S/PP {\\x. '@Action'('Sort', x)}
    $Sort => (S/NP)/PP {\\y x. '@Action'('Sort', x, y)}
    $Sort => (S/NP)/NP {\\y x. '@Action'('Sort', x, y)}
    $Sort => S/VP {\\x. '@Action'('Sort', x)}
    $Sort => (S/VP)/PP {\\y x. '@Action'('Sort', x, y)}
    $Sort => (S/VP)/NP {\\y x. '@Action'('Sort', x, y)}
    $Sort => VP/NP {\\x. '@Action'('Sort', x)}
    $Sort => VP/PP {\\x. '@Action'('Sort', x)}

    # $Concatenate => S/NP {\\x. '@Action'('Concatenate', x)} # can be also Merge
    # $Concatenate => (S/NP)/PP  {\\y x. '@Action'('Concatenate', x, y)} # can be also Merge
    # $Concatenate => (S/NP)/NP  {\\y x. ''@Action'('Concatenate', x, y)} # can be also Merge

    # $Split => S/NP {\\x. '@Action'('Split', x)}
    # $Split => S\\NP {\\x. '@Action'('Split', x)}
    # $Split => (S/NP)/PP {\\y x. '@Action'('Split', x, y)}

    # $Round => S/NP {\\x. '@Action'('Round', x)}
    # $Round => S/PP {\\x. '@Action'('Round', x)}
    # $Round => (S/NP)/PP {\\y x. '@Action'('Round', x, y)}

    $Convert => S/PP {\\x. '@Action'('Convert', x)}
    $Convert => S/NP {\\x. '@Action'('Convert', x)}
    $Convert => (S/NP)/PP {\\y x. '@Action'('Convert', x, y)}
    $Convert => (S/NP)/NP {\\y x. '@Action'('Convert', x, y)}
    $Convert => S/VP {\\x. '@Action'('Convert', x)}
    $Convert => VP/PP {\\x. '@Action'('Convert', x)}
    $Convert => VP/NP {\\x. '@Action'('Convert', x)}
    $Convert => (VP/NP)/PP {\\y x. '@Action'('Convert', x, y)}
    $Convert => (VP/NP)/NP {\\y x. '@Action'('Convert', x, y)}
    $Convert => (S/VP)/PP {\\y x. '@Action'('Convert', x, y)}
    $Convert => (S/VP)/NP {\\y x. '@Action'('Convert', x, y)}

    # $Add => S/NP {\\x. '@Action'('Add', x)}
    # $Add => S/PP {\\x. '@Action'('Add', x)}
    # $Add => (S/NP)/PP {\\y x. '@Action'('Add', x, y)}
    # $Add => (S/NP)/NP {\\y x. '@Action'('Add', x, y)}

    $Remove => S/NP {\\x. '@Action'('Remove', x)}
    $Remove => (S/NP)/PP {\\y x. '@Action'('Remove', x, y)}
    $Remove => (S/NP)/NP {\\y x. '@Action'('Remove', x, y)}
    $Remove => S/VP {\\x. '@Action'('Remove', x)}
    $Remove => (S/VP)/PP {\\y x. '@Action'('Remove', x, y)}
    $Remove => (S/VP)/NP {\\y x. '@Action'('Remove', x, y)}
    $Remove => VP/NP {\\x. '@Action'('Remove', x)}
    $Remove => (VP/NP)/PP {\\y x. '@Action'('Remove', x, y)}
    $Remove => (VP/NP)/NP {\\y x. '@Action'('Remove', x, y)}

    $Create => S/NP {\\x. '@Action'('Create', x)}
    $Create => (S/NP)/PP {\\y x. '@Action'('Create', x, y)}
    $Create => (S/NP)/NP {\\y x. '@Action'('Create', x, y)}
    $Create => VP/NP {\\x. '@Action'('Create', x)}
    $Create => S/VP {\\x. '@Action'('Create', x)}
    $Create => (VP/NP)/PP {\\y x. '@Action'('Create', x, y)}
    $Create => (S/VP)/PP {\\y x. '@Action'('Create', x, y)}
    $Create => (VP/NP)/NP {\\y x. '@Action'('Create', x, y)}
    $Create => (S/VP)/NP {\\y x. '@Action'('Create', x, y)}

    $Load => S/NP {\\x. '@Action'('Load', x)}
    $Load => S/PP {\\x. '@Action'('Load', x)}
    $Load => (S/NP)/PP {\\y x. '@Action'('Load', x, y)}
    $Load => (S/NP)/NP {\\y x. '@Action'('Load', x, y)}
    $Load => S/VP {\\x. '@Action'('Load', x)}
    $Load => VP/NP {\\x. '@Action'('Load', x)}
    $Load => VP/PP {\\x. '@Action'('Load', x)}
    $Load => (VP/NP)/PP {\\y x. '@Action'('Load', x, y)}
    $Load => (VP/NP)/NP {\\y x. '@Action'('Load', x, y)}
    $Load => (S/VP)/PP {\\y x. '@Action'('Load', x, y)}
    $Load => (S/VP)/NP {\\y x. '@Action'('Load', x, y)}

    $Save => S/NP {\\x. '@Action'('Save', x)}
    $Save => S/PP {\\x. '@Action'('Save', x)}
    $Save => (S/NP)/PP {\\y x. '@Action'('Save', x, y)}
    $Save => (S/NP)/NP {\\y x. '@Action'('Save', x, y)}
    $Save => S/VP {\\x. '@Action'('Save', x)}
    $Save => VP/NP {\\x. '@Action'('Save', x)}
    $Save => VP/PP {\\x. '@Action'('Save', x)}
    $Save => (VP/NP)/PP {\\y x. '@Action'('Save', x, y)}
    $Save => (VP/NP)/NP {\\y x. '@Action'('Save', x, y)}
    $Save => (S/VP)/PP {\\y x. '@Action'('Save', x, y)}
    $Save => (S/VP)/NP {\\y x. '@Action'('Save', x, y)}

    $Print => S/NP {\\x. '@Action'('Print', x)}
    $Print => (S/NP)/PP {\\y x. '@Action'('Print', x, y)}
    $Print => (S/NP)/NP {\\y x. '@Action'('Print', x, y)}
    $Print => VP/NP {\\x. '@Action'('Print', x)}
    $Print => S/VP {\\x. '@Action'('Print', x)}
    $Print => (VP/NP)/PP {\\y x. '@Action'('Print', x, y)}
    $Print => (VP/NP)/NP {\\y x. '@Action'('Print', x, y)}
    $Print => (S/VP)/PP {\\y x. '@Action'('Print', x, y)}
    $Print => (S/VP)/NP {\\y x. '@Action'('Print', x, y)}

    $Append => S/NP {\\x. '@Action'('Append', x)}
    $Append => S/PP {\\x. '@Action'('Append', x)}
    $Append => (S/NP)/PP {\\y x. '@Action'('Append', x, y)}
    $Append => VP/NP {\\x. '@Action'('Append', x)}
    $Append => VP/PP {\\x. '@Action'('Append', x)}
    $Append => S/VP {\\x. '@Action'('Append', x)}
    $Append => (S/VP)/PP {\\y x. '@Action'('Append', x, y)}
    $Append => (VP/NP)/PP {\\y x. '@Action'('Append', x, y)}

    $Compare => S/NP {\\x. '@Action'('Compare', x)}
    $Compare => S/PP {\\x. '@Action'('Compare', x)}
    $Compare => (S/NP)/PP {\\y x. '@Action'('Compare', x, y)}
    $Compare => (S/NP)/NP {\\y x. '@Action'('Compare', x, y)}
    $Compare => VP/NP {\\x. '@Action'('Compare', x)}
    $Compare => VP/PP {\\x. '@Action'('Compare', x)}
    $Compare => (S/VP)/PP {\\y x. '@Action'('Compare', x, y)}
    $Compare => (S/VP)/NP {\\y x. '@Action'('Compare', x, y)}
    $Compare => (VP/NP)/PP {\\y x. '@Action'('Compare', x, y)}
    $Compare => (VP/NP)/NP {\\y x. '@Action'('Compare', x, y)}

    $Assign => (S/NP)/PP {\\y x. '@Action'('Assign', x, y)}
    $Assign => VP/PP {\\y x. '@Action'('Assign', x, y)}

    $Replace => S/NP {\\x. '@Action'('Replace', x)}
    $Replace => (S/NP)/PP {\\y x. '@Action'('Replace', x, y)}
    $Replace => (S/NP)/NP {\\y x. '@Action'('Replace', x, y)}
    $Replace => VP/NP {\\x. '@Action'('Replace', x)}
    $Replace => (VP/NP)/PP {\\y x. '@Action'('Replace', x, y)}
    $Replace => (VP/NP)/NP {\\y x. '@Action'('Replace', x, y)}
    $Replace => (S/VP)/PP {\\y x. '@Action'('Replace', x, y)}
    $Replace => (S/VP)/NP {\\y x. '@Action'('Replace', x, y)}

    # $Contain => (S/NP)/PP {\\y x. '@Action'('Contain', x, y)}

    # $Match => S/NP {\\x. '@Action'('Match', x)}
    # $Match => (S/NP)/PP {\\y x. '@Action'('Match', x, y)}
'''

QUESTION_WORDS = [
    ['how', 'to'],
    ['how', 'do', 'i'], ['how', 'would', 'i'], ['how', 'should', 'i'],
    ['how', 'i', 'would'], ['how', 'i', 'should'],
    ['how', 'can', 'i'], ['can', 'i'], ['how', 'i', 'can'],
    ['how', 'do', 'we'], ['how', 'would', 'we'],
    ['how', 'should', 'we'], ['how', 'we', 'would'],
    ['how', 'we', 'should'],
    ['how', 'can', 'we'], ['can', 'we'], ['how', 'we', 'can'],
    ['how', 'do', 'you'], ['how', 'would', 'you'],
    ['how', 'should', 'you'], ['how', 'you', 'would'],
    ['how', 'you', 'should'], ['how', 'does', 'this'],
    ['how', 'can', 'you'], ['can', 'you'], ['how', 'you', 'can'],
    ['how', 'does', 'one'], ['how', 'would', 'one'],
    ['how', 'should', 'one'], ['how', 'one', 'would'],
    ['how', 'one', 'should'],
    ['how', 'can', 'one'], ['can', 'one'], ['how', 'one', 'can'],
    ['cannot'], ['can\'t'], ['can', 'not'],
    ['is', 'there', 'a', 'way', 'to'],
    ['is', 'it', 'possible', 'to'],
    ['is', 'there'], ['are', 'there'], ['is', 'it', 'possible', 'to'],
    ['how', 'can'], ['can'],
    ['what', 'is', 'the', 'best', 'way', 'to'],
]

PYTHON_WORDS = [
    ['in', 'python'], ['with', 'python'],
    ['using', 'python'], ['pythonic', 'way'],
]
