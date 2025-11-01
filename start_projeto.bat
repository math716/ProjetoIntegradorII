@echo off
title Projeto Integrador II - Instalador automático
color 0b

echo =======================================================
echo     🚀 Iniciando configuracao do Projeto Integrador II
echo =======================================================
echo.

:: Pausa inicial para o usuário ler
pause

:: Verifica se o Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python nao encontrado no sistema!
    echo 👉 Baixe e instale em: https://www.python.org/downloads/
    echo 💡 Marque a opcao "Add Python to PATH" durante a instalacao.
    echo.
    pause
    exit /b
)

:: Cria o ambiente virtual se não existir
if not exist "venv\" (
    echo 🧱 Criando ambiente virtual...
    python -m venv venv
)

:: Ativa o ambiente virtual
echo 🔄 Ativando ambiente virtual...
call venv\Scripts\activate.bat

:: Atualiza pip
echo 🔧 Atualizando pip...
python -m pip install --upgrade pip

:: Instala dependencias
echo 📦 Instalando dependencias do projeto...
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart

:: Verifica se o main.py existe
if not exist "main.py" (
    echo ❌ ERRO: Arquivo main.py nao encontrado na pasta atual!
    echo Certifique-se de que o .bat esta na MESMA pasta do main.py.
    echo.
    pause
    exit /b
)

:: Inicia o sistema
echo ✅ Instalacao concluida com sucesso!
echo 🌐 O sistema sera iniciado em http://127.0.0.1:8000
echo =======================================================
echo.

start "" "http://127.0.0.1:8000"
python -m uvicorn main:app --reload

echo.
echo 💚 Sistema encerrado. Pressione qualquer tecla para sair.
pause
