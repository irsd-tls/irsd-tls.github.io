# Site IRSD - Documentation

Le site est organisé en fichiers textes.
Le contenu est écrit en Markdown (extension `.md`, voir [plus bas](#syntaxe-markdown-pour-le-contenu)). 

Pour modifier le site, il faut **trouver le bon fichier et le modifier**.
La mise à jour du site se fait pour l'instant dans un deuxième temps, manuellement, par le webmaster (Jean, pour le moment).
Donc, faites vos modifications puis prévenez que le site doit être mis à jour en ligne.

Le site est **bilingue** : chaque page est associée à deux fichiers, un pour la version française et un pour la version anglaise. Si vous ne voulez pas écrire les deux versions, c'est facile de donner un fichier à une IA ([chat.inserm](https://chat.inserm.fr/)) et demander de le traduire. Le résultat est, en général, dans le bon format markdown et donc prêt à être copié-collé.

Un conseil : n'hésitez pas à regarder les pages existantes pour vous inspirer/copier. 
Par exemple, [`content/eq4.md`](content/eq4.md) ou [`content/people/jean.monlong.md`](content/people/jean.monlong.md).

Liens rapides :

- [Quels fichiers modifier](#quels-fichiers-modifier)
- [Syntaxe Markdown pour le contenu](#syntaxe-markdown-pour-le-contenu)
- [Comment modifier un fichier markdown](#comment-modifier-un-fichier-markdown)
- [Page Membre](#page-membre)
- [IDs des Équipes/Plateformes](#ids-équipes-plateformes)
- [Images](#images)
- [Publications](#publications)

## Quels fichiers modifier

- Page d'une équipe ou d'une plateforme, directement dans le dossier `content`
    - `content/eq1.md` (version française)
    - `content/eq1.en.md` (version anglaise)
- Page d'un membre, dans le dossier `content/people` (voir [Page Membre](#page-membre))
    - `content/people/prenom.nom.md` (version française)
    - `content/people/prenom.nom.en.md` (version anglaise)
- Photo d'un membre dans le dossier `static/images/people`
    - `static/images/people/leon.kautz.png`
    - Note: doit correspondre au champ `image:` de l'en-tête du fichier membre. Voir [Page Membre](#page-membre).
- Photo *bannière* en haut de la page d'équipe, dans le dossier correspondant de `static/images`
    - `static/images/eq1/banner.jpg`
- "Logo" utilisé dans les pages [Équipes](https://www.irsd.fr/equipes/) ou [Plateformes](https://www.irsd.fr/platforms/)
    - `static/images/eq1/logo.svg`

## Syntaxe Markdown pour le contenu

Les pages sont écrites en **langage Markdown** : fichier de texte avec une syntaxe simple pour définir de la mise en forme (titre, listes, gras/italiques, etc).
Pour un résumé de la syntaxe, voir [ce tutoriel](https://docs.forge.apps.education.fr/modeles/tutoriels/tutomd/) ou l'exemple plus bas.

Chaque fichier contient un **en-tête**, entouré de `---`, qui contient des métadonnées.
En général, pas besoin d'y toucher, sauf si vous savez ce que vous faites !

Le contenu vient ensuite, et c'est sans doute cette partie que vous voudrez modifier.

Par exemple, un fichier ressemble à ça :

```md
---
title: "Le titre de la page"
image: images/une_image.jpg
---

Contenu de la page écrit en Markdown.

# Un titre de niveau 1

## Un titre de niveau 2

Une phrase avec des mots **en gras** et *en italique*.
Une liste non numérotée avec : 

- un élément
- un autre élément
    - un sous-élément
    - un autre sous-élément

On peut aussi écrire des liens comme ça : [texte à afficher](https://www.url.du.lien.fr).
...
```

## Comment modifier un fichier markdown

Pour modifier un fichier markdown, il vaut mieux **ne pas l'ouvrir avec Word**.
Je vous conseille cet éditeur en ligne : [https://markdownviewer.org/](https://markdownviewer.org/).
Vous pouvez :

1. Importer un fichier avec *Import Markdown*
2. Modifier le contenu dans l'onglet de gauche, et voir/vérifier le résultat sur l'onglet à droite.
3. Exporter le fichier avec *Export* et remplacer le fichier original, au bon endroit.

[VSCode](https://code.visualstudio.com/) est une autre option. 
Sinon, demandez au service informatique d'installer un logiciel spécial ?

## Page membre

Les fichiers s'appellent `content/people/prenom.nom.md` (ou `content/people/prenom.nom.en.md` pour la version anglaise). 
Idéalement, `nom.prénom` est l'identifiant utilisé dans le mail INSERM.

Dans l'en-tête des fichiers, on renseigne des informations basiques.
Pour un exemple assez complet, voir [`content/people/jean.monlong.md`](content/people/jean.monlong.md).

### Template

Pour remplir les pages des membres de vos équipes :

1. Partager les liens si dessous avec la personne
2. Après l'avoir modifié, elle l'*Export* et vous l'envoie
3. Vous copiez le contenu dans la page correspondante, par exemple `content/people/prenom.nom.md`.

- [Template en français](https://markdownviewer.org/#share=eJyNVttu20YQfedXDBS4SQSTutjyrU3T1E4BF7HjOkkbICiCFTmWNuDu0nuxXQT5l776O_RjPUNKjty6RQ1IIpczO2fOnLNmnudZ1LHmA-qd-cWtdYZOnellbJSusdh4xlqBzw_aBvamuPC97JqnQUdJmsfYhIPBoGEfnFV1gUeNmvGgl810nKcpYrqLjwnpVhnuZc6XusKDIf5yfMb5_u7Wbj6ZjHZ6WTN3VnYeTmhnTLvbtD2hrWEv884ZLP84GY8R5FBfO4uFwzn7cs4JsALXXEauPlZOBzwaDYvRcGtvELZHk72dfDjeyoeTvf2d_OZbeTQa7wxCqdmWXKjpbG9vd9TLcjCSPXpEJ9rq_PDXLMup3x_t7-_n4-Fw1O_TK10ymCC29P79e1r8SW9dqh26K9pYCZPYbcSeqBDZU8WrUPzcRW1L1C6ijlwZnVdRAurH76y-Apk6Lm6XiZtUKRuoZqoWt43ykQ3buHxY0Jl3nzge3Nt7b7X3O8ukrF3cssSXi9uQPFPjkqfFbc1XLbogCzWHu_RdpI8k_cyFWK3gdSgeL24vk2744a5GuznSDufKzzr851x2A6Lj0zcvz0-6Jo_P3xwVLc8vbyCdqEHogN4i1urLxEFoP0x1FLCCm-taAAJzAzEBuVZyq23kELWVm7WMqSrBnsdkLWP58uzwHD-_sQzD0rR2EbcvyqivWpYb7_Dj6j-i1G5RdZw-CU-lul-1kGWvnGdDugnJUOVq5wmDIog6blLpIAvIDxBAhap0o6EuOyOudez3NylwhSRinYJxFWGMDTbQFmbQVcJEU6RaTVGCOHbbM_WNmllFqgY21S-ydxHK04ZURUbLxRVuldkkDCWQxbx8qohvAFhHJR6hVNfKlK7bW4J00FKr3VM3CCZWgG-AynVtoFYssiPZUqXIpH07ibZjbcEIzoU524o92sfClatTg3IMOOiWOGCgpcbUzKoRTnSRZho6sgKIIGTcJF9kL29KbiIcDDLBgitLxSXiytToSkXJQBeYkq6ge_AoXKFomepGSd_kLi50qZVImb08Na4WGEoI0qAjLJlNBqp7gzmgfTmyGkmD-iihF0zNGZBDGkKBii3gBWLvl2O-axLsl2UKykZ915-BdFAjVd3qJkUXlSGRi0KldkSsJAjqEdQKxpwSKHLoBUOMQtKVENoCggIQg0EpKA9nLTxIUwYbCNLyXekyqo4LvmlqXaK_Ijtl4zqBSBmzjhlEqdV96HQbGjmSRbCYMrlK1nAhc4qdXtukpSRQCpGiR71sGjBdaCfgW6nxej1J0WQZJkCmQJPuIXnvWrGiPSOTaaW7YnHprbbs3w3W769ZTAy18lgnujXAohebTFcBdoMeKr00nOoc929-a-1mln4z7Zzk7Pva1z8tqB7yoLnnQTTWuhBU-qY1YUgAjsNs6UoXJP--M6t7ztRfnZn88-yXlTflBKjhLlAnHr1vTWEWTmH1sEPbFq2e61ocI0cphLVWZrPdu7Px-pCk2tLMl8l9FdV9Zz_vjtI0FXEKC-2x_vr88PjogD7ImwNeHNp3gcL52eCBt4Hfn_yfqKfY9QPKnHDVJcgLyfX1dWHLqS5sjdcXPS9m7mrQpKnhavAc_wfMsxNna2dnG-PDjfHwZ1Z2YzL9CQ3g7kWKc-dxcQrlbUwqXL0-x9d_pBzDw-BvpuJ64jfB-fgMhxg_zbLPn7_DoeOamvNmjRT6_suXLMv-AhkUS5U)
- [Template en anglais](https://markdownviewer.org/#share=eJyNVv1PG0cQ_f3-ipEjqsbizh9gDLRp2gCpqEJCIWkjRVW0vht8297uHvsBRFH-9765s4lpk6pIxnu7Mzszb94bX57nWdSx4UMaPNc-RKsM0wvVLwYZG6UbnLWerTMFPj9qG9ib4soPslteBB3Ft46xDYejUcs-OKuaAketWvJokC11rNMCNv3ifYJ7f7nzpa5wMMZfjs80P5jvzPPZbLI3yNraWbl5PKO9Kc13aXdGO-NB5p0z2H42m05h5BBfO4uNCw6sfFkz8grccBm5el85HXA2GReT8c7-KOxOZvt7-Xi6k49n-wd7-d13cjSZ7o1CqdmWXKjFcn9_PhlkOZDJHj2iy9r5SEe_ZVlOw-Hk4OAgn47Hk-GQXuiSgQVpS2_fvpWv1y41DvUVna2Yie0ubM-AKPu1qYoUa6Y3Vt8ALx0_kLuSg3u_XfGbw--8Pv6q9bZcJydyZcWt8tGwjQWde_cn6j98cOX--sqfVUsfABVFR15pFFDWuvyL7b3pHKaTLroLsXJldF41dMVN4243Y75mZSS7jTCTeS5-IIiyyIU-d4VOX16eXJyJ_enF5XHRgXtyB8JEyWGE28ra6uvEQaA-tZFD1KAScQvicKOxLJEDlamJyTOMnil02XcH93vX50cX-PqdBXBLi8ZFPAKSyK75EHVJcNI3gLHLoEuwrKntMUPsF86zId2GZKhyjfMEzAmEjdtUOjQcMREL5apKtxrEsUtCenE43KbAFZyIdQrGVRTZtE7aDqLrKgGQFKlRC4Qgjv31TEOjllaRalC9GhbZm0hsNaCtyGhZ3OBRmW26TjqQRVN8qojvGPqJSvhPqWmUKV1_txjpoCVWd6duYUyskL5BVq4vA7FikR3LlSpF0NgDwFXFaLJnaL5mWwHgKBs3rkktwjHSQbXEQaijm2aNE0pKdJWWGi22khCBknhIvshO7kpuIycBEyi4slRcwq5Mra5UFA9UgSboCrQBjoIVgqKvrZK6wfkrXWoFomN-yKlxjaShBCANOMIK2WTArUv0AeXLOGrFDRyjhFrQNWcADmnQA0y1SC8Qe79q832RQL8sU1A26vv6DMiJGKnqd7ehoAgFCF1UKzzEFisxAnska8WkFgSIHGpBE6OAdCOAdgmBAbBBo0QhmKMQGi0YaMBIy_9Kl1H1WPBd2-gS9RXZSzauJ4iEMZs5Ayi1fg49b0Mr41YIiy6Tq2QPC-lT7PnaOa0ogVCwFD7qVdFI04WuA76jGm_GExdNliECeEpqUj0o711HVpRnpDMdddcorrTVhf2nwIbDDYmJoNYa60m3kbDwxSbTR4DcwIdKrwSnesV9TW-d3MxKb6brE2rbqOvfElRf0qB5oEEU1qkQUPq2E2FISBzDa6VKF8T_oTKrB8rUn5WZ_NPs17U2ZQJgDiKgFo0-lKYgC6Ww-rJCuxKtrnUjipGZCmJthNnu7u5lvNkkibYS83Vyn0n1UNlPuyF6nhZCTkGhG96vLo5Ojw_pnbwV4KWg-50vnF-OvvBL_8e3_8fqMW59hzBnXPUO8rJxe3tb2HKhC9vg1UTXxdLdjNq0MFyNnmL6mydnzjbOLremR1vT8S-s7NZs8RwF4OmnFPHLjsVLMG9rVmH16gL__sPlFBoGfksVNx2_CXhBeIIhxo-z7OPH7zF0XNtw3m6AQj98-pRl2d-yHDbN)

Note: `{{< people-publications >}}` sera remplacé par la liste de publications de la personne.

### En-tête

#### Informations nécessaires

- `title:` prénom(s) et nom de famille
- `email:` email institutionnel
- `team:` équipe ou plateforme d'appartenance. Voir [liste équipes/plateformes](#ids-équipes-plateformes).
- `image:` nom du fichier photo dans `static/images/people`
- `position:` position dans l'institut, par exemple *Doctorant*

#### Autres informations

- `phone:` numéro de téléphone
- `room:` bâtiment/bureau
- `subteam:` sous-équipe (pour l'équipe 2 pour l'instant). Voir [liste équipes/plateformes](#ids-équipes-plateformes).
- `website:` un site internet personnel
- `github:` identifiant GitHub
- `orcid:` identifiant ORCID
- `team2`/`position2` pour apparaitre dans une autre équipe/plateforme ([exemple](content/people/nathalie.vergnolle.md))

#### Pour les anciens membres

- `alumni:` (ancienne) équipe. Même option que pour `team`.
- `alumni_position:` comme pour `position`

#### Pour les publications mises en avant

Par défaut, seront affichées les publications dont la personne est co-auteur et qui ont été listées pour les pages d'équipe (ou autres pages membres).
Deux champs peuvent être utilisés dans l'en-tête : `selected_dois:` et `oa_id`.
Plus de détails dans la section [Publications](#publications).

## IDs Équipes Plateformes

Dans les pages des membres, les champs `team:` correspondant à chaque équipe/plateforme sont :

- `eq1`/.../`eq6` pour les équipes 1, ..., 6.
- `eqjv` équipe émergente de Julien.
- `platform-digestive` modèles digestifs
- `platform-organoid` organoides
- `platform-bip` BIP

Les sous-équipes de l'Équipe 2, pour le champ `subteam` : 

- `genotoxins`: Génotoxines bactériennes
- `ev`: Vésicules extracellulaires bactériennes
- `resistant`: Écologie des bactéries pathogènes et antibiorésistantes
- `admin`: Gestion-logistique

## Images

Où placer des images ?

- visage des membres dans : [`static/images/people/`](static/images/people/)
    - image carrée, pas trop grande (ex 600x600)
    - nom fichier utilisant l'identifiant INSERM, ex `jean.monlong.png`
        - Note : doit correspondre au champ `image:` de l'en-tête du fichier membre. Voir [Page Membre](#page-membre).
- pour une page d'équipe/plateforme : `static/images/ID_EQUIPE/` avec `ID_EQUIPE` correspondant à l'équipe/plateforme (voir [liste équipes/plateformes](#ids-equipes-plateformes)).

Utilisation sur une page :

```
{{< img "images/platform-organoid/financements.jpg" "80%" >}}

{{< img2 "images/eq4/enhancer-gene_orig.png" "images/eq4/tubemap-for-website_orig.png" "60%" >}}
```

## Publications

Le site utilise [OpenAlex](https://openalex.org/) pour extraire les informations des publications. 
Deux champs sont utilisés dans l'en-tête des fichiers markdown : `selected_dois:` et `oa_id`

### `selected_dois`

Pour les pages *équipe* ou *membre*, le champ `selected_dois:` de l'en-tête sert à **lister les DOIs** à inclure. 
Les DOIs sont séparés par des `;`, par exemple : 

```yaml
selected_dois: "10.1038/s41586-023-05896-x;10.1126/science.abg8871;10.1186/s13059-020-1941-7"
```

### `oa_id`

Dans l'en-tête d'une page *membre*, vous pouvez aussi renseigner `oa_id` avec l'identifiant OpenAlex de la personne.
Pour trouver l'ID correspondant, cherchez sur [OpenAlex](https://openalex.org/) puis utilisez l'identifiant dans l'adresse de la page *Author*.
Par exemple, pour [https://openalex.org/authors/a5048124649](https://openalex.org/authors/a5048124649) : 

```yaml
oa_is: a5048124649
```

