def get_input(start, end, input_statement, wrong_statement):
    try:
        
        option = int(input(input_statement))
        if start >= option >= end:
            print(wrong_statement)
            return get_input(start, end, input_statement, wrong_statement)
        
    except ValueError:
        print(wrong_statement)
        return get_input(start, end, input_statement, wrong_statement)
    
    print()
    return option
     