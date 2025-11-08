"""
Bot Telegram multi-agent : Table ronde avec ChatGPT, Claude et DeepSeek.

Ce bot permet de lancer des débats entre trois IA expertes avec des personnalit?s
distinctes. L'utilisateur peut interrompre, orienter le débat, et recevoir des
synthèses structur?es.

Usage:
    python bot.py
"""

import asyncio
import logging
from typing import Dict, Optional
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from telegram.constants import ParseMode

from config import Config
from agents import ChatGPTAgent, ClaudeAgent, DeepSeekAgent, Synthesizer

# Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO if not Config.DEBUG_MODE else logging.DEBUG
)
logger = logging.getLogger(__name__)


class RoundtableBot:
    """
    Bot Telegram orchestrant la table ronde entre les trois agents IA.
    """
    
    def __init__(self):
        """
        Initialise le bot et les agents IA.
        """
        self.chatgpt = ChatGPTAgent()
        self.claude = ClaudeAgent()
        self.deepseek = DeepSeekAgent()
        self.synthesizer = Synthesizer()
        
        # Stockage des contextes par utilisateur
        self.user_contexts: Dict[int, list] = {}
        
        logger.info("? Bot initialis? avec succ?s")
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Commande /start : Message de bienvenue.
        
        Args:
            update: Objet Update de Telegram
            context: Contexte de la conversation
        """
        welcome_message = """🎉 **BIENVENUE À LA TABLE RONDE IA**

Trois experts IA débattent pour vous :

**🧠 ChatGPT** → Logique & Structuration
Analyse méthodique et argumentation rationnelle

**🎯 Claude** → Nuance & Profondeur  
Réflexion critique et perspectives subtiles

**⚡ DeepSeek** → Franc-parler & Innovation
Critique directe, humour noir, idées disruptives

━━━━━━━━━━━━━━━━

**COMMENT ÇA MARCHE ?**

1️⃣ Posez une question ou partagez une idée
2️⃣ Les 3 IA débattent (format bullet points)
3️⃣ Synthèse automatique avec recommandations
4️⃣ Vous pouvez interrompre/orienter à tout moment

━━━━━━━━━━━━━━━━

**COMMANDES DISPONIBLES :**

/start → Afficher ce message
/help → Aide détaillée
/status → Vérifier l'état des API
/reset → Réinitialiser le contexte
/stop → Arrêter le débat en cours

━━━━━━━━━━━━━━━━

**STYLE DE DÉBAT :**
- Réponses ultra courtes (bullet points)
- Critiques franches et constructives
- Pas de complaisance
- Synthèse systématique

🚀 **Prêt ? Posez votre première question !**
"""
        await update.message.reply_text(
            welcome_message,
            parse_mode=ParseMode.MARKDOWN
        )
        logger.info(f"Commande /start par user {update.effective_user.id}")
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Commande /help : Aide d?taill?e.
        """
        help_message = """?? **AIDE D?TAILL?E**

**UTILISATION DE BASE :**

Envoyez simplement votre question ou id?e en message.
Le bot lance automatiquement le débat entre les 3 IA.

**EXEMPLES DE QUESTIONS :**

?? "Comment optimiser mon funnel de conversion ?"
?? "Strat?gie marketing pour un SaaS B2B ?"
?? "Architecture microservices : pour ou contre ?"
?? "Comment pitcher mon projet ? des investisseurs ?"

????????????????????

**PERSONNALIT?S DES AGENTS :**

**ChatGPT** ??
? D?compose m?thodiquement
? Structure la r?flexion
? Argumentation logique

**Claude** ??
? Identifie les nuances
? Questionne les hypoth?ses
? Approche critique et r?fl?chie

**DeepSeek** ?
? Franc-parler, sans filtre
? Critique durement si n?cessaire
? Propositions innovantes/provocantes
? Humour noir autoris?

????????????????????

**ASTUCES :**

? Soyez pr?cis dans vos questions
? Donnez du contexte si n?cessaire
? Interrompez pour orienter le débat
? Utilisez /reset si le contexte d?rive

**LIMITES :**

?? R?ponses courtes par design
?? Pas de code long (extraits uniquement)
?? Focus sur l'essentiel, pas les d?tails

????????????????????

Des questions ? Testez simplement !
"""
        await update.message.reply_text(
            help_message,
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Commande /status : V?rifier l'?tat des API.
        """
        status = Config.get_status()
        
        status_message = f"""?? **STATUT DES API**

Telegram Bot : {status['Telegram']}
OpenAI (ChatGPT) : {status['OpenAI']}
Anthropic (Claude) : {status['Anthropic']}
DeepSeek : {status['DeepSeek']}

????????????????????

**MOD?LES UTILIS?S :**

? OpenAI : `{Config.OPENAI_MODEL}`
? Anthropic : `{Config.ANTHROPIC_MODEL}`
? DeepSeek : `{Config.DEEPSEEK_MODEL}`

**PARAM?TRES :**

? Temp?rature : {Config.TEMPERATURE}
? Max tokens : {Config.MAX_TOKENS}
? Timeout : {Config.API_TIMEOUT}s
"""
        await update.message.reply_text(
            status_message,
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def reset_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Commande /reset : R?initialiser le contexte de conversation.
        """
        user_id = update.effective_user.id
        
        if user_id in self.user_contexts:
            del self.user_contexts[user_id]
        
        await update.message.reply_text(
            "?? **Contexte r?initialis?**\n\nVous pouvez repartir sur un nouveau sujet.",
            parse_mode=ParseMode.MARKDOWN
        )
        logger.info(f"Contexte r?initialis? pour user {user_id}")
    
    async def stop_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Commande /stop : Arr?ter le débat en cours.
        """
        await update.message.reply_text(
            "?? **D?bat interrompu**\n\nUtilisez /reset pour repartir sur un nouveau sujet.",
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        G?re les messages utilisateur et lance le débat multi-agent.
        
        Args:
            update: Objet Update de Telegram
            context: Contexte de la conversation
        """
        user_id = update.effective_user.id
        user_message = update.message.text
        
        logger.info(f"Message de user {user_id}: {user_message[:50]}...")
        
        # Envoyer un message de chargement
        thinking_msg = await update.message.reply_text(
            "⏳ **Débat en cours...**\n\nLes agents analysent votre question...",
            parse_mode=ParseMode.MARKDOWN
        )
        
        try:
            # Obtenir le contexte de l'utilisateur
            if user_id not in self.user_contexts:
                self.user_contexts[user_id] = []
            
            user_context = self.user_contexts[user_id]
            
            # Lancer les 3 agents en parall?le pour plus de rapidit?
            chatgpt_task = asyncio.create_task(
                self.chatgpt.generate_response(user_message, user_context)
            )
            claude_task = asyncio.create_task(
                self.claude.generate_response(user_message, user_context)
            )
            deepseek_task = asyncio.create_task(
                self.deepseek.generate_response(user_message, user_context)
            )
            
            # Attendre toutes les réponses
            chatgpt_response = await chatgpt_task
            claude_response = await claude_task
            deepseek_response = await deepseek_task
            
            # Stocker les réponses pour la synthèse
            agents_responses = {
                'ChatGPT': chatgpt_response,
                'Claude': claude_response,
                'DeepSeek': deepseek_response
            }
            
            # G?n?rer la synthèse
            synthesis = await self.synthesizer.generate_synthesis(
                user_message,
                agents_responses
            )
            
            # Formatter la réponse finale
            formatted_response = self._format_roundtable_response(
                agents_responses,
                synthesis
            )
            
            # Supprimer le message de chargement
            await thinking_msg.delete()
            
            # Envoyer la réponse
            await update.message.reply_text(
                formatted_response,
                parse_mode=ParseMode.MARKDOWN
            )
            
            # Mettre ? jour le contexte
            user_context.append({"role": "user", "content": user_message})
            user_context.append({
                "role": "assistant",
                "content": f"ChatGPT: {chatgpt_response}\nClaude: {claude_response}\nDeepSeek: {deepseek_response}"
            })
            
            # Limiter l'historique pour ?viter les contextes trop longs
            if len(user_context) > 10:
                user_context = user_context[-10:]
                self.user_contexts[user_id] = user_context
            
            logger.info(f"D?bat termin? pour user {user_id}")
            
        except Exception as e:
            logger.error(f"Erreur lors du débat: {e}", exc_info=True)
            
            await thinking_msg.delete()
            await update.message.reply_text(
                "? **Erreur**\n\nUne erreur s'est produite lors du débat. "
                "V?rifiez vos cl?s API et r?essayez.\n\n"
                f"D?tails: {str(e)[:100]}",
                parse_mode=ParseMode.MARKDOWN
            )
    
    def _format_roundtable_response(
        self,
        agents_responses: Dict[str, str],
        synthesis: str
    ) -> str:
        """
        Formate la réponse de la table ronde pour Telegram.
        
        Args:
            agents_responses: R?ponses des agents
            synthesis: Synth?se du débat
            
        Returns:
            str: R?ponse format?e en Markdown
        """
        response = "🎯 **TABLE RONDE**\n\n"
        response += "━━━━━━━━━━━━━━━━\n\n"
        
        # ChatGPT
        response += "**🧠 ChatGPT** • *Logique*\n"
        response += f"{agents_responses['ChatGPT']}\n\n"
        response += "━━━━━━━━━━━━━━━━\n\n"
        
        # Claude
        response += "**🎯 Claude** • *Nuance*\n"
        response += f"{agents_responses['Claude']}\n\n"
        response += "━━━━━━━━━━━━━━━━\n\n"
        
        # DeepSeek
        response += "**⚡ DeepSeek** • *Franc-parler*\n"
        response += f"{agents_responses['DeepSeek']}\n\n"
        response += "━━━━━━━━━━━━━━━━\n\n"
        
        # Synthèse
        response += "**🎯 SYNTHÈSE**\n"
        response += f"{synthesis}\n\n"
        response += "━━━━━━━━━━━━━━━━\n\n"
        response += "📌 *Continuez le débat ou posez une nouvelle question*"
        
        return response
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        G?re les erreurs globales du bot.
        """
        logger.error(f"Exception lors de l'update {update}: {context.error}", exc_info=context.error)


def main():
    """
    Point d'entr?e principal du bot Telegram.
    """
    # Valider la configuration
    try:
        Config.validate()
        logger.info("? Configuration validée")
    except ValueError as e:
        logger.error(f"? Erreur de configuration: {e}")
        return
    
    # Cr?er l'instance du bot
    bot = RoundtableBot()
    
    # Cr?er l'application Telegram
    application = Application.builder().token(Config.TELEGRAM_BOT_TOKEN).build()
    
    # Enregistrer les handlers de commandes
    application.add_handler(CommandHandler("start", bot.start_command))
    application.add_handler(CommandHandler("help", bot.help_command))
    application.add_handler(CommandHandler("status", bot.status_command))
    application.add_handler(CommandHandler("reset", bot.reset_command))
    application.add_handler(CommandHandler("stop", bot.stop_command))
    
    # Handler pour les messages texte
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message)
    )
    
    # Handler d'erreurs
    application.add_error_handler(bot.error_handler)
    
    # Lancer le bot
    logger.info("?? D?marrage du bot Telegram...")
    logger.info("?? Bot en ?coute. Appuyez sur Ctrl+C pour arr?ter.")
    
    # D?marrer le polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
