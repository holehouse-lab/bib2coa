"""
bib2coa
A command-line tool that converts a single bibtex file to a csv with paper, author that can be used as the foundation for an NSF COA form.
"""

# Add imports here
from .bib2coa import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
