#coding: utf-8 -*-
import requests
from lxml import etree

id = raw_input("¿Cual es tu identificador de usuario? ")

respuesta = requests.get('http://eskup.elpais.com/Outeskup?f=xml&t=t1-%s' % id)

print respuesta

#raiz = etree.fromstring(respuesta.encode("utf-8"))
#pretty = etree.tostring(raiz, pretty_print = True)
#conten = raiz.findall("contenido")

