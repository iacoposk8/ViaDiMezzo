from urllib.parse import urlparse
from collections import Counter

links = """
Sito
https://www.raffaellocortina.it/contattaci.html
www.laterza.it
https://www.ponteallegrazie.it/invia-manoscritto
manoscritti.giunti.it/submit
https://www.ilsaggiatore.com/contatti 
https://www.codiceedizioni.it/contatti/ 
https://tlon.it/contatti.html 
www.chiarelettere.it
https://www.lindau.it/Invio-manoscritti
https://www.adelphi.it/contatti
https://www.elliotedizioni.com/contatti/ 
https://www.bompiani.it/contatti
https://www.cairoeditore.it
https://www.castelvecchieditore.com/manoscritti/
https://www.darioflaccovio.it/content/13-come-inviare-proposte-editoriali
https://www.deagostinilibri.it/contatti/scrivici
https://www.deriveapprodi.com/contatti/
https://www.bietti.it/contatti/
https://www.einaudi.it/contatti/
https://www.edizionifrassinelli.it
https://www.garzanti.it/
https://www.giulioperroneditore.com/contatti/
https://www.guanda.it/contatti
https://www.harpercollins.it/contatti/
https://imprimatureditore.tumblr.com/contatti
https://www.lanavediteseo.eu/manoscritti-e-curriculum/
https://lemezzelane.eu/pubblica_con_noi/
https://www.leoneeditore.it/invia-manoscritto/regole-invio/
https://www.longanesi.it/contattaci/
https://marcosymarcos.com/contatti/
https://www.marsilioeditori.it/faq
https://www.minervaedizioni.com/i-vostri-manoscritti
https://www.mondadori.it/contatti/
www.neripozza.it
www.newtoncompton.com
www.editricenord.it
www.edizioninottetempo.it
www.nutrimenti.net
www.pandaedizioni.it
www.edizpiemme.it
www.rizzoli.eu
www.safaraeditore.com
www.salani.it
www.edizionisanpaolo.it

www.sironieditore.it
www.sonzognoeditori.it
www.sperling.it
www.transeuropaedizioni.it
www.mursia.com
hoeplieditore.it/scrivi-per-noi
pianobedizioni.com/contatti
lacaravellaeditrice.it
erickson.it/pubblica-con-noi
vallardi.it/contatti
fontanaistente.com/proposte-editoriali
egeaendente.it
https://www.elledici.org/contatti

https://www.tecnichenuove.com/contattaci
https://anima.tv/anima-edizioni-2
https://www.utetlibri.it/contatti/
https://www.terranuovalibri.it/form-contattaci.html
https://www.este.it/contatti/
https://www.mulino.it/submission

bollatiboringhieri.it

https://www.gruppomacro.com/lp/come-pubblicare-con-macro
https://mgmtedizioni.com/shop/contatti/
https://www.viella.it/ (sezione "Per gli autori")
https://www.gribaudo.it/contatti/
https://www.slowfoodendente.it/it/c/16-contatti
https://www.astrolabio-ubaldini.com/contatti
https://www.edizioniares.it/
https://www.epc.it/collabora-con-noi
https://www.pickwicklibri.it/ (marchio Mondadori)
https://www.edizionilswr.it/content/proponi-un-libro.html


https://www.guidaeditori.it/pubblicare-con-noi/
https://www.edizionigrenelle.com/manoscritti/


www.carocci.it
www.baldinicastoldi.it


www.fandangoeditore.it
www.fabbrieditori.eu


https://edizionidedalo.it/contatti
https://www.mimesisedizioni.it/chi-siamo/contatti
https://abocaedizioni.it/casa-editrice/
https://www.francoangeli.it/contatti
https://www.edizionialtravista.com/casa-editrice#collane
https://www.giovaneholden.it/manoscritti
eleuthera@eleuthera.it













Libri letti


Sito
www.alteregoedizioni.it
www.arcanaedizioni.com
www.autodafe-edizioni.com
www.66thand2nd.com
www.ciessedizioni.it

www.edizionilagru.com
www.edizioniel.com
www.edizionieo.it

www.fanucci.it
www.fazieditore.it
www.fernandel.it
www.frillieditori.com
www.gaffi.it
www.hacca.it
www.edizionimaestrale.com
www.intermezzieditore.it
www.ilsemebianco.it
www.lasvegasedizioni.com
www.miraggiedizioni.it
www.natividigitaliedizioni.it
www.raccontiedizioni.it
www.passiglieditori.it
www.semlibri.com
www.verbavolantedizioni.it


www.stampalternativa.it
https://www.corbaccio.it/contatti
https://www.feltrinellieditore.it/contatti/
https://www.graphe.it/pubblica-con-noi.html

https://www.marcovalerio.it/scriptorium/pubblicare-con-noi/
https://www.minimumfax.com/contatti
https://www.neoedizioni.it/neo/contatti/"""

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
