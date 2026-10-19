# ELETRODEX — O Universo dos Equipamentos Elétricos ⚡

![ELETRODEX Logo](assets/logos/eletrodex-logo.svg)

> **Enciclopédia interativa e gamificada de equipamentos elétricos no Microsoft Power BI.**  
> Projetada para engenheiros eletricistas, integradores solares, analistas de energia e profissionais da indústria moderna.

---

## 🌟 Destaques do Projeto

- **Arquitetura Moderna PBIP**: Estrutura modular com relatório em **PBIR** e modelo semântico em **TMDL**.
- **Modelagem Dimensional Estrita**: Star-Schema profissional com dimensões canônicas, tabelas fato transacionais e tabelas auxiliares desconectadas para comparadores dinâmicos.
- **10 Páginas Completas**:
  1. **Central ELETRODEX**: Visão geral e KPIs dinâmicos da base catalogada.
  2. **Catálogo ELETRODEX**: Grade interativa com filtros multidimensionais por família, fabricante e classe.
  3. **Ficha Técnica Dinâmica**: Detalhamento individual reutilizável com especificações elétricas e links para documentação.
  4. **Comparador A vs B**: Comparação direta entre quaisquer dois equipamentos selecionados de forma independente via DAX.
  5. **Análise de Desempenho**: Gráficos analíticos de dispersão e distribuição por grandezas elétricas.
  6. **Seletor Inteligente**: Mecanismo de recomendação baseado em requisitos de projeto e recursos de segurança.
  7. **Solar & Automação Avançada**: Aplicações de controle dinâmico de injeção zero, inversão de fluxo e SmartLoggers.
  8. **Coleções & Conquistas**: Gamificação editorial por categorias e metas de catálogo.
  9. **Biblioteca Técnica**: Acervo documental oficial com datasheets e manuais rastreáveis.
  10. **Sobre & Auditoria**: Governança, conformidade e transparência metodológica dos dados.
- **Base Técnica Real**: 48 equipamentos elétricos de fabricantes líderes (Huawei, Sungrow, WEG, Schneider, Siemens, ABB, SEL, CLAMPER, etc.), com 37 fontes oficiais auditadas.
- **Identidade Visual Premium**: Tema Dark Tech (`#080F1C`) com acentos em ciano elétrico e verde energético.

---

## 🛠️ Tecnologias Utilizadas

- **Microsoft Power BI Desktop / Service**
- **PBIP / PBIR / TMDL**
- **DAX Avançado** (Modelagem de tabelas desconectadas, medidas com `LOOKUPVALUE`, `REMOVEFILTERS` e `DIVIDE`)
- **Power Query (M)** com parâmetro dinâmico `CaminhoDados`
- **Python 3.12** (Geração automatizada de dados relacionais e testes de integridade)

---

## 🚀 Como Executar o Projeto

1. Clone o repositório ou faça download dos arquivos.
2. Certifique-se de ter o **Microsoft Power BI Desktop** instalado.
3. Dê um duplo clique no arquivo `ELETRODEX.pbip`.
4. Para ajustar o caminho dos dados no Power Query:
   - Vá em **Transformar Dados** -> **Editar Parâmetros**.
   - Atualize `CaminhoDados` para a pasta `data/` local do seu computador.
   - Clique em **Aplicar Alterações**.

Para instruções detalhadas de expansão do catálogo e publicação no Power BI Service, consulte a documentação em [`docs/manual_uso.md`](docs/manual_uso.md).

---

## 📜 Licença e Responsabilidade

Os metadados técnicos e documentos pertencem aos seus respectivos fabricantes. O projeto ELETRODEX é distribuído como código aberto para fins profissionais, educacionais e demonstração técnica.
