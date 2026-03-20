# 🚀 Comandos Git Essenciais

**Configuração inicial:**  
git config --global user.name "Seu Nome"              # Configura nome de usuário global  
git config --global user.email "seu@email.com"        # Configura email global  
git config --list                                      # Lista todas configurações atuais  
git config --global core.editor "code --wait"         # Define VS Code como editor padrão  

**Iniciar repositórios:**  
git clone https://github.com/usuario/repositorio.git   # Clona repositório existente  
git clone https://github.com/usuario/repositorio.git minha-pasta  # Clona em pasta específica  
git init                                                # Inicia Git em projeto local  
git remote add origin https://github.com/usuario/repositorio.git  # Conecta local ao remoto  

**Trabalho diário:**  
git status                                              # Verifica status das alterações  
git add arquivo.txt                                     # Adiciona arquivo específico  
git add .                                                # Adiciona todos arquivos modificados  
git add -A                                               # Adiciona todos (incluindo deletados)  
git commit -m "Mensagem"                                 # Commita com mensagem  
git commit -am "Mensagem"                                # Commit direto em arquivos rastreados  

**Sincronização com GitHub:**  
git push origin main                                     # Envia alterações para o GitHub  
git push -u origin main                                  # Primeiro push (configura upstream)  
git pull origin main                                     # Baixa alterações do GitHub  
git fetch origin                                         # Baixa alterações sem mesclar  
git remote -v                                            # Lista repositórios remotos  

**Trabalhando com Branches:**  
git branch                                               # Lista branches locais  
git branch -a                                            # Lista todas branches (locais/remotas)  
git branch nome-da-branch                                # Cria nova branch  
git checkout nome-da-branch                              # Muda para outra branch  
git checkout -b nome-da-branch                           # Cria e muda para nova branch  
git merge nome-da-branch                                 # Mescla branch atual com outra  
git branch -d nome-da-branch                             # Deleta branch local  
git push origin --delete nome-da-branch                  # Deleta branch remota  

**Visualização e Histórico:**  
git log                                                  # Mostra histórico de commits  
git log --oneline                                        # Histórico simplificado (1 linha/commit)  
git log --graph --oneline --all                          # Histórico com gráfico das branches  
git blame arquivo.txt                                    # Mostra quem modificou cada linha  
git diff                                                 # Mostra diferenças não commitadas  
git diff commit1..commit2                                 # Mostra diferenças entre commits  

**Desfazendo alterações:**  
git reset HEAD arquivo.txt                               # Remove arquivo da área de stage  
git checkout -- arquivo.txt                              # Desfaz alterações no arquivo  
git reset --soft HEAD~1                                  # Desfaz último commit (mantém alterações)  
git reset --hard HEAD~1                                  # Desfaz último commit (perde alterações)  
git revert id-do-commit                                  # Cria novo commit desfazendo anterior  

**Tags e Releases:**  
git tag v1.0.0                                           # Cria tag leve  
git tag -a v1.0.0 -m "Versão 1.0.0"                      # Cria tag anotada com mensagem  
git tag                                                   # Lista todas tags  
git push origin --tags                                   # Envia tags para o GitHub  

**Comandos úteis do GitHub CLI (gh):**  
gh repo view --web                                        # Abre repositório no navegador  
gh pr create                                              # Cria pull request  
gh pr list                                                # Lista pull requests  
gh repo view                                              # Verifica status do repositório  
gh repo clone usuario/repositorio                         # Clona com GitHub CLI  

**Dicas rápidas:**  
git help <comando>                                        # Mostra documentação do comando  
git stash                                                 # Salva alterações temporariamente  
git stash pop                                             # Recupera último stash  
git log --oneline -5                                      # Mostra últimos 5 commits  

**Principais Prefixos (Tipos):**
feat: Nova funcionalidade (feature) para o usuário.
fix: Correção de um bug.
docs: Alterações na documentação (README, comentários).
style: Mudanças que não afetam o significado do código (formatação, ponto e vírgula, etc.).
refactor: Alteração no código que não corrige bug nem adiciona funcionalidade.
perf: Alteração que melhora o desempenho.
test: Adição ou correção de testes.
build: Mudanças que afetam o build ou dependências (npm, maven, gradle).
ci: Configurações de Integração Contínua (Jenkins, GitHub Actions).
chore: Atualização de tarefas de build, pacotes, etc. (sem alteração em código fonte).
revert: Reversão de um commit anterior. 
