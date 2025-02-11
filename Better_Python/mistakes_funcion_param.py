# https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument


# https://web.archive.org/web/20200221224620id_/http://effbot.org/zone/default-values.htm
# list is mutable
# Default parameter values are always evaluated when, and only when, the “def” statement they belong to is executed; see:
def function(data=[]):
    data.append(1)
    print(data)


function()
print(id(function))
function()
print(id(function))


def myfunc(value=None):
    if value is None:
        value = []
    value.append(5)
    print(value)


myfunc()
myfunc()
