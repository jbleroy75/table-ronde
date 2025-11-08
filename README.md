# ?? Bot Telegram Multi-Agent : Table Ronde IA

Bot Telegram en Python simulant une **table ronde entre trois grands mod?les de langage** (ChatGPT, Claude, DeepSeek) et l'utilisateur humain. Chaque IA a une personnalit? et un r?le distinct pour cr?er des d?bats riches, critiques et constructifs.

---

## ?? Caract?ristiques

### ?? **Trois Agents IA Experts**

| Agent | R?le | Personnalit? |
|-------|------|--------------|
| **ChatGPT** ?? | Logique & Structuration | Analyse m?thodique, d?composition des probl?mes, argumentation rationnelle |
| **Claude** ?? | Nuance & Profondeur | R?flexion critique, identification des subtilit?s, questionnement des hypoth?ses |
| **DeepSeek** ? | Franc-parler & Innovation | Critique directe sans filtre, humour noir, id?es disruptives |

### ? **Style de D?bat Unique**

- ? **Format ultra court** : r?ponses en bullet points, phrases percutantes
- ? **Critiques franches** : pas de complaisance, feedback honn?te
- ? **Synth?se automatique** : r?sum? des points cl?s + recommandations
- ? **Interactif** : l'utilisateur peut interrompre et orienter le d?bat

---

## ?? Installation

### **Pr?requis**

- Python 3.9 ou sup?rieur
- pip (gestionnaire de paquets Python)
- Cl?s API pour OpenAI, Anthropic et DeepSeek
- Token de bot Telegram

### **1. Cloner ou t?l?charger le projet**

```bash
cd telegram-ai-roundtable
```

### **2. Installer les d?pendances**

```bash
pip install -r requirements.txt
```

### **3. Configurer les cl?s API**

Copiez le fichier d'exemple et remplissez vos cl?s :

```bash
cp .env.example .env
```

?ditez le fichier `.env` avec vos cl?s API :

```env
# Telegram
TELEGRAM_BOT_TOKEN=votre_token_ici

# OpenAI (ChatGPT)
OPENAI_API_KEY=sk-votre_cle_openai

# Anthropic (Claude)
ANTHROPIC_API_KEY=sk-ant-votre_cle_anthropic

# DeepSeek
DEEPSEEK_API_KEY=sk-votre_cle_deepseek
```

---

## ?? Obtenir les Cl?s API

### **Telegram Bot Token**

1. Ouvrez Telegram et cherchez **@BotFather**
2. Envoyez `/newbot` et suivez les instructions
3. Copiez le token fourni dans votre `.env`

### **OpenAI (ChatGPT)**

1. Cr?ez un compte sur [OpenAI Platform](https://platform.openai.com/)
2. Allez dans **API Keys** : https://platform.openai.com/api-keys
3. Cr?ez une nouvelle cl? et copiez-la

### **Anthropic (Claude)**

1. Cr?ez un compte sur [Anthropic Console](https://console.anthropic.com/)
2. Allez dans **API Keys**
3. Cr?ez une nouvelle cl? et copiez-la

### **DeepSeek**

1. Cr?ez un compte sur [DeepSeek Platform](https://platform.deepseek.com/)
2. Allez dans **API Keys**
3. Cr?ez une nouvelle cl? et copiez-la

---

## ?? Lancement du Bot

### **D?marrer le bot**

```bash
python bot.py
```

Vous devriez voir :

```
? Configuration valid?e
? Bot initialis? avec succ?s
?? D?marrage du bot Telegram...
?? Bot en ?coute. Appuyez sur Ctrl+C pour arr?ter.
```

### **Utiliser le bot sur Telegram**

1. Cherchez votre bot sur Telegram (nom que vous avez choisi avec @BotFather)
2. D?marrez la conversation : `/start`
3. Posez votre premi?re question !

---

## ?? Utilisation

### **Commandes Disponibles**

| Commande | Description |
|----------|-------------|
| `/start` | Afficher le message de bienvenue |
| `/help` | Aide d?taill?e sur l'utilisation |
| `/status` | V?rifier l'?tat des API et configuration |
| `/reset` | R?initialiser le contexte de conversation |
| `/stop` | Arr?ter le d?bat en cours |

### **Exemples de Questions**

```
?? "Comment optimiser mon funnel de conversion ?"
?? "Strat?gie marketing pour un SaaS B2B ?"
?? "Architecture microservices : pour ou contre ?"
?? "Comment pitcher mon projet ? des investisseurs ?"
?? "Faut-il lever des fonds ou bootstrapper ?"
```

### **Format de R?ponse**

Le bot r?pond avec une structure claire :

```
?? TABLE RONDE
????????????????????

?? ChatGPT ? Logique
? Point logique 1
? Structuration m?thodique
? Recommandation rationnelle

????????????????????

?? Claude ? Nuance
? Analyse nuanc?e
? Question critique
? Perspective alternative

????????????????????

? DeepSeek ? Franc-parler
? Critique directe (m?me dure)
? Id?e disruptive
? Humour noir possible

????????????????????

?? SYNTH?SE
? Point de consensus
? Divergences cl?s
? Recommandations actionnables
? Prochaines ?tapes
```

---

## ??? Architecture du Code

### **Structure du Projet**

```
telegram-ai-roundtable/
?
??? bot.py              # Point d'entr?e principal du bot
??? agents.py           # Classes des agents IA (ChatGPT, Claude, DeepSeek)
??? config.py           # Configuration et gestion des cl?s API
??? requirements.txt    # D?pendances Python
??? .env.example        # Exemple de configuration
??? .env               # Configuration r?elle (? cr?er, NON commit?)
??? README.md          # Ce fichier
```

### **Fichiers Principaux**

#### **`config.py`**

Centralise toutes les configurations :
- Cl?s API charg?es depuis variables d'environnement
- Param?tres des mod?les (temp?rature, max_tokens, etc.)
- Validation automatique des cl?s au d?marrage

#### **`agents.py`**

D?finit les classes des agents IA :
- `BaseAgent` : classe de base commune
- `ChatGPTAgent` : appel API OpenAI
- `ClaudeAgent` : appel API Anthropic
- `DeepSeekAgent` : appel API DeepSeek
- `Synthesizer` : g?n?ration des synth?ses

#### **`bot.py`**

Orchestration du bot Telegram :
- Gestion des commandes (`/start`, `/help`, etc.)
- Orchestration des d?bats multi-agent
- Formatage des r?ponses pour Telegram
- Gestion des contextes utilisateur

---

## ?? Configuration Avanc?e

### **Personnaliser les Mod?les**

Dans le fichier `.env`, vous pouvez changer les mod?les utilis?s :

```env
# Utiliser GPT-3.5 au lieu de GPT-4 (moins cher)
OPENAI_MODEL=gpt-3.5-turbo

# Utiliser Claude 3 Opus (plus puissant)
ANTHROPIC_MODEL=claude-3-opus-20240229

# Ajuster la temp?rature (cr?ativit?)
TEMPERATURE=1.0

# Limiter les tokens (?conomiser)
MAX_TOKENS=300
```

### **Modifier les Personnalit?s**

Dans `agents.py`, vous pouvez ajuster les prompts syst?me de chaque agent pour changer leur comportement.

### **Activer le Mode Debug**

```env
DEBUG_MODE=True
```

Affiche des logs d?taill?s dans la console.

---

## ?? S?curit? & Bonnes Pratiques

### **Protection des Cl?s API**

- ? Ne **jamais** commiter le fichier `.env` sur Git
- ? Ajouter `.env` au `.gitignore`
- ? R?g?n?rer les cl?s en cas de fuite
- ? Utiliser des variables d'environnement en production

### **Cr?ation du `.gitignore`**

Cr?ez un fichier `.gitignore` avec :

```gitignore
# Fichiers sensibles
.env

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/

# IDE
.vscode/
.idea/
*.swp
```

### **Limites de Taux API**

- Surveillez votre usage API sur chaque plateforme
- Ajustez `MAX_TOKENS` pour contr?ler les co?ts
- Impl?mentez des limites par utilisateur si n?cessaire

---

## ?? D?pannage

### **Probl?me : "Cl?s API manquantes"**

? **Solution** : V?rifiez que votre fichier `.env` est bien configur? avec toutes les cl?s.

```bash
# V?rifier la pr?sence du fichier .env
ls -la .env

# Tester la configuration
python -c "from config import Config; Config.validate()"
```

### **Probl?me : "Erreur API OpenAI/Anthropic/DeepSeek"**

? **Solution** :
- V?rifiez que vos cl?s API sont valides
- Assurez-vous d'avoir des cr?dits sur chaque plateforme
- V?rifiez votre connexion internet

### **Probl?me : "Le bot ne r?pond pas"**

? **Solution** :
- V?rifiez que le bot est bien d?marr? (`python bot.py`)
- Testez avec `/status` pour voir l'?tat des API
- Consultez les logs dans la console

### **Probl?me : "Timeout"**

? **Solution** : Augmentez le timeout dans `.env` :

```env
API_TIMEOUT=60
```

---

## ?? Co?ts Estim?s

| Mod?le | Co?t Approximatif | Note |
|--------|-------------------|------|
| **GPT-4o** | ~$0.01-0.03/d?bat | Plus cher mais tr?s performant |
| **GPT-3.5** | ~$0.001-0.003/d?bat | Alternative ?conomique |
| **Claude 3.5** | ~$0.015-0.04/d?bat | Excellent rapport qualit?/prix |
| **DeepSeek** | ~$0.001-0.002/d?bat | Le moins cher |

**Total par d?bat (3 agents + synth?se)** : ~$0.03-0.08

?? **Astuce** : Utilisez `MAX_TOKENS=300` pour r?duire les co?ts.

---

## ??? D?veloppement & Extension

### **Ajouter un Nouvel Agent**

1. Cr?ez une nouvelle classe dans `agents.py` h?ritant de `BaseAgent`
2. Impl?mentez la m?thode `generate_response()`
3. Ajoutez l'agent dans `bot.py`

### **Modifier le Format de R?ponse**

?ditez la m?thode `_format_roundtable_response()` dans `bot.py`.

### **Ajouter des Commandes**

```python
# Dans bot.py
async def ma_nouvelle_commande(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ma r?ponse")

# Dans main()
application.add_handler(CommandHandler("macommande", bot.ma_nouvelle_commande))
```

---

## ?? Logs et Monitoring

### **Activer les Logs D?taill?s**

```python
# Dans bot.py, modifiez le niveau de logging
logging.basicConfig(level=logging.DEBUG)
```

### **Logs d'Appels API**

Tous les appels API sont logg?s automatiquement avec horodatage et ID utilisateur.

---

## ?? Support & Contribution

### **Besoin d'Aide ?**

- Consultez les logs dans la console
- V?rifiez la configuration avec `/status`
- Utilisez le mode debug : `DEBUG_MODE=True`

### **Am?liorations Possibles**

- ?? Ajout de modes de d?bat (court, approfondi, technique)
- ?? Historique des d?bats en base de donn?es
- ?? Support multilingue
- ?? Interface web pour visualiser les d?bats
- ?? Analytics et statistiques d'usage

---

## ?? Licence

Ce projet est fourni "tel quel" ? des fins ?ducatives et de d?monstration.

---

## ?? Avertissement

- Ce bot consomme des cr?dits API sur chaque plateforme
- Surveillez votre usage pour ?viter des co?ts inattendus
- Les r?ponses des IA ne constituent pas des conseils professionnels
- Utilisez le mode debug uniquement en d?veloppement

---

## ?? C'est Parti !

Lancez le bot et profitez de d?bats IA de haute qualit? :

```bash
python bot.py
```

**Exemple de premi?re question :**

```
"Comment structurer le lancement d'un MVP SaaS en 3 mois avec un budget limit? ?"
```

?? **Bon d?bat !**
