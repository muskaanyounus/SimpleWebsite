import re
 
 
 validate_string = lambda s: "valid string" if len(s) >= 10 and \
                              any(c.isupper() for c in s) and \
                              any(c.islower() for c in s) and \
                              any(c.isdigit() for c in s) else "invalid string"
 
 input_string = "PaceWisd0m"
 
 print(validate_string(input_string))