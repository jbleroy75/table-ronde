# ?? Ajouter des Cr?dits OpenAI

## ? Probl?me D?tect?

```
Error 429 - insufficient_quota
Vous n'avez pas de cr?dits sur votre compte OpenAI
```

---

## ?? SOLUTION 1 : Ajouter des Cr?dits (Recommand?)

### **?tapes :**

1. **Allez sur votre compte OpenAI :**
   https://platform.openai.com/settings/organization/billing

2. **Ajoutez un mode de paiement :**
   - Cliquez sur "Payment methods"
   - Ajoutez une carte de cr?dit

3. **Ajoutez des cr?dits :**
   - Minimum : **$5** (suffisant pour ~150-500 d?bats)
   - Recommand? : **$10-20** pour commencer

4. **Configurez des limites (optionnel) :**
   - Allez dans "Usage limits"
   - D?finissez une limite mensuelle (ex: $20/mois)

### **Tarifs OpenAI :**

| Mod?le | Prix Input | Prix Output | Estimation/d?bat |
|--------|-----------|-------------|------------------|
| **GPT-4o** | $2.50/1M tokens | $10/1M tokens | ~$0.01-0.03 |
| **GPT-3.5-turbo** | $0.50/1M tokens | $1.50/1M tokens | ~$0.001-0.003 |

?? **Avec $10, vous pouvez faire :**
- ~300-1000 d?bats avec GPT-4o
- ~3000-10000 d?bats avec GPT-3.5-turbo

---

## ?? SOLUTION 2 : Utiliser Uniquement Claude et DeepSeek

Si vous ne voulez pas payer OpenAI pour le moment, **d?sactivez ChatGPT** :

### **Modifier le bot pour 2 agents au lieu de 3 :**

#### **1. ?ditez `bot.py` :**

```bash
nano /Users/jb/telegram-ai-roundtable/bot.py
```

Cherchez cette section (ligne ~25) :

```python
def __init__(self):
    self.chatgpt = ChatGPTAgent()
    self.claude = ClaudeAgent()
    self.deepseek = DeepSeekAgent()
    self.synthesizer = Synthesizer()
```

Commentez ChatGPT :

```python
def __init__(self):
    # self.chatgpt = ChatGPTAgent()  # D?sactiv? - quota insuffisant
    self.claude = ClaudeAgent()
    self.deepseek = DeepSeekAgent()
    self.synthesizer = Synthesizer()
```

#### **2. Cherchez cette section (ligne ~160) :**

```python
# Lancer les 3 agents en parall?le
chatgpt_task = asyncio.create_task(
    self.chatgpt.generate_response(user_message, user_context)
)
claude_task = asyncio.create_task(
    self.claude.generate_response(user_message, user_context)
)
deepseek_task = asyncio.create_task(
    self.deepseek.generate_response(user_message, user_context)
)

# Attendre toutes les r?ponses
chatgpt_response = await chatgpt_task
claude_response = await claude_task
deepseek_response = await deepseek_task
```

Commentez ChatGPT :

```python
# Lancer les 2 agents en parall?le
# chatgpt_task = asyncio.create_task(
#     self.chatgpt.generate_response(user_message, user_context)
# )
claude_task = asyncio.create_task(
    self.claude.generate_response(user_message, user_context)
)
deepseek_task = asyncio.create_task(
    self.deepseek.generate_response(user_message, user_context)
)

# Attendre toutes les r?ponses
# chatgpt_response = await chatgpt_task
chatgpt_response = "? ?? ChatGPT d?sactiv? (quota OpenAI insuffisant)"
claude_response = await claude_task
deepseek_response = await deepseek_task
```

---

## ?? SOLUTION 3 : Utiliser GPT-3.5-turbo (Moins Cher)

**D?j? configur? dans votre `.env` !**

Si vous avez des cr?dits mais voulez ?conomiser :

```env
OPENAI_MODEL=gpt-3.5-turbo
```

GPT-3.5 est **10x moins cher** que GPT-4o :
- GPT-4o : ~$0.02/d?bat
- GPT-3.5 : ~$0.002/d?bat

---

## ?? SOLUTION 4 : Cr?dits Gratuits OpenAI

### **Nouveau Compte :**

OpenAI offre parfois **$5 de cr?dits gratuits** aux nouveaux comptes.

**Pour v?rifier :**
1. Allez sur https://platform.openai.com/settings/organization/billing
2. Regardez "Free trial credits"

### **Si Pas de Cr?dits Gratuits :**

Cr?ez un nouveau compte OpenAI avec une nouvelle adresse email pour obtenir les cr?dits gratuits (si disponibles).

---

## ? V?RIFIER VOS CR?DITS ACTUELS

### **Commande Terminal :**

```bash
curl https://api.openai.com/v1/usage \
  -H "Authorization: Bearer VOTRE_CLE_OPENAI_ICI"
```

### **Via Interface Web :**

https://platform.openai.com/usage

---

## ?? APR?S AVOIR AJOUT? DES CR?DITS

### **1. V?rifiez que c'est OK :**

```bash
cd /Users/jb/telegram-ai-roundtable
python3 test_config.py
```

### **2. Relancez le bot :**

```bash
python3 bot.py
```

### **3. Testez sur Telegram :**

Posez une nouvelle question !

---

## ?? RECOMMANDATION

**Option Id?ale pour D?marrer :**

1. **Ajoutez $10 sur OpenAI** ? Suffisant pour 300-1000 d?bats
2. **Gardez GPT-3.5-turbo** (d?j? configur?) ? 10x moins cher que GPT-4o
3. **Claude et DeepSeek** fonctionnent d?j? ?

**R?sultat :**
- 3 agents IA fonctionnels
- Co?t par d?bat : ~$0.01-0.02 (tr?s abordable)
- $10 = ~500-1000 d?bats

---

## ?? BESOIN D'AIDE ?

### **V?rifier le statut de votre compte OpenAI :**

1. https://platform.openai.com/settings/organization/billing
2. Regardez "Credit balance"
3. Si $0.00 ? Ajoutez un mode de paiement

### **Probl?me de paiement :**

- Contactez le support OpenAI : https://help.openai.com/
- V?rifiez que votre carte est accept?e internationalement

---

## ?? ALTERNATIVES COMPL?TES SANS OPENAI

Si vous ne voulez vraiment pas utiliser OpenAI, vous pouvez :

### **Option A : Claude + DeepSeek uniquement**
(d?j? expliqu? dans Solution 2)

### **Option B : Remplacer OpenAI par Mistral/Llama**

Modifier `agents.py` pour utiliser :
- **Mistral AI** : https://mistral.ai/
- **Groq** (LLama gratuit) : https://groq.com/
- **Together AI** : https://together.ai/

Je peux vous aider ? impl?menter ?a si n?cessaire !

---

## ? R?SUM?

**Votre bot fonctionne D?J? avec :**
- ? **Claude** (corrig?)
- ? **DeepSeek** (OK)
- ? **ChatGPT** (besoin de cr?dits)

**Actions :**
1. **Court terme** : Ajoutez $10 sur OpenAI (recommand?)
2. **Alternative** : D?sactivez ChatGPT temporairement (Solution 2)
3. **?conomie** : Utilisez GPT-3.5 au lieu de GPT-4o (d?j? fait)

---

**Relancez le bot apr?s correction :**

```bash
cd /Users/jb/telegram-ai-roundtable
python3 bot.py
```

Le bot devrait maintenant fonctionner avec **Claude et DeepSeek** ! ??
