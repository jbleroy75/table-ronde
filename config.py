"""
Configuration et gestion des cl?s API pour le bot Telegram multi-agent.

Ce fichier centralise toutes les configurations n?cessaires au fonctionnement
du bot : cl?s API des diff?rents mod?les, token Telegram, et param?tres de d?bat.
"""

import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()


class Config:
    """
    Classe de configuration centralis?e pour le bot Telegram.
    
    Toutes les cl?s API sont charg?es depuis les variables d'environnement
    pour des raisons de s?curit?. Ne jamais commit les cl?s en dur.
    """
    
    # === TELEGRAM ===
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    # === API KEYS DES MOD?LES IA ===
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
    
    # === PARAM?TRES DES MOD?LES ===
    # Mod?les utilis?s pour chaque agent
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
    ANTHROPIC_MODEL = os.getenv('ANTHROPIC_MODEL', 'claude-3-5-sonnet-20241022')
    DEEPSEEK_MODEL = os.getenv('DEEPSEEK_MODEL', 'deepseek-chat')
    
    # === PARAM?TRES DE G?N?RATION ===
    # Temp?rature : contr?le la cr?ativit? (0.0 = d?terministe, 2.0 = tr?s cr?atif)
    TEMPERATURE = float(os.getenv('TEMPERATURE', '0.8'))
    
    # Nombre maximum de tokens par r?ponse
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', '500'))
    
    # === PARAM?TRES DE D?BAT ===
    # Timeout pour les appels API (en secondes)
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))
    
    # Activer/d?sactiver les logs d?taill?s
    DEBUG_MODE = os.getenv('DEBUG_MODE', 'False').lower() == 'true'
    
    @classmethod
    def validate(cls):
        """
        Valide que toutes les cl?s API n?cessaires sont configur?es.
        
        Raises:
            ValueError: Si une cl? API obligatoire est manquante.
        """
        required_keys = {
            'TELEGRAM_BOT_TOKEN': cls.TELEGRAM_BOT_TOKEN,
            'OPENAI_API_KEY': cls.OPENAI_API_KEY,
            'ANTHROPIC_API_KEY': cls.ANTHROPIC_API_KEY,
            'DEEPSEEK_API_KEY': cls.DEEPSEEK_API_KEY,
        }
        
        missing_keys = [key for key, value in required_keys.items() if not value]
        
        if missing_keys:
            raise ValueError(
                f"? Cl?s API manquantes : {', '.join(missing_keys)}\n"
                f"Veuillez configurer ces variables dans votre fichier .env"
            )
    
    @classmethod
    def get_status(cls):
        """
        Retourne le statut de configuration sous forme de dictionnaire.
        
        Returns:
            dict: Statut de chaque cl? API (configur?e ou manquante).
        """
        return {
            'Telegram': '?' if cls.TELEGRAM_BOT_TOKEN else '?',
            'OpenAI': '?' if cls.OPENAI_API_KEY else '?',
            'Anthropic': '?' if cls.ANTHROPIC_API_KEY else '?',
            'DeepSeek': '?' if cls.DEEPSEEK_API_KEY else '?',
        }
