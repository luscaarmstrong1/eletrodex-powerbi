# Manual de Uso e Guia de Publicação — ELETRODEX

## 1. Como Abrir no Power BI Desktop
1. Instale o **Microsoft Power BI Desktop** (versão 2023+ com suporte a PBIP habilitado).
2. Dê um duplo clique no arquivo:
   `ELETRODEX.pbip`
3. O Power BI Desktop carregará o relatório modular (`ELETRODEX.Report`) e o modelo semântico TMDL (`ELETRODEX.SemanticModel`).

## 2. Como Alterar o Caminho da Base de Dados
O projeto utiliza um parâmetro M para portabilidade total:
1. No menu superior do Power BI Desktop, clique em **Transformar Dados** -> **Editar Parâmetros**.
2. Altere o parâmetro `CaminhoDados` para a pasta onde os arquivos CSV estão localizados no seu computador (com barra no final):
   `C:/Caminho/Para/eletrodex-powerbi/data/`
3. Clique em **Aplicar Alterações**.

## 3. Como Expandir o Catálogo com Novos Equipamentos
1. Abra `data/equipamentos.csv` em qualquer editor de planilhas ou texto.
2. Adicione uma nova linha com o próximo `EquipamentoID` sequencial (`49`), código `EDX-0049`, fabricante, categoria e URLs.
3. Adicione as especificações do novo equipamento em `data/especificacoes.csv`.
4. No Power BI Desktop, clique no botão **Atualizar** na guia Página Inicial.
5. O novo equipamento surgirá automaticamente no **Catálogo**, na **Ficha Técnica**, no **Comparador** e nas **Coleções**, sem necessidade de recriar nenhum visual!

## 4. Guia de Publicação no Power BI Service
1. Faça login com sua conta corporativa/estudante no Power BI Desktop.
2. Clique em **Publicar** -> selecione seu **Workspace**.
3. No Power BI Service:
   - Configure o Gateway de Dados ou o caminho na nuvem (ex: OneDrive / SharePoint) caso queira atualização agendada.
   - Para divulgar no LinkedIn / Portfólio sem autenticação, use **Arquivo -> Publicar na Web (Público)** (requer permissão do administrador do tenant).
