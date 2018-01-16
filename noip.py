#!/usr/bin/python
import requests
import Config
from requests.auth import HTTPBasicAuth

header = {"User-Agent": "NoIPupdate by Andrea Draghetti"}
timeoutconnection = 120

url = "https://dynupdate.no-ip.com/nic/update?hostname=" + Config.hostname
r = requests.get(url, auth=HTTPBasicAuth(Config.username, Config.password), headers=header, timeout=timeoutconnection)


if "nochg" in r.text:
    print "Indirizzo IP corrente, nessun aggiornamento eseguito."

if "good" in r.text:
    print "Indirizzo IP aggiornato: %s" + r.text

if "nohost" in r.text:
    print "Hostname inesistente per l'account specificato."

if "badauth" in r.text:
    print "Nome utente o password non validi."

if "badagent" in r.text:
    print "Client disabilitato."

if "abuse" in r.text:
    print "Nome utente bloccato a causa di un abuso"

if "911" in r.text:
    print "Errore imprevisto."