#!/bin/bash
# Iniciar o Nginx em primeiro plano
service nginx start
# Iniciar o aplicativo Python em segundo plano
python3 app.py