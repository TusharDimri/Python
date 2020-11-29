# Public, Private & Protected Access Specifiers for OOPS IN Python
"""
Access Specifiers are used for OOPS in Python to specify the scope of a variable within a class.

1. Public Access Specifiers are the variables of a class which can be accessed by any other class be it a subclass of
the class or not. If we simply name a variable in python it is is declared public by default

2. Protected  Access Specifiers are the variables of a class which can be accessed only by the base class or the sub
classes of the base class.To declare a variable as protected we type a 'single underscore' before our variable name.For
Example:-
'_xyz' is an example of a protected variable.There should not be ay space between underscore and variable name.

3. Private  Access Specifiers are the variables which can be accessed only by their own class i.e. the class in which
they are declared .To declare a variable as Private we type two underscores before our variable name.for example:-
'__abc' is an example of a Private  Access Specifiers
Note that we cannot simply call a Private Access Specifier in Python because of "Name Angling" in Python.
To call a Private Variable we type:-
 _<class name>__<variable name>
"""

class Fender:
    instruments_no = 1
    _user = "Any Guitarist" # This is a Protected Access Specifier
    __gtype = "Strat" # This is a Private Access Specifier

    def __init__(self, argument_name, argument_role, argument_net):
        self.name = argument_name
        self.role = argument_role
        self.net = argument_net

    def help(self):
        return f"Name is {self.name},role is {self.role} & net worth is {self.net} million$"

kurt = Fender("Kurt Cobain", "Singer & Guitarist", 200)

class Musician(Fender):
    def __init__(self, argument_name, argument_role, argument_net,argument_band):
        self.name = argument_name
        self.role = argument_role
        self.net = argument_net
        self.band = argument_band

slash = Musician("Slash", "Guitarist", 100 , "Guns N Roses")

#Conclusions:-

print(slash._user)  # User can be called by objects slash of subclass Musician because user is a Protected variable & can
# be accessed by class Fender and all of its subclasses(Musician being one such subclass)



print(kurt._Fender__gtype)  #We type _Fender before __gtype fpr private variable to avoid error due to name angling in python
# NOTE that code " print(slash._Fender__gtype) " will give error bacause gtype is a PrIVATE variable & can only be accessed by insta
# -nces of class Fender


