def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        
def function_with_explicit_close(filename):
    try:
        f = open(filename, 'r')
        # ... some code that processes the file ...
        for line in f:
          print(line.strip())
        f.close() 
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}") 