from urllib.parse import urlparse
from collections import Counter

links = """
proposte@raffaellocortina.it
glaterza@laterza.it
proposte@ponteallegrazie.it
manoscritti.giunti.it/submit
proposte@ilsaggiatore.com
manoscritti@codiceedizioni.it
redazione@tlon.it
proposte.editoriali@chiarelettere.it
direzione.editoriale@lindau.it
manoscritti@adelphi.it
manoscritti@elliotedizioni.it
direzioneeditoriale@giunti.it
infolibri@cairoeditore.it
manoscritti.saggistica@castelvecchieditore.com
f.alo@lswr.it
proposte.editoriali@deagostinilibri.it
proposte@deriveapprodi.org
info@bietti.it
einaudi@einaudi.it
info@sperling.it
info@garzantilibri.it
manoscritti@giulioperroneditore.com
info@guanda.it
segreteria.editoriale@harpercollins.it
imprimatureditore@gmail.com
comunicazione@lanavediteseo.eu
manoscritti@lemezzelane.eu
https://www.leoneeditore.it/invia-manoscritto/invio-manoscritto-online/
info@longanesi.it
proposte@marcosymarcos.com
segreteria@marsilioeditori.it
editing@minervaedizioni.com
segreteria.letteraria@mondadori.it
manoscritti@editricenord.it
manoscritti@nutrimenti.net
info@pandaedizioni.it
proposte@rizzoli.eu
info@safaraeditore.com
sanpaoloedizioni@stpauls.it
info@sellerio.it 
segreteria@marsilioeditori.it
info@transeuropaedizioni.it
dattiloscritti@mursia.com
hoepli@hoepli.it
info@pianobedizioni.com
redazione@lacaravellaeditrice.it
redazione@erickson.it
info@vallardi.it
info@fontanaeditore.com
editoriale@egeaonline.com
https://www.elledici.org/contatti/
info@brunoleoni.org
https://www.tecnichenuove.com/contattaci
info@utetlibri.it
libri@terranuova.it
segreteria@este.it
https://www.mulino.it/submission
redazione@roiedizioni.it
info@bollatiboringhieri.it
segreteria@mylife.it
copyright@gruppomacro.com
info@mgmtedizioni.com
manoscritti@viella.it
c.cauda@slowfood.it
b.ciampichetti@astrolabio-ubaldini.com
info@edizioniares.it
l.lavarello@epclibri.it
ordinilswr@lswr.it (sezione "Segnalazione catalogo")
editori@guida.it
manoscritti@edizionigrenelle.com
info@centroesserci.it
www.carocci.it/proposte-editoriali
manoscritti@baldinicastoldi.it
info@erasmolibri.it


editore@donzelli.it
redazione@edizionidedalo.it
mimesis@mimesisedizioni.it
info@abocaedizioni.it
info@francoangeli.it


proposte@rubbettino.it
proposte@quodlibet.it
redazione@santellieditore.it






manoscritti@gemmaedizioni.it

"""

links = links.split("\n")

def extract_domain(url: str) -> str:
    url = url.strip()
    if "@" in url:
        return url  # è un'email, la restituiamo così com'è
    if not url.startswith("http"):
        url = "https://" + url
    try:
        hostname = urlparse(url).hostname or ""
        return hostname.lower().removeprefix("www.")
    except Exception:
        return url.lower().removeprefix("www.").split("/")[0]


# Costruiamo la mappa dominio -> lista di URL originali
domain_map: dict[str, list[str]] = {}
for link in links:
    if link.strip()=="" or link == "Sito":
        continue
    domain = extract_domain(link)
    domain_map.setdefault(domain, []).append(link)

# Troviamo i duplicati (domini con più di un link)
duplicates = {d: urls for d, urls in domain_map.items() if len(urls) > 1}

print("=" * 60)
print(f"  Link totali   : {len(links)}")
print(f"  Domini unici  : {len(domain_map)}")
print(f"  Domini duplicati: {len(duplicates)}")
print("=" * 60)

if duplicates:
    print("\nDOMINI DUPLICATI:\n")
    for domain, urls in duplicates.items():
        print(f"  {domain}  ({len(urls)} occorrenze)")
        for u in urls:
            print(f"    - {u}")
        print()
else:
    print("\nNessun dominio duplicato trovato.")
