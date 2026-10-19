import pandas as pd
import glob
import os
import sys

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

def check_integrity():
    print("=== INICIANDO VALIDAÇÃO DE QUALIDADE DE DADOS ELETRODEX ===")
    
    # Carregar arquivos
    df_fab = pd.read_csv(os.path.join(DATA_DIR, "fabricantes.csv"), sep=";")
    df_cat = pd.read_csv(os.path.join(DATA_DIR, "categorias.csv"), sep=";")
    df_par = pd.read_csv(os.path.join(DATA_DIR, "parametros.csv"), sep=";")
    df_fon = pd.read_csv(os.path.join(DATA_DIR, "fontes.csv"), sep=";")
    df_eq = pd.read_csv(os.path.join(DATA_DIR, "equipamentos.csv"), sep=";")
    df_esp = pd.read_csv(os.path.join(DATA_DIR, "especificacoes.csv"), sep=";")
    df_apl = pd.read_csv(os.path.join(DATA_DIR, "aplicacoes.csv"), sep=";")
    df_p_apl = pd.read_csv(os.path.join(DATA_DIR, "ponte_equipamento_aplicacao.csv"), sep=";")
    df_rec = pd.read_csv(os.path.join(DATA_DIR, "recursos.csv"), sep=";")
    df_p_rec = pd.read_csv(os.path.join(DATA_DIR, "ponte_equipamento_recurso.csv"), sep=";")

    erros = 0

    # 1. Teste de Unicidade de Chaves Primárias
    for name, df, pk in [
        ("DimFabricantes", df_fab, "FabricanteID"),
        ("DimCategorias", df_cat, "CategoriaID"),
        ("DimParametros", df_par, "ParametroID"),
        ("DimFontes", df_fon, "FonteID"),
        ("DimEquipamentos", df_eq, "EquipamentoID"),
        ("DimAplicacoes", df_apl, "AplicacaoID"),
        ("DimRecursos", df_rec, "RecursoID")
    ]:
        dups = df[pk].duplicated().sum()
        if dups > 0:
            print(f"[FALHA] Chave primária duplicada em {name}: {dups} registros!")
            erros += 1
        else:
            print(f"[OK] PK {name}.{pk} é 100% única ({len(df)} linhas).")

    # 2. Teste de Chaves Estrangeiras Órfãs em DimEquipamentos
    orf_fab = set(df_eq["FabricanteID"]) - set(df_fab["FabricanteID"])
    if orf_fab:
        print(f"[FALHA] Fabricantes órfãos em DimEquipamentos: {orf_fab}")
        erros += 1
    else:
        print("[OK] FK DimEquipamentos -> DimFabricantes consistente.")

    orf_cat = set(df_eq["CategoriaID"]) - set(df_cat["CategoriaID"])
    if orf_cat:
        print(f"[FALHA] Categorias órfãs em DimEquipamentos: {orf_cat}")
        erros += 1
    else:
        print("[OK] FK DimEquipamentos -> DimCategorias consistente.")

    # 3. Teste de Integridade em FatoEspecificacoes
    orf_esp_eq = set(df_esp["EquipamentoID"]) - set(df_eq["EquipamentoID"])
    orf_esp_par = set(df_esp["ParametroID"]) - set(df_par["ParametroID"])
    orf_esp_fon = set(df_esp["FonteID"]) - set(df_fon["FonteID"])
    if orf_esp_eq or orf_esp_par or orf_esp_fon:
        print(f"[FALHA] Órfãos em FatoEspecificacoes! Eq: {orf_esp_eq}, Par: {orf_esp_par}, Fon: {orf_esp_fon}")
        erros += 1
    else:
        print(f"[OK] FatoEspecificacoes ({len(df_esp)} fatos) perfeitamente relacionada com Equipamentos, Parâmetros e Fontes.")

    # 4. Distribuição por Categoria
    contagem_cat = df_eq["CategoriaID"].value_counts().to_dict()
    print("\n[INFO] Distribuição de Equipamentos por Categoria:")
    for cat_id, qtd in sorted(contagem_cat.items()):
        nome = df_cat.loc[df_cat['CategoriaID'] == cat_id, 'Nome'].values[0]
        print(f"  - Categoria {cat_id} ({nome}): {qtd} equipamentos")

    print("\n=======================================================")
    if erros == 0:
        print(">>> SUCESSO TOTAL: 0 INCONSISTÊNCIAS IDENTIFICADAS. BASE PRONTA PARA MODELAGEM! <<<")
        return 0
    else:
        print(f">>> FORAM ENCONTRADOS {erros} ERROS. REVISE OS DADOS. <<<")
        return 1

if __name__ == "__main__":
    sys.exit(check_integrity())
