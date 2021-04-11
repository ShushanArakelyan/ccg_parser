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
    "nothing": ["$Not"],
    "never": ["$Not"],
    # "without": ["$Without"],

    # Transforming verbs
    "find": ["$Find"],
    "finding": ["$Find"],
    "locate": ["$Find"],
    "locating": ["$Find"],
    "calcuate": ["$Find"],
    "search": ["$Find"],
    "searching": ["$Find"],
    "filter": ["$Find"],
    "filtering": ["$Find"],
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
    "concatenating": ["$Concatenate"],
    "concatenation": ["$Concatenate"],
    "combine": ["$Concatenate"],
    "combinate": ["$Concatenate"],
    "zip": ["$Concatenate"],
    "slice": ["$Split"],
    "slicing": ["$Split"],
    "split": ["$Split"],
    "splitting": ["$Split"],
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
    "removing": ["$Remove"],
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
    "create": ["$Create"],
    "creating": ["$Create"],
    "created": ["$Create"],
    "generate": ["$Create"],
    "initialize": ["$Create"],
    "init": ["$Create"],
    "declare": ["$Create"],
    "define": ["$Create"],
    "copy": ["$Create"],
    "copying": ["$Create"],
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
    "selecting": ["$Load"],
    "upload": ["$Load"],
    "download": ["$Load"],
    "downloading": ["$Load"],
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
    "set": ["$Save", "$Set"],
    "setting": ["$Save"],
    "write": ["$Save"],
    "writing": ["$Save"],
    "update": ["$Save"],
    "updating": ["$Save"],
    "keep": ["$Save"],
    "print": ["$Print"],
    "printing": ["$Print"],
    "show": ["$Print"],
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
    "breaks": ["$Break"],
    "continue": ["$Continue"], # no examples found for continue
    "cont": ["$Continue"],
    "skip": ["$Continue"],
    "followed": ["$Continue"],
    "determine": ["$Compare"],
    "check": ["$Compare"],
    "checking": ["$Compare"],
    "comp": ["$Compare"],
    "comparing": ["$Compare"],
    "compare": ["$Compare"],
    "normalizing": ["$Parse"],
    "normalize": ["$Parse"],
    "flatten": ["$Parse"],
    "parse": ["$Parse"],
    "parsing": ["$Parse"],
    "assign": ["$Assign"],
    "assignment": ["$Assign"],
    "assigning": ["$Assign"],
    "indexing": ["$Assign", "$Index"],
    "reorder": ["$Sort"],
    "reordering": ["$Sort"],
    "order": ["$Sort"],
    "ordered": ["$Sort"],
    "sort": ["$Sort"],
    # "sorted": ["$Sort"],
    "sorting": ["$Sort"],
    "contain": ["$Contain"],
    "contained": ["$Contain"],
    "contains": ["$Contain"],
    "containing": ["$Contain"],
    "match": ["$Match"],
    "matched": ["$Match"],
    "matchable": ["$Match"],
    "matches": ["$Match"],
    "matching": ["$Match"],
    "move": ["$Replace"],
    "change": ["$Replace"],
    "changing": ["$Replace"],
    "replace": ["$Replace"],
    "replacing": ["$Replace"],
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
    # "only": ["$Only"],
    # "all": ["$All", "$And"],
    # "every": ["$All"],
    "none": ["$None", "$Not"],

    # Prepositions
    "by": ["$By"],
    "in": ["$In"],
    "into": ["$Into"],
    "to": ["$To"],
    "on": ["$On"],
    "for": ["$For"],
    "from": ["$From"],
    "with": ["$With"],
    "as": ["$As"],
    "through": ["$Through"],
    "over": ["$Over"],
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
    $Number => N {'Number'}
    $Number => NP {'Number'}
    $Set => N {'Set'}
    $Set => NP {'Set'}

    $EQ => NP/NP {\\x.'@EQ'(x)}


    $In => PP/NP {\\x.'@In'(x)}
    $Into => PP/NP {\\x.'@Into'(x)}
    $Into => (PP/NP)/NP {\\x y.'@Into'(x, y)}
    $By => PP/NP {\\x.'@By'(x)}
    $By => (PP/NP)/NP {\\x y.'@By'(x, y)}
    $By => PP/S {\\x.'@By'(x)}
    $To => PP/NP {\\x. '@To'(x)}
    $To => PP/S {\\x. '@To'(x)}
    $To => (PP/NP)/NP {\\x y.'@To'(x, y)}
    $On => PP/NP {\\x. '@On'(x)}
    $On => (PP/NP)/NP {\\x y.'@On'(x, y)}
    $For => PP/NP {\\x.'@For'(x)}
    $For => (PP/NP)/NP {\\x y.'@For'(x, y)}
    $From => PP/NP {\\x.'@From'(x)}
    $From => (PP/NP)/NP {\\x y.'@From'(x, y)}
    $With => PP/NP {\\x.'@With'(x)}
    $With => (PP/NP)/NP {\\x y.'@With'(x, y)}
    $As => PP/NP {\\x. '@As'(x)}
    $As => (PP/NP)/NP {\\x y.'@As'(x, y)}
    $Through => PP/NP {\\x. '@Through'(x)}
    $Over => PP/NP {\\x. '@Over'(x)}

    $And => var\\.,var/.,var {\\y x.'@And'(x,y)}
    $Or => var\\.,var/.,var {\\y x.'@Or'(x,y)}
    $Not => S/NP {\\x. '@Not'(x)} # is used in and a lot
    $Not => NP/NP {\\x. '@Not'(x)}
    $Exist => NP/NP {\\x. '@Exist'(x)}

    $Find => S/NP {\\x.'@Find'(x)}
    $Find => (S\\NP)/NP {\\y x.'@Find'('@Desc'(x), y)}
    $Find => (S/NP)/NP {\\y x.'@Find'('@Desc'(x), y)}
    $Find => (S/NP)/PP {\\y x.'@Find'('@Desc'(x), y)}
    $Find => (S\\PP\\PP)/PP {\\y x z.'@Find'('@Desc'(x), y, z)}
    $Find => (S/NP)/PP/NP {\\y x z. '@Find'('@Desc'(y), z, x)}
    $Find => (S/PP)/PP/NP {\\y x z. '@Find'('@Desc'(y), z, x)}
    $Find => (S/PP)/NP/NP/NP {\\y x z k. '@Find'('@Desc'(y), x, z, k)}'
    $Return => S/NP {\\x.'@Return'(x)}
    $Return => (S/NP)/NP {\\y x.'@Return'('@Desc'(x), y)}
    $Return => (S/NP)/NP/NP {\\y x z.'@Return'('@Desc'(x), y, z)}
    $Return => (S/NP)/PP/NP {\\y x z.'@Return'('@Desc'(x), y, z)}
    $Return => (S/PP)/PP/PP {\\y x z.'@Return'('@Desc'(x), y, z)}
    $Return => (S/PP)/PP/NP/NP {\\y x z k. '@Return'('@Desc'(y), x, z, k)}'
    $Transform => (S/NP)/NP {\\x y.'@Transform'(x, y)}.
    $Merge => NP {'Merge'}
    $Merge => S/NP {\\x. '@Merge'(x)}
    $Merge => (S\\NP)/NP {\\y x. '@Merge'('@Desc'(x), y)}
    $Merge => (S/NP)/NP {\\y x. '@Merge'('@Desc'(x), y)}
    $Merge => (S/NP)/PP {\\y x. '@Merge'('@Desc'(x), y)}
    $Merge => (S/NP)/NP/NP {\\y x z. '@Merge'('@Desc'(y), z, x)}
    $Merge => (S/NP)/PP/NP {\\y x z. '@Merge'('@Desc'(y), z, x)}'
    $Merge => (S/PP)/PP/NP {\\y x z. '@Merge'('@Desc'(y), z, x)}'
    $Iterate => NP {'Iterator'}
    $Iterate => S/NP {\\x. '@Iterate'(x)}
    $Iterate => S/PP {\\x. '@Iterate'(x)}
    $Iterate => (S/NP)/NP {\\y x. '@Iterate'('@Desc'(x), y)}
    $Iterate => (S/NP)/PP {\\y x. '@Iterate'('@Desc'(x), y)}
    $Iterate => (S/PP)/PP {\\y x. '@Iterate'('@Desc'(y), x)}
    $Sort => NP {'Order'}
    $Sort => S/NP {\\x. '@Sort'(x)}
    $Sort => S/PP {\\x. '@Sort'(x)}
    $Sort => (S/NP)/NP {\\y x. '@Sort'('@Desc'(x), y)}
    $Sort => (S/NP)/PP {\\y x. '@Sort'('@Desc'(x), y)}
    $Sort => (S\\NP)/NP {\\y x. '@Sort'('@Desc'(x), y)}
    $Sort => (S/NP)/NP/NP {\\y x z. '@Sort'('@Desc'(x), y)}
    $Sort => (S/NP)/PP/NP {\\y x z. '@Sort'('@Desc'(y), x, z)}
    $Sort => (S/PP)/PP/NP {\\y x z. '@Sort'('@Desc'(y), x, z)}
    $Sort => (S/PP)/PP/NP/NP {\\y x z k. '@Sort'('@Desc'(y), x, z, k)}'
    $Sort => (S/PP)/NP/NP/NP {\\y x z k. '@Sort'('@Desc'(y), x, z, k)}'
    $Concatenate => S/NP {\\x. '@Concatenate'(x)} # can be also Merge
    $Concatenate => S/NP/NP {\\x y. '@Concatenate'(x, y)} # can be also Merge
    $Concatenate => S/NP/PP {\\x y. '@Concatenate'(x, y)} # can be also Merge
    $Concatenate => (S/NP)/PP/NP {\\y x z. '@Concatenate'('@Desc'(y), z, x)}
    $Concatenate => (S/PP)/PP/NP {\\y x z. '@Concatenate'('@Desc'(y), z, x)}
    $Split => S/NP {\\x. '@Split'(x)}
    $Split => (S/NP)/NP {\\y x. '@Split'('@Desc'(x), y)}
    $Split => (S\\NP)/NP {\\y x. '@Split'('@Desc'(x), y)}
    $Split => (S/NP)/PP {\\y x. '@Split'('@Desc'(x), y)}
    $Split => (S/PP)/PP {\\y x. '@Split'('@Desc'(x), y)}
    $Split => (S/NP)/PP/NP {\\y x z. '@Split'('@Desc'(y), z, x)}
    $Split => (S/PP)/PP/NP {\\y x z. '@Split'('@Desc'(y), z, x)}
    $Split => (S/PP)/PP/NP/NP {\\y x z k. '@Split'('@Desc'(y), x, z, k)}'
    $Round => S/NP {\\x. '@Round'(x)}
    $Round => (S/NP)/NP {\\y x. '@Round'('@Desc'(x), y)}
    $Round => (S/NP)/PP {\\y x. '@Round'('@Desc'(x), y)}
    $Convert => (S/NP)/NP {\\y x. '@Convert'('@Desc'(x), y)}
    $Convert => (S/NP)/NP/NP {\\y x z. '@Convert'('@Desc'(x), y, z)}
    $Convert => (S/NP)/PP {\\y x. '@Convert'('@Desc'(x), y)}
    $Convert => (S\\NP)/PP {\\y x. '@Convert'('@Desc'(x), y)}
    $Convert => (S/NP)/PP/NP {\\y x z. '@Convert'('@Desc'(y), z, x)}
    $Convert => (S/PP)/PP/NP {\\y x z. '@Convert'('@Desc'(y), z, x)}
    $Convert => (S/PP)/PP/NP/NP {\\y x z k. '@Convert'('@Desc'(y), x, z, k)}'
    $Convert => (S/PP)/PP/PP/NP {\\y x z k. '@Convert'('@Desc'(y), x, z, k)}'
    $Convert => (S\\PP)/PP/PP/NP {\\y x z k. '@Convert'('@Desc'(y), x, z, k)}'
    $Add => NP {'Add'}
    $Add => S/NP {\\x. '@Add'(x)}
    $Add => (S/NP)/NP {\\y x. '@Add'('@Desc'(x), y)}
    $Add => (S/NP)/PP {\\y x. '@Add'('@Desc'(x), y)}
    $Add => (S\\NP)/NP {\\y x. '@Add'('@Desc'(x), y)}
    $Add => (S\\NP)/NP/NP {\\y x z. '@Add'('@Desc'(x), y, z)}
    $Add => (S/NP)/NP/NP {\\y x z. '@Add'('@Desc'(x), y, z)}
    $Add => (S/NP)/PP/NP {\\y x z. '@Add'('@Desc'(y), z, x)}
    $Add => (S/PP)/PP/NP {\\y x z. '@Add'('@Desc'(y), z, x)}
    $Add => (S/PP)/PP/NP/NP {\\y x z k. '@Add'('@Desc'(y), x, z, k)}'
    $Add => (S/PP)/PP/PP/NP {\\y x z k. '@Add'('@Desc'(y), x, z, k)}'
    $Add => (S/PP)/NP/PP/NP {\\y x z k. '@Add'('@Desc'(y), z, x, k)}'
    $Add => (S/PP)/NP/PP/NP {\\y x z k. '@Add'('@Desc'(y), z, x, k)}'
    $Remove => S/NP {\\x. '@Remove'(x)}
    $Remove => (S/NP)/NP {\\y x. '@Remove'('@Desc'(x), y)}
    $Remove => (S/NP)/PP {\\y x. '@Remove'('@Desc'(x), y)}
    $Remove => (S\\NP)/NP {\\y x. '@Remove'('@Desc'(x), y)}
    $Remove => (S/NP)/NP/NP {\\y x z. '@Remove'('@Desc'(x), y, z)}
    $Remove => (S/NP)/PP/NP {\\y x z. '@Remove'('@Desc'(y), z, x)}
    $Remove => (S/PP)/PP/NP {\\y x z. '@Remove'('@Desc'(y), z, x)}
    $Remove => (S/PP)/PP/NP/NP {\\y x z k. '@Remove'('@Desc'(y), z, x, k)}'
    $Remove => (S/PP)/PP/PP/NP {\\y x z k. '@Remove'('@Desc'(y), z, x, k)}'
    $Map => (S/NP)/NP {\\y x. '@Map'('@Desc'(x), y)}
    $Map => (S/NP)/PP {\\y x. '@Map'('@Desc'(x), y)}
    $Map => (S/NP)/PP/NP {\\y x z. '@Map'('@Desc'(y), z, x)}
    $Map => (S/PP)/PP/NP {\\y x z. '@Map'('@Desc'(y), z, x)}
    $Create => NP/NP {\\x.'@Create'(x)}
    $Create => NP\\NP {\\x.'@Create'(x)}
    $Create => S/NP {\\x. '@Create'(x)}
    $Create => (S/NP)/NP {\\y x. '@Create'('@Desc'(x), y)}
    $Create => (S/NP)/PP {\\y x. '@Create'('@Desc'(x), y)}
    $Create => (S\\NP)/NP {\\y x. '@Create'('@Desc'(x), y)}
    $Create => (S/NP)/PP/NP {\\y x z. '@Create'('@Desc'(y), z, x)}
    $Create => (S/PP)/PP/NP {\\y x z. '@Create'('@Desc'(y), z, x)}
    $Create => (S/PP)/PP/PP/NP {\\y x z k. '@Create'('@Desc'(y), x, z, k)}'
    $Create => (S/PP)/NP/NP/NP {\\y x z k. '@Create'('@Desc'(y), x, z, k)}'
    $Load => NP\\NP {\\x.'@Load'(x)}
    $Load => S/NP {\\x. '@Load'(x)}
    $Load => S/PP {\\x. '@Load'(x)}
    $Load => S\\NP {\\x. '@Load'(x)} # for nouns that come before
    $Load => (S/NP)/NP {\\y x. '@Load'('@Desc'(x), y)}
    $Load => (S/NP)/PP {\\y x. '@Load'('@Desc'(x), y)}
    $Load => (S/PP)/PP {\\y x. '@Load'('@Desc'(x), y)}
    $Load => (S\\NP)/PP {\\y x. '@Load'('@Desc'(x), y)}
    $Load => (S/NP)/NP/NP {\\y x z. '@Load'('@Desc'(x), y, z)}
    $Load => (S/NP)/PP/NP  {\\y x z. '@Load'('@Desc'(y), z, x)}
    $Load => (S/PP)/PP/NP  {\\y x z. '@Load'('@Desc'(y), z, x)}
    $Load => (S/NP)/NP/PP  {\\y x z. '@Load'('@Desc'(y), z, x)}
    $Load => (S/PP)/NP/PP/NP {\\y x z k. '@Load'('@Desc'(y), x, z, k)}'
    $Load => (S/PP)/NP/NP/NP {\\y x z k. '@Load'('@Desc'(y), x, z, k)}'
    $Load => (S/PP)/PP/NP/NP {\\y x z k. '@Load'('@Desc'(y), x, z, k)}'
    $Load => (S/PP)/PP/PP/NP {\\y x z k. '@Load'('@Desc'(y), x, z, k)}'
    $Load => (S/PP)/NP/PP/PP/NP {\\y x z k l. '@Load'('@Desc'(y), z, x, k, l)}'
    $Load => (S/PP)/PP/PP/PP/NP {\\y x z k l. '@Load'('@Desc'(y), z, x, k, l)}'
    $Save => NP {'Save'}
    $Save => S/NP {\\x. '@Save'(x)}
    $Save => (S/NP)/NP {\\y x. '@Save'('@Desc'(x), y)}
    $Save => (S/NP)/PP {\\y x. '@Save'('@Desc'(x), y)}
    $Save => (S/NP)/NP/NP {\\y x z. '@Save'('@Desc'(y), z, x)}
    $Save => (S/NP)/PP/NP {\\y x z. '@Save'('@Desc'(y), z, x)}
    $Save => (S/PP)/PP/NP {\\y x z. '@Save'('@Desc'(y), z, x)}
    $Save => (S/PP)/PP/NP/NP {\\y x z k. '@Save'('@Desc'(y), x, z, k)}'
    $Print => NP {'Print'}
    $Print => S/NP {\\x. '@Print'(x)}
    $Print => S\\NP {\\x. '@Print'(x)}
    $Print => (S/NP)/NP {\\y x. '@Print'('@Desc'(x), y)}
    $Print => (S/NP)/PP {\\y x. '@Print'('@Desc'(x), y)}
    $Print => (S/PP)/PP/NP {\\y x z. '@Print'('@Desc'(y), z, x)}
    $Print => (S/PP)/PP/PP/NP {\\y x z k. '@Print'('@Desc'(y), x, z, k)}'
    $Append => NP {'Append'}
    $Append => S/NP {\\x. '@Append'(x)}
    $Append => (S/NP)/NP {\\y x. '@Append'('@Desc'(x), y)}
    $Append => (S/NP)/PP {\\y x. '@Append'('@Desc'(x), y)}
    $Append => (S\\NP)/PP {\\y x. '@Append'('@Desc'(x), y)}
    $Append => (S/NP)/PP/NP {\\y x z. '@Append'('@Desc'(y), z, x)}
    $Append => (S/PP)/PP/NP {\\y x z. '@Append'('@Desc'(y), z, x)}
    $Break => NP {'Break'}
    $Continue => S/NP {\\x. '@Continue'(x)}
    $Continue => S/PP {\\x. '@Continue'(x)}
    $Compare => NP {'Check'} #if compare is not used as NP, will use this
    $Compare => S/NP {\\x. '@Compare'(x)}
    $Compare => S/PP {\\x. '@Compare'(x)}
    $Compare => (S/NP)/NP {\\y x. '@Compare'('@Desc'(x), y)}
    $Compare => (S/NP)/PP {\\y x. '@Compare'('@Desc'(x), y)}
    $Compare => (S/NP)/NP/NP {\\y x z. '@Compare'('@Desc'(x), y, z)}
    $Compare => (S/NP)/PP/NP {\\y x z. '@Compare'('@Desc'(y), z, x)}
    $Compare => (S/PP)/PP/NP {\\y x z. '@Compare'('@Desc'(y), z, x)}
    $Parse => S/NP {\\x. '@Parse'(x)}
    $Parse => S\\NP {\\x. '@Parse'(x)}
    $Parse => (S/NP)/NP {\\y x. '@Parse'('@Desc'(x), y)}
    $Parse => (S/NP)/PP {\\y x. '@Parse'('@Desc'(x), y)}
    $Parse => (S/NP)/NP/NP {\\y x z. '@Parse'('@Desc'(x), y, z)}
    $Parse => (S/NP)/PP/NP {\\y x z. '@Parse'('@Desc'(y), z, x)}
    $Parse => (S/PP)/PP/NP {\\y x z. '@Parse'('@Desc'(y), z, x)}
    $Parse => (S/PP)/PP/PP {\\y x z. '@Parse'('@Desc'(y), z, x)}
    $Parse => (S\\NP)/PP/NP/PP {\\y x z k. '@Parse'('@Desc'(y), x, z, k)}'
    $Assign => (S/NP)/NP {\\y x. '@Assign'('@Desc'(x), y)}
    $Assign => (S\\NP)/NP {\\y x. '@Assign'('@Desc'(x), y)}
    $Assign => (S/NP)/PP {\\y x. '@Assign'('@Desc'(y), x)}
    $Assign => (S/PP)/PP/NP {\\y x z. '@Assign'('@Desc'(y), x, z)}
    $Replace => S/NP {\\x. '@Replace'(x)}
    $Replace => S\\NP {\\x. '@Replace'(x)}
    $Replace => (S/NP)/NP {\\y x. '@Replace'('@Desc'(x), y)}
    $Replace => (S/NP)/PP {\\y x. '@Replace'('@Desc'(x), y)}
    $Replace => (S\\NP)/NP {\\y x. '@Replace'('@Desc'(x), y)}
    $Replace => (S/PP)/PP/NP {\\y x z. '@Replace'('@Desc'(y), z, x)}
    $Replace => (S/NP)/PP/NP {\\y x z. '@Replace'('@Desc'(y), z, x)}
    $Replace => (S/PP)/PP/NP/NP {\\y x z k. '@Replace'('@Desc'(y), z, x, k)}'
    $Contain => NP/NP {\\x. '@Contain'(x)} # as it is used with other verbs
    $Contain => S\\NP {\\x. '@Contain'(x)}
    $Contain => (S\\NP)\\NP {\\y x. '@Contain'('@Desc'(x), y)}
    $Contain => (S\\NP)\\PP {\\y x. '@Contain'('@Desc'(x), y)}
    $Match => NP {'Match'}
    $Match => NP/NP {\\x. '@Match'(x)}
    $Match => S/NP {\\x. '@Match'(x)}
    $Match => S\\NP {\\x. '@Match'(x)}
    $Match => (S/NP)/NP {\\y x. '@Match'('@Desc'(x), y)}
    $Match => (S/NP)/PP {\\y x. '@Match'('@Desc'(x), y)}
    $Match => (S\\NP)/NP {\\y x. '@Match'('@Desc'(x), y)}

'''
#      $index => NP {'index'}
#      $index => NP/NP {\\x. '@Concat'('index', x)}
#      $item => NP {'item'}
#      $item => NP/NP {\\x. '@Concat'('item', x)}
#
#      $of => NP {'of'}
#      $of => NP/NP {\\x. '@Concat'('of', x)}
#      $in => NP {'in'}
#      $in => NP/NP {\\x. '@Concat'('in', x)}
#
#      $intersection => NP {'intersection'}
#      $intersection => NP/NP {\\x. '@Concat'('intersection', x)}
#      $nested => NP {'nested'}
#      $nested => NP/NP {\\x. '@Concat'('nested', x)}
#      $two => NP {'two'}
#      $two => NP/NP {\\x. '@Concat'('two', x)}

#     "index": ["$index"],
#     "item": ["$item"],
#     "in": ["$in"],
#     "of": ["$of"],
#
#     "current": ["$current"],
#     "dir": ["$dir"],
#     "file": ["$file"],
#
#     "intersection": ["$intersection"],
#     "nested": ["$nested"],
#     "two": ["$two"],

# $Find2 => (S/NP)/NP {\\x y.'@Find2'('@What'(y), '@Desc'(x))}
# $Find1 => S/NP {\\x.'@Find1'('@What'(x))}
# $Find => (S/NP)/PP {\\x y.'@Find'('@What'(y), '@Where'(x))}
# $UNK => NP/NP {\\x.'UNK'}
# $UNK => NP/N {\\x.'UNK'x}

# $index => var/.,var {\\x. x}
# $index => var\\.,var {\\x. x}
# $item => var/.,var {\\x. x}
# $item => var\\.,var {\\x. x}
# $in => PP {\\F x. F(x)}

# $of => PP {\\x F. F(x)} # element of a list -> 'List'('element')
# $of => PP {\\x y. '@And'(x, y)}


QUESTION_WORDS = [
    "(what|what's)",
    "(who|who's)",
    "where",
    "when",
    "which",
    "whose",
    "whom",
    "how",
    "why",
    "(can|could|may|might|should)",
    "(is|are|were|was)",
    "(will|would)",
    "(do|does|did)",
    "(has|have|had)",
    "how do I",
    "(best|fastest|most efficient) way to",
    # "(name|identify|describe|define)" # TODO
]
