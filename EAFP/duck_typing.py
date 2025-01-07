# Duck Typing and Easier to ask forgiveness than permission (EAFP)


class Duck:

    def quack(self):
        print("Quack, quack")

    def fly(self):
        print("Flap, Flap!")


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly_1(thing):
    # not Duck-Typed (Non-Pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("This has to be a Duck!")

    print()


def quack_and_fly(thing):
    # LBYL (Non-Pythonic), check everything before calling
    if hasattr(thing, "quack"):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, "fly"):
        if callable(thing.fly):
            thing.fly()

    # Easier to ask forgiveness than permission (EAFP)
    # if not work, then we handle the exception
    # if works great, if not, we handle the exception
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


d = Duck()

quack_and_fly(d)

p = Person()
quack_and_fly(p)
