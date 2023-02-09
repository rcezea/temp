"""contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    class_list = dict()
    class_list = {'BaseModel': BaseModel}
    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True
    do_quit = do_EOF
    
    def help_quit(self):
        print ("Quit command to exit the program")
    help_EOF = help_quit

    '''Updating command interpreter to have these commands
    create, show, destroy, all, update
    '''
    def do_create(self, line):
        #text = line.split()
        #if text in self.class_list:
        #    new_instance = eval(text(0))
        #    print(new_instance.id)
        #    new_instance.save()
        if line == "BaseModel":
            new_instance = BaseModel()
            print(new_instance.id)
            new_instance.save()
        elif line == '' or line is None:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
    def help_create(self):
        pass

    def do_show(self, line):
        texts = line.split()
        if texts[0] == '' or texts is None:
            print("** class name missing **")
        if texts[0] not in self.class_list:
            print("** class doesn't exist **")
        if texts[1] == '' or texts[1] is None:
            print("** instance id missing **")
        id = ".".join(texts[:2])
        try:
            display = storage.all()[id]
            print(display)
        except:
            print("** no instance found **")
    
'''
    def do_destroy(self, line):
        texts = line.split()
        if texts[0] == '' or texts is None:
            print("** class name missing **")
        if texts[0] not in self.class_list:
            print("** class doesn't exist **")
        if texts[1] == '' or texts[1] is None:
            print("** instance id missing **")
        id = ".".join(texts[:2])
        try:
            display = (storage.all()[id])
        except:
            print("** no instance found **")
        
    def help_destroy(self):
        print("Destroys an instance")
'''

if __name__ == '__main__':
    '''
    if sys.argv:
        HBNBCommand.do_create('self',sys.argv[0])
    '''
    HBNBCommand().cmdloop()
