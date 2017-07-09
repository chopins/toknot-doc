"""
Install and setup Toknot highlighting for Pygments.
"""

from setuptools import setup

entry_points = """
[pygments.lexers]
tklexer = tklexer.tklexer:ToknotLexer
ymllexer = tklexer.ymllexer:YmlLexer
"""

setup(
    name='pytklexer',
    version='0.1',
    description=__doc__,
    author="chopin",
    packages=['tklexer'],
    install_requires=(
        'sphinx >= 1.0.7',
        'sphinxcontrib-phpdomain >= 0.1.3-1'
    ),
    entry_points=entry_points
)
