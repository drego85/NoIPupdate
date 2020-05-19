#!/usr/bin/python
import Config
import logging
import requests
from requests.auth import HTTPBasicAuth

header = {"User-Agent": "NoIPupdate by Andrea Draghetti"}
timeoutconnection = 120

# Inizializzo i LOG ignorando i messaggi standard delle librerie requests e urllib3
logging.basicConfig(filename="noip.log",
                    format="%(asctime)s - %(funcName)10s():%(lineno)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("selenium").setLevel(logging.WARNING)
logging.getLogger("dropbox").setLevel(logging.WARNING)

url = "https://dynupdate.no-ip.com/nic/update?hostname=" + Config.hostname

try:
    r = requests.get(url, auth=HTTPBasicAuth(Config.username, Config.password), headers=header,
                     timeout=timeoutconnection)

    if "nochg" in r.text:
        logging.info("Indirizzo IP corrente, nessun aggiornamento eseguito.")

    if "good" in r.text:
        logging.info("Indirizzo IP aggiornato: %s" + r.text)

    if "nohost" in r.text:
        logging.info("Hostname inesistente per l'account specificato.")

    if "badauth" in r.text:
        logging.info("Nome utente o password non validi.")

    if "badagent" in r.text:
        logging.info("Client disabilitato.")

    if "abuse" in r.text:
        logging.info("Nome utente bloccato a causa di un abuso")

    if "911" in r.text:
        logging.info("Errore imprevisto.")
except:
    logging.info("Errore imprevisto.")
