# Documentation avancée

## Tester le site localement

Le site utilise [Hugo](https://gohugo.io/).
Une fois installé, le site peut-être "compilé" et ouvert localement dans un navigateur avec :


```sh
hugo server --disableFastRender
```

## Icon de Font Awesome

https://fontawesome.com/v5/search

## Menus

- Français: [`config/_default/menus.toml`](config/_default/menus.toml)
- Anglais: [`config/_default/menus.en.toml`](config/_default/menus.en.toml)

## Informations pour les pages "spéciales"

- Page d'accueil [`data/fr/homepage.yml`](data/fr/homepage.yml)/[`data/en/homepage.yml`](data/en/homepage.yml)
- Liste des équipes [`data/fr/teams.yml`](data/fr/teams.yml)/[`data/en/teams.yml`](data/en/teams.yml)
- Liste des plateformes [`data/fr/platforms.yml`](data/fr/platforms.yml)/[`data/en/platforms.yml`](data/en/platforms.yml)
- Liste des services [`data/fr/services.yml`](data/fr/services.yml)/[`data/en/services.yml`](data/en/services.yml)

## List de membres d'une équipe

Le shortcode qui s'utilise avec `{{< people-list >}}` est défini dans [layouts/shortcodes/people-list.html](layouts/shortcodes/people-list.html).

Pour l'équipe 2 (pour l'instant), on veut peut-être lister les membres de sous-équipes avec le shortcode `{{< people-list-subteam compath >}}` défini dans [layouts/shortcodes/people-list-subteam.html](layouts/shortcodes/people-list-subteam.html).

Pour les anciens membres: `{{< former-people-list >}}` défini dans [layouts/shortcodes/former-people-list.html](layouts/shortcodes/former-people-list.html).

## Liste de tous les membres de l'IRSD

[layouts/_default/peoples.html](layouts/_default/peoples.html)

## Couleur et autres contrôles esthétiques

[assets/sass/custom.scss](assets/sass/custom.scss)

## Listes des publications

- Page globale : [layouts/_default/pubs.html](layouts/_default/pubs.html)
- Pour une équipe : [layouts/shortcodes/team-publications.html](layouts/shortcodes/team-publications.html)
- Pour un membre : [layouts/shortcodes/people-publications.html](layouts/shortcodes/people-publications.html)

## Scripts automatiques

Voir [scripts/README.md](scripts/README.md).

# TODO list

1. Fix le bug avec les listes de gens https://github.com/metafizzy/isotope/issues/1575
2. Mettre en place une fonctionnalité de galerie d'image
3. Améliorer la gestion des membres et alumnis, en prenant en compte la période d'activité pour les publications ?

# Pour gérer les publications

*En cours de rédaction*

- `oa_id` l'identifiant OpenAlex à utiliser pour extraire périodiquement les publications. 
    - Chercher sur [OpenAlex](https://openalex.org/) puis utiliser l'identifiant dans l'adresse de la page *Author*, par exemple *a5048124649* pour [https://openalex.org/authors/a5048124649](https://openalex.org/authors/a5048124649).
- `selected_dois` liste de DOIs des publications à afficher en priorité sur la page perso/équipe. 
    - Séparés par `;` sans espaces, par exemple: `10.1038/s41586-023-05896-x;10.1126/science.abg8871;10.1186/s13059-020-1941-7`.
