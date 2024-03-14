# Write your code here
import re

def is_valid_email_address(string):
    return re.fullmatch(r"[0-9a-z.]{1,}@(ucll.be|student.ucll.be){1}", string)
