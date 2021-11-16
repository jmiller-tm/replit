from third_party.python3.md2py import md2py  # noqa: E402
from third_party.python3.markdown.extensions.fenced_code import FencedCodeExtension  # noqa: E402
from third_party.python3.markdown.extensions.tables import TableExtension  # noqa: E402

from common.python.confluence.parser.extensions.newline_remover import NewlineRemoverExtension


def parse_markdown(content: str) -> (str, str):
    """Parses a given string for Markdown content, outputting HTML.

    Returns the first <h1> value as the title, and the remaining HTML as
    the body.
    """

    tree = md2py(content, extensions=[
        FencedCodeExtension(),
        NewlineRemoverExtension(),
        TableExtension(),
    ]).source

    h1 = tree.find('h1')
    title = h1.extract().string if h1 else ""

    return title, str(tree)


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        print(parse_markdown(f.read()))
