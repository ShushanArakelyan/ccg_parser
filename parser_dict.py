STRING2PREDICATE = {
    "dict": ["$Dict"],
    "dictionary": ["$Dict"],
    "int": ["$Int"],
    "integer": ["$Int"],
    "list": ["$List"],
    "lists": ["$List"],
    "array": ["$List"],
    "find": ["$Find"],
    "the": ["$The"],
}

WORD_NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
WORD2NUMBER = {elem: str(i) for i, elem in enumerate(WORD_NUMBERS)}


RAW_LEXICON = ''' :- S, NP, N, VP
     Det :: NP/N
     Pro :: NP
     Modal :: S\\NP/VP

     TV :: VP/NP
     DTV :: TV/NP

     $The => N/N {\\x.x}
     $The => NP/NP {\\x.x}
     
     $UNK => NP/NP {\\y x.'@ToString'(y)}
     $UNK => N/N {\\y x.'@ToString'(y)}
     
     $Dict => N {'Dict'}
     $Dict => NP {'Dict'}
     $List => N {'List'}
     $List => NP {'List'}

     and => var\\.,var/.,var {\\x y.'@And'(x,y)}
     $Find => S/NP {\\x.'@Find'(x)}
     is => (S\\NP)/NP {\\y x.'@Is'(x,y)}
'''
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
    # "(name|identify|describe|define)" # TODO
]