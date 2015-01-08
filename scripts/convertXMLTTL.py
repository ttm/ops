#!/usr/bin/python
#-*- coding: utf-8 -*-
import rdflib as r
import time, os
T=time.time()
l=os.listdir("../rdf/")
l_=[ll for ll in l if ll.endswith(".rdf")]
for ll in l_:
    g=r.Graph()
    name="../rdf/"+ll
    g.parse(name)
    f=open(name.replace(".rdf",".ttl"),"wb")
    f.write(g.serialize(format="turtle"))
    f.close()
l_=[ll for ll in l if ll.endswith(".owl")]
for ll in l_:
    g=r.Graph()
    name="../rdf/"+ll
    g.parse(name)
    f=open(name.replace(".owl",".ttl"),"wb")
    f.write(g.serialize(format="turtle"))
    f.close()
