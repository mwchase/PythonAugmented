# SYNTAX TEST "Packages/Python Augmented/Python Augmented.sublime-syntax"

if __debug__ and __name__ \
        and int:        # ^ punctuation.separator.continuation.line.python
    pass

shouldnt_work = 1 + \ 2
#                   ^ punctuation.separator.continuation.line.python
#                    ^^ invalid.illegal.unexpected-text.python
