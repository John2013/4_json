# Prettify JSON

Prints human-readable JSON data from a file

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python pprint_json.py <path to file>
```

Output sample:
```json
[
    {
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1,
        "Cells": {
            "global_id": 14371450,
            "Name": "Ароматный Мир",
            "geoData": {
                "type": "Point",
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ]
            }
        }
    }
]
```

File must be in utf-8 encoding

[JSON file](https://devman.org/media/filer_public/1d/32/1d32132e-efa4-4a6c-bd32-312acc3710ad/alco_shops.json) for testing

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
