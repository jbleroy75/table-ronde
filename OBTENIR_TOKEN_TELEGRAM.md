# ?? Comment Obtenir Votre Token Telegram Bot

## ?? ?tapes Rapides (2 minutes)

### 1?? Ouvrir Telegram
- Sur votre t?l?phone ou sur https://web.telegram.org/

### 2?? Chercher @BotFather
- Dans la barre de recherche Telegram, tapez : **@BotFather**
- C'est le bot officiel de Telegram pour cr?er des bots
- Il a une coche bleue de v?rification ?

### 3?? D?marrer la Conversation
- Cliquez sur "START" ou envoyez `/start`

### 4?? Cr?er un Nouveau Bot
Envoyez la commande :
```
/newbot
```

### 5?? Choisir un Nom
BotFather va vous demander un **nom d'affichage** pour votre bot.

**Exemple :**
```
Table Ronde IA
```

### 6?? Choisir un Username
Ensuite, choisissez un **username** (doit se terminer par "bot").

**Exemples valides :**
```
tableronde_ia_bot
roundtable_ai_bot
debate_expert_bot
mon_bot_ia_2025
```

### 7?? R?cup?rer le Token
BotFather va vous r?pondre avec un message contenant votre **token** :

```
Done! Congratulations on your new bot. You will find it at t.me/votre_bot.

Use this token to access the HTTP API:
123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567890

For a description of the Bot API, see this page:
https://core.telegram.org/bots/api
```

**Copiez le token** (la longue suite de caract?res apr?s "Use this token to access the HTTP API:")

---

## ?? Configurer le Token

### M?thode 1 : ?diter .env manuellement

```bash
cd /Users/jb/telegram-ai-roundtable
nano .env
```

Remplacez la ligne :
```
TELEGRAM_BOT_TOKEN=VOTRE_TOKEN_TELEGRAM_ICI
```

Par :
```
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567890
```

Sauvegardez avec `Ctrl+O`, puis `Enter`, puis quittez avec `Ctrl+X`.

### M?thode 2 : Utiliser sed (plus rapide)

```bash
# Remplacez VOTRE_TOKEN par le token que vous avez re?u
sed -i '' 's/TELEGRAM_BOT_TOKEN=.*/TELEGRAM_BOT_TOKEN=VOTRE_TOKEN_ICI/' /Users/jb/telegram-ai-roundtable/.env
```

---

## ? V?rifier la Configuration

Une fois le token ajout?, testez :

```bash
cd /Users/jb/telegram-ai-roundtable
python3 test_config.py
```

Vous devriez voir :
```
   Telegram             : ?
   OpenAI               : ?
   Anthropic            : ?
   DeepSeek             : ?

? CONFIGURATION VALIDE !
```

---

## ?? Lancer le Bot

```bash
cd /Users/jb/telegram-ai-roundtable
python3 bot.py
```

Vous verrez :
```
? Configuration valid?e
? Bot initialis? avec succ?s
?? D?marrage du bot Telegram...
?? Bot en ?coute. Appuyez sur Ctrl+C pour arr?ter.
```

---

## ?? Tester Votre Bot

1. Sur Telegram, cherchez votre bot (le username que vous avez choisi)
2. Cliquez sur "START" ou envoyez `/start`
3. Vous devriez recevoir le message de bienvenue du bot
4. Posez votre premi?re question !

**Exemple :**
```
Comment optimiser mon funnel de conversion pour un SaaS B2B ?
```

---

## ?? Probl?mes Courants

### "Unauthorized: bot token is invalid"
? Le token est incorrect ou mal copi?.
? Retournez sur @BotFather et utilisez `/token` pour r?cup?rer ? nouveau le token.

### "Can't find bot on Telegram"
? Vous cherchez le mauvais username.
? Le username exact est dans le message de BotFather (t.me/votre_bot).

### "Bot doesn't respond"
? Le script Python n'est pas lanc?.
? Assurez-vous que `python3 bot.py` est en cours d'ex?cution dans le terminal.

---

## ?? S?curit? du Token

?? **Le token Telegram donne un acc?s complet ? votre bot.**

**? faire :**
- ? Garder le token secret
- ? Ne jamais le commiter sur Git (d?j? prot?g? par .gitignore)
- ? Le stocker uniquement dans .env

**? ne PAS faire :**
- ? Partager le token publiquement
- ? Le mettre dans le code
- ? L'envoyer par email non chiffr?

**Si le token est compromis :**
1. Allez sur @BotFather
2. Envoyez `/revoke` et s?lectionnez votre bot
3. G?n?rez un nouveau token avec `/token`
4. Mettez ? jour votre .env

---

## ?? Commandes BotFather Utiles

```
/mybots          - Liste de tous vos bots
/token           - R?cup?rer le token d'un bot existant
/setname         - Changer le nom d'affichage
/setdescription  - Ajouter une description
/setabouttext    - Texte "? propos"
/setuserpic      - Changer la photo de profil
/deletebot       - Supprimer un bot
```

---

**Une fois le token configur?, votre bot sera 100% op?rationnel ! ??**
