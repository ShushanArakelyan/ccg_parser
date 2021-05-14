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

    # conjunctions
    # 'and': ['$And'],
    # 'that': ['$And'],
    # 'then': ['$And'],
    # 'both': ['$And'],
    # 'too': ['$And'],
    # 'also': ['$And'],
    # 'including': ['$And'],
    # 'or': ['$Or'],
    # 'else': ['$Or'],
    # 'rather': ['$Or'],
    # 'either': ['$Or'],
    # 'not': ['$Not'],
    # 'non': ['$Not'],
    # 'none': ['$Not'],
    # 'nothing': ['$Not'],
    # 'never': ['$Not'],
    # 'without': ['$Not'],

    # Transforming verbs
    'find': ['$Find'],
    'locate': ['$Find'],
    'calcuate': ['$Find'],
    'search': ['$Find'],
    'filter': ['$Find'],
    'extract': ['$Find'],
    'lookup': ['$Find'],
    'understand': ['$Find'],
    # 'find if': ['$Check']
    # 'find out': ['$Return']?
    # kind of the same as 'get'? return smth [from smth/smwh]
    'return': ['$Return'],
    'fallback': ['$Return'],
    'raise': ['$Return'],
    # merge smth-s into smth; merge smth-s; merge smth with smth; merge in NP[e.g. merge sort]
    'merge': ['$Merge'],
    'join': ['$Merge'],
    'coalesce': ['$Merge'],
    'group': ['$Merge'],
    'interleave': ['$Merge'],
    'concat': ['$Concatenate'],
    'concatenate': ['$Concatenate'],
    'concatenation': ['$Concatenate'],
    'append': ['$Concatenate'],
    'combine': ['$Concatenate'],
    'combinate': ['$Concatenate'],
    'queue': ['$Concatenate'],
    'zip': ['$Concatenate'],
    'stack': ['$Concatenate'],
    'slice': ['$Split'],
    'split': ['$Split'],
    'cut': ['$Split'],
    'segment': ['$Split'],
    'round': ['$Round'],
    'limit': ['$Round'],
    'clamping': ['$Round'],
    'throttle': ['$Round'],
    'reset': ['$Convert'],
    'rename': ['$Convert'],
    'convert': ['$Convert'],
    'translate': ['$Convert'],
    'turn': ['$Convert'],
    'divide': ['$Convert'],
    'transform': ['$Convert'],
    'aggregate': ['$Convert'],
    'unpivot': ['$Convert'],
    'encode': ['$Convert'],
    'urlencode': ['$Convert'],
    'decode': ['$Convert'],
    'customize': ['$Convert'],
    'binarize': ['$Convert'],
    'inverse': ['$Convert'],
    'color': ['$Convert'],
    'resize': ['$Convert'],
    'autosize': ['$Convert'],
    'transformation': ['$Convert'],
    'editing': ['$Convert'],
    'compress': ['$Convert'],
    'hash': ['$Convert'],
    'decorate': ['$Convert'],
    'serialize': ['$Convert'],
    'wrap': ['$Convert'],
    'add': ['$Add'],
    'addition': ['$Add'],
    'format': ['$Add'],
    'formatting': ['$Add'],
    'insert': ['$Add'],
    'inserting': ['$Add'],
    'multiply': ['$Add'],
    'multiplication': ['$Add'],
    'average': ['$Add'],
    'share': ['$Add'],
    'integrate': ['$Add'],
    'increase': ['$Add'],
    'feed': ['$Add'],
    'code': ['$Add'],
    'improve': ['$Add'],
    'subclass': ['$Add'],
    'remove': ['$Remove'],
    'delete': ['$Remove'],
    'drop': ['$Remove'],
    'suppress': ['$Remove'],
    'dump': ['$Remove'],
    'disable': ['$Remove'],
    'kill': ['$Remove'],
    'exclude': ['$Remove'],
    'excluding': ['$Remove'],
    'terminate': ['$Remove'],
    'strip': ['$Remove'],
    'ignore': ['$Remove'],
    'exit': ['$Remove'],
    'erase': ['$Remove'],
    'reduce': ['$Remove'],
    'dereference': ['$Remove'],
    'disallow': ['$Remove'],
    'clear': ['$Remove'],
    'clean': ['$Remove'],
    'escape': ['$Remove'],
    'suppress': ['$Remove'],
    'close': ['$Remove'],
    'rollback': ['$Remove'],
    'abort': ['$Remove'],
    'pad': ['$Pad'],
    'map': ['$Map', '$Dict'],
    'unzip': ['$Map'],
    'unpack': ['$Map'],
    'unpacking': ['$Map'],
    'interpolate': ['$Map'],
    'reverse': ['$Map'],
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
    'rebuild': ['$Create'],
    'draw': ['$Create'],
    'programm': ['$Create'],
    'load': ['$Load'],
    'read': ['$Load'],
    'describe': ['$Load'],
    'crawl': ['$Load'],
    'repeat': ['$Load'],
    'indicate': ['$Load'],
    'unroll': ['$Load'],
    'grow': ['$Load'],
    'serve': ['$Load'],
    'know': ['$Load'],
    'shade': ['$Load'],
    'interact': ['$Load'],
    'pass': ['$Load'],
    'get': ['$Load'],
    'talk': ['$Load'],
    'build': ['$Load'],
    'apply': ['$Load'],
    'detect': ['$Load'],
    'animate': ['$Load'],
    'connect': ['$Load'],
    'select': ['$Load'],
    'upload': ['$Load'],
    'download': ['$Load'],
    'display': ['$Load'],
    'call': ['$Load'],
    'edit': ['$Load'],
    'sample': ['$Load'],
    'resample': ['$Load'],
    'throw': ['$Load'],
    # 'plot': ['$Load'],
    'access': ['$Load'],
    'use': ['$Load'],
    'control': ['$Load'],
    'take': ['$Load'],
    # 'count': ['$Load'],
    'choose': ['$Load'],
    'input': ['$Load'],
    'implement': ['$Load'],
    'reference': ['$Load'],
    'listen': ['$Load'],
    'blaze': ['$Load'],
    'extract': ['$Load'],
    'calculate': ['$Load'],
    'account': ['$Load'],
    'launch': ['$Load'],
    'stream': ['$Load'],
    'run': ['$Load'],
    'fill': ['$Load'],
    'derive': ['$Load'],
    'click': ['$Load'],
    'sum': ['$Load'],
    'subtract': ['$Load'],
    'explode': ['$Load'],
    'refer': ['$Load'],
    'use': ['$Load'],
    'compile': ['$Load'],
    'import': ['$Load'],
    'execute': ['$Load'],
    'redirect': ['$Load'],
    'retrieve': ['$Load'],
    'log': ['$Load'],
    'listing': ['$Load'],
    'capture': ['$Load'],
    'obtain': ['$Load'],
    'pull': ['$Load'],
    'grab': ['$Load'],
    'open': ['$Load'],
    'receive': ['$Load'],
    'send': ['$Load'],
    'fitting': ['$Load'],
    'sending': ['$Load'],
    'identify': ['$Load'],
    'animate': ['$Load'],
    'process': ['$Load'],
    'go': ['$Load'],
    'track': ['$Load'],
    'install': ['$Load'],
    'connect': ['$Load'],
    'perform': ['$Load'],
    'scroll': ['$Load'],
    'debug': ['$Load'],
    'fetch': ['$Load'],
    'handle': ['$Load'],
    'work': ['$Load'],
    'inherit': ['$Load'],
    'moderate': ['$Load'],
    'output': ['$Load'],
    'play': ['$Load'],
    'annotate': ['$Load'],
    'test': ['$Load'],
    'evaluate': ['$Load'],
    'visualize': ['$Load'],
    'simulate': ['$Load'],
    'login': ['$Load'],
    'solve': ['$Load'],
    'do': ['$Load'],
    # 'frame': ['$Load'],
    'save': ['$Save'],
    'submit': ['$Save'],
    'set': ['$Set', '$Save'],
    'compute': ['$Save'],
    'write': ['$Save'],
    'put': ['$Save'],
    'update': ['$Save'],
    'store': ['$Save'],
    'configure': ['$Save'],
    'export': ['$Save'],
    'keep': ['$Save'],
    'validate': ['$Save'],
    'preserve': ['$Save'],
    'pickle': ['$Save'],
    'print': ['$Print'],
    'show': ['$Print'],
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
    'bind': ['$Append'],
    'break': ['$Break'],
    'stop': ['$Break'],
    'continue': ['$Continue'],  # no examples found for continue
    'cont': ['$Continue'],
    'skip': ['$Continue'],
    'determine': ['$Compare'],
    'check': ['$Compare'],
    'see': ['$Compare'],
    'comp': ['$Compare'],
    'compare': ['$Compare'],
    'difference': ['$Compare'],
    'confuse': ['$Compare'],
    'normalize': ['$Parse'],
    'flatten': ['$Parse'],
    'parse': ['$Parse'],
    'assign': ['$Assign'],
    'assignment': ['$Assign'],
    'indexing': ['$Assign', '$Index'],
    'reorder': ['$Sort'],
    'reordering': ['$Sort'],
    'order': ['$Sort'],
    'ordered': ['$Sort'],
    'sort': ['$Sort'],
    'order': ['$Sort'],
    'contain': ['$Contain'],
    'match': ['$Match'],
    'matchable': ['$Match'],
    'move': ['$Replace'],
    'change': ['$Replace'],
    'replace': ['$Replace'],
    'substitute': ['$Replace'],
    'fix': ['$Replace'],
    'swap': ['$Replace'],
    'rotate': ['$Replace'],
    'modify': ['$Replace'],
    'switch': ['$Replace'],
    'uniqify': ['$Replace'],
    'shift': ['$Replace'],
    'override': ['$Replace'],
    'shuffle': ['$Replace'],

    # Conditions
    # 'exist': ['$Exist'],
    # 'if': ['$And', '$Exist'],
    # 'largest': ['$Largest'],
    # 'less than': ['$LT'],
    # 'smallest': ['$Smallest'],
    # 'greater than': ['$GT'],
    # 'equal': ['$EQ'],
    # 'equals': ['$EQ'],
    # 'all': ['$All'],
    # 'only': ['$Only'],
    # 'every': ['$All'],
    # 'none': ['$None', '$Not'],
    # 'but': ['$But'],

    # Prepositions
    'by': ['$By'],
    'in': ['$In'],
    'within': ['$In'],
    'inside': ['$In'],
    'into': ['$Into'],
    'to': ['$To'],
    'on': ['$On'],
    'for': ['$For'],
    'from': ['$From'],
    'as': ['$As'],
    'through': ['$Through'],
    'over': ['$Over'],
    'of': ['$Of'],
    'based on': ['$By'],
    'using': ['$With'],
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

    # $EQ => NP/NP {\\x.'@EQ'(x)}
    # $EQ => NP/PP {\\x.'@EQ'(x)}
    # $Largest => NP/NP {\\x.'@Largest'(x)}

    # Prepositions
    $In => PP/NP {\\x.'@In'(x)}
    $In => (NP\\NP)/NP {\\x y.'@In'(x, y)}
    $In => (NP/NP)\\NP {\\x y. '@In'(x, y)}

    $Into => PP/NP {\\x.'@Into'(x)}
    $Into => (PP/NP)/NP {\\x y.'@Into'(x, y)}
    $Into => (NP/NP)\\NP {\\x y. '@Into'(x, y)}

    $By => PP/NP {\\x.'@By'(x)}
    $By => (NP/NP)\\NP {\\x y.'@By'(x, y)}
    $By => S/S {\\x. x}
    $To => S/S {\\x. x}
    $To => PP/NP {\\x. '@To'(x)}
    $To => (NP/NP)\\NP {\\x y.'@To'(x, y)}
    $On => PP/NP {\\x. '@On'(x)}
    $On => (NP/NP)\\NP {\\x y.'@On'(x, y)}
    $For => PP/NP {\\x.'@For'(x)}
    $For => (NP/NP)\\NP {\\x y.'@For'(x, y)}
    $From => PP/NP {\\x.'@From'(x)}
    $From => PP/S {\\x.'@From'(x)}
    $From => (NP/NP)\\NP {\\x y.'@From'(x, y)}
    $With => PP/NP {\\x.'@With'(x)}
    $With => (NP/NP)\\NP {\\x y. '@With'(x, y)}
    $As => PP/NP {\\x. '@As'(x)}
    $As => (NP/NP)\\NP {\\x y.'@As'(x, y)}
    $Through => PP/NP {\\x. '@Through'(x)}
    $Over => PP/NP {\\x. '@Over'(x)}

    # $And => var\\.,var/.,var {\\y x.'@And'(x,y)}
    # $Or => var\\.,var/.,var {\\y x.'@Or'(x,y)}
    # $Not => S/NP {\\x. '@Not'(x)} # is used in and a lot
    # $Not => NP/NP {\\x. '@Not'(x)}
    # $Not => (NP/NP)\\NP {\\x y.'@Not'(x, y)}
    # $All => NP/NP {\\x. '@All'(x)}
    # $Exist => NP/NP {\\x. '@Exist'(x)}

    $Of => PP/NP {\\x. x}
    $Of => (NP/NP)\\NP {\\F x. F(x)}
    $Of => (NP\\NP)/NP {\\F x. F(x)}

    $But => var\\.,var/.,var {\\y x.'@But'(x,y)}

    $Find => S/NP {\\x.'@Find'(x)}
    $Find => (S/NP)/PP {\\y x.'@Find'(x, y)}
    $Find => (S/NP)/NP {\\y x.'@Find'(x, y)}

    $Return => NP/NP {\\x.'@Return'(x)}
    $Return => S/NP {\\x.'@Return'(x)}
    $Return => (S/NP)/PP {\\y x.'@Return'(x, y)}
    $Return => (S/NP)/NP {\\y x.'@Return'(x, y)}

    $Transform => S/NP {\\x. '@Transform'(x)}
    $Transform => S/PP {\\x. '@Transform'(x)}
    $Transform => (S/NP)/PP {\\y x. '@Transform'(x, y)}
    $Transform => (S/NP)/NP {\\y x. '@Transform'(x, y)}

    $Merge => S/NP {\\x. '@Merge'(x)}
    $Merge => (S/NP)/PP {\\y x. '@Merge'(x, y)}

    $Iterate => S/PP {\\x. '@Iterate'(x)}
    $Iterate => (S/NP)/PP {\\y x. '@Iterate'('@Desc'(x), y)}
    $Iterate => (S/NP)/NP {\\y x. '@Iterate'('@Desc'(x), y)}

    $Sort => S/NP {\\x. '@Sort'(x)}
    $Sort => S/PP {\\x. '@Sort'(x)}
    $Sort => (S/NP)/PP {\\y x. '@Sort'('@Desc'(x), y)}
    $Sort => (S/NP)/NP {\\y x. '@Sort'('@Desc'(x), y)}

    $Concatenate => S/NP {\\x. '@Concatenate'(x)} # can be also Merge
    $Concatenate => (S/NP)/PP  {\\x y. '@Concatenate'(x, y)} # can be also Merge
    $Concatenate => (S/NP)/NP  {\\x y. '@Concatenate'(x, y)} # can be also Merge

    $Split => S/NP {\\x. '@Split'(x)}
    $Split => S\\NP {\\x. '@Split'(x)}
    $Split => (S/NP)/PP {\\y x. '@Split'(x, y)}

    $Round => S/NP {\\x. '@Round'(x)}
    $Round => S/PP {\\x. '@Round'(x)}
    $Round => (S/NP)/PP {\\y x. '@Round'(x, y)}

    $Convert => S/PP {\\x. '@Convert'(x)}
    $Convert => S/NP {\\x. '@Convert'(x)}
    $Convert => (S/NP)/PP {\\y x. '@Convert'(x, y)}
    $Convert => (S/NP)/NP {\\y x. '@Convert'(x, y)}

    $Add => S/NP {\\x. '@Add'(x)}
    $Add => S/PP {\\x. '@Add'(x)}
    $Add => S\\NP {\\x. '@Add'(x)}
    $Add => (S/NP)/PP {\\y x. '@Add'(x, y)}
    $Add => (S/NP)/NP {\\y x. '@Add'(x, y)}

    $Remove => S/NP {\\x. '@Remove'(x)}
    $Remove => (S/NP)/PP {\\y x. '@Remove'(x, y)}
    $Remove => (S/NP)/NP {\\y x. '@Remove'(x, y)}

    $Map => (S/NP)/PP {\\y x. '@Map'(x, y)}

    $Create => NP/NP {\\x.'@Create'(x)}
    $Create => S/NP {\\x. '@Create'(x)}
    $Create => (S/NP)/PP {\\y x. '@Create'(x, y)}
    $Create => (S/NP)/NP {\\y x. '@Create'(x, y)}

    $Load => S/NP {\\x. '@Load'(x)}
    $Load => S/PP {\\x. '@Load'(x)}
    $Load => (S/NP)/PP {\\y x. '@Load'(x, y)}
    $Load => (S/NP)/NP {\\y x. '@Load'(x, y)}

    $Save => S/NP {\\x. '@Save'(x)}
    $Save => S/PP {\\x. '@Save'(x)}
    $Save => (S/NP)/PP {\\y x. '@Save'(x, y)}
    $Save => (S/NP)/NP {\\y x. '@Save'(x, y)}

    $Print => S/NP {\\x. '@Print'(x)}
    $Print => (S/NP)/PP {\\y x. '@Print'(x, y)}
    $Print => (S/NP)/NP {\\y x. '@Print'(x, y)}

    $Append => S/NP {\\x. '@Append'(x)}
    $Append => S/PP {\\x. '@Append'(x)}
    $Append => (S/NP)/PP {\\y x. '@Append'(x, y)}

    $Break => NP {'Break'}
    $Break => (S/NP)/PP {\\y x. '@Break'(x, y)}

    $Continue => S/NP {\\x. '@Continue'(x)}

    $Compare => S/NP {\\x. '@Compare'(x)}
    $Compare => S/PP {\\x. '@Compare'(x)}
    $Compare => (S/NP)/PP {\\y x. '@Compare'(x, y)}
    $Compare => (S/NP)/NP {\\y x. '@Compare'(x, y)}

    $Parse => S/NP {\\x. '@Parse'(x)}
    $Parse => (S/NP)/PP {\\y x. '@Parse'(x, y)}
    $Parse => (S/NP)/NP {\\y x. '@Parse'(x, y)}

    $Assign => (S/NP)/PP {\\y x. '@Assign'(x, y)}

    $Replace => S/NP {\\x. '@Replace'(x)}
    $Replace => S\\NP {\\x. '@Replace'(x)}
    $Replace => (S/NP)/PP {\\y x. '@Replace'(x, y)}
    $Replace => (S/NP)/NP {\\y x. '@Replace'(x, y)}

    $Contain => NP/NP {\\x. '@Contain'(x)} # as it is used with other verbs
    $Contain => (S/NP)/PP {\\y x. '@Contain'(x, y)}

    $Match => S/NP {\\x. '@Match'(x)}
    $Match => (S/NP)/PP {\\y x. '@Match'(x, y)}
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
