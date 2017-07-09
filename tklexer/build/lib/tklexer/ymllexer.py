
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class YmlLexer(RegexLexer):
    """ 
    Lexer for configuration files in Yml style.
    """

    name = 'yml'
    aliases = ['yml']
    filenames = ['*.yml']
    mimetypes = ['text/x-yml']

    tokens = { 
        'root': [
            (r'\s+', Text),
            (r'[#].*', Comment.Single),
            (r'\[<<|~|:]$', Keyword),
            (r'(.*?)([ \t]*)(:)([ \t]*)(.*\n)',
             bygroups(Name.Attribute, Text, Operator, Text, String)),
            # standalone option, supported by some INI parsers
            (r'(.+?):$', Name.Attribute),
        ],
    }  
