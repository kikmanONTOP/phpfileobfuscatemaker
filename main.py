import re
import random
import string



print('''__88_88__  dP""Yb  __88_88__  dP""Yb  d8b  dP""Yb  __88_88__ .dPIIY8 .o. dP    .db.   .o. dP  .dPIIY8 __88_88__ .dPIIY8 .o. dP  
""88"88"" dP PY Yb ""88"88"" dP PY Yb Y8P dP PY Yb ""88"88"" `YbII " `"'dP   .dP'`Yb. `"'dP   `YbII " ""88"88"" `YbII " `"'dP   
__88_88__ Yb boodP __88_88__ Yb boodP `"' Yb boodP __88_88__ o.`II8b   dP.o.            dP.o. o.`II8b __88_88__ o.`II8b   dP.o. 
""88"88""  Ybooo   ""88"88""  Ybooo   (8)  Ybooo   ""88"88"" 8boIIP'  dP `"'           dP `"' 8boIIP' ""88"88"" 8boIIP'  dP ''')

def generate_random_name(length=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def generate_special_character():
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?\\"
    return random.choice(special_characters)

php_file_name = input("name of php file to obfuscate: ")


with open(php_file_name, 'r') as php_file:
    php_content = php_file.read()


php_content = re.sub(r'(\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)', lambda match: '$' + generate_random_name(), php_content)
php_content = re.sub(r'(function\s+[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)', lambda match: 'function ' + generate_random_name(), php_content)


php_content = re.sub(r'(["\']).*?\1', lambda match: '"' + ''.join(generate_special_character() for _ in range(len(match.group()))) + '"', php_content)


with open('obfuscated_' + php_file_name, 'w') as obfuscated_file:
    obfuscated_file.write(php_content)

print("Done.")
