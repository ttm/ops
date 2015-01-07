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
G(ops.Person,  rdfs.label, L(u"Person",0,"en"))
G(ops.Person,  rdfs.label, L(u"Pessoa",0,"pt"))
G(ops.Person,  rdfs.label, L(u"Persona",0,"es"))
G(ops.Person,  rdfs.comment, L(u"a person (social actor is a person)",0,"en"))

G(ops.Organization,  rdf.type, rdfs.Class)
G(ops.Organization,  rdf.type, owl.Class)
G(ops.Organization,  rdfs.label, L(u"Organization",0,"en"))
G(ops.Organization,  rdfs.label, L(u"Organização",0,"pt"))
G(ops.Organization,  rdfs.label, L(u"Organización",0,"es"))
G(ops.Organization,  rdfs.comment, L(u"social actor is a group of individuals, organized formally or informally (e.g. movements, collectives)",0,"en"))

G(ops.Executor,  rdf.type, rdfs.Class)
G(ops.Executor,  rdf.type, owl.Class)
G(ops.Executor,  rdfs.label, L(u"Executor",0,"en"))
G(ops.Executor,  rdfs.label, L(u"Executor",0,"pt"))
G(ops.Executor,  rdfs.label, L(u"Ejecutor",0,"es"))
G(ops.Executor,  rdfs.comment, L(u"performs action directly and is responsible for results",0,"en"))

G(ops.Initiator,  rdf.type, rdfs.Class)
G(ops.Initiator,  rdf.type, owl.Class)
G(ops.Initiator,  rdfs.label, L(u"Initiator",0,"en"))
G(ops.Initiator,  rdfs.label, L(u"Iniciador",0,"pt"))
G(ops.Initiator,  rdfs.label, L(u"Iniciador",0,"es"))
G(ops.Initiator,  rdfs.comment, L(u"originates cause, individually or collaborativelly",0,"en"))

G(ops.Supporter,  rdf.type, rdfs.Class)
G(ops.Supporter,  rdf.type, owl.Class)
G(ops.Supporter,  rdfs.label, L(u"Supporter",0,"en"))
G(ops.Supporter,  rdfs.label, L(u"Apoiador",0,"pt") )
G(ops.Supporter,  rdfs.label, L(u"Apoyador",0,"es") )
G(ops.Supporter,  rdfs.comment, L(u"supports cause with resources of any kind (e.g. cognitive, financial, equipments)",0,"en"))

G(ops.SocialActor,  rdf.type, rdfs.Class)
G(ops.SocialActor,  rdf.type, owl.Class)
G(ops.SocialActor,  rdfs.label,   L(u"Social Actor",0,"en"))
G(ops.SocialActor,  rdfs.label,   L(u"Ator Social",0,"pt"))
G(ops.SocialActor,  rdfs.label,   L(u"Actor Social",0,"es"))
G(ops.SocialActor,  rdfs.comment, L(u"entity that might have a participatory role",0,"en"))
G(ops.Organization, rdfs.subClassOf,ops.SocialActor)
G(ops.Person, rdfs.subClassOf,ops.SocialActor)
G(ops.Initiator, rdfs.subClassOf,ops.SocialActor)
G(ops.Executor, rdfs.subClassOf,ops.SocialActor)
G(ops.Supporter, rdfs.subClassOf,ops.SocialActor)

G(ops.ParticipationCharacteristic,  rdf.type, rdfs.Class)
G(ops.ParticipationCharacteristic,  rdf.type, owl.Class)
G(ops.ParticipationCharacteristic,  rdfs.label, L(u"Participation Characteristic",0,"en")   )
G(ops.ParticipationCharacteristic,  rdfs.label, L(u"Característica de Participação",0,"pt") )
G(ops.ParticipationCharacteristic,  rdfs.label, L(u"Característica de Participación",0,"es"))
G(ops.ParticipationCharacteristic,  rdfs.comment, L(u"the way the participation of specific actor is happening",0,"en"))

G(ops.Cause,  rdf.type, rdfs.Class)
G(ops.Cause,  rdf.type, owl.Class)
G(ops.Cause,  rdfs.label, L(u"Cause",0,"en") )
G(ops.Cause,  rdfs.label, L(u"Causa",0,"pt") )
G(ops.Cause,  rdfs.label, L(u"Causa",0,"es") )
G(ops.Cause,  rdfs.comment, L(u"the motivation for Action",0,"en"))

G(ops.Theme,  rdf.type, rdfs.Class)
G(ops.Theme,  rdf.type, owl.Class)
G(ops.Theme,  rdfs.label, L(u"Theme",0,"en"))
G(ops.Theme,  rdfs.label, L(u"Tema",0,"pt") )
G(ops.Theme,  rdfs.label, L(u"Tema",0,"es") )
G(ops.Theme,  rdfs.comment, L(u"the theme in focus by Action",0,"en"))

G(ops.Action,  rdf.type, rdfs.Class)
G(ops.Action,  rdf.type, owl.Class)
G(ops.Action,  rdfs.label, L(u"Action",0,"en"))
G(ops.Action,  rdfs.label, L(u"Ação",0,"pt")  )
G(ops.Action,  rdfs.label, L(u"Acción",0,"es"))
G(ops.Action,  rdfs.comment, L(u"what is done in terms os social participation",0,"en"))

G(ops.Scope,  rdf.type, rdfs.Class)
G(ops.Scope,  rdf.type, owl.Class)
G(ops.Scope,  rdfs.label, L(u"Scope",0,"en") )
G(ops.Scope,  rdfs.label, L(u"Escopo",0,"pt"))
G(ops.Scope,  rdfs.label, L(u"Ambito",0,"es"))
G(ops.Scope,  rdfs.comment, L(u"the scope of Action",0,"en"))

G(ops.Result,  rdf.type, rdfs.Class)
G(ops.Result,  rdf.type, owl.Class)
G(ops.Result,  rdfs.label, L(u"Result",0,"en")   )
G(ops.Result,  rdfs.label, L(u"Resultado",0,"pt"))
G(ops.Result,  rdfs.label, L(u"Resultado",0,"es"))
G(ops.Result,  rdfs.comment, L(u"the result obtained with Action",0,"en"))

G(ops.Solution,  rdf.type, rdfs.Class)
G(ops.Solution,  rdf.type, owl.Class)
G(ops.Solution,  rdfs.label, L(u"Solution",0,"en"))
G(ops.Solution,  rdfs.label, L(u"Solução",0,"pt") )
G(ops.Solution,  rdfs.label, L(u"Solución",0,"es"))
G(ops.Solution,  rdfs.comment, L(u"solution achieved with Action",0,"en"))

G(ops.Problem,  rdf.type, rdfs.Class)
G(ops.Problem,  rdf.type, owl.Class)
G(ops.Problem,  rdfs.label, L(u"Problem",0,"en") )
G(ops.Problem,  rdfs.label, L(u"Problema",0,"pt"))
G(ops.Problem,  rdfs.label, L(u"Problema",0,"es"))
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
G(ops.Scope,                 rdfs.subClassOf, snap.DependentContinuant)

# Propriedades
G(ops.theme, rdf.type, rdf.Property)
G(ops.theme, rdf.type, owl.ObjectProperty)
G(ops.theme, rdfs.label, L(u"theme",0,"en"))
G(ops.theme, rdfs.label, L(u"tema",0,"pt"))
G(ops.theme, rdfs.label, L(u"tema",0,"es"))
#G(ops.theme, rdfs.domain, ops.Cause)
G(ops.theme, rdfs.range,  ops.Theme)

G(ops.belongsTo, rdf.type, rdf.Property)
G(ops.belongsTo, rdf.type, owl.ObjectProperty)
G(ops.belongsTo, rdfs.label, L(u"belongs to",0,"en"))
G(ops.belongsTo, rdfs.label, L(u"pertence ao",0,"pt"))
G(ops.belongsTo, rdfs.label, L(u"pertence al",0,"es"))
#G(ops.belongsTo, rdfs.domain, ops.Action)
G(ops.belongsTo, rdfs.range, ops.Scope )

G(ops.supports, rdf.type, rdf.Property)
G(ops.supports, rdf.type, owl.ObjectProperty)
G(ops.supports, rdfs.label, L(u"supports",0,"en"))
G(ops.supports, rdfs.label, L(u"apoia",0,"pt"))
G(ops.supports, rdfs.label, L(u"apoya",0,"es"))
#G(ops.supports, rdfs.domain, ops.Supporter)
#G(ops.supports, rdfs.range, ops.Cause )

G(ops.contributesTo, rdf.type, rdf.Property)
G(ops.contributesTo, rdf.type, owl.ObjectProperty)
G(ops.contributesTo, rdfs.label, L(u"contributes to",0,"en"))
G(ops.contributesTo, rdfs.label, L(u"contribui para",0,"pt"))
G(ops.contributesTo, rdfs.label, L(u"contribuye a la",0,"es"))
#G(ops.contributesTo, rdfs.domain, ops.Result)
#G(ops.contributesTo, rdfs.range,  ops.Solution)

G(ops.executes, rdf.type, rdf.Property)
G(ops.executes, rdf.type, owl.ObjectProperty)
G(ops.executes, rdfs.label, L(u"executes",0,"en"))
G(ops.executes, rdfs.label, L(u"executa",0,"pt"))
G(ops.executes, rdfs.label, L(u"ejecuta",0,"es"))
#G(ops.executes, rdfs.domain, ops.Executor)
#G(ops.executes, rdfs.range,  ops.Action)

G(ops.generates, rdf.type, rdf.Property)
G(ops.generates, rdf.type, owl.ObjectProperty)
G(ops.generates, rdfs.label, L(u"generates",0,"en"))
G(ops.generates, rdfs.label, L(u"gera",0,"pt"))
G(ops.generates, rdfs.label, L(u"genera",0,"es"))
#G(ops.generates, rdfs.domain, ops.Problem)
#G(ops.generates, rdfs.range,  ops.Cause)

G(ops.starts, rdf.type, rdf.Property)
G(ops.starts, rdf.type, owl.ObjectProperty)
G(ops.starts, rdfs.label, L(u"starts",0,"en"))
G(ops.starts, rdfs.label, L(u"inicia",0,"pt"))
G(ops.starts, rdfs.label, L(u"inicia",0,"es"))
#G(ops.starts, rdfs.domain, ops.Initiator)
#G(ops.starts, rdfs.range,  ops.Cause)

G(ops.solves, rdf.type, rdf.Property)
G(ops.solves, rdf.type, owl.ObjectProperty)
G(ops.solves, rdfs.label, L(u"solves",0,"en"))
G(ops.solves, rdfs.label, L(u"soluciona",0,"pt"))
G(ops.solves, rdfs.label, L(u"resuelve",0,"es"))
#G(ops.solves, rdfs.domain, ops.Solution)
#G(ops.solves, rdfs.range,  ops.Problem)

G(ops.action, rdf.type, rdf.Property)
G(ops.action, rdf.type, owl.ObjectProperty)
G(ops.action, rdfs.label, L(u"action",0,"en"))
G(ops.action, rdfs.label, L(u"ação",0,"pt"))
G(ops.action, rdfs.label, L(u"acción",0,"es"))
#G(ops.action, rdfs.domain, ops.Cause)
#G(ops.action, rdfs.range,  ops.Action)

G(ops.produces, rdf.type, rdf.Property)
G(ops.produces, rdf.type, owl.ObjectProperty)
G(ops.produces, rdfs.label, L(u"produces",0,"en"))
G(ops.produces, rdfs.label, L(u"produz",0,"pt"))
G(ops.produces, rdfs.label, L(u"produce",0,"es"))
#G(ops.produces, rdfs.domain, ops.Action)
#G(ops.produces, rdfs.range,  ops.Result)

G(ops.proposes, rdf.type, rdf.Property)
G(ops.proposes, rdf.type, owl.ObjectProperty)
G(ops.proposes, rdfs.label, L(u"proposes",0,"en"))
G(ops.proposes, rdfs.label, L(u"propõe",0,"pt"))
G(ops.proposes, rdfs.label, L(u"propone",0,"es"))
#G(ops.proposes, rdfs.domain, ops.Cause)
#G(ops.proposes, rdfs.range,  ops.Solution)

G(ops.trait, rdf.type, rdf.Property)
G(ops.trait, rdf.type, owl.ObjectProperty)
G(ops.trait, rdfs.label, L(u"trait",0,"en"))
G(ops.trait, rdfs.label, L(u"traço",0,"pt"))
G(ops.trait, rdfs.label, L(u"rasgo",0,"es"))
#G(ops.trait, rdfs.domain, ops.SocialActor)
#G(ops.trait, rdfs.range,  ops.ParticipationCharacteristic)




















