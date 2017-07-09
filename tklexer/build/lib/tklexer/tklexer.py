from pygments.lexer import DelegatingLexer
from pygments.lexers.web import PhpLexer, HtmlLexer


class ToknotLexer(DelegatingLexer):
    """
    Handles HTML, PHP, JavaScript, and CSS is highlighted
    PHP is highlighted with the "startline" option
    """

    name = 'Toknot'
    aliases = ['tk', 'toknot']
    filenames = ['*.html', '*.css', '*.php', '*.xml', '*.static']
    mimetypes = ['text/html', 'application/xhtml+xml']

    def __init__(self, **options):
        super(ToknotLexer, self).__init__(HtmlLexer,
                                               PhpLexer,
                                               startinline=True)
                                               


                                               
