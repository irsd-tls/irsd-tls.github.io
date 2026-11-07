k# Documentation avancée

## Tester le site localement

Le site utilise [Hugo](https://gohugo.io/).
Une fois installé, le site peut-être "compilé" et ouvert localement dans un navigateur avec :


```sh
hugo server --disableFastRender
```

## Scripts pour la préparation des publications

Voir [scripts/README.md](scripts/README.md).

## Icon de Font Awesome

Dans certaines pages, on peut utiliser des icon de FontAwesome. 
Le site utilise la version 5: [https://fontawesome.com/v5/search](https://fontawesome.com/v5/search).

On utilise ces icones pour les informations des membres, par exemples.

## Menus

- Français: [`config/_default/menus.toml`](config/_default/menus.toml)
- Anglais: [`config/_default/menus.en.toml`](config/_default/menus.en.toml)

## Informations pour les pages "spéciales"

- Page d'accueil [`data/fr/homepage.yml`](data/fr/homepage.yml)/[`data/en/homepage.yml`](data/en/homepage.yml)
- Liste des équipes [`data/fr/teams.yml`](data/fr/teams.yml)/[`data/en/teams.yml`](data/en/teams.yml)
- Liste des plateformes [`data/fr/platforms.yml`](data/fr/platforms.yml)/[`data/en/platforms.yml`](data/en/platforms.yml)
- Liste des services [`data/fr/services.yml`](data/fr/services.yml)/[`data/en/services.yml`](data/en/services.yml)

## Liste de membres d'une équipe

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

# TODO list

1. Fix le bug avec les listes de gens https://github.com/metafizzy/isotope/issues/1575
2. Mettre en place une fonctionnalité de galerie d'image
3. Améliorer la gestion des membres et alumnis, en prenant en compte la période d'activité pour les publications ?
