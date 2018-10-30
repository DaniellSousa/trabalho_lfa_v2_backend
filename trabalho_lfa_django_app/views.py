from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.


class Comando():
    comando = ""


class Acao():
    acao = ""


class Transicao():# q0,$-q0,$,R;
    comando = Comando() # q0,$
    acao = Acao() # q0,$,R


def getOrganizeEstados(estados):
    lista = []
    for e in estados:
        if e != ",":
            lista.append(e)

    return lista


def getOrganizeSimbolosEntrada(simbolosEntrada):
    lista = []

    for se in simbolosEntrada:
        if se != ",":
            lista.append(se)

    return lista


def getOrganizeSimbolosCompleto(simbolosCompleto):
    lista = []

    for sc in simbolosCompleto:
        if sc != ",":
            lista.append(sc)

    return lista


def getOrganizeSimbolosFinais(estadosFinais):
    lista = []

    for ef in estadosFinais:
        if ef != ",":
            lista.append(ef)

    return lista


def getOrganizeFuncoes(funcoes): #q0,$-q0,$,R;
    lista = []
    jaPegouComando = False
    podeAddTransicao = False
    strComando = ""
    strAcao = ""

    for f in funcoes:

        if not jaPegouComando:

            if f == "-":
                jaPegouComando = True
                continue

            strComando += f
            continue

        if f == ";":
            podeAddTransicao = True
        else:
            strAcao += f

        if podeAddTransicao:
            trans = Transicao()

            comando = Comando()
            comando.comando = strComando

            trans.comando = comando

            acao = Acao()
            acao.acao = strAcao

            trans.acao = acao

            lista.append(trans)

            strComando = ""
            strAcao = ""

            podeAddTransicao = False

            jaPegouComando = False

    return lista


@api_view(["POST"])
@permission_classes([AllowAny])
def verify_mt(request):
    try:
        estados = request.data.get("estados")
        simbolosEntrada = request.data.get("simbolosEntrada")
        simbolosCompleto = request.data.get("simbolosCompleto")
        estadoInicial = request.data.get("estadoInicial")
        estadosFinais = request.data.get("estadosFinais")
        palavraTeste = request.data.get("palavraTeste")
        funcoes = request.data.get("funcoes")

        saida = 0

        # listaEstados = []
        listaEstados = getOrganizeEstados(estados)

        # listaSimbolosEntrada = []
        listaSimbolosEntrada = getOrganizeSimbolosEntrada(simbolosEntrada)

        # listaSimbolosCompleto = []
        listaSimbolosCompleto = getOrganizeSimbolosCompleto(simbolosCompleto)

        # listaEstadosFinais = []
        listaEstadosFinais = getOrganizeSimbolosFinais(estadosFinais)

        # listaTransicaoFuncoes = []
        listaTransicaoFuncoes = getOrganizeFuncoes(funcoes)

        print (listaEstados)
        print (listaSimbolosEntrada)
        print (listaSimbolosCompleto)
        print (listaEstadosFinais)

        for tf in listaTransicaoFuncoes:
            print ("" + str(tf.comando.comando) + "-" + str(tf.acao.acao))

        # print (listaTransicaoFuncoes)

        return Response({"status": 200, "saida": saida})
    except Exception, e:
        return Response({"status": 300, "saida": 0})