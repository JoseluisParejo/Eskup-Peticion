#coding: utf-8 -*-
import requests
from lxml import etree

id = raw_input("¿Cual es tu identificador de usuario? ")

respuesta = requests.get('http://eskup.elpais.com/Outeskup?f=xml&t=t1-%s' % id)


raiz = etree.fromstring(respuesta.text.encode("utf-8"))
pretty = etree.tostring(raiz, pretty_print = True)
conten = raiz.find("mensajes/elements/contenido")

if content = 
print conten.text

