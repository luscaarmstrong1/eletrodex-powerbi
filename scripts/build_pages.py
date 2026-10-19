import json
import os

PAGES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ELETRODEX.Report", "definition", "pages")

pages_meta = [
    {
        "id": "central_eletrodex",
        "displayName": "01 - Central ELETRODEX",
        "description": "Página inicial de impacto, visão geral do universo elétrico catalogado e vitrine de destaques.",
        "visuals": [
            {"id": "header_title", "type": "textbox", "title": "ELETRODEX — Explore. Compare. Domine a tecnologia elétrica.", "position": {"x": 20, "y": 20, "width": 1240, "height": 70}},
            {"id": "card_total_eq", "type": "card", "measure": "[Total Equipamentos]", "position": {"x": 20, "y": 100, "width": 290, "height": 110}},
            {"id": "card_total_fab", "type": "card", "measure": "[Total Fabricantes]", "position": {"x": 330, "y": 100, "width": 290, "height": 110}},
            {"id": "card_total_cat", "type": "card", "measure": "[Total Categorias]", "position": {"x": 640, "y": 100, "width": 290, "height": 110}},
            {"id": "card_total_fichas", "type": "card", "measure": "[Fichas 100% Verificadas]", "position": {"x": 950, "y": 100, "width": 310, "height": 110}},
            {"id": "bar_eq_por_categoria", "type": "barChart", "category": "DimCategorias[Nome]", "measure": "[Total Equipamentos]", "position": {"x": 20, "y": 230, "width": 600, "height": 450}},
            {"id": "table_destaques", "type": "tableEx", "columns": ["DimEquipamentos[CodigoEletrodex]", "DimFabricantes[Nome]", "DimEquipamentos[Modelo]", "DimCategorias[Nome]", "DimEquipamentos[ClasseEditorial]"], "position": {"x": 640, "y": 230, "width": 620, "height": 450}}
        ]
    },
    {
        "id": "catalogo_eletrodex",
        "displayName": "02 - Catálogo ELETRODEX",
        "description": "Grade interativa de exploração de equipamentos com múltiplos filtros cruzados e acesso dinâmico à ficha.",
        "visuals": [
            {"id": "slicer_categoria", "type": "slicer", "field": "DimCategorias[Nome]", "position": {"x": 20, "y": 20, "width": 260, "height": 180}},
            {"id": "slicer_fabricante", "type": "slicer", "field": "DimFabricantes[Nome]", "position": {"x": 20, "y": 210, "width": 260, "height": 220}},
            {"id": "slicer_classe", "type": "slicer", "field": "DimEquipamentos[ClasseEditorial]", "position": {"x": 20, "y": 440, "width": 260, "height": 240}},
            {"id": "grid_equipamentos", "type": "tableEx", "columns": ["DimEquipamentos[ImagemURL]", "DimEquipamentos[CodigoEletrodex]", "DimFabricantes[Nome]", "DimEquipamentos[Modelo]", "DimCategorias[Nome]", "DimEquipamentos[ClasseEditorial]", "DimEquipamentos[AplicacaoPrincipal]", "DimEquipamentos[StatusValidacao]"], "position": {"x": 300, "y": 20, "width": 960, "height": 660}}
        ]
    },
    {
        "id": "ficha_tecnica",
        "displayName": "03 - Ficha Técnica Dinâmica",
        "description": "Detalhamento dinâmico e contextual por equipamento selecionado com parâmetros elétricos e links de datasheet.",
        "visuals": [
            {"id": "slicer_selecao_eq", "type": "slicer", "field": "DimEquipamentos[Modelo]", "position": {"x": 20, "y": 20, "width": 320, "height": 120}},
            {"id": "card_id_selecionado", "type": "card", "measure": "[Equipamento Selecionado Codigo]", "position": {"x": 360, "y": 20, "width": 240, "height": 120}},
            {"id": "card_nome_selecionado", "type": "card", "measure": "[Equipamento Selecionado Nome]", "position": {"x": 620, "y": 20, "width": 640, "height": 120}},
            {"id": "table_especificacoes_eq", "type": "tableEx", "columns": ["DimParametros[Grupo]", "DimParametros[Nome]", "FatoEspecificacoes[ValorTexto]", "FatoEspecificacoes[CondicaoEnsaio]", "DimFontes[NomeDocumento]"], "position": {"x": 20, "y": 160, "width": 800, "height": 520}},
            {"id": "matrix_recursos_eq", "type": "tableEx", "columns": ["DimRecursos[Grupo]", "DimRecursos[Nome]", "PonteEquipamentoRecurso[EstadoVerificacao]"], "position": {"x": 840, "y": 160, "width": 420, "height": 520}}
        ]
    },
    {
        "id": "comparador",
        "displayName": "04 - Comparador de Equipamentos",
        "description": "Comparação lado a lado entre dois equipamentos independentes A vs B com cálculo dinâmico de diferenças.",
        "visuals": [
            {"id": "slicer_eq_a", "type": "slicer", "field": "AuxEquipamentoA[NomeDisplay_A]", "position": {"x": 20, "y": 20, "width": 400, "height": 140}},
            {"id": "card_nome_a", "type": "card", "measure": "[Comparador Equipamento A Nome]", "position": {"x": 20, "y": 180, "width": 400, "height": 100}},
            {"id": "slicer_eq_b", "type": "slicer", "field": "AuxEquipamentoB[NomeDisplay_B]", "position": {"x": 860, "y": 20, "width": 400, "height": 140}},
            {"id": "card_nome_b", "type": "card", "measure": "[Comparador Equipamento B Nome]", "position": {"x": 860, "y": 180, "width": 400, "height": 100}},
            {"id": "grid_comparador_diff", "type": "matrix", "rows": ["DimParametros[Grupo]", "DimParametros[Nome]"], "values": ["[Comparador Valor Texto A]", "[Comparador Valor Texto B]", "[Comparador Diferença Absoluta]", "[Comparador Diferença Percentual]"], "position": {"x": 20, "y": 300, "width": 1240, "height": 380}}
        ]
    },
    {
        "id": "analise_desempenho",
        "displayName": "05 - Análise de Desempenho",
        "description": "Visualização analítica e rankings de potências nominais, eficiências máximas e parâmetros técnicos.",
        "visuals": [
            {"id": "slicer_cat_perf", "type": "slicer", "field": "DimCategorias[Nome]", "position": {"x": 20, "y": 20, "width": 260, "height": 200}},
            {"id": "bar_potencias", "type": "barChart", "category": "DimEquipamentos[Modelo]", "measure": "MAX(FatoEspecificacoes[ValorNormalizado])", "position": {"x": 300, "y": 20, "width": 960, "height": 340}},
            {"id": "scatter_eficiencia_potencia", "type": "scatterChart", "x": "Potência (kW)", "y": "Eficiência (%)", "position": {"x": 300, "y": 380, "width": 960, "height": 300}}
        ]
    },
    {
        "id": "seletor_inteligente",
        "displayName": "06 - Seletor Inteligente",
        "description": "Motor de recomendação preliminar por requisitos de projeto (tensão, potência, MPPTs, injeção zero).",
        "visuals": [
            {"id": "slicer_sel_classe", "type": "slicer", "field": "DimEquipamentos[ClasseEditorial]", "position": {"x": 20, "y": 20, "width": 260, "height": 160}},
            {"id": "slicer_sel_aplicacao", "type": "slicer", "field": "DimAplicacoes[Nome]", "position": {"x": 20, "y": 200, "width": 260, "height": 220}},
            {"id": "slicer_sel_recurso", "type": "slicer", "field": "DimRecursos[Nome]", "position": {"x": 20, "y": 440, "width": 260, "height": 240}},
            {"id": "table_candidatos", "type": "tableEx", "columns": ["DimEquipamentos[CodigoEletrodex]", "DimFabricantes[Nome]", "DimEquipamentos[Modelo]", "DimCategorias[Nome]", "DimEquipamentos[AplicacaoPrincipal]", "DimEquipamentos[StatusValidacao]"], "position": {"x": 300, "y": 20, "width": 960, "height": 660}}
        ]
    },
    {
        "id": "solar_automacao",
        "displayName": "07 - Solar & Automação Avançada",
        "description": "Módulo especializado em controle de injeção zero, inversão de fluxo e orquestração SmartLogger.",
        "visuals": [
            {"id": "text_cenario_didatico", "type": "textbox", "title": "Cenários Didáticos de Engenharia: Usina Solar 10 kW com Injeção Máxima de 8 kW e Monitoramento Smart Meter", "position": {"x": 20, "y": 20, "width": 1240, "height": 80}},
            {"id": "table_equipamentos_injecao_zero", "type": "tableEx", "columns": ["DimFabricantes[Nome]", "DimEquipamentos[Modelo]", "DimCategorias[Nome]", "DimEquipamentos[Descricao]"], "position": {"x": 20, "y": 120, "width": 600, "height": 560}},
            {"id": "matrix_arquitetura_fluxo", "type": "tableEx", "columns": ["DimRecursos[Nome]", "DimRecursos[Descricao]"], "position": {"x": 640, "y": 120, "width": 620, "height": 560}}
        ]
    },
    {
        "id": "colecoes_conquistas",
        "displayName": "08 - Coleções & Conquistas",
        "description": "Gamificação editorial com insígnias e barras de progresso do catálogo de engenharia elétrica.",
        "visuals": [
            {"id": "card_badge_solar", "type": "card", "measure": "'Mestres da Energia Solar (15/15)'", "position": {"x": 20, "y": 20, "width": 380, "height": 130}},
            {"id": "card_badge_protecao", "type": "card", "measure": "'Guardiões da Proteção (17/17)'", "position": {"x": 440, "y": 20, "width": 380, "height": 130}},
            {"id": "card_badge_transformacao", "type": "card", "measure": "'Gigantes da Transformação (6/6)'", "position": {"x": 860, "y": 20, "width": 400, "height": 130}},
            {"id": "table_colecoes_detalhe", "type": "tableEx", "columns": ["DimColecoes[Nome]", "DimColecoes[Descricao]", "DimColecoes[MetaEquipamentos]"], "position": {"x": 20, "y": 180, "width": 1240, "height": 500}}
        ]
    },
    {
        "id": "biblioteca_tecnica",
        "displayName": "09 - Biblioteca Técnica",
        "description": "Acervo oficial de datasheets, manuais de operação e catálogos com URLs verificadas e revisões.",
        "visuals": [
            {"id": "slicer_tipo_doc", "type": "slicer", "field": "DimFontes[TipoDocumento]", "position": {"x": 20, "y": 20, "width": 260, "height": 220}},
            {"id": "slicer_fab_doc", "type": "slicer", "field": "DimFontes[Fabricante]", "position": {"x": 20, "y": 260, "width": 260, "height": 420}},
            {"id": "table_documentos", "type": "tableEx", "columns": ["DimFontes[FonteID]", "DimFontes[Fabricante]", "DimFontes[NomeDocumento]", "DimFontes[TipoDocumento]", "DimFontes[Revisao]", "DimFontes[DataPublicacao]", "DimFontes[StatusLink]", "DimFontes[URL]"], "position": {"x": 300, "y": 20, "width": 960, "height": 660}}
        ]
    },
    {
        "id": "sobre_auditoria",
        "displayName": "10 - Sobre o Projeto & Auditoria",
        "description": "Manifesto de desenvolvimento, governança de dados, conformidade e metadados de engenharia.",
        "visuals": [
            {"id": "card_conformidade", "type": "card", "measure": "[Status Conformidade Técnica]", "position": {"x": 20, "y": 20, "width": 600, "height": 100}},
            {"id": "card_cobertura", "type": "card", "measure": "[% Cobertura Documental]", "position": {"x": 640, "y": 20, "width": 620, "height": 100}},
            {"id": "textbox_manifesto", "type": "textbox", "title": "ELETRODEX — O Universo dos Equipamentos Elétricos. Desenvolvido para conectar engenharia de potência, governança de dados e experiência digital premium.", "position": {"x": 20, "y": 140, "width": 1240, "height": 180}},
            {"id": "table_auditoria_stats", "type": "tableEx", "columns": ["DimCategorias[Nome]", "DimCategorias[Descricao]"], "position": {"x": 20, "y": 340, "width": 1240, "height": 340}}
        ]
    }
]

for p in pages_meta:
    page_folder = os.path.join(PAGES_DIR, p["id"])
    os.makedirs(page_folder, exist_ok=True)
    page_json_path = os.path.join(page_folder, "page.json")
    page_data = {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/1.0.0/schema.json",
        "name": p["id"],
        "displayName": p["displayName"],
        "displayOption": "FitToPage",
        "width": 1280,
        "height": 720,
        "visuals": p["visuals"]
    }
    with open(page_json_path, "w", encoding="utf-8") as f:
        json.dump(page_data, f, indent=2, ensure_ascii=False)
    print(f"Página gerada: {p['displayName']} ({p['id']})")

print("\nTodas as 10 páginas PBIR foram geradas com sucesso.")
