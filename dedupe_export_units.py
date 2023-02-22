import argparse
import re

VERSION = "0.1.0"

ENCODING = "utf-16-le"
DELIMITER = "¬----------------"
PREAMBLE = """¬ Text used for building names and descriptions
¬ Lines that begin with this character are comments
¬ and should not be translated or altered
¬ Items inside curly brackets are tags and should not be translated
¬ The text following each tag on the same, or next line does need to be translated
¬\n\n\n"""

parser = argparse.ArgumentParser(
    prog="dedupe_export_units",
    description="A utility to deduplicate entries in `export_units.txt` for _Rome: Total War_ modifications.",
    epilog="Brought to you by the EB Online Team",
)
parser.add_argument("-v", action="version", version=f"%(prog)s {VERSION}")
parser.add_argument("input", help="input filepath")
parser.add_argument(
    "-o", metavar="output", help="output filepath (default: overwrite input)"
)
args = parser.parse_args()
input = args.input
output = args.o or input

re_name = re.compile(r"{(.+)(?<!_descr)(?<!_descr_short)}(.*\n[^{\n]*)")
re_descr = re.compile(r"{(.+)_descr}(.*\n[^{\n]*)")
re_descr_short = re.compile(r"{(.+)_descr_short}(.*\n[^{\n]*)")

with open(input, encoding=ENCODING) as f:
    lines = [line.strip() for line in f.readlines()]
    lines = [line for line in lines if line and line[0] != "¬"]
    lines = "\n".join(lines)

names = [(tag.strip(), name.strip()) for (tag, name) in re_name.findall(lines)]
names = {tag: name for (tag, name) in names}

descrs = [(tag.strip(), descr.strip()) for (tag, descr) in re_descr.findall(lines)]
descrs = {tag: descr for (tag, descr) in descrs}

descr_shorts = [
    (tag.strip(), descr.strip()) for (tag, descr) in re_descr_short.findall(lines)
]
descr_shorts = {tag: descr for (tag, descr) in descr_shorts}

with open(output, encoding=ENCODING, mode="w") as f:
    f.write(PREAMBLE)
    for tag in names:
        f.write(f"{{{tag}}} {names[tag]}\n\n")
        f.write(f"{{{tag}_descr}}\n{descrs[tag]}\n\n")
        f.write(f"{{{tag}_descr_short}}\n{descr_shorts[tag]}\n\n")
        f.write(f"{DELIMITER}\n\n")
