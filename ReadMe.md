# Password Table Generator

## Description

This Python script generates a table of random strings. The table is both printed to the console and saved to a file.

## Installation

To run the script, you need Python and the packages `optparse`, `termcolor`, and `prettytable`. You can install these packages with pip:

```
pip install optparse termcolor prettytable
```

Usage
The script can be run with various options:

```
-c or --column: Number of columns in the table (default is 5)
-l or --charLength: Number of characters in the randomly generated strings (default is 3)
-o or --output: Name of the output file (default is output.txt)
```
Example:
```
python passwordtable.py -c 8 -l 3 -o mytable.txt
```

This example generates a table with 8 columns, where each randomly generated string is 3 characters long. 
The table is saved to the file mytable.txt.

Example Output:

```

+---+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|   | ABC | DEF | GHI | JKL | MNO | PQR | STU | VWX | YZ. |
+---+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| 1 | H^C | Qyg | diQ | vQn | In] | R>B | QZ@ | JJG | I.+ |
|   |     |     |     |     |     |     |     |     |     |
| 2 | >q* | TZ8 | YM[ | }7' | BoW | Ozw | R7] | eBL | %[1 |
|   |     |     |     |     |     |     |     |     |     |
| 3 | Mpq | 6Nd | -k^ | #`V | 4f~ | RR, | 5u` | |%1 | JcE |
|   |     |     |     |     |     |     |     |     |     |
| 4 | uNu | [>/ | D$O | kqJ | {XW | "!A | F9h | 6Ky | d_: |
|   |     |     |     |     |     |     |     |     |     |
| 5 | g'w | (qK | yS7 | %!r | WXC | ,H< | XkH | tr| | hjh |
|   |     |     |     |     |     |     |     |     |     |
| 6 | ZPv | 9{4 | =TR | G3G | \$M | dff | 8Wj | 1Tg | YP< |
|   |     |     |     |     |     |     |     |     |     |
| 7 | &O@ | NJ] | 1sk | ,g[ | {5q | WK@ | Sp4 | d<B | 9m% |
|   |     |     |     |     |     |     |     |     |     |
| 8 | P|v | `F[ | VH& | Q5c | 5[m | ,eo | :AX | <~- | q9B |
|   |     |     |     |     |     |     |     |     |     |
+---+-----+-----+-----+-----+-----+-----+-----+-----+-----+

Output file: mytable.txt

```