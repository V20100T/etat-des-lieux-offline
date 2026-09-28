# CLAUDE.md — site vitrine « État des lieux Offline »

Site Hugo (extended **0.121.1**, fixé dans le workflow) pour vendre l'app d'états des lieux (dépôt séparé : `../Etats des lieux`, PWA Preact).
Tout le contenu est **en français**.

## Principes
- **Aucun cookie, aucun traceur, aucune ressource externe au chargement** : pas de Google Fonts, pas d'analytics. La vidéo YouTube (nocookie) n'est chargée qu'au clic, et `lemon.js` seulement si un lien de paiement est renseigné. C'est un argument de vente : ne pas le casser.
- CSS maison dans `assets/css/main.css`, avec variables CSS et thème sombre automatique. Pas de framework.
- Les textes modifiables sont dans `data/*.yaml` (atouts, tarifs, FAQ) et dans `hugo.toml` `[params]` (paiement, e-mail, vidéo, démo).
- Syntaxe compatible avec Hugo 0.121 : `paginate = 9`, et non `[pagination]`.

## Positionnement et messages
- Cibles : petites agences immobilières, bailleurs particuliers, loueurs Airbnb, petites conciergeries.
- Points forts : hors-ligne, données sur le téléphone (pas de compte ni de cloud), payé une fois, comparaison entrée/sortie automatique.
- Prix : Particulier 5 €/an, Particulier à vie 50 € (avec `**` : tant que GitHub Pages fournit l'hébergement gratuit ; l'app installée continue de marcher), Pro 5 €/mois.
- Signature : présentée honnêtement comme une **signature électronique simple, non certifiée**, dans une démarche de bonne foi, renforcée par l'accusé de réception « Bien reçu, OK » des deux parties. Rappeler le délai légal de 10 jours pour compléter l'EDL d'entrée (art. 3-2, loi 89-462). Ne jamais surpromettre sur la valeur juridique.
- Le comparatif avec les « applications classiques » reste prudent et vérifiable (publicité comparative) : ne pas citer de concurrents ni affirmer de faits invérifiables.
- Livraison : instance de l'app personnalisée, déployée à la main par le vendeur, lien envoyé sous 24 h ouvrées.

## À faire côté app (promis sur le site)
- Bouton « Envoyer aux deux parties » : e-mail prérempli avec le PDF, la consigne « répondre Bien reçu, OK » et le rappel du délai de 10 jours.
- Personnalisation de marque (nom et logo) par instance.

## Commandes
- `hugo server` puis ouvrir http://localhost:1313/etat-des-lieux-offline/ · `hugo --gc --minify`
- Déploiement : push sur `main` (workflow `.github/workflows/hugo.yml`, GitHub Pages).
