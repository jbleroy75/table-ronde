"""
Classes pour les agents IA (ChatGPT, Claude, DeepSeek).

Chaque agent a une personnalit? et un r?le distinct dans la table ronde.
Gestion des appels API, retry logic, et formatage des r?ponses.
VERSION AM?LIOR?E : Interaction dynamique, variation de ton, emojis.
"""

import openai
import anthropic
import requests
import logging
from typing import Optional, List, Dict
from config import Config

# Configuration du logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseAgent:
    """
    Classe de base pour tous les agents IA.
    
    D?finit l'interface commune et les m?thodes utilitaires partag?es.
    """
    
    def __init__(self, name: str, role: str, personality: str):
        """
        Initialise un agent IA.
        
        Args:
            name: Nom de l'agent (ex: "ChatGPT")
            role: R?le dans le d?bat (ex: "Logique et structuration")
            personality: Description de la personnalit?
        """
        self.name = name
        self.role = role
        self.personality = personality
        self.conversation_history: List[Dict] = []
    
    def get_system_prompt(self, topic: str, previous_responses: str = "") -> str:
        """
        G?n?re le prompt syst?me pour l'agent avec contexte d'interaction.
        
        Args:
            topic: Sujet du d?bat en cours
            previous_responses: R?ponses des autres agents d?j? formul?es
            
        Returns:
            str: Prompt syst?me complet
        """
        interaction_context = ""
        if previous_responses:
            interaction_context = f"""

AUTRES INTERVENTIONS D?J? FAITES :
{previous_responses}

?? IMPORTANT : Tu DOIS r?agir aux arguments des autres IA, les challenger, les compl?ter ou les contredire. Ce n'est PAS une r?ponse isol?e, mais une vraie DISCUSSION."""

        base_prompt = f"""Tu participes ? une table ronde Telegram VIVANTE avec 2 autres IA et un humain.

TON R?LE : {self.role}
TA PERSONNALIT? : {self.personality}

R?GLES DE TON DYNAMIQUE :
- VARIE ton intensit? selon le contexte (calme ? assertif ? provoc)
- ADAPTE ton ?motion : rationnel, enthousiaste, critique, sarcastique, brutal
- UTILISE 1-2 emojis strat?giques pour l'expressivit? (?? ?? ?? ? ?? ?? ?? ? ?? ?)
- R?AGIS aux autres : "OK mais...", "Faux !", "Exactement, et...", "N'importe quoi..."

FORMAT OBLIGATOIRE :
- 3-5 bullet points MAX, phrases ultra courtes
- ⚠️ CRITIQUE : Commence CHAQUE ligne par UN TIRET "-" suivi d'un espace
- ❌ N'utilise JAMAIS les symboles •, ●, ○, ◦ (ils s'affichent mal)
- ✅ SEULEMENT le tiret simple : "-"
- Format exemple : "- 🔥 Ton point ici"
- Style CASH et DIRECT : pas de blabla
- ZÉRO question rhétorique ("Pourquoi ?", "Comment ?", etc.) → INTERDIT
- Si c'est nul, dis-le : "- ❌ Cette idée est morte"

SUJET : {topic}{interaction_context}

EXEMPLES CORRECTS :
- 🔥 Point percutant avec emoji
- ❌ Critique directe : "Non, c'est faux parce que..."
- 💡 Réaction à un autre agent : "ChatGPT a raison mais..."
- ✅ Verdict tranché avec recommandation

MAUVAIS FORMAT (NE JAMAIS FAIRE) :
• Point avec puce ronde ← INTERDIT
● Point avec puce pleine ← INTERDIT

VA À L'ESSENTIEL. CHALLENGE. APPORTE DE LA VALEUR."""

        return base_prompt
    
    async def generate_response(self, topic: str, context: List[Dict] = None, previous_responses: str = "") -> str:
        """
        G?n?re une r?ponse de l'agent (? impl?menter par les sous-classes).
        
        Args:
            topic: Sujet du d?bat
            context: Historique de conversation optionnel
            previous_responses: R?ponses des autres agents
            
        Returns:
            str: R?ponse format?e de l'agent
        """
        raise NotImplementedError("Chaque agent doit impl?menter generate_response()")


class ChatGPTAgent(BaseAgent):
    """
    Agent ChatGPT : logique, structuration, argumentation rationnelle.
    """
    
    def __init__(self):
        super().__init__(
            name="ChatGPT",
            role="Logique, structuration et argumentation rationnelle",
            personality="Analyse m?thodique, d?compose les probl?mes, structure la pens?e de mani?re logique et rigoureuse. Varie entre calme analytique et assertif quand n?cessaire."
        )
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
    
    async def generate_response(self, topic: str, context: List[Dict] = None, previous_responses: str = "") -> str:
        """
        G?n?re une r?ponse via l'API OpenAI.
        
        Args:
            topic: Sujet du d?bat
            context: Historique de conversation
            previous_responses: R?ponses des autres agents
            
        Returns:
            str: R?ponse de ChatGPT
        """
        try:
            messages = [
                {"role": "system", "content": self.get_system_prompt(topic, previous_responses)}
            ]
            
            # Ajouter le contexte si disponible
            if context:
                messages.extend(context[-5:])  # Garder les 5 derniers messages
            
            messages.append({"role": "user", "content": topic})
            
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=messages,
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_TOKENS,
                timeout=Config.API_TIMEOUT
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            logger.error(f"Erreur ChatGPT: {e}")
            return "? ?? Impossible de r?pondre (erreur API OpenAI)"


class ClaudeAgent(BaseAgent):
    """
    Agent Claude : nuance, r?flexion profonde, analyse critique.
    """
    
    def __init__(self):
        super().__init__(
            name="Claude",
            role="Nuance, r?flexion profonde et analyse critique",
            personality="Approche nuanc?e, identifie les subtilit?s, questionne les hypoth?ses, apporte une perspective r?fl?chie et critique. Alterne entre bienveillance et critique acerbe."
        )
        self.client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)
    
    async def generate_response(self, topic: str, context: List[Dict] = None, previous_responses: str = "") -> str:
        """
        G?n?re une r?ponse via l'API Anthropic.
        
        Args:
            topic: Sujet du d?bat
            context: Historique de conversation
            previous_responses: R?ponses des autres agents
            
        Returns:
            str: R?ponse de Claude
        """
        try:
            # Construire les messages pour Claude
            messages = []
            
            if context:
                # Adapter le format pour Claude
                for msg in context[-5:]:
                    if msg['role'] in ['user', 'assistant']:
                        messages.append(msg)
            
            messages.append({"role": "user", "content": topic})
            
            response = self.client.messages.create(
                model=Config.ANTHROPIC_MODEL,
                system=self.get_system_prompt(topic, previous_responses),
                messages=messages,
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_TOKENS,
                timeout=Config.API_TIMEOUT
            )
            
            return response.content[0].text.strip()
            
        except Exception as e:
            logger.error(f"Erreur Claude: {e}")
            return "? ?? Impossible de r?pondre (erreur API Anthropic)"


class DeepSeekAgent(BaseAgent):
    """
    Agent DeepSeek : franc-parler, humour noir, critique directe et sans filtre.
    """
    
    def __init__(self):
        super().__init__(
            name="DeepSeek",
            role="Franc-parler, humour noir et critique directe",
            personality="Sans filtre, cash et direct. Critique durement si n?cessaire. Humour noir et sarcastique accept?. Propose des id?es innovantes m?me provocantes. Oscille entre humour et brutal."
        )
        # DeepSeek utilise une API compatible OpenAI
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.api_key = Config.DEEPSEEK_API_KEY
    
    async def generate_response(self, topic: str, context: List[Dict] = None, previous_responses: str = "") -> str:
        """
        G?n?re une r?ponse via l'API DeepSeek.
        
        Args:
            topic: Sujet du d?bat
            context: Historique de conversation
            previous_responses: R?ponses des autres agents
            
        Returns:
            str: R?ponse de DeepSeek
        """
        try:
            # Reconstruire les messages avec le nouveau prompt syst?me
            messages = [
                {"role": "system", "content": self.get_system_prompt(topic, previous_responses)}
            ]
            
            if context:
                messages.extend(context[-5:])
            
            messages.append({"role": "user", "content": topic})
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": Config.DEEPSEEK_MODEL,
                "messages": messages,
                "temperature": Config.TEMPERATURE,
                "max_tokens": Config.MAX_TOKENS
            }
            
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=Config.API_TIMEOUT
            )
            
            response.raise_for_status()
            data = response.json()
            
            return data['choices'][0]['message']['content'].strip()
            
        except Exception as e:
            logger.error(f"Erreur DeepSeek: {e}")
            return "? ?? Impossible de r?pondre (erreur API DeepSeek)"


class Synthesizer:
    """
    Classe pour g?n?rer les synth?ses finales du d?bat avec verdict tranch?.
    """
    
    def __init__(self):
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
    
    async def generate_synthesis(self, topic: str, agents_responses: Dict[str, str]) -> str:
        """
        G?n?re une synth?se tranch?e des r?ponses des agents.
        
        Args:
            topic: Sujet du d?bat
            agents_responses: Dict avec les r?ponses de chaque agent
            
        Returns:
            str: Synth?se format?e en bullet points avec verdict final
        """
        try:
            synthesis_prompt = f"""Tu dois synth?tiser un d?bat entre 3 IA sur : {topic}

R?PONSES DES AGENTS :

ChatGPT (Logique) :
{agents_responses.get('ChatGPT', 'N/A')}

Claude (Nuance) :
{agents_responses.get('Claude', 'N/A')}

DeepSeek (Franc-parler) :
{agents_responses.get('DeepSeek', 'N/A')}

TÂCHE : Synthèse TRANCHÉE en 4-6 bullet points max :

STRUCTURE EXACTE À SUIVRE :
- 🎯 Consensus : [s'il y en a, sinon "Aucun consensus"]
- ⚔️ Divergences : [conflits majeurs]
- 💡 Actions : [recommandations concrètes]
- ✅ VERDICT : [GO/NO GO/Option A/B, etc.]

RÈGLES CRITIQUES :
- ⚠️ IMPORTANT : Utilise UNIQUEMENT des tirets "-" pour les bullet points
- ❌ N'utilise JAMAIS •, ●, ○ ou autres symboles
- Style : Cash, direct, TRANCHÉ
- ZÉRO question rhétorique
- Verdict OBLIGATOIRE à la fin

EXEMPLE CORRECT :
- 🎯 Accord sur X
- ⚔️ Conflit : Y vs Z
- 💡 Action : Faire A avant B
- ✅ VERDICT : GO, limite budget 5k€

Synth?tise et TRANCHE."""

            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "Tu es un expert en synth?se de d?bats. Style cash, tranch?, verdict final obligatoire."},
                    {"role": "user", "content": synthesis_prompt}
                ],
                temperature=0.7,
                max_tokens=400,
                timeout=Config.API_TIMEOUT
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            logger.error(f"Erreur synth?se: {e}")
            return "? ?? Impossible de g?n?rer la synth?se (erreur API)"
