from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def getBulletNumFromBulletString(bulletPoints, bulletChar="."):
    """
    Function returns the bullet point numbers of bulleted strings.

    Parameters
    ==========
    bulletPoints: is a iterable that contains the bulleted strings. The bulleted
    strings need to be in the following format. All the function does is tokenizes
    the string elements. It then converts the first element to int and adds it to
    a list before returning the list of ints.

    nn{bulletChar} {followed by a string}

    where nn is an integer and bulletChar can be any charater found in common bullet points. For example
    the following are common valid bullet points.

    '1. The moon is 384,400 km away from Earth'

    or

    '1) The moon is 384,400 km away from Earth'

    In the first example the bulletChar argument is '.'.

    In the second examoke the bulletChar argument is ')'.

    In all examples the bullet strings must have a bullet point number in the formats
    above or the function will fail with errors and its the callers responsibility that
    the arguments are in the correct format for the function to succeed.

    bulletChar: is the charater separater that separates the bullet text from
    the bullet point number.

    Return
    ======
    The function will return a list of all the bullet point numbers as a tuple.
    """

    bulletNos = []

    for bulletpoint in bulletPoints:
        no, string = bulletpoint.split(bulletChar)
        bulletNos.append(int(no))

    return bulletNos