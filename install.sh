#!/bin/bash

# ===================================
# Script d'installation du Bot Telegram Multi-Agent
# ===================================

echo "?? INSTALLATION DU BOT TELEGRAM MULTI-AGENT"
echo "=============================================="
echo ""

# V?rifier Python
echo "1?? V?rification de Python..."
if ! command -v python3 &> /dev/null; then
    echo "? Python 3 n'est pas install?."
    echo "   Installez Python 3.9+ depuis https://www.python.org/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "? Python $PYTHON_VERSION d?tect?"
echo ""

# V?rifier pip
echo "2?? V?rification de pip..."
if ! command -v pip3 &> /dev/null; then
    echo "? pip3 n'est pas install?."
    exit 1
fi
echo "? pip3 disponible"
echo ""

# Installer les d?pendances
echo "3?? Installation des d?pendances..."
pip3 install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "? D?pendances install?es avec succ?s"
else
    echo "? Erreur lors de l'installation des d?pendances"
    exit 1
fi
echo ""

# Copier .env.example si .env n'existe pas
echo "4?? Configuration..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "? Fichier .env cr??"
    echo ""
    echo "??  IMPORTANT : ?ditez le fichier .env et ajoutez vos cl?s API"
    echo ""
    echo "   ?ditez avec : nano .env"
    echo ""
    echo "   Cl?s requises :"
    echo "   - TELEGRAM_BOT_TOKEN"
    echo "   - OPENAI_API_KEY"
    echo "   - ANTHROPIC_API_KEY"
    echo "   - DEEPSEEK_API_KEY"
else
    echo "? Fichier .env existe d?j?"
fi
echo ""

# Instructions finales
echo "=============================================="
echo "?? INSTALLATION TERMIN?E !"
echo "=============================================="
echo ""
echo "?? PROCHAINES ?TAPES :"
echo ""
echo "1. Configurez vos cl?s API dans .env :"
echo "   nano .env"
echo ""
echo "2. Testez la configuration :"
echo "   python3 test_config.py"
echo ""
echo "3. Lancez le bot :"
echo "   python3 bot.py"
echo ""
echo "=============================================="
echo ""
echo "?? Documentation compl?te : README.md"
echo "?? Guide rapide : GUIDE_RAPIDE.md"
echo "?? Exemples : EXEMPLES_USAGE.md"
echo ""
