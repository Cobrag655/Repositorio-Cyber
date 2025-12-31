# Exercício de IDOR (Insecure Direct Object Reference)

## Visão Geral
Este repositório documenta um exercício prático sobre a vulnerabilidade **IDOR (Insecure Direct Object Reference)**, realizado em um ambiente de laboratório fornecido pela plataforma TryHackMe. O objetivo foi entender como falhas de controle de acesso podem expor dados sensíveis de outros usuários e como esse tipo de problema pode ser evitado em aplicações reais. [file:5]

## O Que Foi Feito
- Acessei uma aplicação web de exemplo (TrypresentMe) atuando como um usuário autenticado em um painel de “parent dashboard”. [file:6]
- Analisei:
- O **armazenamento local** do navegador, identificando informações do usuário logado (como `user_id`, nome, e-mail e papel de acesso). [file:5]
- As **requisições de rede** no DevTools, observando endpoints que utilizavam `user_id` como parâmetro (por exemplo, `view_accountinfo?user_id=15`). [file:7]
- Com isso, foi possível entender como a aplicação retornava dados de perfil e de “children” vinculados ao usuário, ilustrando na prática o conceito de IDOR e a importância de validar permissões no backend. [file:6][file:7]
- Todas as ações foram realizadas apenas dentro do ambiente controlado da TryHackMe, sem qualquer interação com sistemas reais.

## Objetivo Educacional
- Compreender o conceito de IDOR e sua classificação dentro de falhas de controle de acesso.
- Treinar o uso de ferramentas do navegador (DevTools, aba Network, Storage) para análise de requisições e respostas.
- Refletir sobre boas práticas de desenvolvimento seguro:
- Verificação de autorização no servidor.
- Não confiar apenas em IDs no lado do cliente.
- Minimizar exposição de dados no frontend.

## Aviso Ético
- Este exercício foi realizado **exclusivamente** em um laboratório de treinamento, com ambiente e dados fictícios.
- Testes desse tipo em sistemas reais só devem ser feitos com **autorização formal** (contrato, escopo definido, regras de engajamento).
- A exploração não autorizada de vulnerabilidades pode ser crime, além de violar políticas de uso de serviços.

## Ambiente Utilizado
- Plataforma: TryHackMe (sala de IDOR).
- SO: Kali Linux em máquina virtual.
- Navegador: Firefox com DevTools.
- Ferramentas principais: inspetor, aba Network, Storage/Local Storage para análise de requisições e tokens.

## Como Este Repositório Pode Ser Usado
- Referência de estudo para quem está iniciando em:
- Segurança de aplicações web.
- OWASP Top 10 e falhas de controle de acesso.
- Metodologia de análise de requisições HTTP no navegador.
- Base para anotações pessoais, screenshots e resumos teóricos de IDOR.

## Licença
MIT License – uso exclusivamente educacional.
