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

```
python passwordtable.py -c 10 -l 5 -o mytable.txt
```


This example generates a table with 10 columns, where each randomly generated string is 5 characters long. 
The table is saved to the file mytable.txt.

Example Output:

```

+---+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|   |  a  |  b  |  c  |  d  |  e  |  f  |  g  |  h  |  i  |  j  |  k  |  l  |  m  |  n  |  o  |  p  |  q  |  r  |  s  |  t  |  u  |  v  |  w  |  x  |  y  |  z  |
+---+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| 1 | abc | def | ghi | jkl | mno | pqr | stu | vwx | yz1 | 23a | bc4 | de5 | fg6 | hi7 | jk8 | lm9 | nop | qr0 | st1 | uv2 | wx3 | yz4 | 12a | bc5 | de6 | fg7 |
|   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 2 | hij | klm | nop | qrs | tuv | wxy | z12 | 34a | bc5 | de6 | fg7 | hi8 | jk9 | lm0 | no1 | pq2 | rs3 | tu4 | vw5 | xy6 | z78 | 9ab | cd0 | ef1 | gh2 | ij3 |
|   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
...
+---+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

Output file: mytable.txt

```