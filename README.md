# changetone.py

In this project you can send a txt file with the tones for example:

_myfile.txt_
```
[C]        [F]       [G]
Lorem ipsum dolor sit amet
``` 

## Execute the command in this way:
```
$ python changetone.py myfile.txt > output.txt
 Main tone: C
 Target tone: G 
```
Note: You can also use Do or Sol

_Output:_
```
------
diff tones: 8
------ 
[G]        [C]       [D]
Lorem ipsum dolor sit amet
``` 


## Especial features
$ python changetone.py myfile.txt esp

_Output:_
```
------
diff tones: 8
------ 
[Sol]         [Do]       [Re]
Lorem ipsum dolor sit amet
``` 

$ python changetone.py myfile.txt nobrackets

_Output:_
```
------
diff tones: 8
------ 
G          C       D
Lorem ipsum dolor sit amet
``` 


## Requirements:
Python 3.8 