**This is documentation refering to [this Repository](https://github.com/CSDUMMI/cli_framework)**
# cli_framework
A Framework to make it easier for myself to develop small cli apps

# An example implementation
To implement this with CLI.py.
You import the `CLI` class from `CLI.py`:
```python
from CLI import CLI
```

Then you define a class that inherits
from `CLI` and define `__init__` like this:

```python
class App(CLI):
  def __init__(self):
    super().__init__('app.json','add','remove','list')
```
The `__init__` Function from `CLI` takes one positional
argument `file` or in this case `'app.json'`.
This is the file where the variable `self.state`
is loaded from and saved to before and after execution.
You can thus modify `self.state` like any `dict` and
then it will be saved afterwards.
The other arguments are the names of methods
you want to be accessed from the command-line.
These names must be members of the class `App` in this case.
This means you now have to implement these functions:
```python
  def add(self,args):
    name = args[0]
    balance = args[1]
    self.state[name] = balance

  def remove(self,args):
    name = args[0]
    del self.state[name]

  def list(self,*args):
    for i in self.state.keys():
      print("Name: {}\nBalance: {}".format(i,self.state[i]))
```
As you can see the names of the methods and the arguments in
`__init__`.

You can now use your CLI App like this:
```bash
$ python3 App.py add <name> <balance>
$ python3 App.py remove <name>
$ python3 App.py list
$ python3 App.py help
$ python3 App.py
```
You can execute these commands right now,
all code here was written in the file `App.py` in this Repository.

### `help` == `''`
If there is no command, the `help` function, that was inherited from `CLI`
is executed, it prints the docstring of `self`: `self.__doc__`.
If you want usage information for your CLI App to appear,
you just write the usage or help into the docstring like this:
```python
class App(CLI):
  """
  Usage:
  add <name> <balance>\t:Add new user
  remove <name>\t:Remove user
  list:\tList all current users
  help:\tDisplay this help
  """
  ...
```
Then you can use execute the CLI with this:
```python
if __name__ == '__main__':
  app = App() # Create Instance of CLI App
  app.run() # Execute Commandline Parsing
```
I hope this helped you and you can implement your own CL Apps or interfaces
soon.
