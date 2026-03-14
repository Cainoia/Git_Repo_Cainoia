Git commands to remember

============================================================

Configuração inicial

# Configurar nome de usuário (global)
git config --global user.name "Seu Nome"

# Configurar email (global)
git config --global user.email "seu@email.com"

# Verificar configurações
git config --list

# Configurar editor padrão
git config --global core.editor "code --wait"

=============================================================

Iniciar repositórios

# Clonar um repositório existente
git clone https://github.com/usuario/repositorio.git

# Clonar em uma pasta específica
git clone https://github.com/usuario/repositorio.git minha-pasta

# Iniciar Git em um projeto local
git init

# Conectar repositório local ao remoto
git remote add origin https://github.com/usuario/repositorio.git

=============================================================

Trabalho diário

# Verificar status das alterações
git status

# Adicionar arquivos específicos
git arquivo.txt

# Adicionar todos os arquivos modificados
git add .

# Adicionar todos os arquivos (incluindo deletados)
git add -A

# Commitar com mensagem
git commit -m "Mensagem descritiva do que foi feito"

# Commitar todos os arquivos rastreados diretamente
git commit -am "Mensagem do commit"

=============================================================

 Sincronização com GitHub

 # Enviar alterações para o GitHub
git push origin main

# Enviar e configurar upstream (primeiro push)
git push -u origin main

# Baixar alterações do GitHub
git pull origin main

# Baixar alterações sem mesclar (fetch)
git fetch origin

# Verificar repositórios remotos configurados
git remote -v

=============================================================

Trabalhando com Branches

# Listar branches locais
git branch

# Listar todas as branches (incluindo remotas)
git branch -a

# Criar nova branch
git branch nome-da-branch

# Mudar para outra branch
git checkout nome-da-branch

# Criar e mudar para nova branch
git checkout -b nome-da-branch

# Mesclar branch atual com outra
git merge nome-da-branch

# Deletar branch local
git branch -d nome-da-branch

# Deletar branch remota
git push origin --delete nome-da-branch

=============================================================

Visualização e Histório

# Ver histórico de commits
git log

# Ver histórico simplificado (uma linha por commit)
git log --oneline

# Ver histórico com gráfico das branches
git log --graph --oneline --all

# Ver quem modificou cada linha do arquivo
git blame arquivo.txt

# Ver diferenças não commitadas
git diff

# Ver diferenças entre commits
git diff commit1..commit2

=============================================================

Desfazendo alterações

# Remover arquivo da área de stage
git reset HEAD arquivo.txt

# Desfazer alterações em um arquivo (voltar ao último commit)
git checkout -- arquivo.txt

# Desfazer último commit (mantendo alterações)
git reset --soft HEAD~1

# Desfazer último commit (perdendo alterações)
git reset --hard HEAD~1

# Criar novo commit desfazendo um commit anterior
git revert id-do-commit

=============================================================

Comandos úteis do Github CLI (gh)

# Abrir repositório no navegador
gh repo view --web

# Criar pull request
gh pr create

# Listar pull requests
gh pr list

# Verificar status do repositório
gh repo view

# Clonar repositório com GitHub CLI
gh repo clone usuario/repositorio
