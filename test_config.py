"""
Script de test pour v?rifier la configuration du bot.

Usage:
    python test_config.py
"""

import sys
from config import Config

def test_configuration():
    """
    Teste la configuration du bot et affiche le statut.
    """
    print("=" * 50)
    print("?? TEST DE CONFIGURATION DU BOT TELEGRAM")
    print("=" * 50)
    print()
    
    # Tester le chargement de la configuration
    print("?? V?rification des variables d'environnement...")
    print()
    
    status = Config.get_status()
    
    for service, status_icon in status.items():
        print(f"   {service:20s} : {status_icon}")
    
    print()
    print("-" * 50)
    print()
    
    # Validation compl?te
    try:
        Config.validate()
        print("? CONFIGURATION VALIDE !")
        print()
        print("Mod?les configur?s :")
        print(f"   ? OpenAI    : {Config.OPENAI_MODEL}")
        print(f"   ? Anthropic : {Config.ANTHROPIC_MODEL}")
        print(f"   ? DeepSeek  : {Config.DEEPSEEK_MODEL}")
        print()
        print("Param?tres :")
        print(f"   ? Temp?rature : {Config.TEMPERATURE}")
        print(f"   ? Max Tokens  : {Config.MAX_TOKENS}")
        print(f"   ? Timeout     : {Config.API_TIMEOUT}s")
        print(f"   ? Debug Mode  : {Config.DEBUG_MODE}")
        print()
        print("=" * 50)
        print("?? Le bot est pr?t ? ?tre lanc? !")
        print("   Commande : python bot.py")
        print("=" * 50)
        return 0
        
    except ValueError as e:
        print("? CONFIGURATION INVALIDE")
        print()
        print(f"Erreur : {e}")
        print()
        print("?? Actions requises :")
        print("   1. Cr?ez le fichier .env : cp .env.example .env")
        print("   2. ?ditez .env et ajoutez vos cl?s API")
        print("   3. Relancez ce test : python test_config.py")
        print()
        print("=" * 50)
        return 1

if __name__ == "__main__":
    sys.exit(test_configuration())
