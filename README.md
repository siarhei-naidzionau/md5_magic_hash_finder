
This tool can find magic hashes for MD5 hashing algorithm.

Magic hash is string that can be processed as a number in exponential notation (for example 0e123456 that means 0 x 10^123456).

Problem lies in comparison of this kind of strings using PHP == operator.
For more details - https://www.whitehatsec.com/blog/magic-hashes/ .

## Example of using:

***python3 magic_hashes.py -min 1 -max 5***
    **-h**, --help  show this help message and exit
    **-min 1**      Minimum number of symbols in source phrase
    **-max 5**      Maximum number of symbols in source phrase (required)