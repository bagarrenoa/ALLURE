---
name: reunion
description: Réunion d'équipe du QG Allure. Victor (gérant) fait travailler tous les pôles sur un sujet, Basile (avocat du diable) attaque le résultat, puis Victor rend un compte-rendu daté dans rapports/. Utiliser quand le fondateur dit « réunion », « fais travailler toute l'équipe » ou « point général ».
---
# Réunion d'équipe Allure

Sujet : $ARGUMENTS (si vide : « point général de la semaine : où en est Allure et que faire maintenant ? »)

1. Lire `BRIEF.md`, `QUESTIONS.md`, et les 3 derniers fichiers de `rapports/`.
2. **Tour de table en parallèle** : lancer avec l'outil Agent, dans un seul message, les agents concernés par le sujet parmi
   `ines-cmo`, `malik-growth`, `lou-influence`, `mila-directrice-creative`, `rui-sourcing-portugal`, `clara-ops`, `hugo-finance-juridique`, `nora-veille`.
   Chacun écrit son livrable dans son dossier et renvoie un résumé de 10 lignes max.
3. **Contre-expertise** : envoyer la synthèse à `basile-avocat-du-diable`.
4. **Compte-rendu** : rédiger `rapports/AAAA-MM-JJ-compte-rendu.md` au format défini dans `.claude/agents/victor-ceo.md`, ajouter les nouvelles questions à `QUESTIONS.md`.
5. Mettre à jour `qg/etat.js` : pour chaque agent, `statut` (`au poste`, `en réunion`, `en pause`) et `tache` (une phrase), pour que le plateau du QG l'affiche.
6. Répondre au fondateur avec le résumé en 5 lignes + les décisions à prendre.
