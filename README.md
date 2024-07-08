# hescan

The script searches and filters BGP (Border Gateway Protocol) data based on a keyword provided by the user, allowing filtering, country, and saving the results and IP combinations in files.

![image](https://github.com/k45t0/hescan/assets/155916762/8f4fb159-d2e1-4942-8b29-7177daa25c55)

# Installation

```
git clone https://github.com/k45t0/hescan
```
```
cd hescan
```
```
pip3 install requirements.txt
```
<hr>
# Usage

```
  _
 | |
 | |__   ___  ___  ___ __ _ _ ___
 | '_ \ / _ \/ __|/ __/ _` | '_  \ 
 | | | |  __/\__ \ (_| (_| | | | |
 |_| |_|\___||___/\___\__,_|_| |_|

      CODED BY @wh0l5th3r00t | V2.0

usage: hescan.py [-h] -k KEYWORD [-or] [-o OUTPUT] [-oar OUTPUT_ALL_RANGES] [-i {result,type,description,country} [{result,type,description,country} ...]] [-c COUNTRY]

Fetch and filter BGP results.

options:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
                        Keyword to search for.
  -or, --only_results   Save only results (ASN and IP) to the output file.
  -o OUTPUT, --output OUTPUT
                        Output file to save the results.
  -oar OUTPUT_ALL_RANGES, --output_all_ranges OUTPUT_ALL_RANGES
                        Output file to save all IP combinations for the results.
  -i {result,type,description,country} [{result,type,description,country} ...], --ignore {result,type,description,country} [{result,type,description,country} ...]
                        Columns to ignore in the output.
  -c COUNTRY, --country COUNTRY
                        Filter results by country.

Example usage: python3 hescan.py -k Microsoft -or results.txt -c US
```

<h2>Exemple 1</h2>

```
python3 hescan.py -k Microsoft
```

<h2>Exemple 2</h2>

```
python3 hescan.py -k Microsoft -o results.txt
```

<h2>Exemple 3</h2>

```
python3 hescan.py -k Microsoft -o results.txt -c Country
```
