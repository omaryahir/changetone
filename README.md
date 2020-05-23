# changetone.py

In this project you can send a txt file with the tones for example:

_myfile.txt_
```
[C]        [F]       [G]
Lorem ipsum dolor sit amet
``` 

### Execute the command in this way:
```
$ python changetone.py myfile.txt > output.txt
 Main tone: Do
 Target tone: Sol 
```

Output:

_output.txt_
```
------
diff tones: 8
------ 
[G]        [C]       [D]
Lorem ipsum dolor sit amet
``` 


### Especial features
$ python changetone.py myfile.txt esp

Output:
```
------
diff tones: 8
------ 
[Sol]         [Do]       [Re]
Lorem ipsum dolor sit amet
``` 

$ python changetone.py myfile.txt nobrackets

Output:
```
------
diff tones: 8
------ 
G          C       D
Lorem ipsum dolor sit amet
``` 


### Requirements:
Python 3.8 