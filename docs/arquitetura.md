# Arquitetura Técnica — ELETRODEX

## 1. Visão Geral da Solução
O **ELETRODEX** é uma enciclopédia interativa desenvolvida em **Microsoft Power BI** com base no novo formato moderno para desenvolvedores:
- **PBIP** (Power BI Project): Formato modular compatível com Git.
- **PBIR** (Power BI Report): Relatório em JSON declarativo e versionável.
- **TMDL** (Tabular Model Definition Language): Definição semântica limpa, hierárquica e legível.

## 2. Modelo Dimensional Star-Schema
O semântico adota modelagem dimensional estrita para garantir performance analítica e escalabilidade:

### Dimensões Centrais:
- `DimFabricantes`: 16 fabricantes globais e nacionais (Huawei, Sungrow, WEG, Schneider, ABB, SEL, Siemens, CLAMPER, etc.).
- `DimCategorias`: 8 famílias tecnológicas estruturadas com paleta e ícones próprios.
- `DimEquipamentos`: 48 equipamentos elétricos com identificação padronizada (`EDX-0001` a `EDX-0048`), fotos e metadados.
- `DimParametros`: 14 parâmetros técnicos canônicos (potência, tensões, grau IP, correntes de ruptura, funções ANSI).
- `DimFontes`: 37 documentos oficiais catalogados (datasheets, manuais de operação e catálogos técnicos).
- `DimAplicacoes`: 6 perfis de aplicação (Solar, Injeção Zero, Média Tensão, Automação, DPS).
- `DimRecursos`: 8 recursos tecnológicos de vanguarda (AFCI, Injeção Zero, Modbus, IEC 61850).
- `DimColecoes`: 5 coleções gamificadas para exploração editorial.

### Tabelas Fato e Pontes (Bridges):
- `FatoEspecificacoes`: Tabela fato transacional com 135+ parâmetros verificados, condições de ensaio, unidades canônicas e rastreabilidade documental direta.
- `PonteEquipamentoAplicacao`: N:N entre equipamentos e aplicações.
- `PonteEquipamentoRecurso`: N:N entre equipamentos e recursos com estado de certificação em datasheet.

### Tabelas Desconectadas para Análise Comparativa:
- `AuxEquipamentoA` e `AuxEquipamentoB`: Tabelas calculadas DAX para viabilizar a seleção independente no Comparador de Equipamentos (Página 04).

## 3. Camada DAX e Métricas
- Medidas centralizadas na tabela `Medidas`.
- Cálculos dinâmicos de diferenças absolutas e percentuais entre grandezas do Equipamento A e B.
- Auditoria e conformidade em tempo real.
- Parametrização dinâmica do caminho dos dados (`CaminhoDados`) no Power Query.
