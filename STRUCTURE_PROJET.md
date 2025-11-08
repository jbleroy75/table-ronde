# ?? Structure du Projet

## Arborescence Compl?te

```
telegram-ai-roundtable/
?
??? ?? bot.py                    # Point d'entr?e principal du bot
??? ?? agents.py                 # Classes des 3 agents IA + Synthesizer
??? ?? config.py                 # Configuration et gestion des cl?s API
?
??? ?? requirements.txt          # D?pendances Python
??? ?? .env.example              # Mod?le de configuration (? copier)
??? ?? .env                      # Configuration r?elle (NON commit?)
??? ?? .gitignore                # Fichiers ? ignorer par Git
?
??? ??? install.sh                # Script d'installation automatique
??? ?? test_config.py            # Script de test de configuration
?
??? ?? README.md                 # Documentation compl?te
??? ?? GUIDE_RAPIDE.md           # Guide de d?marrage en 3 minutes
??? ?? EXEMPLES_USAGE.md         # Exemples concrets d'utilisation
??? ?? STRUCTURE_PROJET.md       # Ce fichier
```

---

## ?? Description des Fichiers

### **Fichiers Python Principaux**

#### `bot.py` (12.7 KB)
**Point d'entr?e du bot Telegram**

- Classe `RoundtableBot` : orchestration globale
- Handlers de commandes : `/start`, `/help`, `/status`, `/reset`, `/stop`
- Handler de messages : gestion du d?bat multi-agent
- Formatage des r?ponses Telegram (Markdown)
- Gestion des contextes utilisateurs
- Logging et error handling

**Fonctions cl?s :**
```python
async def handle_message()        # G?re les messages utilisateur
async def start_command()          # Commande /start
def _format_roundtable_response()  # Formate la r?ponse finale
```

---

#### `agents.py` (10.2 KB)
**Classes des agents IA**

**Structure :**
- `BaseAgent` : classe abstraite commune
  - `get_system_prompt()` : g?n?re les prompts syst?me
  - `generate_response()` : m?thode abstraite

- `ChatGPTAgent` : agent logique
  - API : OpenAI Chat Completions
  - R?le : structuration, argumentation rationnelle

- `ClaudeAgent` : agent nuanc?
  - API : Anthropic Messages
  - R?le : analyse critique, r?flexion profonde

- `DeepSeekAgent` : agent franc-parler
  - API : DeepSeek Chat (compatible OpenAI)
  - R?le : critique directe, humour noir, innovation

- `Synthesizer` : g?n?rateur de synth?ses
  - Agr?ge les r?ponses des 3 agents
  - Produit une synth?se structur?e

**Flow :**
```
User Question ? 3 Agents (parallel) ? Synthesizer ? Formatted Response
```

---

#### `config.py` (3.0 KB)
**Centralisation de la configuration**

**Classe `Config` :**
- Chargement des variables d'environnement via `python-dotenv`
- Validation des cl?s API au d?marrage
- Param?tres configurables :
  - Mod?les IA (GPT-4o, Claude 3.5, DeepSeek)
  - Temp?rature (cr?ativit?)
  - Max tokens par r?ponse
  - Timeouts API
  - Mode debug

**M?thodes :**
```python
Config.validate()     # Valide toutes les cl?s
Config.get_status()   # Statut de chaque API
```

---

#### `test_config.py` (1.9 KB)
**Script de test de configuration**

- V?rifie la pr?sence du fichier `.env`
- Teste le chargement des variables
- Valide les cl?s API
- Affiche le statut de configuration complet

**Usage :**
```bash
python test_config.py
```

---

### **Fichiers de Configuration**

#### `.env.example` (1.5 KB)
**Mod?le de configuration**

Contient tous les champs n?cessaires avec instructions.

**? copier en `.env` et remplir :**
```bash
cp .env.example .env
nano .env
```

#### `.env` (non commit?)
**Configuration r?elle avec cl?s API**

?? **NE JAMAIS COMMITER CE FICHIER**

Contenu type :
```env
TELEGRAM_BOT_TOKEN=123456:ABC...
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
DEEPSEEK_API_KEY=sk-...
```

#### `.gitignore` (751 B)
**Fichiers exclus de Git**

Prot?ge :
- `.env` (cl?s API)
- `__pycache__/`
- Environnements virtuels
- Fichiers temporaires
- Logs

---

### **Fichiers de D?pendances**

#### `requirements.txt` (741 B)
**D?pendances Python du projet**

Packages principaux :
```
python-telegram-bot==21.0.1   # Bot Telegram
openai==1.54.0                # ChatGPT
anthropic==0.39.0             # Claude
requests==2.32.3              # DeepSeek API
python-dotenv==1.0.0          # Variables d'environnement
```

**Installation :**
```bash
pip install -r requirements.txt
```

---

### **Scripts Utilitaires**

#### `install.sh` (ex?cutable)
**Script d'installation automatique**

Automatise :
1. V?rification Python 3.9+
2. V?rification pip
3. Installation des d?pendances
4. Copie de `.env.example` vers `.env`
5. Instructions de configuration

**Usage :**
```bash
./install.sh
```

---

### **Documentation**

#### `README.md` (10.0 KB)
**Documentation compl?te du projet**

**Sections :**
- Pr?sentation et caract?ristiques
- Installation pas ? pas
- Obtention des cl?s API
- Lancement et utilisation
- Commandes disponibles
- Architecture du code
- Configuration avanc?e
- S?curit? et bonnes pratiques
- D?pannage
- Estimation des co?ts
- D?veloppement et extensions

---

#### `GUIDE_RAPIDE.md` (3.6 KB)
**Guide de d?marrage en 3 minutes**

Installation ultra-rapide :
1. `pip install -r requirements.txt`
2. Configuration `.env`
3. `python bot.py`

Inclut :
- Liens directs vers les plateformes API
- Checklist de d?pannage
- Exemples de premi?res questions
- Commandes utiles

---

#### `EXEMPLES_USAGE.md` (11.2 KB)
**Exemples concrets d'utilisation**

**Contenu :**
- Questions types par cat?gorie :
  - Business & Strat?gie
  - Technique & Architecture
  - Marketing & Growth
  - Produit & MVP
- Exemples de r?ponses format?es
- Dynamique de d?bat (style "cash")
- Conseils pour obtenir les meilleures r?ponses
- Cas d'usage avanc?s
- Interpr?tation des divergences

---

#### `STRUCTURE_PROJET.md` (ce fichier)
**Description de l'architecture du projet**

Vue d'ensemble technique pour les d?veloppeurs.

---

## ?? Flow d'Ex?cution

### D?marrage du Bot

```
1. Ex?cution : python bot.py
2. Chargement config.py
3. Validation des cl?s API (Config.validate())
4. Initialisation RoundtableBot
   ??? ChatGPTAgent
   ??? ClaudeAgent
   ??? DeepSeekAgent
   ??? Synthesizer
5. Cr?ation Application Telegram
6. Enregistrement des handlers
7. D?marrage polling Telegram
```

### Traitement d'un Message Utilisateur

```
1. R?ception message Telegram
2. RoundtableBot.handle_message()
3. R?cup?ration contexte utilisateur
4. Appels parall?les aux 3 agents (asyncio.create_task)
   ??? ChatGPTAgent.generate_response()
   ??? ClaudeAgent.generate_response()
   ??? DeepSeekAgent.generate_response()
5. Attente des 3 r?ponses (await)
6. Synthesizer.generate_synthesis()
7. Formatage de la r?ponse (_format_roundtable_response)
8. Envoi r?ponse Telegram
9. Mise ? jour contexte utilisateur
```

### Sch?ma des Appels API

```
User Message
    ?
    ???? ChatGPTAgent ??? OpenAI API ??? Response 1
    ?
    ???? ClaudeAgent ??? Anthropic API ??? Response 2
    ?
    ???? DeepSeekAgent ??? DeepSeek API ??? Response 3
         ?
         ???? Synthesizer ??? OpenAI API ??? Synthesis
              ?
              ???? Formatted Response ??? Telegram
```

---

## ?? Architecture des Classes

### Hi?rarchie d'H?ritage

```
BaseAgent (abstract)
    ?
    ??? ChatGPTAgent
    ?       ??? client: openai.OpenAI
    ?       ??? generate_response() [override]
    ?
    ??? ClaudeAgent
    ?       ??? client: anthropic.Anthropic
    ?       ??? generate_response() [override]
    ?
    ??? DeepSeekAgent
            ??? api_url: str
            ??? generate_response() [override]

Synthesizer
    ??? client: openai.OpenAI
    ??? generate_synthesis()

RoundtableBot
    ??? chatgpt: ChatGPTAgent
    ??? claude: ClaudeAgent
    ??? deepseek: DeepSeekAgent
    ??? synthesizer: Synthesizer
    ??? user_contexts: Dict[int, list]
```

---

## ?? D?pendances Entre Fichiers

```
bot.py
    ??? import config (Config)
    ??? import agents (ChatGPTAgent, ClaudeAgent, DeepSeekAgent, Synthesizer)

agents.py
    ??? import config (Config)

test_config.py
    ??? import config (Config)

config.py
    ??? import dotenv (load_dotenv)
```

---

## ?? S?curit?

### Fichiers Sensibles (NON commit?s)

- `.env` : contient toutes les cl?s API
- `*.log` : logs potentiellement sensibles
- `__pycache__/` : bytecode Python

### Protection par `.gitignore`

Tous les fichiers sensibles sont automatiquement exclus de Git.

### Bonnes Pratiques

1. **Ne jamais** hardcoder les cl?s API dans le code
2. **Toujours** utiliser des variables d'environnement
3. **Valider** les cl?s au d?marrage (Config.validate())
4. **Logger** les erreurs sans exposer les cl?s

---

## ?? Commandes Utiles

### Installation

```bash
# Installation automatique
./install.sh

# Installation manuelle
pip install -r requirements.txt
cp .env.example .env
```

### Tests

```bash
# Tester la configuration
python test_config.py

# V?rifier les imports
python -c "from config import Config; from agents import *; print('OK')"
```

### Lancement

```bash
# Lancement normal
python bot.py

# Lancement avec logs d?taill?s
DEBUG_MODE=True python bot.py

# Lancement en arri?re-plan (Linux/Mac)
nohup python bot.py > bot.log 2>&1 &

# Voir les logs en temps r?el
tail -f bot.log
```

### D?veloppement

```bash
# Formater le code (si black install?)
black *.py

# Linter (si flake8 install?)
flake8 *.py

# Type checking (si mypy install?)
mypy *.py
```

---

## ?? Taille des Fichiers

| Fichier | Taille | Type |
|---------|--------|------|
| `bot.py` | 12.7 KB | Code Python |
| `agents.py` | 10.2 KB | Code Python |
| `config.py` | 3.0 KB | Code Python |
| `test_config.py` | 1.9 KB | Code Python |
| `README.md` | 10.0 KB | Documentation |
| `EXEMPLES_USAGE.md` | 11.2 KB | Documentation |
| `GUIDE_RAPIDE.md` | 3.6 KB | Documentation |
| `.env.example` | 1.5 KB | Configuration |
| `requirements.txt` | 741 B | D?pendances |
| `.gitignore` | 751 B | Git |
| `install.sh` | ~2 KB | Script |

**Total : ~57 KB** (sans d?pendances externes)

---

## ?? Workflow Git Recommand?

### Premier Commit

```bash
cd telegram-ai-roundtable
git init
git add .
git commit -m "Initial commit: Bot Telegram multi-agent"
```

### Workflow Standard

```bash
# Cr?er une nouvelle fonctionnalit?
git checkout -b feature/nom-feature

# D?velopper...

# Commiter
git add .
git commit -m "feat: description de la feature"

# Merger
git checkout main
git merge feature/nom-feature
```

### ?? Important

**TOUJOURS** v?rifier que `.env` est bien dans `.gitignore` avant de push :

```bash
git status
# .env ne doit PAS appara?tre
```

---

## ?? Ressources Compl?mentaires

### Documentation des APIs

- **Telegram Bot API** : https://core.telegram.org/bots/api
- **python-telegram-bot** : https://docs.python-telegram-bot.org/
- **OpenAI API** : https://platform.openai.com/docs/api-reference
- **Anthropic API** : https://docs.anthropic.com/
- **DeepSeek API** : https://platform.deepseek.com/docs

### Tutoriels

- Configuration bot Telegram : https://core.telegram.org/bots/tutorial
- Async Python : https://docs.python.org/3/library/asyncio.html

---

**Projet cr?? pour faciliter les d?bats multi-agents via Telegram. Code document? et pr?t pour la production.**
