POTENTIAL_FUTURE_PREDICATES = [
    "Number -> count",
    "Count -> count",
    "Edit",
    "Move",
    "Tuple",
    "Duplicate -> Check[EQ]",
    "Output",
]


# Everything that is defined in this dictionary MUST have corresponding rules in RAW_LEXICONE, or the parse will fail.
STRING2PREDICATE = {
    "dict": ["$Dict"],
    "dicts": ["$Dict"],
    "dictionary": ["$Dict"],
    "int": ["$Int"],
    "integer": ["$Int"],
    "list": ["$List"],
    "lists": ["$List"],
    "array": ["$List"],
    "string": ["$String"],
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
    "unicode": ["$Char"],
    "unicode": ["$Char"],
    "path": ["$Path"],
    "dir": ["$Path"],
    "directory": ["$Path"],
    "set": ["$Set"],
    "class": ["$Class"],
    "object": ["$Class"],
    "object": ["$Class"],
    "member": ["$Class"],
    "func": ["$Func"],
    "function": ["$Func"],
    "method": ["$Func"],
    "index": ["$Index"],
    "id": ["$Index"],

    #det-s
    "the": ["$The"],
    "an": ["$The"],
    "a": ["$The"],

    #conjunctions
    "and": ["$And"],
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

    #Transforming verbs
    "find": ["$Find"],
    # "find if": ["$Check"]
    # "find out": ["$Return"]?
    "return": ["$Return"], # kind of the same as "get"? return smth [from smth/smwh]
    "merge": ["$Merge"], # merge smth-s into smth; merge smth-s; merge smth with smth; merge in NP[e.g. merge sort]
    "sort": ["$Sort"],
    "concat": ["$Concatenate"],
    "concatenate": ["$Concatenate"],
    "concatenation": ["$Concatenate"],
    "combine": ["$Concatenate"],
    "split": ["Split"],
    "round": ["$Round"],
    "convert": ["$Convert"],
    "add": ["$Add"],
    "remove": ["$Remove"],
    "pad": ["$Pad"],
    "map": ["$Dict", "$Map"],
    "create": ["$Create"],
    "generate": ["$Create"],
    "initialize": ["$Create"],
    "init": ["$Create"],
    "declare": ["$Create"],
    "copy": ["$Create"],
    "load": ["$Load"],
    "read": ["$Load"],
    "get": ["$Load"],
    "save": ["$Save"],
    "set": ["$Save"],
    "write": ["$Save"],
    "print": ["$Save"],
    "iterate": ["$Iterate"],
    "iter": ["$Iterate"],
    "it": ["$Iterate"],
    "break": ["$Break"],
    "continue": ["$Continue"],
    "cont": ["$Continue"],
    "check": ["$Compare"],
    "comp": ["$Compare"],
    "compare": ["$Compare"],

    #Conditions
    "exist": ["$Exist"],
    "exists": ["$Exist"],
    "largest": ["$Largest"],
    "less than": ["$LT"],
    "smallest": ["$Smallest"],
    "greater than": ["$GT"],
    "equal": ["$EQ"],
    "equals": ["$EQ"],
    "only": ["$Only"],
    "all": ["$All", "$And"],
    # "every": ["$All"],
    "none": ["$None", "$Not"],

    # Prepositions
    # "as": ["$as"],
}

WORD_NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
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
    $String => N {'String'}
    $String => NP {'String'}
    $File => N {'File'}
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


    $And => var\\.,var/.,var {\\y x.'@And'(x,y)}
    $Find => S/NP {\\x.'@Find'(x)}
    $Find => (S\\NP)/NP {\\y x.'@Find'('@Desc'(x), y)}
    $Return => S/NP {\\x.'@Return'(x)}
    $Transform => (S/NP)/NP {\\x y.'@Transform'(x, y)}
    $Merge => S/NP {\\x. '@Merge'(x)}
    $Merge => NP {'Merge'}
    $Merge => (S\\NP)/NP {\\y x. '@Merge'('@Desc'(x), y)}
    $Sort => S/NP {\\x. '@Sort'(x)}
    $Sort => (S/NP)/NP {\\y x. '@Sort'(@'Desc'(x), y)}
    $Sort => (S\\NP)/NP {\\y x. '@Sort'('@Desc'(x), y)}
    $Concatenate => S/NP {\\x. '@$Concatenate'(x)} # can be also Merge
    $Concatenate => S/NP/NP {\\x y. '@$Concatenate'(x, y)} # can be also Merge
'''

#
#
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