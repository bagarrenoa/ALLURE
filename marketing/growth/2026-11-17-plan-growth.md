# Plan growth Allure — réunion de lancement du 17/11/2026

**Auteur** : Malik (Growth) — **Statut** : proposition, rien n'est lancé sans validation du fondateur.
**Sources internes** : `BRIEF.md`, `QUESTIONS.md`.

---

## 0. Ce qu'on sait / ce qu'on ne sait pas

| Donnée | Valeur | Source |
|---|---|---|
| Abonnés Instagram `@allure_officiel_` | 3 227 (6 publications) | BRIEF.md, 17/11/2026 |
| Précommandes reçues à ce jour | ❓ | QUESTIONS.md n°11 |
| Prix de vente de l'ensemble | ❓ | QUESTIONS.md n°10 |
| Précommande « gratuite » = sans paiement ? acompte ? | ❓ | QUESTIONS.md n°11 |
| Budget pub mensuel | ❓ | QUESTIONS.md n°17 |
| Compte TikTok | ❓ | QUESTIONS.md n°16 |
| Compte Instagram pro relié à une page Facebook | ❓ (**obligatoire pour faire de la pub Meta**) | QUESTIONS.md n°22 |
| Date de livraison promise | ❓ | QUESTIONS.md n°14 |
| Code source du site | ❓ | QUESTIONS.md n°13 |

**Préalable non négociable** : tant que le nom « Allure » n'est pas vérifié à l'INPI/EUIPO en classe 25 (risque déjà relevé dans BRIEF §6), on limite la pub à un **test de 1 à 2 semaines**. On ne met pas d'argent dans une notoriété qu'on risque de devoir rebaptiser.

---

## 1. Audit du site de précommande

### 1.1 Accès
`https://allure-precommande.netlify.app` **n'a pas pu être consulté le 17/11/2026** : le domaine n'est pas joignable depuis l'environnement de travail (domaine non autorisé dans les réglages réseau de la session). Pour un audit réel, il faut soit autoriser ce domaine, soit ajouter le code du site dans ce dépôt (QUESTIONS n°13).
→ L'audit ci-dessous est une **grille de contrôle de bonnes pratiques**. Le fondateur (ou moi, une fois l'accès ouvert) coche chaque ligne.

### 1.2 Grille d'audit (à cocher)

| # | Critère | Pourquoi | Ce qu'il faut voir sur le site | Présent ? | Priorité |
|---|---|---|---|---|---|
| 1 | **Vitesse mobile** | 90 % du trafic viendra d'Instagram/TikTok, donc de mobiles | Score PageSpeed Insights mobile, images compressées en WebP, < 1 Mo au-dessus de la ligne de flottaison | ❓ | Haute |
| 2 | **Offre claire en 5 secondes** | Le visiteur venu d'une pub ne sait rien de la marque | Titre type : « L'ensemble de ski Allure — veste + pantalon — précommande ouverte » + photo du produit porté + prix (ou « prix révélé le JJ/MM ») | ❓ | Haute |
| 3 | **Prix affiché** | Sans prix, une précommande ne vaut pas grand-chose comme signal | Prix ou fourchette, avantage précommande (ex. -X % « early ») | ❓ (prix inconnu) | Haute |
| 4 | **Ce que veut dire « précommande gratuite »** | Ambigu : on ne sait pas si on s'engage à quelque chose | Phrase explicite : « Tu réserves ta taille et ton coloris, tu ne paies rien maintenant, on te prévient avant le lancement » (à valider avec Hugo pour le cadre légal) | ❓ | Haute |
| 5 | **Capture e-mail** (champ unique, au-dessus de la ligne de flottaison) | La liste d'attente est l'actif n°1 avant production | Champ e-mail + bouton, coloris + taille en option. Case de consentement marketing non pré-cochée (RGPD) | ❓ | Haute |
| 6 | **Page / message de confirmation** | Moment où l'inscrit est le plus motivé à partager | Message « Tu es le n° X » + bouton de partage + lien de parrainage | ❓ | Haute |
| 7 | **Preuve sociale** | Rassure un inconnu | Compteur d'inscrits, captures de commentaires Instagram, photos de vrais gens portant l'ensemble, nombre d'abonnés | ❓ | Moyenne |
| 8 | **Compteur de précommandes** | Effet de masse + urgence | « 347 ensembles réservés » (n'afficher qu'à partir d'un seuil crédible, ex. 100 — seuil ❓) | ❓ | Moyenne |
| 9 | **Urgence / rareté honnête** | Pousse à agir maintenant | « Première série limitée à N pièces numérotées » — **N doit correspondre à la vraie quantité de production** (QUESTIONS n°9) ; fausse rareté = pratique commerciale trompeuse | ❓ | Moyenne |
| 10 | **Parrainage** | Croissance gratuite | Lien perso « invite 3 amis = avantage » (voir §3.3) | ❓ | Haute |
| 11 | **Visuels** | Le personnage cagoulé est l'atout de la marque | Vidéo courte en haut de page, les 5 coloris, zoom sur détails (zips, poches cargo, étoiles) — **retirer tout logo tiers (planche Bataleon)** | ❓ | Moyenne |
| 12 | **Guide des tailles** | Frein n°1 en mode en ligne | Tableau tailles ❓ (QUESTIONS n°7) | ❓ | Moyenne |
| 13 | **Specs techniques** | Crédibilité ski | Imperméabilité, respirabilité, coutures ❓ (QUESTIONS n°6) — ne rien afficher tant que non confirmé | ❓ | Moyenne |
| 14 | **Mentions légales, CGV, politique de confidentialité** | Obligatoire, et rassure | Liens en pied de page — à faire avec Hugo | ❓ | Haute (légal) |
| 15 | **Suivi des conversions** | Sans ça, impossible de mesurer les pubs | Pixel Meta + API Conversions, pixel TikTok, événement « Lead » sur la confirmation, paramètres UTM | ❓ (probablement absent) | **Bloquant pour la pub** |
| 16 | **Bandeau cookies** | Obligatoire dès qu'on pose des pixels | Bandeau conforme CNIL (refuser aussi simple qu'accepter) | ❓ | Haute (légal) |
| 17 | **Sortie des données** | Aujourd'hui chaque précommande arrive dans Gmail : pas de tableau, pas de relance | Brancher le formulaire sur un outil de liste (Netlify Forms export, ou outil d'e-mailing) — à cadrer avec Clara, données clients restent dans `ops/` | ❓ | Haute |
| 18 | **Domaine** | `*.netlify.app` fait « site de test », baisse la confiance | Nom de domaine propre (coût ❓, à valider avec Hugo après vérif. de marque) | Non | Moyenne |

### 1.3 Les 5 actions à faire en premier (avant toute pub)
1. **Pixel Meta + pixel TikTok + événement « Lead »** sur la page de confirmation. Qui : dev du site (❓ qui a fait le site ?). Coût : 0 €.
2. **Réécrire le haut de page** : titre + photo/vidéo + phrase claire sur « précommande gratuite » + champ e-mail. Qui : Inès (message) + Zoé (visuel). Coût : 0 €.
3. **Page de confirmation avec rang + lien de parrainage** (voir §3.2–3.3). Qui : dev. Coût : 0 € à ❓ selon outil.
4. **Mentions légales / confidentialité / cookies**. Qui : Hugo. Coût : 0 € (modèles CNIL).
5. **Compteur de réservations** une fois le seuil atteint. Qui : dev. Coût : 0 €.

---

## 2. Plan pub de test Meta (Instagram) + TikTok

### 2.1 Prérequis
- Compte Instagram **professionnel** relié à une **page Facebook** + compte Meta Business (❓ QUESTIONS n°22).
- Compte TikTok + TikTok Ads Manager (❓ QUESTIONS n°16).
- Pixels installés (§1.3 action 1). **Sans pixel, on ne lance pas** : on paierait des clics sans savoir qui s'inscrit.
- Objectif de campagne : **prospects / conversions sur l'événement « Lead »** (inscription liste d'attente). Pas d'objectif « J'aime » ou « abonnés ».

### 2.2 Budget minimum testable

| Phase | Plateforme | Budget | Durée | Total | Condition pour passer à la suite |
|---|---|---|---|---|---|
| **Test 1** | Meta (Instagram uniquement, Reels + Stories) | **10 €/jour** | 7 jours | **70 €** | Coût par inscrit ≤ cible (§2.5) et au moins une créa qui sort du lot |
| **Test 1** | TikTok | **20 €/jour** (TikTok impose un budget minimum par groupe d'annonces — montant exact à vérifier dans l'Ads Manager au lancement ❓) | 7 jours | **~140 €** | Idem |
| **Total test** | | | | **~210 €** | Validation du fondateur |
| Phase 2 (si test OK) | Plateforme gagnante seulement | 20–30 €/jour | 14 jours | 280–420 € | Coût par inscrit stable ou en baisse |
| Phase 3 (si phase 2 OK) | Gagnante + reciblage | à définir selon budget ❓ (QUESTIONS n°17) | | | |

Si le fondateur n'a que ~100 € : **Meta seul, 10 €/jour × 7 jours**. Instagram est déjà le canal où la marque existe.

### 2.3 Audiences (France, ❓ autres pays selon QUESTIONS n°19)

| Audience | Plateforme | Ciblage | Rôle |
|---|---|---|---|
| A — Large | Meta + TikTok | 18–30 ans, France, aucun intérêt (laisser l'algorithme trouver) | Référence ; souvent la moins chère sur les comptes récents |
| B — Intérêts glisse | Meta | 18–30 ans, intérêts snowboard, ski freestyle, stations (ex. sports d'hiver) | Tester le cœur de cible |
| C — Intérêts streetwear | Meta | 18–30 ans, intérêts streetwear, gorpcore, sneakers | Tester le positionnement « se porte en ville » |
| D — Reciblage (phase 2) | Meta + TikTok | Personnes ayant interagi avec `@allure_officiel_` ou vu 50 % d'une vidéo, visiteurs du site non inscrits | Conversion la moins chère, seulement quand il y a du volume |
| E — Similaires (phase 3) | Meta | Audience similaire aux inscrits (nécessite un volume d'inscrits ❓ ; **fichier client uploadé = donnée personnelle → validation fondateur + Hugo obligatoire**) | Passage à l'échelle |

Test 1 Meta : A et B seulement (5 €/jour chacune). Pas plus de 2 audiences avec 70 €, sinon aucune n'apprend.

### 2.4 Créas à tester (brief pour Sam / Mila / Zoé)
Format : vidéo verticale 9:16, 7–15 s, sous-titrée, accroche dans la 1re seconde, **visage caché (cagoule + masque)**, aucune marque tierce.

| # | Nom | Accroche (1re seconde) | Contenu | Hypothèse testée |
|---|---|---|---|---|
| 1 | **« Le personnage »** | Plan serré sur la cagoule + masque, texte : « Personne ne sait qui on est. » | 3 potes cagoulés en télécabine puis en ville, révélation du logo dans le dos | L'anonymat intrigue et arrête le scroll |
| 2 | **« 5 coloris, 1 seul choix »** | Écran split des 5 coloris, texte : « Lequel tu prends ? » | Défilé rapide Sauge / Rose / Marine / Orange / Noir, CTA « Réserve ton coloris » | L'interaction (commentaires) fait baisser le CPM |
| 3 | **« Détails »** | Zip fluo qui s'ouvre en gros plan, son ASMR | Poches cargo modulaires, étoiles sur la capuche, zips de ventilation | La cible ski veut du technique |
| 4 | **« Piste → béton »** | Même personne en descente puis dans un parking à Madrid, coupe sur le beat | Transition montagne/ville | Le positionnement streetwear élargit la cible |
| 5 | **« Numéro de série »** (seulement si quantité limitée confirmée) | Étiquette « N° 001/❓ » | « Première série limitée, réserve gratuitement ton numéro » | L'urgence/rareté fait convertir |

Test 1 : créas 1, 2, 4 sur Meta ; 1, 2, 3 sur TikTok (format plus « brut »). On coupe une créa après ~3 jours si son coût par inscrit est > 2× la meilleure.

### 2.5 KPI cibles (repères marché + cibles Allure)

**Repères publiés (moyennes tous pays, majoritairement US, en dollars ; à lire comme ordres de grandeur, les méthodes diffèrent selon les sources) :**

| Indicateur | Repère | Source |
|---|---|---|
| CPM Meta moyen 2025 | ~14,19 $ | [Influee — Facebook Ads Benchmarks](https://influee.co/blog/facebook-ads-benchmarks) |
| CPM Meta, 12 derniers mois | ~15,06 $ | [Triple Whale — Facebook Ads Benchmarks](https://www.triplewhale.com/blog/facebook-ads-benchmarks) |
| CPC Meta secteur habillement | ~0,45 $ (CTR ~1,24 %) | [Bestever — Facebook Ads Benchmarks 2025](https://www.bestever.ai/post/facebook-ads-benchmarks), [ContentStudio](https://contentstudio.io/blog/meta-ads-benchmarks) |
| CPC Meta mode/bijoux (autre méthode) | ~0,86 $ (CTR ~1,29 %) | [LocaliQ](https://localiq.com/blog/facebook-advertising-benchmarks/) |
| CPM TikTok moyen 2025 | ~13,26 $ | [Influee — TikTok Ads Benchmarks](https://influee.co/blog/tiktok-ads-benchmarks) |
| CPM / CPC TikTok (fourchettes) | CPM 4,20–9 $ ; CPC 0,17–1 $ | [Influee FR — Coût des TikTok Ads](https://influee.co/fr/blog/tiktok-ads-cost) |
| Taux de conversion médian d'une landing page e-commerce | 4,2 % (top 25 % : ≥ 11,4 %) | [Unbounce — benchmarks de conversion](https://unbounce.com/conversion-benchmark-report-2021/) |

Pas de repère France spécifique trouvé pour TikTok : on mesurera nos propres chiffres pendant le test.

**Cibles Allure pour le test 1 (hypothèses de travail, à recalculer après 7 jours) :**

| KPI | Cible | Calcul / justification |
|---|---|---|
| CPM | ≤ 15 € | Aligné sur les moyennes ci-dessus |
| CTR (lien) | ≥ 1 % | Moyennes habillement ~1,2–1,3 % |
| CPC | ≤ 0,80 € | Entre les deux repères habillement |
| Taux visite → inscription | ≥ 10 % | Une inscription gratuite à liste d'attente est plus facile qu'un achat ; médiane e-commerce 4,2 %, top 25 % 11,4 % |
| **Coût par inscrit** | **≤ 8 €** (0,80 € / 10 %) | Si on atteint 4 € → on accélère ; si > 15 € → on revoit site ou créas avant de remettre de l'argent |
| **Coût par précommande** | ❓ | Dépend de ce qu'est une précommande (gratuite vs acompte) et du prix (QUESTIONS n°10–11). Cible à fixer avec Hugo : ne doit pas dépasser une fraction de la marge unitaire ❓ |
| Taux inscrit → parrain actif | ≥ 10 % | Hypothèse interne à mesurer |

Avec 210 € et un coût par inscrit de 8 €, on obtient **~26 inscrits** : c'est un test pour **apprendre quelle créa et quelle plateforme marchent**, pas pour remplir la liste. Le volume viendra des mécaniques virales (§3) et de l'influence (Lou).

---

## 3. Trois mécaniques virales

### 3.1 Concours « Gagne ton ensemble Allure »
- **Mécanique** : 1 ensemble (coloris au choix) à gagner. Pour participer : s'abonner à `@allure_officiel_`, commenter avec son coloris préféré + identifier 2 amis. **Bonus** : participation supplémentaire si inscrit sur la liste d'attente (lien en bio).
- **Durée** : 7 jours, tirage au sort en live/story.
- **Quand** : seulement quand on a une **date de livraison crédible** (QUESTIONS n°14) — on ne fait pas gagner un produit qui n'existe pas encore sans dire quand il arrive.
- **Cadre légal** : depuis 2014 le dépôt du règlement chez un huissier n'est plus obligatoire, mais un **règlement écrit reste recommandé**, et le jeu ne doit pas être une pratique commerciale déloyale ([Blog du Modérateur](https://www.blogdumoderateur.com/jeux-concours-reseaux-sociaux-regles/), [donneespersonnelles.fr](https://donneespersonnelles.fr/jeu-concours-rgpd)). Mention obligatoire que Meta n'est pas partenaire. **Hugo rédige le règlement** et vérifie le texte en vigueur sur Légifrance.
- **Coût** : 1 ensemble (coût de revient ❓) + envoi ❓. Option : 30–50 € de boost sur le post (10 €/jour × 3–5 jours).
- **KPI** : nouveaux abonnés, nouveaux inscrits pendant la semaine, coût par inscrit du concours.
- **Qui** : Malik (mécanique), Zoé (visuel), Hugo (règlement), fondateur (valide et publie).

### 3.2 Liste d'attente avec rang
- **Mécanique** : à l'inscription, l'utilisateur voit « Tu es le n° 412 sur la liste ». Chaque ami inscrit via son lien le fait **remonter de 10 places** (valeur à ajuster). Les **100 premiers** (❓ selon quantité de production) accèdent à la précommande 48 h avant tout le monde et choisissent leur numéro de série.
- **Pourquoi** : le rang crée une raison de partager même sans remise, donc sans coût sur la marge.
- **Outil** : soit développement sur le site Netlify (dev ❓), soit outil de liste d'attente avec parrainage intégré (tarif ❓ à comparer avant de choisir ; attention : les e-mails clients sortent alors vers un service externe → **validation fondateur + Hugo (RGPD) obligatoire**, conformément à la règle 6 du QG).
- **E-mail de relance** : J+3 « Tu es passé n° X, il te manque 2 amis pour entrer dans le top 100 ». Aucun e-mail n'est envoyé sans validation du fondateur.
- **KPI** : % d'inscrits qui partagent, nombre moyen d'amis invités par inscrit (coefficient viral = inscrits venus d'un parrainage / inscrits totaux).

### 3.3 Parrainage « Invite 3 amis = remise »
- **Mécanique** : 3 amis inscrits via ton lien → **remise de ❓ %** sur ton ensemble au lancement (ou accessoire offert, ex. tour de cou/cagoule Allure, coût ❓). Chaque ami parrainé reçoit aussi une petite remise (❓ %) → les deux côtés gagnent.
- **Paliers** (exemple, à chiffrer avec Hugo selon la marge) :
  - 3 amis → remise ❓ %
  - 10 amis → cagoule Allure offerte (coût ❓)
  - 25 amis → ensemble offert (1 seul gagnant / tirage parmi ceux qui atteignent le palier)
- **Garde-fou** : une remise ne compte que si l'ami valide son e-mail (anti-faux comptes) et, si possible, ne se déclenche qu'au moment d'une précommande payée ❓.
- **Lien avec 3.2** : même lien perso, deux récompenses (rang + remise). Une seule mécanique à expliquer : « Partage ton lien ».
- **KPI** : nombre de parrains actifs, inscrits par parrain, coût de la remise par inscrit obtenu (à comparer au coût par inscrit payé en pub).

### Bonus : drop à date fixe
Annoncer **une date d'ouverture des précommandes payantes** (❓, dépend de l'usine portugaise) avec compte à rebours en story et sur le site. La liste d'attente reçoit l'accès en premier. À caler avec Inès dans le calendrier de lancement.

---

## 4. Tableau de bord hebdomadaire

À remplir chaque lundi (semaine précédente). Qui : Malik prépare, Clara fournit les chiffres de précommandes (données nominatives restent dans `ops/`, ici uniquement des totaux).

| Semaine | Abonnés IG (total) | Δ abonnés | Portée IG (comptes touchés) | Abonnés TikTok | Vues TikTok | Visites site | Inscrits liste (total) | Δ inscrits | dont via parrainage | Précommandes (total) | Δ précommandes | Conv. visite → inscrit | Conv. inscrit → précommande | Dépense pub | Coût par inscrit | Coût par précommande | Meilleure créa |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S47 (17/11) | 3 227 | — | ❓ | ❓ | ❓ | ❓ | ❓ | — | 0 | ❓ | — | ❓ | ❓ | 0 € | — | — | — |
| S48 | | | | | | | | | | | | | | | | | |
| S49 | | | | | | | | | | | | | | | | | |

**Où trouver chaque chiffre**
- Abonnés, portée : statistiques Instagram (nécessite un compte pro ❓).
- Visites site : Netlify Analytics (option payante ❓) ou outil d'analyse gratuit respectueux RGPD ❓.
- Inscrits / précommandes : export du formulaire ou décompte Gmail par Clara.
- Dépense, CPM, CPC : Meta Ads Manager / TikTok Ads Manager.

**Règles de décision hebdo**
- Coût par inscrit ≤ cible 2 semaines de suite → proposer au fondateur +20 à 30 % de budget (jamais plus d'un coup, sinon l'algorithme repart en apprentissage).
- Coût par inscrit > 2× la cible → couper la pub, corriger le site ou les créas.
- Taux visite → inscrit < 5 % → le problème est le site, pas la pub.
- Part des inscrits via parrainage < 10 % → retravailler la page de confirmation et la récompense.

---

## 5. Calendrier proposé

| Quand | Quoi | Qui | Coût |
|---|---|---|---|
| Semaine du 17/11 | Réponses QUESTIONS n°10, 11, 13, 16, 17, 22 | Fondateur | 0 € |
| Semaine du 17/11 | Accès au site (code dans le dépôt ou domaine autorisé) → audit réel | Fondateur + Malik | 0 € |
| Semaine du 24/11 | Corrections site §1.3 (pixels, haut de page, confirmation, légal) | Dev ❓, Inès, Hugo | 0 € à ❓ |
| Semaine du 24/11 | Tournage des créas 1 à 4 | Sam, Mila | ❓ |
| Semaine du 01/12 | Liste d'attente avec rang + parrainage en ligne | Dev ❓, Malik | ❓ |
| Semaine du 01/12 | **Test pub 7 jours (~210 €, ou 70 € Meta seul)** — après validation fondateur | Malik | 70–210 € |
| Semaine du 08/12 | Bilan test → décision phase 2 | Malik → fondateur | — |
| Quand date de livraison connue | Concours « Gagne ton ensemble » | Malik, Zoé, Hugo | 1 ensemble + ❓ |

---

## 6. Questions à ajouter pour le fondateur
- Qui a construit le site Netlify et qui peut le modifier ?
- Quantité de la 1re série (pour afficher une rareté honnête, ex. « 300 pièces numérotées ») ?
- Quelle remise / quel cadeau es-tu prêt à donner pour le parrainage ?
- Accepterais-tu un outil externe de liste d'attente (les e-mails des inscrits y seraient stockés) ou préfères-tu tout garder sur le site ?
- Autoriser l'accès au domaine `allure-precommande.netlify.app` dans les réglages réseau de la session Claude pour l'audit réel.

## Sources
- [Influee — Facebook Ads Benchmarks 2026](https://influee.co/blog/facebook-ads-benchmarks)
- [Triple Whale — Facebook Ads Benchmarks](https://www.triplewhale.com/blog/facebook-ads-benchmarks)
- [Bestever — Facebook Ads Benchmarks 2025](https://www.bestever.ai/post/facebook-ads-benchmarks)
- [ContentStudio — Meta Ads Benchmarks](https://contentstudio.io/blog/meta-ads-benchmarks)
- [LocaliQ — Facebook Advertising Benchmarks](https://localiq.com/blog/facebook-advertising-benchmarks/)
- [Influee — TikTok Ads Benchmarks](https://influee.co/blog/tiktok-ads-benchmarks)
- [Influee FR — Coût des TikTok Ads](https://influee.co/fr/blog/tiktok-ads-cost)
- [Unbounce — Conversion Benchmark Report](https://unbounce.com/conversion-benchmark-report-2021/)
- [Blog du Modérateur — Jeux concours sur les réseaux sociaux](https://www.blogdumoderateur.com/jeux-concours-reseaux-sociaux-regles/)
- [donneespersonnelles.fr — Jeu-concours et RGPD](https://donneespersonnelles.fr/jeu-concours-rgpd)
