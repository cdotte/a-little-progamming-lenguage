# coding=utf-8
from sexpdata import loads, dumps
import io

a = loads("((1))")


def parser(sexpr):

    ssexpr = loads(sexpr)

    expr = ""

    #caso vacio
    if len(ssexpr) == 0:
        expr = "error: expresión inválida " + dumps(ssexpr)
    #caso de que es una lista en el primer elemento, error.
    elif isinstance(ssexpr[0], list):
        expr = "error: expresión inválida " + dumps(ssexpr)
    #numero
    elif dumps(ssexpr[0]).isdigit():
        if len(ssexpr) == 1:
            expr = dumps(ssexpr)
        else:
            expr = "error: expresión inválida " + dumps(ssexpr)
    #suma
    elif dumps(ssexpr[0]) == "+":
        if len(ssexpr) == 3:
            expr = ["add", parser(ssexpr[1]), parser(ssexpr[2])]
        else:
            expr = "error: expresión inválida " + dumps(ssexpr)
    #resta
    elif dumps(ssexpr[0]) == "-":
        if len(ssexpr) == 3:
            expr = ["sub", parser(ssexpr[1]), parser(ssexpr[2])]
        else:
            expr = "error: expresión inválida " + dumps(ssexpr)
    #if0
    elif dumps(ssexpr[0]) == "if0":
        if len(ssexpr) == 4:
            expr = ["if0", parser(ssexpr[1]), parser(ssexpr[2])]
        else:
            expr = "error: expresión inválida " + dumps(ssexpr)
    #aplicacion de funcion
    elif len(ssexpr) == 2:
        expr = ["app", parser(ssexpr[0]), parser(ssexpr[1])]
    elif dumps(ssexpr[0]) == "fun":
        if len(ssexpr) == 3:
            expr = ["fun", parser(ssexpr[1]), parser(ssexpr[2])]
        else:
            expr = "error: expresión inválida " + dumps(ssexpr)
    elif dumps(ssexpr[0]) == "with":
        if len(ssexpr) == 3:
            expr = ["with", parser(ssexpr[1]), parser(ssexpr[2])]
        else:
            expr = "error: expresión inválida " + dumps(ssexpr)
    elif dumps(ssexpr[0]) == "set":
        if len(ssexpr) == 2:
            expr = ["set", parser(ssexpr[1])]
        else:
            expr = "error: expresión inválida " + dumps(ssexpr)
    elif dumps(ssexpr[0]) == "seqn":
        if len(ssexpr) == 3:
            expr = ["seqn", parser(ssexpr[1]), parser(ssexpr[2])]
        else:
            expr = "error: expresión inválida " + dumps(ssexpr)
print (a)


