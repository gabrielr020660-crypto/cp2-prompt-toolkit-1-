import json
import tiktoken

def contar_tokens(texto):

    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(str(texto)))


def medir_acuracia(resposta, esperado):

    resposta = str(resposta).strip().lower()
    esperado = str(esperado).strip().lower()

    if resposta == esperado:
        return 1

    if esperado in resposta:
        return 1

    return 0


def medir_consistencia(respostas):

    if not respostas:
        return 0

    iguais = respostas.count(respostas[0])

    return round((iguais / len(respostas)) * 100, 2)


def testar_temperatura(client, prompt, system=""):

    temperaturas = [0.1, 0.5, 1.0]

    resultados = []

    for temp in temperaturas:

        resposta = client.chat(
            prompt=prompt,
            system=system,
            temp=temp
        )

        resultados.append({
            "temperatura": temp,
            "resposta": resposta["resposta"]
        })

    return resultados


def avaliar_resultado(resposta, esperado):

    return medir_acuracia(resposta, esperado)