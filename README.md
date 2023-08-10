# Biblioteca do Frederico

Api para gerenciar coleção pessoal de livros, mangas e quadrinhos.

## Items

Um item pode ou não fazer parte de uma serie, ele representa um livro, manga ou quadrinho de uma coleção/usuário

### Entidade

- id (not null)
- titulo (not null)
- autor (not null)
- numero (null)
- serie (null)

### Rotas

- [ ] Inserir item na biblioteca(Ao adicionar item, deve-se identificar se faz parte de uma serie ou não, caso faça, adicionar a serie)
- [ ] Editar item na biblioteca
- [ ] Excluir item na biblioteca(Deve excluir da serie tbm)
- [ ] Buscar todos os itens da biblioteca
- [ ] Buscar item especifico da biblioteca

## Serie

### Entidade

- id (not null)
- titulo (not null)
- autor (not null)
- quantidade (not null)
- volumes (not null)
- items (not null)

### Rotas

- [ ] Inserir serie na biblioteca
- [ ] Editar serie na biblioteca
- [ ] Excluir serie na biblioteca
- [ ] Buscar todos as series da biblioteca
- [ ] Buscar serie especifico da biblioteca

Serie == Lista de livros pertencentes a mesma linha

## Usuário/biblioteca



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
