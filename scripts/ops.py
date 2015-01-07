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
snap = r.Namespace("http://www.ifomis.org/bfo/1.1/snap#")
span = r.Namespace("http://www.ifomis.org/bfo/1.1/span#")
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
G(ouri,rdfs.label,L(u"Ontologia de Participação Social",0,"pt"))
G(ouri,rdfs.label,L(u"Social Participation Ontology",0,"en"))
G(ouri,rdfs.label,L(u"Ontología de la participación social",0,"es"))
G(ouri,owl.versionInfo,L(u"0.02",xsd.string))
G(ouri,rdfs.comment,L(u"Ontologia de Participação Social capitaneada pelo Cidade Democrática, Governo Federal Brazileiro e Plataforma Corais, em colaboração direta com dezenas de agentes de toda américa latina",0,"pt"))
G(ouri,rdfs.comment,L(u"Social Participation Ontology headed by Cidade Democrática, Brazilian Federal Government and Corais Platform, in direct collaboration with dozens of actors throughout latin america",0,"en"))
G(ouri,rdfs.comment,L(u"Ontología de Participación Social conducida por el Cidade Democrática, el Gobierno Federal de Brasil y la Plataforma Corais, en colaboración directa con docenas de actores en toda América Latina",0,"es"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/opa"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/ocd"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/aa"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/obs"))
G(ouri,rdfs.seeAlso,U(u"http://purl.org/socialparticipation/vbs"))

G(ops.Person,  rdf.type, rdfs.Class)
G(ops.Person,  rdf.type, owl.Class)
G(ops.Person,  rdfs.label, L(u"Person",0,"en")
G(ops.Person,  rdfs.label, L(u"Pessoa",0,"pt")
G(ops.Person,  rdfs.label, L(u"Persona",0,"es")
G(ops.Person,  rdfs.comment, L(u"a person (social actor is a person)",0,"en"))

G(ops.Organization,  rdf.type, rdfs.Class)
G(ops.Organization,  rdf.type, owl.Class)
G(ops.Organization,  rdfs.label, L(u"Organization",0,"en")
G(ops.Organization,  rdfs.label, L(u"Organização",0,"pt")
G(ops.Organization,  rdfs.label, L(u"Organización",0,"es")
G(ops.Organization,  rdfs.comment, L(u"social actor is a group of individuals, organized formally or informally (e.g. movements, collectives)",0,"en"))

G(ops.Executor,  rdf.type, rdfs.Class)
G(ops.Executor,  rdf.type, owl.Class)
G(ops.Executor,  rdfs.label, L(u"Executor",0,"en")
G(ops.Executor,  rdfs.label, L(u"Executor",0,"pt")
G(ops.Executor,  rdfs.label, L(u"Ejecutor",0,"es")
G(ops.Executor,  rdfs.comment, L(u"performs action directly and is responsible for results",0,"en"))

G(ops.Initiator,  rdf.type, rdfs.Class)
G(ops.Initiator,  rdf.type, owl.Class)
G(ops.Initiator,  rdfs.label, L(u"Initiator",0,"en")
G(ops.Initiator,  rdfs.label, L(u"Iniciador",0,"pt")
G(ops.Initiator,  rdfs.label, L(u"Iniciador",0,"es")
G(ops.Initiator,  rdfs.comment, L(u"originates cause, individually or collaborativelly",0,"en"))

G(ops.Supporter,  rdf.type, rdfs.Class)
G(ops.Supporter,  rdf.type, owl.Class)
G(ops.Supporter,  rdfs.label, L(u"Supporter",0,"en")
G(ops.Supporter,  rdfs.label, L(u"Apoiador",0,"pt")
G(ops.Supporter,  rdfs.label, L(u"Apoyador",0,"es")
G(ops.Supporter,  rdfs.comment, L(u"supports cause with resources of any kind (e.g. cognitive, financial, equipments)",0,"en"))

G(ops.SocialActor,  rdf.type, rdfs.Class)
G(ops.SocialActor,  rdf.type, owl.Class)
G(ops.SocialActor,  rdfs.label,   L(u"Social Actor",0,"en")
G(ops.SocialActor,  rdfs.label,   L(u"Ator Social",0,"pt")
G(ops.SocialActor,  rdfs.label,   L(u"Actor Social",0,"es")
G(ops.SocialActor,  rdfs.comment, L(u"entity that might have a participatory role",0,"en"))
G(ops.Organization, rdfs.subClassOf,ops.SocialActor)
G(ops.Person, rdfs.subClassOf,ops.SocialActor)
G(ops.Initiator, rdfs.subClassOf,ops.SocialActor)
G(ops.Executor, rdfs.subClassOf,ops.SocialActor)
G(ops.Supporter, rdfs.subClassOf,ops.SocialActor)

G(ops.ParticipationCharacteristic,  rdf.type, rdfs.Class)
G(ops.ParticipationCharacteristic,  rdf.type, owl.Class)
G(ops.ParticipationCharacteristic,  rdfs.label, L(u"Participation Characteristic",0,"en")
G(ops.ParticipationCharacteristic,  rdfs.label, L(u"Característica de Participação",0,"pt")
G(ops.ParticipationCharacteristic,  rdfs.label, L(u"Característica de Participación",0,"es")
G(ops.ParticipationCharacteristic,  rdfs.comment, L(u"the way the participation of specific actor is happening",0,"en"))

G(ops.Cause,  rdf.type, rdfs.Class)
G(ops.Cause,  rdf.type, owl.Class)
G(ops.Cause,  rdfs.label, L(u"Cause",0,"en")
G(ops.Cause,  rdfs.label, L(u"Causa",0,"pt")
G(ops.Cause,  rdfs.label, L(u"Causa",0,"es")
G(ops.Cause,  rdfs.comment, L(u"the motivation for Action",0,"en"))

G(ops.Theme,  rdf.type, rdfs.Class)
G(ops.Theme,  rdf.type, owl.Class)
G(ops.Theme,  rdfs.label, L(u"Theme",0,"en")
G(ops.Theme,  rdfs.label, L(u"Tema",0,"pt")
G(ops.Theme,  rdfs.label, L(u"Tema",0,"es")
G(ops.Theme,  rdfs.comment, L(u"the theme in focus by Action",0,"en"))

G(ops.Action,  rdf.type, rdfs.Class)
G(ops.Action,  rdf.type, owl.Class)
G(ops.Action,  rdfs.label, L(u"Action",0,"en")
G(ops.Action,  rdfs.label, L(u"Ação",0,"pt")
G(ops.Action,  rdfs.label, L(u"Acción",0,"es")
G(ops.Action,  rdfs.comment, L(u"what is done in terms os social participation",0,"en"))

G(ops.Scope,  rdf.type, rdfs.Class)
G(ops.Scope,  rdf.type, owl.Class)
G(ops.Scope,  rdfs.label, L(u"Scope",0,"en")
G(ops.Scope,  rdfs.label, L(u"Escopo",0,"pt")
G(ops.Scope,  rdfs.label, L(u"Ambito",0,"es")
G(ops.Scope,  rdfs.comment, L(u"the scope of Action",0,"en"))

G(ops.Result,  rdf.type, rdfs.Class)
G(ops.Result,  rdf.type, owl.Class)
G(ops.Result,  rdfs.label, L(u"Result",0,"en")
G(ops.Result,  rdfs.label, L(u"Resultado",0,"pt")
G(ops.Result,  rdfs.label, L(u"Resultado",0,"es")
G(ops.Result,  rdfs.comment, L(u"the result obtained with Action",0,"en"))

G(ops.Solution,  rdf.type, rdfs.Class)
G(ops.Solution,  rdf.type, owl.Class)
G(ops.Solution,  rdfs.label, L(u"Solution",0,"en")
G(ops.Solution,  rdfs.label, L(u"Solução",0,"pt")
G(ops.Solution,  rdfs.label, L(u"Solución",0,"es")
G(ops.Solution,  rdfs.comment, L(u"solution achieved with Action",0,"en"))

G(ops.Problem,  rdf.type, rdfs.Class)
G(ops.Problem,  rdf.type, owl.Class)
G(ops.Problem,  rdfs.label, L(u"Problem",0,"en")
G(ops.Problem,  rdfs.label, L(u"Problema",0,"pt")
G(ops.Problem,  rdfs.label, L(u"Problema",0,"es")
G(ops.Problem,  rdfs.comment, L(u"the problem that the Action aims to solve",0,"en"))


# Relações disjoint entre as classes
G(ops.Organization, owl.disjointWith,ops.Person)

## Conexão com ontologias de topo: FOAF e BFO
# FOAF
G(ops.Person, rdfs.subClassOf,       foaf.Person)
G(ops.Organization, rdfs.subClassOf, foaf.Organization)

# BFO
G(ops.Action, rdfs.subClassOf, span.ProcessualEntity)

G(ops.Theme,   rdfs.subClassOf, snap.IndependentContinuant)
G(ops.Cause,   rdfs.subClassOf, snap.IndependentContinuant)
G(ops.Problem, rdfs.subClassOf, snap.IndependentContinuant)

G(ops.Person,       rdfs.subClassOf, snap.MaterialEntity)
G(ops.Organization, rdfs.subClassOf, snap.MaterialEntity)
G(ops.SocialActor,  rdfs.subClassOf, snap.MaterialEntity)
G(ops.Executor,     rdfs.subClassOf, snap.MaterialEntity)
G(ops.Initiator,    rdfs.subClassOf, snap.MaterialEntity)
G(ops.Supporter,    rdfs.subClassOf, snap.MaterialEntity)
snap.DependentContinuant

G(ops.Solution,                    rdfs.subClassOf, snap.DependentContinuant)
G(ops.Result,                      rdfs.subClassOf, snap.DependentContinuant)
G(ops.ParticipationCharacteristic, rdfs.subClassOf, snap.DependentContinuant)
G(ops.ActionScope,                 rdfs.subClassOf, snap.DependentContinuant)

# Propriedades
