TASKS = [

    {
        "nome": "classificacao_sentimento",

        "tipo": "classificacao",

        "instrucao":
        "Classifique o sentimento do cliente como POSITIVO, NEGATIVO, NEUTRO ou MISTO.",

        "formato_output":
        "Responda APENAS com uma palavra: POSITIVO, NEGATIVO, NEUTRO ou MISTO.",

        "exemplos_fewshot": [
            {
                "input": "Produto excelente, chegou rapido.",
                "output": "POSITIVO"
            },
            {
                "input": "Veio quebrado e atrasado.",
                "output": "NEGATIVO"
            },
            {
                "input": "Bom preco mas qualidade media.",
                "output": "MISTO"
            }
        ],

        "passos_cot": [
            "Identifique pontos positivos.",
            "Identifique pontos negativos.",
            "Compare os aspectos.",
            "Defina o sentimento final."
        ],

        "persona": "analista_cx"
    },

    {
        "nome": "extracao_dados",

        "tipo": "extracao",

        "instrucao":
        "Extraia produto, preco e problema da mensagem.",

        "formato_output":
        "Retorne um JSON com produto, preco e problema.",

        "exemplos_fewshot": [
            {
                "input": "Notebook Dell de R$3500 com tela quebrada.",
                "output":
                '{"produto":"Notebook Dell","preco":"R$3500","problema":"tela quebrada"}'
            },
            {
                "input": "Mouse Logitech R$120 com clique falhando.",
                "output":
                '{"produto":"Mouse Logitech","preco":"R$120","problema":"clique falhando"}'
            }
        ],

        "passos_cot": [
            "Identifique o nome do produto.",
            "Identifique o valor monetario.",
            "Identifique o defeito relatado.",
            "Monte o JSON final."
        ],

        "persona": "especialista_suporte"
    },

    {
        "nome": "geracao_resposta",

        "tipo": "geracao",

        "instrucao":
        "Gere uma resposta educada e profissional ao cliente.",

        "formato_output":
        "Retorne uma resposta curta e profissional.",

        "exemplos_fewshot": [
            {
                "input": "Meu pedido atrasou.",
                "output":
                "Pedimos desculpas pelo atraso. Estamos verificando sua entrega."
            },
            {
                "input": "Recebi produto errado.",
                "output":
                "Lamentamos o ocorrido. Vamos ajudar na troca imediatamente."
            }
        ],

        "passos_cot": [
            "Entenda o problema do cliente.",
            "Demonstre empatia.",
            "Ofereca solucao.",
            "Finalize profissionalmente."
        ],

        "persona": "gerente_relacionamento"
    }
]