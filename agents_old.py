"""
Classes pour les agents IA (ChatGPT, Claude, DeepSeek).

Chaque agent a une personnalit? et un r?le distinct dans la table ronde.
Gestion des appels API, retry logic, et formatage des r?ponses.
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
    
    def get_system_prompt(self, topic: str) -> str:
        """
        G?n?re le prompt syst?me pour l'agent.
        
        Args:
            topic: Sujet du d?bat en cours
            
        Returns:
            str: Prompt syst?me complet
        """
        base_prompt = f"""Tu participes ? une table ronde Telegram avec 2 autres IA et un humain.

TON R?LE : {self.role}
TA PERSONNALIT? : {self.personality}

R?GLES ABSOLUES :
- R?ponses ULTRA COURTES : 3-5 bullet points max, phrases percutantes
- Format OBLIGATOIRE : bullet points uniquement (?)
- Style CASH et DIRECT : pas de politesse excessive, va ? l'essentiel
- Critique HONN?TE : si c'est nul, dis-le franchement
- PAS de longues tirades, PAS de paragraphes, UNIQUEMENT des points cl?s
- Apporte ta perspective unique selon ton r?le

SUJET DU D?BAT : {topic}

EXEMPLES DE FORMAT ATTENDU :
? Point cl? 1 (court et percutant)
? Critique directe si n?cessaire
? Recommandation concr?te

Analyse vite, critique sans filtre, apporte de la valeur."""

        return base_prompt
    
    async def generate_response(self, topic: str, context: List[Dict] = None, previous_responses: str = "") -> str:
        """
        G?n?re une r?ponse de l'agent (? impl?menter par les sous-classes).
        
        Args:
            topic: Sujet du d?bat
            context: Historique de conversation optionnel
            
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
            personality="Analyse m?thodique, d?compose les probl?mes, structure la pens?e de mani?re logique et rigoureuse."
        )
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
    
    async def generate_response(self, topic: str, context: List[Dict] = None, previous_responses: str = "") -> str:
        """
        G?n?re une r?ponse via l'API OpenAI.
        
        Args:
            topic: Sujet du d?bat
            context: Historique de conversation
            
        Returns:
            str: R?ponse de ChatGPT
        """
        try:
            messages = [
                {"role": "system", "content": self.get_system_prompt(topic)}
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
            personality="Approche nuanc?e, identifie les subtilit?s, questionne les hypoth?ses, apporte une perspective r?fl?chie et critique."
        )
        self.client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)
    
    async def generate_response(self, topic: str, context: List[Dict] = None, previous_responses: str = "") -> str:
        """
        G?n?re une r?ponse via l'API Anthropic.
        
        Args:
            topic: Sujet du d?bat
            context: Historique de conversation
            
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
            personality="Sans filtre, cash et direct. Critique durement si n?cessaire. Humour noir accept?. Propose des id?es innovantes m?me provocantes."
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
            
        Returns:
            str: R?ponse de DeepSeek
        """
        try:
            messages = [
                {"role": "system", "content": self.get_system_prompt(topic)}
            ]
            
            # Ajouter le contexte si disponible
            if context:
                messages.extend(context[-5:])
            
            messages.append({"role": "user", "content": topic})
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Reconstruire les messages avec le nouveau prompt syst?me
            messages_with_context = [
                {"role": "system", "content": self.get_system_prompt(topic, previous_responses)}
            ]
            
            if context:
                messages_with_context.extend(context[-5:])
            
            messages_with_context.append({"role": "user", "content": topic})
            
            payload = {
                "model": Config.DEEPSEEK_MODEL,
                "messages": messages_with_context,
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
    Classe pour g?n?rer les synth?ses finales du d?bat.
    """
    
    def __init__(self):
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
    
    async def generate_synthesis(self, topic: str, agents_responses: Dict[str, str]) -> str:
        """
        G?n?re une synth?se des r?ponses des agents.
        
        Args:
            topic: Sujet du d?bat
            agents_responses: Dict avec les r?ponses de chaque agent
            
        Returns:
            str: Synth?se format?e en bullet points
        """
        try:
            synthesis_prompt = f"""Tu dois synth?tiser un d?bat entre 3 IA sur ce sujet : {topic}

R?PONSES DES AGENTS :

ChatGPT (Logique) :
{agents_responses.get('ChatGPT', 'N/A')}

Claude (Nuance) :
{agents_responses.get('Claude', 'N/A')}

DeepSeek (Franc-parler) :
{agents_responses.get('DeepSeek', 'N/A')}

T?CHE : Synth?se ULTRA COURTE en bullet points (4-6 points max) :
? Points de consensus
? Points de divergence
? Recommandations concr?tes et actionnables
? Prochaines ?tapes sugg?r?es

Format OBLIGATOIRE : bullet points uniquement, phrases courtes et percutantes."""

            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "Tu es un expert en synth?se de d?bats. R?ponses ultra courtes en bullet points uniquement."},
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
