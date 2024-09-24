# Biblioteca do Frederico

Api para gerenciar coleção pessoal de livros, mangas e quadrinhos.

## Item

Um item pode ou não fazer parte de uma serie, ele representa um livro, manga ou quadrinho de uma coleção/usuário

### Model

- id (not null)
- titulo (not null)
- gênero (not null)
- lançamento(not null)
- edição(null)
- fk autor (not null)
- fk serie (null)
- fk editora (not null)

### Rotas

- [ ] Inserir item na biblioteca(Ao adicionar item, deve-se identificar se faz parte de uma serie ou não, caso faça, adicionar a serie)
- [ ] Editar item na biblioteca
- [ ] Excluir item na biblioteca(Deve excluir da serie tbm)
- [ ] Buscar todos os itens da biblioteca
- [ ] Buscar item especifico da biblioteca

## Usuário/biblioteca

O usuário representa uma biblioteca e vice versa, cada usuário tem apenas a sua coleção e não é possível criar novas, tanto itens soltos quanto coleções pertencem ao usuário/biblioteca

### Entidade

- id(not null)
- nome(not null)
- email(not null)

### Rotas

- [ ] Criar usuário/biblioteca
- [ ] Buscar usuário/biblioteca
- [ ] Excluir usuário/biblioteca
- [ ] Editar usuário/biblioteca

Todo usuário é uma biblioteca

para iniciar o migrate
$ flask db init

para criar migrate
$ flask db migrate -m "Initial migration."

para subir migrate
$ flask db upgrade