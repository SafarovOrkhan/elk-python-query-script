# elk-python-query-script
Python script that automatically query the current indices on ELK server and get size corparisions and data

---
# how to use

ELK server can query indices with "localhost:9200/_cat/indices?v" (You can change it in application code for custom. But be aware that output must be same) in linux by using curl command.
I approach this script with this command, simple.
Output goes to a file and then with various text manipulations We achive following queries :
  - Search by indice name.
  - Total size of all indices
  - Today's size of selected indice
  - Average size of selected indice
  - Total size of selected indice

---
# Before usage
python3 must be installed
curl command must be installed
Only tested in linux.
This script works if indice names are formatted with : indiceName-YYYY.MM.DD
Any indice does not follows this format will get collected in "Indice Names with Date IS NOT Formatted" field
In this field Today's date and average file size is not going to calculated.

---
# usage
After cloning repository, go to repository folder and run main.py with python3

```
root@server:~/elk-python-query-script# python3 main.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 43550  100 43550    0     0   106k      0 --:--:-- --:--:-- --:--:--  120k
Filtered output saved to: ./filtered_output.txt
=========[ Indice Names with Date IS NOT Formatted ]========= (use 'u' prefix for these values)
Index 0: non-formatted-indiceName1
Index 1: non-formatted-indiceName2
Index 2: non-formatted-indiceName3
Index 3: non-formatted-indiceName4
Index 4: non-formatted-indiceName5
=========[ Indice Names with Date IS Formatted ]=============
Index 0: formatted-indiceName1
Index 1: formatted-indiceName2
Index 2: formatted-indiceName3
Index 3: formatted-indiceName4
Index 4: formatted-indiceName5
--------------------------
Enter the index number:
```


You have 3 options:
  - for non-formatted-indiceNames use 'u' followed by index number : u3 , u17 , u0
  - for formatted-indiceNames use only index number : 1 , 0 , 17
  - for complete total size use "all" keyword : all

```
root@server:~/elk-python-query-script# python3 main.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 43550  100 43550    0     0   106k      0 --:--:-- --:--:-- --:--:--  120k
Filtered output saved to: ./filtered_output.txt
=========[ Indice Names with Date IS NOT Formatted ]========= (use 'u' prefix for these values)
Index 0: non-formatted-indiceName1
Index 1: non-formatted-indiceName2
Index 2: non-formatted-indiceName3
Index 3: non-formatted-indiceName4
Index 4: non-formatted-indiceName5
=========[ Indice Names with Date IS Formatted ]=============
Index 0: formatted-indiceName1
Index 1: formatted-indiceName2
Index 2: formatted-indiceName3
Index 3: formatted-indiceName4
Index 4: formatted-indiceName5
--------------------------
Enter the index number: u1
Extracted index number: 1
Selected Indice Name :  non-formatted-indiceName2
Indice "non-formatted-indiceName2" size is : 0.0745 mb
root@server:~/elk-python-query-script#
```
```
root@server:~/elk-python-query-script# python3 main.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 43550  100 43550    0     0   106k      0 --:--:-- --:--:-- --:--:--  120k
Filtered output saved to: ./filtered_output.txt
=========[ Indice Names with Date IS NOT Formatted ]========= (use 'u' prefix for these values)
Index 0: non-formatted-indiceName1
Index 1: non-formatted-indiceName2
Index 2: non-formatted-indiceName3
Index 3: non-formatted-indiceName4
Index 4: non-formatted-indiceName5
=========[ Indice Names with Date IS Formatted ]=============
Index 0: formatted-indiceName1
Index 1: formatted-indiceName2
Index 2: formatted-indiceName3
Index 3: formatted-indiceName4
Index 4: formatted-indiceName5
--------------------------
Enter the index number: 2
Extracted index number: 2
==============[ Calculating ... ]==============
Selected Indice Name :  formatted-indiceName3
Total number of files : 33
Total size of indices of "formatted-indiceName3" : 3952.23 mb
Average size of indices of "formatted-indiceName3" : 119.76 mb
formatted-indiceName3 for today is : 0.73 mb
root@server:~/elk-python-query-script#
```
```
root@server:~/elk-python-query-script# python3 main.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 43550  100 43550    0     0   106k      0 --:--:-- --:--:-- --:--:--  120k
Filtered output saved to: ./filtered_output.txt
=========[ Indice Names with Date IS NOT Formatted ]========= (use 'u' prefix for these values)
Index 0: non-formatted-indiceName1
Index 1: non-formatted-indiceName2
Index 2: non-formatted-indiceName3
Index 3: non-formatted-indiceName4
Index 4: non-formatted-indiceName5
=========[ Indice Names with Date IS Formatted ]=============
Index 0: formatted-indiceName1
Index 1: formatted-indiceName2
Index 2: formatted-indiceName3
Index 3: formatted-indiceName4
Index 4: formatted-indiceName5
--------------------------
Enter the index number: all
==============================
Total complete size of all indices : 17323.33 mb
==============================
root@server:~/elk-python-query-script#
```
