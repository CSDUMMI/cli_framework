#!/usr/bin/python3
import json,sys, inspect

class CLI:
    """
    Structure
    =========
    Every app has a JSON file with
    all important data and they can load it
    """
    def __init__(self,file,directory="",*commands):
        if file != '':
            # state,
            self.state = json.load(open(directory+file))
        else:
            self.state = {}

        self.file = file
        self.commands = list(commands) + ['help']

    def save(self):
        json.dump(self.state,open(self.directory+file,'w'))

    def help(self,*args):
        print(self.__doc__)


    def run(self):
        if len(sys.argv) < 2:
            print(self.__doc__)
            return
        for c in self.commands:
            if c == sys.argv[1]:
                c = getattr(self,c)
                c(sys.argv[2:])
                self.save()
                break
        else:
            print(self.__doc__)
