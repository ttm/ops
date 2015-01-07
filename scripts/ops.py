#!/usr/bin/python
#-*- coding: utf-8 -*-
import rdflib as r
import time
T=time.time()

# funções auxiliares
def L(data, datatype_=None,lang_=None):
    if lang_:
        return r.Literal(data, lang=lang_)
    elif datatype_:
        return r.Literal(data, datatype=datatype_)
    else:
        return r.Literal(data)
def G(S,P,O):
    g.add((S,P,O))
U=r.URIRef

# declarações auxiliares
ops = r.Namespace("http://purl.org/socialparticipation/ops/")
xsd = r.namespace.XSD
rdf = r.namespace.RDF
rdfs = r.namespace.RDFS
owl = r.namespace.OWL
foaf = r.namespace.FOAF

g = r.Graph()
g.namespace_manager.bind("ops", ops)
g.namespace_manager.bind("xsd",  xsd)    
g.namespace_manager.bind("rdf",  rdf)    
g.namespace_manager.bind("rdfs", rdfs)    
g.namespace_manager.bind("owl",  owl)
g.namespace_manager.bind("foaf", foaf)

# faz ontologia:
# 1) info sobre esta ontologia
ouri=ops.ops+".owl"
G(ouri,rdf.type,owl.Ontology)
G(ouri,rdfs.label,L(u"OPS",xsd.string))
G(ouri,rdfs.label,L(u"Ontologia de Participação Social","pt"))
G(ouri,rdfs.label,L(u"Social Participation Ontology","en"))
G(ouri,rdfs.label,L(u"Ontología de la participación social","es"))
G(ouri,owl.versionInfo,L(u"0.02",xsd.string))
G(ouri,rdfs.comment,L(u"Ontologia de Participação Social capitaneada pelo Cidade Democrática, Governo Federal Brazileiro e Plataforma Corais, em colaboração direta com dezenas de agentes de toda américa latina","pt"))
G(ouri,rdfs.comment,L(u"Social Participation Ontology headed by Cidade Democrática, Brazilian Federal Government and Corais Platform, in direct collaboration with dozens of actors throughout latin america","en"))
G(ouri,rdfs.comment,L(u"Ontología de Participación Social conducida por el Cidade Democrática, el Gobierno Federal de Brasil y la Plataforma Corais, en colaboración directa con docenas de actores en toda América Latina","en"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/opa"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/ocd"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/aa"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/obs"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/vbs"))


