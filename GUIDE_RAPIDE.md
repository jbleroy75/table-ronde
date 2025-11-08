# ?? Guide de D?marrage Rapide

## Installation en 3 Minutes

### 1?? Installer les d?pendances

```bash
pip install -r requirements.txt
```

### 2?? Configurer les cl?s API

```bash
# Copier le fichier d'exemple
cp .env.example .env

# ?diter avec vos cl?s (nano, vim, ou votre ?diteur pr?f?r?)
nano .env
```

**Remplissez ces 4 cl?s obligatoires :**

```env
TELEGRAM_BOT_TOKEN=votre_token_de_botfather
OPENAI_API_KEY=sk-votre_cle_openai
ANTHROPIC_API_KEY=sk-ant-votre_cle_anthropic
DEEPSEEK_API_KEY=sk-votre_cle_deepseek
```

### 3?? Lancer le bot

```bash
python bot.py
```

? **C'est tout !** Votre bot est op?rationnel.

---

## ?? Obtenir les Cl?s (Liens Directs)

| Service | Lien Direct | Temps |
|---------|-------------|--------|
| **Telegram Bot** | https://t.me/BotFather | 2 min |
| **OpenAI** | https://platform.openai.com/api-keys | 5 min |
| **Anthropic** | https://console.anthropic.com/ | 5 min |
| **DeepSeek** | https://platform.deepseek.com/ | 5 min |

---

## ?? Premiers Pas sur Telegram

1. Cherchez votre bot sur Telegram (nom choisi avec BotFather)
2. Envoyez : `/start`
3. Posez votre question :

```
"Quelle strat?gie de pricing pour un SaaS B2B ?"
```

---

## ?? Checklist de D?pannage

- [ ] Python 3.9+ install? ? (`python --version`)
- [ ] D?pendances install?es ? (`pip list | grep telegram`)
- [ ] Fichier `.env` cr?? ? (`ls -la .env`)
- [ ] 4 cl?s API configur?es dans `.env` ?
- [ ] Bot d?marr? ? (`python bot.py` en cours)
- [ ] Bot trouv? sur Telegram ?

---

## ?? Exemples de Questions

**Business & Strat?gie :**
```
"Bootstrapping vs lev?e de fonds pour une startup SaaS ?"
"Comment valider un MVP avant d'investir 6 mois de dev ?"
"Strat?gie de go-to-market pour un march? satur? ?"
```

**Technique :**
```
"Architecture monolithe vs microservices : quand choisir quoi ?"
"Comment scaler une API ? 10k req/s avec un budget limit? ?"
"PostgreSQL vs MongoDB pour une app e-commerce ?"
```

**Marketing :**
```
"Content marketing vs paid ads : quel mix pour un SaaS ?"
"Comment construire une audience de 10k abonn?s en 3 mois ?"
"Strat?gie SEO vs SEA : o? investir en premier ?"
```

---

## ?? Commandes Utiles

```bash
# V?rifier que Python est install?
python --version

# Installer les d?pendances
pip install -r requirements.txt

# V?rifier la configuration
python -c "from config import Config; Config.validate(); print('? Config OK')"

# Lancer le bot
python bot.py

# Lancer en arri?re-plan (Linux/Mac)
nohup python bot.py > bot.log 2>&1 &

# Voir les logs en temps r?el
tail -f bot.log
```

---

## ?? Estimation des Co?ts

**Pour 100 d?bats (3 agents + synth?se par d?bat) :**

- GPT-4o : ~2-3?
- Claude 3.5 : ~1.5-2?  
- DeepSeek : ~0.10-0.20?

**Total : ~3.5-5? pour 100 d?bats complets**

?? Pour ?conomiser : utilisez `gpt-3.5-turbo` au lieu de `gpt-4o` dans `.env`

---

## ?? Probl?mes Courants

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Cl?s API manquantes"
```bash
# V?rifiez votre .env
cat .env

# Format attendu :
TELEGRAM_BOT_TOKEN=123456:ABC...
OPENAI_API_KEY=sk-...
```

### "Bot ne r?pond pas"
1. V?rifiez que `python bot.py` est en cours d'ex?cution
2. Testez avec `/status` sur Telegram
3. Consultez les logs dans le terminal

### "Timeout API"
```env
# Dans .env, augmentez le timeout
API_TIMEOUT=60
```

---

## ?? C'est Parti !

Une fois le bot lanc? :

1. Ouvrez Telegram
2. Cherchez votre bot
3. `/start`
4. Posez votre premi?re question !

**Le bot r?pondra avec :**
- ?? ChatGPT (logique)
- ?? Claude (nuance)  
- ? DeepSeek (franc-parler)
- ?? Synth?se finale

---

Besoin d'aide ? Consultez le **README.md** complet !
