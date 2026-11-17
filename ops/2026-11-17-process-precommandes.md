# Process précommandes Allure — du mail reçu au colis livré

**Auteur** : Clara (ops) — **Date** : 17/11/2026 — **Statut** : proposition, à valider par le fondateur
**État actuel** : `ops/precommandes.csv` est **vide** (en-tête seul). Aucun e-mail de précommande reçu côté ops, aucun accès Gmail. Tout ce qui suit est prêt à tourner dès réception des premiers e-mails.

---

## 0. Ce qu'il me faut pour démarrer (bloquant)
| # | Quoi | Qui | Quand |
|---|---|---|---|
| 1 | 2-3 e-mails de précommande **transférés tels quels** (pour connaître les champs exacts envoyés par le formulaire Netlify) — Q12 | Fondateur | Cette semaine |
| 2 | Choix : transfert manuel des e-mails OU connecteur Gmail (Q21) | Fondateur | Cette semaine |
| 3 | Définition de « précommande gratuite » (§7) — Q11 | Fondateur | Avant toute communication de date ou de prix |
| 4 | Grille de tailles (Q7) et liste définitive des coloris | Fondateur + Rui | Avant la 1re synthèse usine |
| 5 | Accès au code du site (Q13) pour vérifier que le formulaire capte bien coloris/taille/quantité/pays | Fondateur | Dès que possible |

---

## 1. Le flux en 6 étapes

```
Client remplit le formulaire (allure-precommande.netlify.app)
   -> Netlify envoie un e-mail sur le Gmail du fondateur
   -> Filtre Gmail : libellé "Allure/Précommandes/À saisir"
   -> Fondateur transfère (ou Clara lit via connecteur) -> Clara saisit une ligne dans ops/precommandes.csv
   -> Contrôle doublons/incohérences -> brouillon d'e-mail de confirmation (envoyé PAR LE FONDATEUR)
   -> Libellé passe à "Allure/Précommandes/Saisie"
```

| Étape | Qui | Délai cible |
|---|---|---|
| 1. Réception + libellé automatique | Gmail (filtre) | Instantané |
| 2. Transfert à Clara (si pas de connecteur) : 1 fois par jour, en lot | Fondateur | J+1 |
| 3. Saisie dans le CSV + contrôle | Clara | J+1 |
| 4. Brouillon de confirmation (modèle §5.1) | Clara | J+1 |
| 5. Relecture + envoi de la confirmation | Fondateur | J+2 max |
| 6. Synthèse hebdo coloris × taille (§4) | Clara | Chaque lundi |

**Règle** : Clara n'envoie jamais d'e-mail elle-même (règle 4 du QG). Elle prépare, le fondateur envoie.

---

## 2. Gmail : libellés et filtre à créer (par le fondateur, 5 min)

### Libellés (Gmail → Paramètres → Libellés → Créer)
- `Allure/Précommandes/À saisir`
- `Allure/Précommandes/Saisie`
- `Allure/Précommandes/Problème` (doublon, info manquante, demande d'annulation)
- `Allure/SAV` (questions clients, réponses aux e-mails)

### Filtre (Gmail → barre de recherche → icône « options » → Créer un filtre)
- **De** : `formresponses@netlify.com` *(adresse d'expédition habituelle des notifications de formulaire Netlify — ❓ à confirmer sur un vrai e-mail)*
- **Objet contient** : le nom du formulaire tel qu'il apparaît dans l'objet ❓ (à lire sur un vrai e-mail)
- Actions : cocher « Appliquer le libellé » → `Allure/Précommandes/À saisir`, « Ne jamais envoyer dans le spam », « Toujours marquer comme important ».
- Cocher « Appliquer aussi aux conversations correspondantes » pour reclasser les e-mails déjà reçus.

Astuce : tant que le filtre n'est pas sûr, rechercher `from:netlify` dans Gmail pour retrouver toutes les précommandes déjà arrivées.

---

## 3. Le tableau `ops/precommandes.csv`

### Colonnes (existantes) + règles de saisie
| Colonne | Format | Règle |
|---|---|---|
| `date` | `AAAA-MM-JJ` | Date de réception de l'e-mail Netlify (pas la date de saisie) |
| `prenom` | texte | Tel que saisi par le client |
| `email` | minuscules, sans espaces | Clé de détection des doublons |
| `coloris` | `sauge` / `rose` / `marine` / `orange` / `noir` | Liste fermée (BRIEF §2). Autre valeur → statut `a_verifier` |
| `taille` | ❓ grille à fixer (ex. XS–XXL) | Liste fermée dès que la grille est validée (Q7) |
| `quantite` | entier ≥ 1 | > 3 → signaler (revendeur ? erreur ?) |
| `pays` | code ISO 2 lettres (`FR`, `BE`, `CH`, `ES`…) | Sert au calcul transport + douane (CH/UK hors UE) |
| `statut` | voir ci-dessous | Une seule valeur |
| `source` | `site` / `instagram_dm` / `email` / `salon` / `autre` | D'où vient la précommande |

### Colonnes à ajouter (proposition, à valider)
| Colonne | Pourquoi |
|---|---|
| `id` | `PC-0001`, `PC-0002`… — référence unique à citer dans les e-mails et le SAV |
| `produit` | `ensemble` / `veste` / `pantalon` si la vente séparée est retenue (Q10) |
| `paiement` | `aucun` / `acompte` / `paye` + montant — indispensable si on sort du « gratuit » (§7) |
| `date_confirmation` | Date d'envoi de l'e-mail de confirmation |
| `notes` | Doublon, demande spéciale, changement de taille… |

**Données personnelles** : pas d'adresse postale tant qu'on n'expédie pas. Les adresses seront collectées au moment de l'expédition, dans `ops/` uniquement. Le CSV ne doit jamais être envoyé à un outil externe (Sendcloud compris) sans validation : l'import transporteur se fera au moment de l'expédition, et seulement avec les colonnes nécessaires.

### Statuts (cycle de vie)
| Statut | Signification | Passe au suivant quand… |
|---|---|---|
| `a_verifier` | Info manquante/incohérente ou doublon possible | Le fondateur/client a clarifié |
| `recue` | Saisie, valide, confirmation pas encore envoyée | Fondateur envoie la confirmation |
| `confirmee` | Client a reçu la confirmation | Client a payé (si paiement mis en place) |
| `payee` | Paiement ou acompte encaissé | Lot en production |
| `en_production` | Comptée dans une commande usine | Colis préparé |
| `expediee` | Numéro de suivi envoyé | Livraison confirmée |
| `livree` | Reçue par le client | (fin, ou `retour`) |
| `annulee` | Annulée par le client ou nous | — |
| `retour` | Retour/échange en cours | — |

### Contrôles à chaque saisie (je les signale dans `notes` + libellé Gmail `Problème`)
1. **Doublon** : même e-mail déjà présent. Même coloris + taille → probable double clic → garder une seule ligne, statut `a_verifier`. Coloris/taille différents → peut être une 2e commande légitime → demander au client.
2. **E-mail invalide** (pas de `@`, domaine tapé de travers type `gmial.com`) → `a_verifier`.
3. **Coloris ou taille hors liste** → `a_verifier`.
4. **Quantité anormale** (0, vide, > 3) → `a_verifier`.
5. **Pays hors zone de livraison** (à définir) → `a_verifier`.
6. **Prénom/e-mail fantaisistes** (« test », « aaa », adresse jetable) → `a_verifier`, exclu des quantités.

---

## 4. Calcul des quantités à commander à l'usine

### Méthode (synthèse chaque lundi : `ops/AAAA-MM-JJ-synthese-precommandes.md`)
1. **Base** = somme des `quantite` des lignes en statut `confirmee`, `payee` (et `recue` en option, à part). On **exclut** `a_verifier`, `annulee`.
2. **Tableau croisé coloris × taille** de la base.
3. **Taux de conversion attendu** (clé avec des précommandes gratuites) :
   `Commandes réelles attendues = précommandes gratuites × taux de conversion + précommandes payées × ~100 %`
   Le taux de conversion d'une précommande sans paiement est **inconnu** ❓ : pas de chiffre inventé. On le mesurera sur la première vague (e-mail « passez au paiement » → nombre de payeurs / nombre de précommandes).
4. **Marge de sécurité par cellule** : `+ X %` arrondi à l'unité supérieure, avec **au moins +1 pièce** dans les tailles centrales. X est à fixer par le fondateur ❓ (proposition de départ à discuter : 10 % sur les précommandes payées, couvre défauts usine, échanges de taille, ventes après lancement).
5. **Contrainte usine** : remonter chaque coloris au **minimum de commande (MOQ)** par coloris et par taille imposé par l'usine portugaise ❓ (Rui). Si un coloris n'atteint pas le MOQ : soit on le supprime de la 1re série (et on prévient les clients concernés avec un autre coloris), soit on paye le surplus — décision fondateur.
6. **Échantillons/influence** : ajouter les tenues prévues pour influenceurs/shootings (Q18, Lou) sur une ligne séparée.

### Formule par cellule
```
Qté_usine(coloris, taille) = max( MOQ_taille ,  arrondi_sup( payées + gratuites × taux_conv ) × (1 + marge) + influence )
```

### Gabarit de synthèse (vide aujourd'hui : 0 précommande dans le tableau)
| Coloris \ Taille | ❓ | ❓ | ❓ | ❓ | ❓ | Total |
|---|---|---|---|---|---|---|
| Sauge | | | | | | |
| Rose | | | | | | |
| Marine | | | | | | |
| Orange | | | | | | |
| Noir | | | | | | |
| **Total précommandes** | | | | | | **0** |
| + marge X % | | | | | | |
| + influence | | | | | | |
| **À commander (après MOQ)** | | | | | | |

---

## 5. Modèles d'e-mails clients
Variables entre `{ }`. Ton : tutoiement, direct, à l'image de la marque (à valider par Inès). Envoi **par le fondateur** uniquement. Mention légale de bas de page (raison sociale, désinscription) ❓ à fournir par Hugo une fois la structure créée.

### 5.1 Confirmation de précommande
> **Objet** : Ta précommande Allure {id} est bien enregistrée
>
> Salut {prenom},
>
> Ta précommande est bien notée :
> - Ensemble Allure — coloris **{coloris}**, taille **{taille}**, quantité **{quantite}**
> - Référence : **{id}**
>
> Ce qui se passe maintenant : on finalise la production au Portugal. Tu recevras des nouvelles à chaque étape importante (prototype validé, lancement de la production, expédition).
> {SI GRATUITE : « Tu n'as rien payé à ce stade. Avant la production, on t'enverra un lien pour confirmer et régler ta commande ; sans confirmation de ta part, ta place sera libérée. »}
> {SI ACOMPTE : « Nous avons bien reçu ton acompte de {montant} €. Le solde de {solde} € te sera demandé avant l'expédition. »}
>
> Une erreur de taille ou de coloris ? Réponds simplement à ce mail.
>
> À très vite sur les pistes (ou dans la rue),
> {prénom du fondateur} — Allure

### 5.2 Nouvelles de la production
> **Objet** : Allure — des nouvelles de ton ensemble {coloris}
>
> Salut {prenom},
>
> Petit point d'avancement sur ta précommande {id} :
> - ✔ {étape franchie, ex. « Usine choisie au Portugal »}
> - ✔ {étape, ex. « Prototype validé »}
> - ⏳ {étape en cours, ex. « Production lancée, fin prévue {date} »}
>
> {1 photo des coulisses : atelier, tissu, prototype — Studio}
>
> Ta taille reste {taille} ; si tu veux changer, c'est **jusqu'au {date_limite_modif}**.
>
> {prénom du fondateur} — Allure

### 5.3 Date de livraison / expédition
> **Objet** : Ton ensemble Allure part cette semaine 📦 *(retirer l'emoji si la charte l'exclut)*
>
> Salut {prenom},
>
> Ton ensemble **{coloris} — {taille}** (réf. {id}) {est expédié / sera expédié le {date}}.
> - Transporteur : {transporteur}
> - Suivi : {lien_suivi}
> - Livraison estimée : {date_livraison}
> - {Point relais : {adresse_point_relais}}
>
> Un souci de taille à la réception ? Tu as {délai_retour ❓} jours pour l'échanger : réponds à ce mail.
>
> {prénom du fondateur} — Allure

### 5.4 Retard
> **Objet** : Allure — ta commande {id} prend un peu de retard
>
> Salut {prenom},
>
> On préfère te le dire franchement : ta commande aura du retard.
> - **Pourquoi** : {raison concrète, ex. « le tissu ripstop est arrivé à l'usine avec 2 semaines de retard »}
> - **Nouvelle date estimée** : {nouvelle_date}
> - **Ce qu'on fait pour toi** : {geste, ex. « code -10 % sur ta prochaine commande » — à valider par le fondateur/Hugo}
>
> Si ce délai ne te convient plus, tu peux annuler {et être remboursé intégralement sous 14 jours} : réponds simplement « annuler » à ce mail.
>
> Désolé pour l'attente,
> {prénom du fondateur} — Allure

### 5.5 Demande d'avis (J+10 après livraison)
> **Objet** : Alors, cet ensemble Allure ?
>
> Salut {prenom},
>
> Ça fait une dizaine de jours que tu as ton ensemble {coloris}. On veut ton avis honnête :
> 1. La taille {taille} te va comment ? (petit / juste / grand)
> 2. Testé sur la neige ? Imperméabilité, chaleur, liberté de mouvement ?
> 3. Une note sur 5 ?
>
> Et si tu le portes sur une photo ou une vidéo, tague **@allure_officiel_** : on repartage (visage caché ou pas, comme tu veux).
>
> {prénom du fondateur} — Allure

---

## 6. Logistique d'expédition France / Europe

### Données manquantes avant de chiffrer précisément
- **Poids de l'ensemble emballé** (veste + pantalon + sachet + carton/pochette) ❓ — à peser sur le prochain prototype (Rui). Le tarif dépend de la tranche de poids (1 kg, 2 kg, 3 kg…).
- **Lieu d'expédition** : depuis la France (chez le fondateur) ou directement depuis le Portugal (usine/logisticien) ❓ — change tous les tarifs.
- **Volume** : nombre de colis à expédier au lancement ❓ (= nombre de précommandes confirmées).

### Options transporteurs (tarifs publics particuliers 2026, **à revérifier** au moment de l'achat)
| Option | France | Europe (UE) | Points forts | Limites | Source |
|---|---|---|---|---|---|
| **Colissimo domicile** (La Poste) | 9,59 € (1 kg) / 11,19 € (2 kg) | 19,39 € (1 kg) / 22,19 € (2 kg), zone UE/CH/UK | Fiable, suivi, dépôt partout | Cher, surtout à l'export | [laposte.fr – tarifs Colissimo en ligne](https://www.laposte.fr/colissimo-en-ligne/tarifs), [laposte.fr – tarifs colis](https://www.laposte.fr/tarifs-postaux-colis) |
| **Colissimo point retrait** | ≈ 8,89 € (1 kg) / 10,49 € (2 kg) | — | ~0,70 € moins cher que domicile | — | idem |
| **Mondial Relay point relais/locker** | ≈ 5,99 € (1 kg, particulier, juin 2026) | dès ≈ 4,60 € BE/LU (offre promo), ≈ 6,60 € ES (500 g) | Le moins cher en France, très utilisé par la cible 18-30 ans | Client doit aller en point relais ; surcharge possible 3 € HT dans certains cas (CGV offre Start) | [margeoapp – grille Mondial Relay 2026](https://margeoapp.com/blog/tarifs-mondial-relay-2026), [ShippyPro – tarifs 2026 France](https://www.shippypro.com/blog/fr/envoyer-un-colis-prix-et-tarifs-2026-des-transporteurs-en-france), [CGV Mondial Relay offre Start 2026 (PDF)](https://www.mondialrelay.fr/media/126253/20260107-france-offre-start-conditions-generales-de-vente-fr-2.pdf) |
| **Sendcloud** (plateforme multi-transporteurs) | Tarifs transporteurs facturés en plus | idem | Étiquettes en lot, suivi automatique, page de retours, comparaison des transporteurs | Abonnement : plan Free, puis Lite ≈ 35 €/mois (chiffres d'agrégateurs, contradictoires) | [PricingSaaS – Sendcloud](https://pricingsaas.com/companies/sendcloud), [Capterra – Sendcloud](https://www.capterra.com/p/189663/SendCloud/pricing/), [Toolradar](https://toolradar.com/tools/sendcloud/pricing) |
| **Compte pro Colissimo / Mondial Relay** | Grille négociée dégressive | idem | Moins cher dès quelques dizaines de colis/mois | Ouverture de compte = engagement → validation fondateur ; nécessite une structure (Q1) | [artisansdeuxpointzero – Mondial Relay pro](https://artisansdeuxpointzero.fr/mondial-relay-tarif-pro-artisan) |

**Fiabilité des chiffres** : les tarifs Colissimo France sont cohérents entre plusieurs sources ; les tarifs Mondial Relay et Sendcloud viennent de sites tiers et divergent. La page officielle laposte.fr n'a pas pu être consultée depuis cette session (domaine non autorisé dans les réglages réseau de la session) → **à vérifier sur laposte.fr, mondialrelay.fr et sendcloud.com/pricing avant décision**.

### Recommandation de départ (à valider)
1. **France** : Mondial Relay point relais par défaut (moins cher), Colissimo domicile en option payante pour le client.
2. **Europe** : Mondial Relay pour BE/LU/ES/PT/NL… ; Colissimo pour les pays non couverts.
3. **Suisse / Royaume-Uni** : hors UE → droits de douane et déclaration CN23 ; à éviter au lancement ou à faire chiffrer par Hugo.
4. **Outil** : Sendcloud plan gratuit à tester **uniquement au moment des expéditions**, avec export limité aux colonnes nécessaires (nom, adresse, e-mail pour suivi) — validation fondateur requise car c'est un service externe qui recevra des données clients.
5. **Qui paye le port** : inclus dans le prix ou facturé au client ? ❓ (Hugo, lié au prix de vente Q10).

### Emballage
- Sachet individuel (recyclé/compostable) par pièce + pochette d'expédition souple renforcée (plus léger et moins cher qu'un carton → reste dans une tranche de poids basse).
- Petite carte de remerciement + QR vers Instagram (Studio).
- Coût unitaire de l'emballage ❓ (devis à demander, éventuellement fourni par l'usine portugaise — Rui).

### Retours
- Vente à distance en France : **droit de rétractation de 14 jours** pour le client (Code de la consommation, art. L221-18 — [Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226842)). Qui paie le retour : à écrire dans les CGV (Hugo).
- Process : client répond au mail d'expédition → Clara passe le statut à `retour` → étiquette retour (Mondial Relay ou Sendcloud) → contrôle à réception → échange ou remboursement validé par le fondateur.

---

## 7. Précommandes « gratuites » : ce qu'il faut clarifier (Q11, Q14)

La bio Instagram annonce « Précommandes gratuites ». C'est le point le plus risqué pour les quantités et la trésorerie.

| Question | Pourquoi ça compte | Options |
|---|---|---|
| **Gratuite = aucun paiement du tout ?** | Sans paiement, c'est une liste d'attente, pas une commande. On ne peut pas produire sur cette base sans risque de stock invendu. | A) Liste d'attente gratuite + paiement complet à l'ouverture des ventes ; B) Acompte (ex. ❓ €) remboursable ; C) Paiement complet en précommande |
| **Engagement du client ?** | Détermine le taux de conversion ❓ et donc la quantité à produire | Ajouter une étape de « confirmation avec paiement » avant le lancement production, avec date limite |
| **Prix communiqué ?** | Le client précommande-t-il sans connaître le prix (Q10) ? Si oui, conversion encore plus incertaine | Communiquer le prix avant la demande de paiement |
| **Date de livraison promise ?** (Q14) | Avec un prototype pakistanais refusé et une usine pas encore choisie, toute date est fragile | Ne pas promettre de date ferme avant signature avec l'usine ; parler de « saison » |
| **Cadre légal si paiement** | Encaisser avant production = obligations (date de livraison à indiquer, remboursement si retard, CGV) | Hugo : CGV + mentions avant tout encaissement |
| **Le formulaire collecte-t-il le consentement** pour recevoir des e-mails ? | RGPD : sans case de consentement, on ne peut envoyer que des e-mails liés à la commande, pas de marketing | Ajouter une case au formulaire (Q13) |
| **Combien de précommandes déjà reçues ?** | Le tableau est vide : il faut rattraper l'historique Gmail | Transfert de tous les e-mails Netlify existants |

**Proposition Clara** : garder la liste gratuite pour mesurer l'intérêt, mais **ne dimensionner la production que sur des précommandes payées (ou avec acompte)**, collectées lors d'une « fenêtre de confirmation » de 7 à 10 jours avant la commande usine. Décision : fondateur, avec Hugo (trésorerie/CGV) et Malik (impact conversion).

---

## 8. Prochaines actions
| Action | Qui | Échéance |
|---|---|---|
| Transférer 2-3 e-mails de précommande + total déjà reçu | Fondateur | 20/11/2026 |
| Créer libellés + filtre Gmail (§2) | Fondateur | 20/11/2026 |
| Trancher « gratuit / acompte / payé » (§7) | Fondateur (+ Hugo, Malik) | Avant la prochaine réunion |
| Grille de tailles + coloris prioritaires | Fondateur + Rui | Avant la 1re synthèse |
| Saisie de l'historique + 1re synthèse coloris × taille | Clara | J+2 après réception des e-mails |
| Peser un ensemble emballé, MOQ par coloris/taille | Rui (usine Portugal) | Pendant le voyage |
| Vérifier tarifs sur sites officiels transporteurs | Clara (si domaines autorisés) / fondateur | Avant 1re expédition |
