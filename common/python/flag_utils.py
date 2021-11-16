"""Common utilities for command line flag parsing."""

import sys
import logging
from third_party.python3 import gflags as flags


logger = logging.getLogger(__name__)

flags.DEFINE_boolean("help", False, help="Print usage and exit")
flags.DEFINE_enum(
    "log_level",
    "info",
    ["debug", "info", "warn", "warning", "error", "critical"],
    "Level to set root logger to",
)

FLAGS = flags.FLAGS


def parse_argument_list(argv=None, positional=False):
    remaining = FLAGS(argv)[1:]  # First one is the binary name
    if positional:
        if any(x.startswith("-") and x != "-" for x in remaining):
            raise ValueError("Unknown flags passed: %s" % " ".join(remaining))
    elif any(remaining):
        raise ValueError("Unknown flags passed: %s" % " ".join(remaining))
    return remaining


def parse_flags(argv=None, positional=False):
    """Parses incoming command-line flags.

    Args:
      argv: Command line given to the app. Will use sys.argv if not passed.
      positional: Whether to allow positional arguments. Default raises on any extra args.
    Raises:
      SystemExit: if given unregistered flags.
    Returns:
      The remainder of the command line, excluding the initial argument (i.e. the first param
      passed to exec(), typically the path to this binary).
    """
    try:
        args = parse_argument_list(argv or sys.argv, positional=positional)
        if FLAGS.help:
            print(str(FLAGS), file=sys.stderr)
            sys.exit(0)
        return args
    except flags.Error as err:
        if FLAGS.help:
            print(str(FLAGS), file=sys.stderr)
            sys.exit(0)
        logger.critical(err)
        sys.exit(1)
