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
python passwordtable.py -c 10 -l 4 -o example.txt
```


This example generates a table with 10 columns, where each randomly generated string is 4 characters long. 
The table is saved to the file mytable.txt.

Example Output:

```

+----+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
|    |  a   |  b   |  c   |  d   |  e   |  f   |  g   |  h   |  i   |  j   |  k   |  l   |  m   |  n   |  o   |  p   |  q   |  r   |  s   |  t   |  u   |  v   |  w   |  x   |  y   |  z   |
+----+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
| 1  | QyMC | 61k7 | kRd0 | Oh2R | [LrB | 2Hu] | 8{A_ | uivr | 6%h0 | L5`2 | [^&n | Z>I} | JYj- | Z&2= | gxF7 | ukSP | []ei | HicH | JtYl | EMa` | &e#' | HEun | Yof+ | m*0v | 88U1 | `t~1 |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| 2  | c7Mc | )x$0 | 0}UE | isL! | 9mb~ | rl!: | q=e_ | c3[! | 6*BQ | n<_g | M_fg | X93m | 4V[[ | wm(g | ~0o: | ,,\` | J?O( | -+Yy | Ix+0 | kxf6 | |eaA | $0_z | f>b5 | d,Sh | 5jQH | qh!L |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| 3  | NPw( | 9zcU | Grs# | \~Ll | WLs< | fkb] | sO=F | ;CLq | j7AL | ~B%Q | #*[I | <UBl | #)~$ | ZEN= | f1zJ | KG:v | ~'2, | N"Y3 | TxOa | :NAL | $)}J | @"t[ | 5q4Q | m[ly | 2<>X | m0tg |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| 4  | k_/e | /ulo | p{`N | tQA_ | 2>gB | *e^K | G[0b | \>_R | *AmA | 5or2 | pj2T | >igY | H$1k | oUJ, | "3b. | dCIi | [UB` | ^vv= | #gjf | (XGB | +WpL | h6u6 | r`"8 | <\5| | ApGa | Y_@I |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| 5  | gQ9v | <X2? | TMm$ | 3]VQ | `+]) | TO{m | sg1- | &vM9 | Wtb2 | *o3' | ubkO | #QOI | z=XW | {]a; | p@Kh | MfM& | _EaA | GsTI | NLKl | Q3+c | D`;i | f=Fh | 30aB | IdVq | H@58 | R~6e |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| 6  | g+i# | R=0b | ;3z4 | )YK] | aYCd | L./b | ~\E6 | dGi4 | d>Yi | hm\D | ^EIQ | u@Vz | 5#pO | oa/7 | wa,b | @bqm | Cw@B | B>zt | hNGY | SZ`V | #/,L | ':Gw | W6bt | @H8E | H~5, | JH1\ |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| 7  | k0?? | CkG/ | 7\}r | MJJV | UI:O | -oV> | wSvK | B!5! | }&hn | kcGx | /#Cf | wux= | U?wN | j'>W | _Db# | (+#0 | v2.I | aXVe | +~\n | *44] | )+{p | aVh3 | !>5s | JNoC | JV9W | 2C9o |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| 8  | xkT! | C36G | 2TW* | FoEO | .W&y | Xta- | 5{<+ | TQ]A | Vd~M | \xY@ | %AU{ | CuLW | ZwZT | `4VA | ioA% | irV( | `|[+ | ZZn& | YAYi | t>0L | #hXk | t-:t | JI~a | LqZ; | t.!f | rJ,? |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| 9  | :9Je | 8lLa | 5N~q | zPf] | W"\l | *LmO | S'fY | YH~| | 8c|> | Fg?h | V<>D | *:d= | {@4N | wOkC | V;.V | e[9] | dm3r | !Jr[ | '\HD | I$:5 | )"ZB | aM0= | Le4e | U3l0 | ^nSI | )t(* |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
| 10 | yVei | 9IbW | M,d< | t#ty | qH]4 | Wp/< | Qq(1 | =<jh | )CEn | VROj | a<%4 | +BS- | Fp,Q | l"Jm | n/GA | ]9,X | 9$f} | /W@E | l[W- | !B4H | RaOL | JA|C | ~gP_ | wa&u | (Uq% | umg% |
|    |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
+----+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+------+


Output file: example.txt

```
