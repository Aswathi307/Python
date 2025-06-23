print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
import re
import os
def mad_libs(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    placeholders = re.findall(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', content)
    replacements = []
    for word in placeholders:
        user_input = input(f"Enter a {word.lower()}: ")
        replacements.append(user_input)
    def replace_placeholders(match):
        return replacements.pop(0)
    new_content = re.sub(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', replace_placeholders, content)
    with open(output_file, 'w') as file:
        file.write(new_content)

    print("\nNew Mad Libs story created successfully in", output_file)
dummy_input_content = "The ADJECTIVE dog NOUN VERB quickly ADVERB."
with open('madlibs_input.txt', 'w') as f:
    f.write(dummy_input_content)
mad_libs('madlibs_input.txt', 'madlibs_output.txt')
