"""
Unit and regression test for the bib2coa package.
"""

# Import package, test suite, and other packages as needed
import bib2coa
import pytest
import sys

def test_bib2coa_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "bib2coa" in sys.modules
