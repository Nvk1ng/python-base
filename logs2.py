#!/usr/bin/env python3
import logging
import os 
from logging import handlers

# BOILERPLATE
# TODO: usar funcao 
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger(__name__, log_level) 
fh = handlers.RotatingFileHandler("meulog.log", maxBytes=100, backupCount=10,)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
    )
fh.setFormatter(fmt)
log.addHandler(fh)


"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: O banco de dados sumiu")
"""

try: 
    1 / 0 
except ZeroDivisionError as e:
   log.error("[ERRO] DEU ERRO %s", str(e)) 