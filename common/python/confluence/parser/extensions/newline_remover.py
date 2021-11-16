"""A markdown parser extension for removing newlines from HTML paragraphs.

In Confluence, whitespace characters, such as newlines, are converted into
their HTML tags, such as </ br>. This extension will remove such newlines from
paragraphs, allowing line breaks to exist in the source markdown.
"""

import re

from third_party.python3.markdown.extensions import Extension  # noqa: E402
from third_party.python3.markdown.treeprocessors import Treeprocessor  # noqa: E402


class NewlineRemoverExtension(Extension):

    def extendMarkdown(self, md):
        md.registerExtension(self)

        md.treeprocessors.register(NewlineRemoverTreeprocessor(md), "newline_remover", 100)


class NewlineRemoverTreeprocessor(Treeprocessor):

    def run(self, root):
        self.remove_newlines(root)

    def remove_newlines(self, element):
        pattern = re.compile("$\n^\\s*", re.M)

        for child in element:
            if child.tag in ["p", "li"]:
                try:
                    child.text = pattern.sub(" ", child.text)
                except TypeError:
                    pass
            self.remove_newlines(child)
