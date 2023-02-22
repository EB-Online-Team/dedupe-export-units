# dedupe_export_units

A utility to deduplicate entries in `export_units.txt` for _Rome: Total War_ modifications.

## Requirements

No dependencies are required.

Tested to run correctly on Python 3.11.2.

## Usage

Run `python ./dedupe_export_units.py -h` for the help message.

The only required argument is the filepath of `export_units.txt`. By default, the deduplication process will overwrite the file.

If you wish to leave the file alone, specify an output filepath using `-o` followed by a filepath.

### Example

```sh
python ./dedupe_export_units.py "C:\my_mod\text\export_units.txt"
```

NOTE: The above command will deduplicate entries and overwrite the specified file.

---

```sh
python ./dedupe_export_units.py "C:\my_mod\text\export_units.txt" -o "C:\other_folder\export_units.txt"
```

The above command will leave the original file alone and save the deduped output to the specified location.

Brought to you by the EB Online Team
