POTENTIAL_FUTURE_PREDICATES = [
    "Number -> count",
    "Count -> count",
    "Edit",
    "Move",
    "Tuple",
    "Duplicate -> Check[EQ]",
    "Output",
    "that -> and",
]


# Everything that is defined in this dictionary MUST have corresponding rules in RAW_LEXICONE, or the parse will fail.
STRING2PREDICATE = {
    "dict": ["$Dict"],
    "dicts": ["$Dict"],
    "dictionary": ["$Dict"],
    "dictionaries": ["$Dict"],
    "int": ["$Int"],
    "integer": ["$Int"],
    "integers": ["$Int"],
    "array": ["$List"],
    "arrays": ["$List"],
    "list": ["$List"],
    "lists": ["$List"],
    "tuple": ["$Tuple"],
    "tuples": ["$Tuple"],
    "array": ["$List"],
    "string": ["$String"],
    "strings": ["$String"],
    "str": ["$String"],
    "file": ["$File"],
    "files": ["$File"],
    "loop": ["$Loop"],
    "for loop": ["$Loop"],
    "enum": ["$Enum"],
    "enumerate": ["$Enum"],
    "bool": ["$Bool"],
    "boolean": ["$Bool"],
    "char": ["$Char"],
    "character": ["$Char"],
    "characters": ["$Char"],
    "unicode": ["$Char"],
    "path": ["$Path"],
    "dir": ["$Path"],
    "directory": ["$Path"],
    "class": ["$Class"],
    "object": ["$Class"],
    "objects": ["$Class"],
    "member": ["$Class"],
    "func": ["$Func"],
    "function": ["$Func"],
    "method": ["$Func"],
    "index": ["$Index"],
    "id": ["$Index"],
    "regex": ["$Regex"],
    "column": ["$Column"],
    "columns": ["$Column"],
    "number": ["$Number"],
    "numbers": ["$Number"],
    "null": ["$Null"],
    "nulls": ["$Null"],
    "nan": ["$Null"],

    # det-s
    "the": ["$The"],
    "an": ["$The"],
    "a": ["$The"],

    # conjunctions
    "and": ["$And"],
    # "that": ["$And"],
    # "then": ["$And"],
    # "both": ["$And"],
    # "too": ["$And"],
    # "also": ["$And"],
    "including": ["$And"],
    "or": ["$Or"],
    "else": ["$Or"],
    # "rather": ["$Or"],
    # "either": ["$Or"],
    "not": ["$Not"],
    "non": ["$Not"],
    "none": ["$Not"],
    "nothing": ["$Not"],
    "never": ["$Not"],
    # "without": ["$Without"],

    # Transforming verbs
    "find": ["$Find"],
    "locate": ["$Find"],
    "locating": ["$Find"],
    "calcuate": ["$Find"],
    "search": ["$Find"],
    "searching": ["$Find"],
    "filter": ["$Find"],
    "filtering": ["$Find"],
    "extract": ["$Find"],
    # "find if": ["$Check"]
    # "find out": ["$Return"]?
    # kind of the same as "get"? return smth [from smth/smwh]
    "return": ["$Return"],
    "fallback": ["$Return"],
    # merge smth-s into smth; merge smth-s; merge smth with smth; merge in NP[e.g. merge sort]
    "merge": ["$Merge"],
    "merging": ["$Merge"],
    "join": ["$Merge"],
    "joining": ["$Merge"],
    "coalesce": ["$Merge"],
    "group": ["$Merge"],
    "grouping": ["$Merge"],
    "concat": ["$Concatenate"],
    "concatenate": ["$Concatenate"],
    "concatenation": ["$Concatenate"],
    "append": ["$Concatenate"],
    "combine": ["$Concatenate"],
    "combinate": ["$Concatenate"],
    "zip": ["$Concatenate"],
    "slice": ["$Split"],
    "slicing": ["$Split"],
    "split": ["$Split"],
    "round": ["$Round"],
    "rounding": ["$Round"],
    "limiting": ["$Round"],
    "reset": ["$Convert"],
    "rename": ["$Convert"],
    "convert": ["$Convert"],
    "converting": ["$Convert"],
    "translate": ["$Convert"],
    "turn": ["$Convert"],
    "turning": ["$Convert"],
    "divide": ["$Convert"],
    "transform": ["$Convert"],
    "transforming": ["$Convert"],
    "aggregate": ["$Convert"],
    "unpivot": ["$Convert"],
    "add": ["$Add"],
    "addition": ["$Add"],
    "adding": ["$Add"],
    "format": ["$Add"],
    "formatting": ["$Add"],
    "insert": ["$Add"],
    "inserting": ["$Add"],
    "multiply": ["$Add"],
    "multiplying": ["$Add"],
    "average": ["$Add"],
    "averaging": ["$Add"],
    "increase": ["$Add"],
    "remove": ["$Remove"],
    "delete": ["$Remove"],
    "deleting": ["$Remove"],
    "drop": ["$Remove"],
    "droping": ["$Remove"],
    "dropping": ["$Remove"],
    "dump": ["$Remove"],
    "dumping": ["$Remove"],
    "disable": ["$Remove"],
    "kill": ["$Remove"],
    "exclude": ["$Remove"],
    "excluding": ["$Remove"],
    "terminate": ["$Remove"],
    "strip": ["$Remove"],
    "ignore": ["$Remove"],
    "pad": ["$Pad"],
    "map": ["$Map", "$Dict"],
    "unzip": ["$Map"],
    "unpack": ["$Map"],
    "unpacking": ["$Map"],
    "reverse": ["$Map"],
    "create": ["$Create"],
    "creating": ["$Create"],
    "created": ["$Create"],
    "generate": ["$Create"],
    "initialize": ["$Create"],
    "init": ["$Create"],
    "declare": ["$Create"],
    "define": ["$Create"],
    "copy": ["$Create"],
    "make": ["$Create"],
    "making": ["$Create"],
    "construct": ["$Create"],
    "load": ["$Load"],
    "read": ["$Load"],
    "reading": ["$Load"],
    "pass": ["$Load"],
    "passing": ["$Load"],
    "get": ["$Load"],
    "getting": ["$Load"],
    "apply": ["$Load"],
    "detect": ["$Load"],
    "select": ["$Load"],
    "selected": ["$Load"],
    "upload": ["$Load"],
    "download": ["$Load"],
    "display": ["$Load"],
    "displaying": ["$Load"],
    "call": ["$Load"],
    "calling": ["$Load"],
    "sample": ["$Load"],
    "sampling": ["$Load"],
    "resample": ["$Load"],
    "plot": ["$Load"],
    "plotting": ["$Load"],
    "access": ["$Load"],
    "accessing": ["$Load"],
    "use": ["$Load"],
    "control": ["$Load"],
    "take": ["$Load"],
    "taking": ["$Load"],
    "count": ["$Load"],
    "choose": ["$Load"],
    "extract": ["$Load"],
    "extracting": ["$Load"],
    "calculate": ["$Load"],
    "account": ["$Load"],
    "run": ["$Load"],
    "fill": ["$Load"],
    "count": ["$Load"],
    "counting": ["$Load"],
    "derive": ["$Load"],
    "click": ["$Load"],
    "sum": ["$Load"],
    "subtract": ["$Load"],
    "exploding": ["$Load"],
    "refer": ["$Load"],
    "use": ["$Load"],
    "using": ["$Load"],
    "compile": ["$Load"],
    "import": ["$Load"],
    "importing": ["$Load"],
    "execute": ["$Load"],
    "redirect": ["$Load"],
    "retrieve": ["$Load"],
    "retrieving": ["$Load"],
    "listing": ["$Load"],
    "capture": ["$Load"],
    "capturing": ["$Load"],
    "obtain": ["$Load"],
    "pull": ["$Load"],
    "grab": ["$Load"],
    "open": ["$Load"],
    "send": ["$Load"],
    "sending": ["$Load"],
    "identify": ["$Load"],
    "identifying": ["$Load"],
    "go": ["$Load"],
    "work": ["$Load"],
    "save": ["$Save"],
    "saved": ["$Save"],
    "saving": ["$Save"],
    "set": ["$Set", "$Save"],
    "setting": ["$Save"],
    "write": ["$Save"],
    "writing": ["$Save"],
    "update": ["$Save"],
    "updating": ["$Save"],
    "keep": ["$Save"],
    "print": ["$Print"],
    "show": ["$Print"],
    "repeat": ["$Iterate"],
    "iterate": ["$Iterate"],
    "iter": ["$Iterate"],
    "iterator": ["$Iterate"],
    "iterators": ["$Iterate"],
    "iterating": ["$Iterate"],
    "loop": ["$Iterate"],
    # "it": ["$Iterate"],
    "extend": ["$Append"],
    "append": ["$Append"],
    "prepend": ["$Append"],
    "appending": ["$Append"],
    "pad": ["$Append"],
    "padding": ["$Append"],
    "break": ["$Break"],
    "continue": ["$Continue"],  # no examples found for continue
    "cont": ["$Continue"],
    "skip": ["$Continue"],
    "followed": ["$Continue"],
    "determine": ["$Compare"],
    "check": ["$Compare"],
    "comp": ["$Compare"],
    "compare": ["$Compare"],
    "normalizing": ["$Parse"],
    "normalize": ["$Parse"],
    "flatten": ["$Parse"],
    "parse": ["$Parse"],
    "assign": ["$Assign"],
    "assignment": ["$Assign"],
    "assigning": ["$Assign"],
    "indexing": ["$Assign", "$Index"],
    "reorder": ["$Sort"],
    "reordering": ["$Sort"],
    "order": ["$Sort"],
    "ordered": ["$Sort"],
    "sort": ["$Sort"],
    "order": ["$Sort"],
    "contain": ["$Contain"],
    "match": ["$Match"],
    "matched": ["$Match"],
    "matchable": ["$Match"],
    "matches": ["$Match"],
    "matching": ["$Match"],
    "move": ["$Replace"],
    "change": ["$Replace"],
    "changing": ["$Replace"],
    "replace": ["$Replace"],
    "replacement": ["$Replace"],
    "substitute": ["$Replace"],
    "swap": ["$Replace"],

    # Conditions
    "exist": ["$Exist"],
    "exists": ["$Exist"],
    # "if": ["$And", "$Exist"],
    "largest": ["$Largest"],
    "less than": ["$LT"],
    "smallest": ["$Smallest"],
    "greater than": ["$GT"],
    "equal": ["$EQ"],
    "equals": ["$EQ"],
    "all": ["$All"],
    # "only": ["$Only"],
    "every": ["$All"],
    "none": ["$None", "$Not"],

    # Prepositions
    "by": ["$By"],
    "in": ["$In"],
    "within": ["$In"],
    "inside": ["$In"],
    "into": ["$Into"],
    "to": ["$To"],
    "on": ["$On"],
    "for": ["$For"],
    "from": ["$From"],
    "as": ["$As"],
    "through": ["$Through"],
    "over": ["$Over"],
    "of": ["$Of"],
    "based on": ["$By"],
    "using": ["$With"],
    "with": ["$With"],
    "with the help of": ["$With"],
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

    $EQ => NP/NP {\\x.'@EQ'(x)}
    $EQ => NP/PP {\\x.'@EQ'(x)}

    # Prepositions
    $In => PP/NP {\\x.'@In'(x)}
    $In => (NP/NP)\\NP {\\x y. '@In'(x, y)}

    $Into => PP/NP {\\x.'@Into'(x)}
    # $Into => (PP/NP)/NP {\\x y.'@Into'(x, y)}
    $Into => (NP/NP)\\NP {\\x y. '@Into'(x, y)}

    $By => PP/NP {\\x.'@By'(x)}
    $By => S/S {\\x. x}
    $To => S/S {\\x. x}
    $To => PP/NP {\\x. '@To'(x)}
    $To => (PP/NP)/NP {\\x y.'@To'(x, y)}
    $On => PP/NP {\\x. '@On'(x)}
    $On => (NP/NP)\\NP {\\x y.'@On'(x, y)}
    $For => PP/NP {\\x.'@For'(x)}
    $For => (NP/NP)\\NP {\\x y.'@For'(x, y)}
    $From => PP/NP {\\x.'@From'(x)}
    $From => (NP/NP)\\NP {\\x y.'@From'(x, y)}
    # $From => (PP/NP)/NP {\\x y.'@From'(x, y)}
    $With => PP/NP {\\x.'@With'(x)}
    $With => (NP/NP)\\NP {\\x y. '@With'(x, y)}
    $As => PP/NP {\\x. '@As'(x)}
    $As => (NP/NP)\\NP {\\x y.'@As'(x, y)}
    $Through => PP/NP {\\x. '@Through'(x)}
    $Over => PP/NP {\\x. '@Over'(x)}

    $And => var\\.,var/.,var {\\y x.'@And'(x,y)}
    $Or => var\\.,var/.,var {\\y x.'@Or'(x,y)}
    $Not => S/NP {\\x. '@Not'(x)} # is used in and a lot
    $Not => NP/NP {\\x. '@Not'(x)}
    $All => NP/NP {\\x. '@All'(x)}
    $Exist => NP/NP {\\x. '@Exist'(x)}

    $Of => PP/NP {\\x. x}
    $Of => (NP/NP)\\NP {\\F x. F(x)}

    $Find => S/NP {\\x.'@Find'(x)}
    # $Find => S/PP {\\x.'@Find'(x)}
    $Find => (S/NP)/PP {\\y x.'@Find'(x, y)}
    # $Find => (S/NP)/S {\\y x.'@Find'(x, y)}
    # $Find => (S/PP)/PP {\\y x.'@Find'(x, y)}

    $Return => NP/NP {\\x.'@Return'(x)}
    $Return => S/NP {\\x.'@Return'(x)}
    $Return => (S/NP)/PP {\\y x.'@Return'('@Desc'(x), y)}

    $Transform => (S/NP)/NP {\\x y.'@Transform'(x, y)}.
    $Merge => NP {'Merge'}
    $Merge => S/NP {\\x. '@Merge'(x)}
    $Merge => (S/NP)/PP {\\y x. '@Merge'('@Desc'(x), y)}

    $Iterate => NP {'Iterator'}
    $Iterate => S/PP {\\x. '@Iterate'(x)}
    $Iterate => (S/NP)/PP {\\y x. '@Iterate'('@Desc'(x), y)}

    $Sort => NP {'Order'}
    $Sort => S/NP {\\x. '@Sort'(x)}
    $Sort => S/PP {\\x. '@Sort'(x)}
    $Sort => (S/NP)/PP {\\y x. '@Sort'('@Desc'(x), y)}

    $Concatenate => S/NP {\\x. '@Concatenate'(x)} # can be also Merge
    $Concatenate => S/NP/PP {\\x y. '@Concatenate'(x, y)} # can be also Merge

    $Split => S/NP {\\x. '@Split'(x)}
    $Split => (S/NP)/PP {\\y x. '@Split'('@Desc'(x), y)}

    $Round => S/NP {\\x. '@Round'(x)}
    $Round => (S/NP)/PP {\\y x. '@Round'('@Desc'(x), y)}

    $Convert => (S/NP)/PP {\\y x. '@Convert'('@Desc'(x), y)}

    $Add => NP {'Add'}
    $Add => S/NP {\\x. '@Add'(x)}
    $Add => (S/NP)/PP {\\y x. '@Add'('@Desc'(x), y)}

    $Remove => S/NP {\\x. '@Remove'(x)}
    $Remove => (S/NP)/PP {\\y x. '@Remove'('@Desc'(x), y)}

    $Map => (S/NP)/PP {\\y x. '@Map'('@Desc'(x), y)}

    $Create => NP/NP {\\x.'@Create'(x)}
    $Create => S/NP {\\x. '@Create'(x)}
    $Create => (S/NP)/PP {\\y x. '@Create'('@Desc'(x), y)}

    $Load => S/NP {\\x. '@Load'(x)}
    $Load => S/PP {\\x. '@Load'(x)}
    $Load => (S/NP)/PP {\\y x. '@Load'('@Desc'(x), y)}

    $Save => NP {'Save'}
    $Save => S/NP {\\x. '@Save'(x)}
    $Save => (S/NP)/PP {\\y x. '@Save'('@Desc'(x), y)}

    $Print => NP {'Print'}
    $Print => S/NP {\\x. '@Print'(x)}
    $Print => (S/NP)/PP {\\y x. '@Print'('@Desc'(x), y)}

    $Append => NP {'Append'}
    $Append => S/NP {\\x. '@Append'(x)}
    $Append => S/PP {\\x. '@Append'(x)}
    $Append => (S/NP)/PP {\\y x. '@Append'('@Desc'(x), y)}

    $Break => NP {'Break'}
    $Continue => S/NP {\\x. '@Continue'(x)}

    $Compare => NP {'Check'} #if compare is not used as NP, will use this
    $Compare => S/NP {\\x. '@Compare'(x)}
    $Compare => S/PP {\\x. '@Compare'(x)}
    $Compare => (S/NP)/PP {\\y x. '@Compare'('@Desc'(x), y)}

    $Parse => S/NP {\\x. '@Parse'(x)}
    $Parse => (S/NP)/PP {\\y x. '@Parse'('@Desc'(x), y)}

    $Assign => NP {'Assignment'}
    $Assign => (S/NP)/PP {\\y x. '@Assign'('@Desc'(y), x)}

    $Replace => S/NP {\\x. '@Replace'(x)}
    $Replace => (S/NP)/PP {\\y x. '@Replace'('@Desc'(x), y)}

    $Contain => NP/NP {\\x. '@Contain'(x)} # as it is used with other verbs
    $Contain => (S/NP)/PP {\\y x. '@Contain'('@Desc'(x), y)}

    $Match => NP {'Match'}
    $Match => S/NP {\\x. '@Match'(x)}
    $Match => (S/NP)/PP {\\y x. '@Match'('@Desc'(x), y)}
'''

QUESTION_WORDS = [
    ["how", "to"],
    ['how', 'do', 'i'], ['how', 'would', 'i'], ['how', 'should', 'i'],
    ['how', 'i', 'would'], ['how', 'i', 'should'],
    ['how', 'can', 'i'], ['can', 'i'], ['how', 'i', 'can'],
    ['how', 'do', 'we'], ['how', 'would', 'we'],
    ['how', 'should', 'we'], ['how', 'we', 'would'],
    ['how', 'we', 'should'],
    ['how', 'can', 'we'], ['can', 'we'], ['how', 'we', 'can'],
    ['how', 'do', 'you'], ['how', 'would', 'you'],
    ['how', 'should', 'you'], ['how', 'you', 'would'],
    ['how', 'you', 'should'],
    ['how', 'can', 'you'], ['can', 'you'], ['how', 'you', 'can'],
    ['how', 'does', 'one'], ['how', 'would', 'one'],
    ['how', 'should', 'one'], ['how', 'one', 'would'],
    ['how', 'one', 'should'],
    ['how', 'can', 'one'], ['can', 'one'], ['how', 'one', 'can'],
    ['cannot'], ["can't"], ['can', 'not'],
    ['is', 'there'], ['are', 'there'], ['is', 'it', 'possible', 'to'],
]

PYTHON_WORDS = [
    ["in", "python"], ["with", "python"],
    ["using", "python"], ["into", "python"],
]
