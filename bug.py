def function_with_unclosed_file(filename):
    f = open(filename, 'r')
    # ... some code that processes the file ... 
    # missing f.close() or with statement