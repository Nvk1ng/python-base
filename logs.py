#!/usr/bin/env python3
import logging
import os 

# BOILERPLATE
# TODO: usar funcao 
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger(__name__, log_level) 
ch = logging.StreamHandler() # console/terminal/stderr
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
    )
ch.setFormatter(fmt)
log.addHandler(ch)


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