import os
import shutil
from unittest import TestCase

from common.python.confluence.parser import parse_markdown
from common.python.resources import resource_folder


class ConfluenceParserTest(TestCase):
    """A test class for the Confluence markdown parser.

    The tests are sourced from the `tests` directory; each subdirectory within
    represents a test, and should contain two files, `input.md` and `output.html`.
    """

    def setUp(self):
        """Copy the test resource folder into a temporary directory."""

        self.test_dir = resource_folder('tests', 'common.python.confluence.parser')

    def tearDown(self):
        """Remove the temporary test resource directory."""

        shutil.rmtree(self.test_dir)

    def test_parse_markdown(self):
        """Asserts that parsing `input.md` is equal to the content of `output.html`."""

        for d in (de for de in os.scandir(self.test_dir) if de.is_dir()):
            with open(os.path.join(d.path, 'input.md')) as i:
                with open(os.path.join(d.path, 'output.html')) as o:
                    self.assertEqual('\n' + o.read(),
                                     parse_markdown(i.read())[1] + '\n')
