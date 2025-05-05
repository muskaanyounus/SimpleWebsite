is_number = lambda s: s.replace('.', '', 1).isdigit() if s.count('.') <= 1 and s.replace('.', '', 1).replace('-', '', 1).isdigit() else False
 
 
 test_strings = ["123", "45.67", "-89", "3.14.15", "abc", ""]
 
 for s in test_strings:
     print(f"Is '{s}' a number? ->", is_number(s))