# Store functions in dictionary to mimic the switch function

```
def func1(x):
	return(x + 1)
	
def func2(x):
	return(x + 2)

f_dict = {"F1":func1, "F2":func2}
```
## Call the function

```
f_dict["F2"](2)
```