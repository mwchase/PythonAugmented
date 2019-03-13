# SYNTAX TEST "Packages/Python Augmented/Python Augmented.sublime-syntax"

# This is a comment
# <- comment.line.number-sign.python

print("This is a line")  # This is a comment
#                        ^^^^^^^^^^^^^^^^^^^ comment.line.number-sign.python

print("This is a string  # this is not a comment")
#                        ^^^^^^^^^^^^^^^^^^^^^^^ - comment

# Augmented extensions:

#!/usr/bin/env python
# <- comment.line.shebang.python comment.line.number-sign.python punctuation.definition.comment.python
#^^^^^^^^^^^^^^^^^^^^ comment.line.shebang.python comment.line.number-sign.python

# type: ignore
# ^^^^^ comment.line.number-sign.python comment.line.type.python
#       ^^^^^^ comment.line.number-sign.python comment.line.type.ignore.python

# type: int
# ^^^^^ comment.line.number-sign.python comment.line.type.python
#       ^^^ comment.line.type.type.python

# pylint: skip-file
# ^^^^^^^ comment.line.pylint.python
#         ^^^^^^^^^ comment.line.pylint.disable.all.python

# pylint: disable=wildcard-import, method-hidden
# ^^^^^^^ comment.line.pylint.python
#         ^^^^^^^^ comment.line.pylint.disable.python
#                 ^^^^^^^^^^^^^^^ comment.line.pylint.message.python
#                                ^ comment.line.pylint.separator.python punctuation.separator.sequence.python
#                                  ^^^^^^^^^^^^^ comment.line.pylint.message.python

# pylint: enable=too-many-lines
# ^^^^^^^ comment.line.pylint.python
#         ^^^^^^^ comment.line.pylint.enable.python
#                ^^^^^^^^^^^^^^ comment.line.pylint.message.python


# XXX
# ^^^ comment.line.note.python comment.line.note.notation.python

# XXX: details
# ^^^ comment.line.note.python comment.line.note.notation.python
#    ^^^^^^^^^ comment.line.note.python
