# Unclosed File Handle Bug in Python
This repository demonstrates a common Python bug: forgetting to close a file handle after opening it. This can lead to resource leaks and potential errors, especially when dealing with many files.

## Bug Description
The `function_with_unclosed_file` in `bug.py` opens a file for reading but doesn't close it properly. This is bad practice because it can lead to the program holding onto resources it no longer needs.

## Solution
The `bugSolution.py` file shows two ways to fix this:
1. Using the `with` statement which automatically handles file closing.
2. Explicitly calling `f.close()` after finishing with the file.