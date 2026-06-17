# Desafio Técnico b2bflow - Estágio em Python

O projeto em Python tem uma funcionalidade que lê contatos de uma tabela no Supabase e envia mensagens personalizadas via WhatsApp utilizando a Z-API.

## Setup da tabela no Supabase

Crie uma tabela chamada `contatos` com as seguintes colunas:
- `id` (int8, Primary Key)
- `nome` (text)
- `telefone` (text) -> Exemplo de formato: `+55(21)99637-7469`

## Variáveis de ambiente