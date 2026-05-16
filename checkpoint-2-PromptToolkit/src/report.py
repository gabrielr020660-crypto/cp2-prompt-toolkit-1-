import os
import pandas as pd
import matplotlib.pyplot as plt

OUTPUT_DIR = "output"
GRAFICOS_DIR = "output/graficos"

os.makedirs(GRAFICOS_DIR, exist_ok=True)

def gerar_tabela(resultados):

    df = pd.DataFrame(resultados)

    caminho = f"{OUTPUT_DIR}/resultados.csv"

    df.to_csv(caminho, index=False)

    return df


def grafico_acuracia(df):

    media = df.groupby("tecnica")["acuracia"].mean()

    plt.figure(figsize=(8, 5))

    media.plot(kind="bar")

    plt.title("Acurácia Média por Técnica")

    plt.ylabel("Acurácia")

    plt.tight_layout()

    plt.savefig(f"{GRAFICOS_DIR}/grafico_acuracia.png")

    plt.close()


def grafico_custo(df):

    df["tokens_totais"] = (
        df["tokens_prompt"] +
        df["tokens_resposta"]
    )

    media = df.groupby("tecnica")["tokens_totais"].mean()

    plt.figure(figsize=(8, 5))

    media.plot(kind="bar")

    plt.title("Tokens Médios por Técnica")

    plt.ylabel("Tokens")

    plt.tight_layout()

    plt.savefig(f"{GRAFICOS_DIR}/grafico_custo.png")

    plt.close()


def grafico_tempo(df):

    media = df.groupby("tecnica")["tempo_ms"].mean()

    plt.figure(figsize=(8, 5))

    media.plot(kind="bar")

    plt.title("Tempo Médio por Técnica")

    plt.ylabel("Tempo (ms)")

    plt.tight_layout()

    plt.savefig(f"{GRAFICOS_DIR}/grafico_tempo.png")

    plt.close()


def recomendar(df):

    ranking = (
        df.groupby("tecnica")["acuracia"]
        .mean()
        .sort_values(ascending=False)
    )

    melhor = ranking.index[0]

    return melhor


def gerar_relatorio(resultados):

    df = gerar_tabela(resultados)

    grafico_acuracia(df)

    grafico_custo(df)

    grafico_tempo(df)

    melhor = recomendar(df)

    print("\n========== RELATÓRIO ==========")

    print(df)

    print("\nMelhor técnica:", melhor)