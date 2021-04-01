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
    # "find if": ["$Check"]
    # "find out": ["$Return"]?
    # kind of the same as "get"? return smth [from smth/smwh]
    "return": ["$Return"],
    # merge smth-s into smth; merge smth-s; merge smth with smth; merge in NP[e.g. merge sort]
    "merge": ["$Merge"],
    "join": ["$Merge"],
    "concat": ["$Concatenate"],
    "concatenate": ["$Concatenate"],
    "concatenating": ["$Concatenate"],
    "concatenation": ["$Concatenate"],
    "combine": ["$Concatenate"],
    "split": ["$Split"],
    "splitting": ["$Split"],
    "round": ["$Round"],
    "rounding": ["$Round"],
    "convert": ["$Convert"],
    "converting": ["$Convert"],
    "add": ["$Add"],
    "addition": ["$Add"],
    "adding": ["$Add"],
    "insert": ["$Add"],
    "inserting": ["$Add"],
    "remove": ["$Remove"],
    "removing": ["$Remove"],
    "delete": ["$Remove"],
    "deleting": ["$Remove"],
    "dump": ["$Remove"],
    "dumping": ["$Remove"],
    "disable": ["$Remove"],
    "pad": ["$Pad"],
    "map": ["$Map", "$Dict"],
    "filter": ["$Map"],
    "create": ["$Create"],
    "created": ["$Create"],
    "generate": ["$Create"],
    "initialize": ["$Create"],
    "init": ["$Create"],
    "declare": ["$Create"],
    "copy": ["$Create"],
    "copying": ["$Create"],
    "make": ["$Create"],
    "load": ["$Load"],
    "read": ["$Load"],
    "reading": ["$Load"],
    "get": ["$Load"],
    "getting": ["$Load"],
    "detect": ["$Load"],
    "select": ["$Load"],
    "selected": ["$Load"],
    "selecting": ["$Load"],
    "upload": ["$Load"],
    "download": ["$Load"],
    "downloading": ["$Load"],
    "display": ["$Load"],
    "displaying": ["$Load"],
    "use": ["$Load"],
    "control": ["$Load"],
    "save": ["$Save"],
    "saved": ["$Save"],
    "saving": ["$Save"],
    "set": ["$Set", "$Save"],
    "write": ["$Save"],
    # "keep": ["$Save"],
    "print": ["$Print"],
    "printing": ["$Print"],
    "show": ["$Print"],
    "iterate": ["$Iterate"],
    "iter": ["$Iterate"],
    "iterator": ["$Iterate"],
    "iterators": ["$Iterate"],
    "iterating": ["$Iterate"],
    # "it": ["$Iterate"],
    "append": ["$Append"],
    "appending": ["$Append"],
    "break": ["$Break"],
    "breaks": ["$Break"],
    "continue": ["$Continue"], # no examples found for continue
    "cont": ["$Continue"],
    "skip": ["$Continue"],
    "determine": ["$Compare"],
    "check": ["$Compare"],
    "checking": ["$Compare"],
    "comp": ["$Compare"],
    "comparing": ["$Compare"],
    "compare": ["$Compare"],
    "parse": ["$Parse"],
    "parsing": ["$Parse"],
    "assign": ["$Assign"],
    "assignment": ["$Assign"],
    "assigning": ["$Assign"],
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
    "replace": ["$Replace"],
    "replacing": ["$Replace"],
    "replacement": ["$Replace"],

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
    # "as": ["$as"],
}

WORD_NUMBERS = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
WORD2NUMBER = {elem: str(i) for i, elem in enumerate(WORD_NUMBERS)}


RAW_LEXICON = ''' :- S, NP, N, VP
    Det :: NP/N
    Pro :: NP
    Modal :: S\\NP/VP

    TV :: VP/NP
    DTV :: TV/NP
    PP :: (NP\\NP)/NP

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

    $And => var\\.,var/.,var {\\y x.'@And'(x,y)}
    $Or => var\\.,var/.,var {\\y x.'@Or'(x,y)}
    $By => NP/NP {\\x.'@By'(x)}
    # $By => var\\.,var/.,var {\\y x.'@By'(x,y)}
    $Not => S/NP {\\x. '@Not'(x)} # is used in and a lot
    $Not => NP/NP {\\x. '@Not'(x)}
    $Exist => NP/NP {\\x. '@Exist'(x)}

    $Find => S/NP {\\x.'@Find'(x)}
    $Find => (S\\NP)/NP {\\y x.'@Find'('@Desc'(x), y)}
    $Find => (S/NP)/NP {\\y x.'@Find'('@Desc'(x), y)}
    $Return => S/NP {\\x.'@Return'(x)}
    $Return => (S/NP)/NP {\\y x.'@Return'('@Desc'(x), y)}
    $Return => (S/NP)/NP/NP {\\y x z.'@Return'('@Desc'(x), y, z)}
    $Transform => (S/NP)/NP {\\x y.'@Transform'(x, y)}
    $Merge => S/NP {\\x. '@Merge'(x)}
    $Merge => NP {'Merge'}
    $Merge => (S\\NP)/NP {\\y x. '@Merge'('@Desc'(x), y)}
    $Sort => S/NP {\\x. '@Sort'(x)}
    $Sort => (S/NP)/NP {\\y x. '@Sort'('@Desc'(x), y)}
    $Sort => (S\\NP)/NP {\\y x. '@Sort'('@Desc'(x), y)}
    $Sort => (S/NP)/NP/NP {\\y x z. '@Sort'('@Desc'(x), y)}
    $Concatenate => S/NP {\\x. '@Concatenate'(x)} # can be also Merge
    $Concatenate => S/NP/NP {\\x y. '@Concatenate'(x, y)} # can be also Merge
    $Split => S/NP {\\x. '@Split'(x)}
    $Split => (S/NP)/NP {\\y x. '@Split'('@Desc'(x), y)}
    $Split => (S\\NP)/NP {\\y x. '@Split'('@Desc'(x), y)}
    $Round => S/NP {\\x. '@Round'(x)}
    $Round => (S/NP)/NP {\\y x. '@Round'('@Desc'(x), y)}
    $Convert => (S/NP)/NP {\\y x. '@Convert'('@Desc'(x), y)}
    $Convert => (S/NP)/NP/NP {\\y x z. '@Convert'('@Desc'(x), y, z)}
    $Add => NP {'Add'}
    $Add => S/NP {\\x. '@Add'(x)}
    $Add => (S/NP)/NP {\\y x. '@Add'('@Desc'(x), y)}
    $Add => (S\\NP)/NP {\\y x. '@Add'('@Desc'(x), y)}
    $Add => (S\\NP)/NP/NP {\\y x z. '@Add'('@Desc'(x), y, z)}
    $Remove => S/NP {\\x. '@Remove'(x)}
    $Remove => (S/NP)/NP {\\y x. '@Remove'('@Desc'(x), y)}
    $Remove => (S\\NP)/NP {\\y x. '@Remove'('@Desc'(x), y)}
    $Remove => (S/NP)/NP/NP {\\y x z. '@Remove'('@Desc'(x), y, z)}
    $Map => (S/NP)/NP {\\y x. '@Map'('@Desc'(x), y)}
    $Create => NP/NP {\\x.'@Create'(x)}
    $Create => NP\\NP {\\x.'@Create'(x)}
    $Create => S/NP {\\x. '@Create'(x)}
    $Create => (S/NP)/NP {\\y x. '@Create'('@Desc'(x), y)}
    $Create => (S\\NP)/NP {\\y x. '@Create'('@Desc'(x), y)}
    $Load => NP\\NP {\\x.'@Load'(x)}
    $Load => S/NP {\\x. '@Load'(x)}
    $Load => S\\NP {\\x. '@Load'(x)} # for nouns that come before
    $Load => (S/NP)/NP {\\y x. '@Load'('@Desc'(x), y)}
    $Load => (S/NP)/NP/NP {\\y x z. '@Load'('@Desc'(x), y, z)}
    $Save => NP {'Save'}
    $Save => S/NP {\\x. '@Save'(x)}
    $Save => (S/NP)/NP {\\y x. '@Save'('@Desc'(x), y)}
    $Print => NP {'Print'}
    $Print => S/NP {\\x. '@Print'(x)}
    $Print => S\\NP {\\x. '@Print'(x)}
    $Print => (S/NP)/NP {\\y x. '@Print'('@Desc'(x), y)}
    $Iterate => NP {'Iterator'}
    $Iterate => S/NP {\\x. '@Iterate'(x)}
    $Iterate => (S/NP)/NP {\\y x. '@Iterate'('@Desc'(x), y)}
    $Append => NP {'Append'}
    $Append => S/NP {\\x. '@Append'(x)}
    $Append => (S/NP)/NP {\\y x. '@Append'('@Desc'(x), y)}
    $Break => NP {'Break'}
    $Continue => S/NP {\\x. '@Continue'(x)}
    $Compare => NP {'Check'} #if compare is not used as NP, will use this
    $Compare => S/NP {\\x. '@Compare'(x)}
    $Compare => (S/NP)/NP {\\y x. '@Compare'('@Desc'(x), y)}
    $Compare => (S/NP)/NP/NP {\\y x z. '@Compare'('@Desc'(x), y, z)}
    $Parse => S/NP {\\x. '@Parse'(x)}
    $Parse => S\\NP {\\x. '@Parse'(x)}
    $Parse => (S/NP)/NP {\\y x. '@Parse'('@Desc'(x), y)}
    $Parse => (S/NP)/NP/NP {\\y x z. '@Parse'('@Desc'(x), y, z)}
    $Assign => (S/NP)/NP {\\y x. '@Assign'('@Desc'(x), y)}
    $Assign => (S\\NP)/NP {\\y x. '@Assign'('@Desc'(x), y)}
    $Replace => S/NP {\\x. '@Replace'(x)}
    $Replace => S\\NP {\\x. '@Replace'(x)}
    $Replace => (S/NP)/NP {\\y x. '@Replace'('@Desc'(x), y)}
    $Replace => (S\\NP)/NP {\\y x. '@Replace'('@Desc'(x), y)}
    $Contain => NP/NP {\\x. '@Contain'(x)} # as it is used with other verbs
    $Contain => S\\NP {\\x. '@Contain'(x)}
    $Contain => (S\\NP)\\NP {\\y x. '@Contain'('@Desc'(x), y)}
    $Match => NP {'Match'}
    $Match => NP/NP {\\x. '@Match'(x)}
    $Match => S/NP {\\x. '@Match'(x)}
    $Match => S\\NP {\\x. '@Match'(x)}
    $Match => (S/NP)/NP {\\y x. '@Match'('@Desc'(x), y)}
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
