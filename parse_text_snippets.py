import re

def parse_sections(text):
    sections = re.split(r'^(\d+)\n', text, flags=re.MULTILINE)
    sections.pop(0)  # Remove the first empty element
    parsed_sections = [(int(sections[i]), sections[i+1]) for i in range(0, len(sections), 2)]
    return parsed_sections


def text_snippets(file_name: str) -> list[tuple[str, str]]:
    with open(file_name, 'r') as snippets_file:
        all_snippets = snippets_file.read()
        sections = parse_sections(all_snippets)
        return sections
