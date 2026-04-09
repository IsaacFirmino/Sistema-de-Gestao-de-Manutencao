# 🛠️ Sistema de Gestão de Manutenção de Dispositivos

Este é um software de linha de comando (CLI) desenvolvido em **Python** para organizar o fluxo de trabalho em assistências técnicas. O sistema resolve o problema comum de perda de informações sobre ordens de serviço, permitindo o controle digital de aparelhos, defeitos e orçamentos.



## 🎯 Objetivo do Projeto
O foco principal foi criar uma ferramenta leve e funcional que aplique conceitos de **CRUD** (Create, Read, Update, Delete) e persistência de dados, simulando um ambiente real de manutenção de eletrônicos e consoles.

## 🚀 Funcionalidades
- **Cadastro de Ordens de Serviço:** Registro do nome do dispositivo, descrição detalhada do problema e valor orçado.
- **Persistência em JSON:** Os dados não são perdidos ao fechar o programa; eles são lidos e gravados automaticamente em um arquivo `.json`.
- **Gerenciamento de Status:** Controle visual se o serviço está "Pendente", "Em Andamento" ou "Concluído".
- **Listagem Geral:** Interface organizada para visualização de todos os serviços ativos na bancada.

## 🛠️ Tecnologias e Conceitos Aplicados
- **Linguagem:** Python 3.x
- **Estrutura de Dados:** Listas e Dicionários para manipulação eficiente de informações.
- **Módulo JSON:** Para armazenamento de dados em formato de texto estruturado.
- **Tratamento de Exceções:** Prevenção de erros caso o arquivo de banco de dados não exista.
