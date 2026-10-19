# Dicionário de Dados — ELETRODEX

## 1. DimEquipamentos
| Coluna | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `EquipamentoID` | Int64 (PK) | Identificador numérico sequencial | `1` |
| `CodigoEletrodex` | String | Identificador canônico da enciclopédia | `EDX-0001` |
| `FabricanteID` | Int64 (FK) | Chave estrangeira para DimFabricantes | `1` |
| `CategoriaID` | Int64 (FK) | Chave estrangeira para DimCategorias | `1` |
| `Modelo` | String | Nome comercial oficial do equipamento | `SUN2000-10KTL-M1` |
| `Variante` | String | Versão / submodelo documentado | `High Current Edition` |
| `Descricao` | String | Descrição técnica editorial | `Inversor solar trifásico...` |
| `AplicacaoPrincipal` | String | Aplicação prioritária recomendada | `Geração Distribuída Comercial` |
| `ClasseEditorial` | String | Classificação gamificada (STANDARD, SMART, etc.) | `SMART` |
| `ImagemURL` | WebURL | Link direto para fotografia de alta resolução | `https://...` |
| `DataInclusao` | Date | Data de catalogação | `2026-10-19` |
| `StatusValidacao` | String | Estado do checklist técnico | `Verificado 100%` |

## 2. FatoEspecificacoes
| Coluna | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `EquipamentoID` | Int64 (FK) | Equipamento referenciado | `1` |
| `ParametroID` | Int64 (FK) | Parâmetro técnico canônico | `1` |
| `ValorNumerico` | Double | Valor bruto em número | `10.0` |
| `ValorTexto` | String | Valor formatado com unidade | `10 kW` |
| `UnidadeOriginal` | String | Unidade declarada pelo fabricante | `kW` |
| `ValorNormalizado` | Double | Valor convertido para unidade canônica | `10.0` |
| `CondicaoEnsaio` | String | Condições técnicas e normas | `Nominal CA / IEC 62109` |
| `FonteID` | Int64 (FK) | Chave estrangeira para DimFontes | `1` |
| `PaginaFonte` | String | Localização exata no datasheet | `Pág. 2` |
| `StatusVerificacao` | String | Nível de conferência | `Verificado` |
