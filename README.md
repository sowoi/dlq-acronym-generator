## DLQ Acronym Generator

The DLQ Acronym Generator is a Python script that generates random acronyms from three word lists. 
These word lists contain German words each starting with the letters D, L, and Q respectively.


## Usage
1. `poetry install`
2. `poetry run start`

## How it works

The script reads words from various text files in the directory. 
All words beginning with the letter `D` are stored in the file `D_Words..txt`, resp. `L_Words..txt` for `L` , etc.  
Nouns in the lists need the suffix "/w" for feminine, "/m" for masculine, and "/s" for neuter, depending on their gender.  
One Word is randomly selected from each of these files.  
A small language processor checks for certain context (no two nouns in a row, no two verbs in a row, ...)

## Example
```
poetry run start
# dezimierte lockere Quetschkommode (DLQ)
# dumpfe lebendige Quieklampe (DLQ)
# dunkelblaues leises Quälgeistchen (DLQ)
# dezidierter löwenstarker Quengelmeister (DLQ)
# Domina lustwandelt (durch) Quakorchester (DLQ)

``` 

## License
Licensed under the terms of GNU General Public License v3.0. See LICENSE file.

# Addendum

The acronym DLQ actually stands for annoying Dead Letter Queue in Apache Camel. 