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
- [Cas pratiques](#cas-pratiques)

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

### Templates

Pour remplir les pages des membres de vos équipes :

1. Partager les liens si dessous avec la personne
2. Après l'avoir modifié, elle l'*Export* et vous l'envoie
3. Vous copiez le contenu dans la page correspondante, par exemple `content/people/prenom.nom.md`.

- [Template en français](https://markdownviewer.org/#share=eJx1VNtu20YQfedXDJSHtIIpS7Jl2UbRtHXyECAJXCdu8xasyLE0BXeX3ovrIsi_9FXfoR_rGVKy5dY1IJO7nNk5c-acLcuySJIaPqfBZdisnbf0wdtBwdZIg802MPZG-P0kLnKwo5swKP7kRZSkSauU2nh-eNhyiN6ZZoRPrVny4aBYSlrlBWL6ly8Z6c5YHhQ-VFLjwxh_JX7T8mx-NC9ns8nJoGhX3unJ4xmdTGl-TMczOhoPiuC9xfYvs-kUQR71xTtsXKw4VCvOgBW54Spx_aX2Es-pICppMBmPJuOj08N4PJmdnpTj6VE5np2enZT3g8eAyfTkMFbCruKRWSxPT-eTQVGCnOLFC3ovTsqL34qipOFwcnZ2Vk7H48lwSO-kYpBC7Ojz58-0-Zs--dx4NDrqYjVMY48R-97ExIFq3oXi8RB1rFFzRL32VfLBJA1oXl47uQOvkjbrbeIB1cZFapjqzbo1IbFll7YfR3QZ_B-czp-cfbo7-9oxGec2a9b4arOOOTC1PgfarBu-69BF3Wg4PqTPkT7R9EsfU72D16N4uVnfZmn5-a4m8xJpFysTlj3-K676WdHbDx_fXL3vm3x79fH1qOP5zT1UlASEHtInxDq5zRyV9ovcJAWruLlpFCAwt9AVkIvRpbjEMYnTxV7GwlRgL2CyjrF9e3lxhcfvrMNwtGh8wvLnKsldx3IbPB6--Stp7Q5Vz-l38XutHnYtFMU7H9iStDFbqn3jA2FQBH2nA6o8ZAElAgKoMLW0AnW5JXEjaTg8oMg1koglR-trwhhbHCAOvpA6Y6I5UWMWKEGc-uOZhtYsnSHTAJsZjorrBOWJJVOTFX25w9LYA8JQIjnMK-Sa-B6AJRm1C-WmMbby_dkaJFG0VnemtAgmNoBvgcr3baBWGhWv9UiTE5OEbhJdx-LACK6IFbuaA9rHxp1vcotyDDjoljhioJVganbXCGe6yUuBjpwCIggZixxGxZv7itsEM4NMsOCrynCFuCq3UpukGegCU5IaugePyhWKVrlpjfZN_uZGKjEqZQ761fpGYRglSEBH3DKbLVT3EXNA-3p7tZoG9VFGL5iatyCHBEKBih3gReIQtmN-aBLsV1WOxiV56M9COqiR6373gJJPxpLKxaBSNyI2GgT1KGoDYy4IFHn0giEmJelOCe0AQQGIwaAMlIdrFx6kBYMNBIn-r6VKpueC79tGKvQ3Kj6w9b1AtIzdxwyizG4de93GVm9nFSymTL7WPbzonFKv1y5pKwmUQqTqUbZNA6aP3QRCJzXer6cpQo5hAmQqNO0ekg--EyvaszqZTro7Frfe6sr-22DD4Z7F1FA7j_Wi2wOsenHZ9hVgN-ihlq3hTO-4__NbZze79Zvt5qR332Nf_7Wgec6D9okH0VjnQlAZ2s6EMQM4LrOtK33U_KfOrJ84Ux6dmcOr4tedN_UGaOAuUKcefWpNZRZOYfO8Q7sWnaykUcfoVQph7ZU56M7ubbw_JK22NfNt9o-ieursV_1VmhcqTmUB1_rXrz_AeL5tuGz3PtCP374VRfEPPo3_7g)
- [Template en anglais](https://markdownviewer.org/#share=eJx1VF1vGzcQfL9fsVDeBJ8syZZlG0VT5KNFACdw7aT1W0Dx1ta2R_LMD8dGkP-e2TvJlttEgKQ7cpe7MzvDuq6rLLnlUxr9LjFlbxzTmRkeRhU7Iy32usg-uAm-v4lPHN3kOo6qL7xKkjV3nXOXTvf3O44peNNOsNWZG94fVTeS12WFmOHhc0H6cHiIVhpsTPGp8Z3XJ8uDZb1YzI5GVbcOXk-eLuhoTstDOlzQwXRUxRAcll8t5nMEBdSX4LFwwYlNtGtGX4lbtpmbz02QdEoVUU2j2XQymx4c76fD2eL4qJ7OD-rp4vjkqL4fPQXM5kf7yQp7yxOzujk-Xs5GVQ2Sqhcv6HIdYqbXf1VVTePx7OTkpJ5Pp7PxmM7EMmgh8XR1daV_H0NpA6BO-lgN09hDxL4HuRy3oSZTXjN98nIH6iQ_ULjWjce8Q81bIu98_ean0Xt6nO7okQ13JmbHPk_oPIZ_QMXpsyOPt0f-YTp6AGuUA0UjAGDXYv9l_xi6ROisrx5SboLNIZqWrrltw5fdmh_ZOO1up8xsWWsetGI8eqGnAdG7D5dvL95r_LuLyzeTnty399BO1h72cZpde7ktnJTqdz5zygJVEXfQELeCR4seyJY2l8gIemUw8NhvPK7dnr--wN_frIR7WrUh4xWUZA7tQxZLSJI70Nh30Ddo19QNnKH2WYjsSLpUHDWhDZHAOUG7eY9swMBRE7UA1zTSCYTjbwjt5fF4jxI3SCKWklxoKLPrgo4dmpemgJCSqTUrlCDOw_FMY2duvCHTAr0ZT6pPmdgLqG3IiT7c4dW4PbotkshjKLE0xPcMK2WjVqDStsbZMJytQZJEa_VnSodgYoP2HboKAwzUypPqjR5pSoaMIwjcIMaQI8P-a_YNCM66cBfa0qEcox2gJU4qHWnbLU-AVOi63AhG7LUhgiTxUuKkentvuctclEywEKw1bBFnSyeNyZoBFBiCNJANeFSuUBRz7YzihuavxYqB0HGV6K4LrbZhlCABHWnDbHHQ1iXmAPh6M3WaBo1RARZMLTiQQwJ5QKke7SXiGDdjfgQJ9q0tyfgsj_gcxIkapRlW9-CgDAeoXEynOsQSGw2CerRrw2RWBIoCsGCIWUm6U0L7hqAAxGBQ6hBcqTAarRhsIEj0txGbzcAF33etWOCbVB_YhUEgWsbt9gyizPY9DbpNnd68KlhMmUKja3jQOeVBr33SRhIohUjVo2xAo82Q-gnEXmq8W09ThDzDBMjU1hQ9JB9DL1bAczqZXrpbFjfe6sv-12Dj8Y7F1FBbjw2i22lY9eKLGyrAbtBDIxvDmcFxP_Nbbze38Zvr5wRsO7j-b0HzIw-6Zx4EsN6FoDJ2vQlTQeO4vDauDEnznzuzeeZMeXJmiS-rP7fe1BsA9yAKinr0uTWVWTiFzY8d2kP0spZWHaN3KoS1U2avP3uw8e6QtNrGzLclPInqubNf9pfoeVmpOJUFXKBfv_4C44Wu5brb2aBfv32rquo7PerrJg)

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
- pour une page d'équipe/plateforme : `static/images/<EQID>/` avec `<EQID>` correspondant à l'équipe/plateforme (voir [liste équipes/plateformes](#ids-equipes-plateformes)).

Utilisation sur une page :

```
{{< img "images/platform-organoid/financements.jpg" "80%" >}}

{{< img2 "images/eq4/enhancer-gene_orig.png" "images/eq4/tubemap-for-website_orig.png" "60%" >}}
```

## Publications

Le site utilise [OpenAlex](https://openalex.org/) pour extraire les informations des publications. 
Deux champs sont utilisés dans l'en-tête des fichiers markdown : `selected_dois:` et `oa_id`

> Note: Ces informations sont partagées entre les deux fichier `.md`/`.en.md` d'une page, donc pas besoin de répéter ces deux champs. Vous pouvez, par exemple, uniquement renseigner `oa_id`/`selected_dois` dans le fichier *français* (`prenome.nom.md` ou `eqX.md`).

### `selected_dois`

Pour les pages *équipe* ou *membre*, le champ `selected_dois:` de l'en-tête sert à **lister les DOIs** à inclure. 
Chaque DOI est listé entre guillements et précédés de `  - `.
Par exemple : 

```yaml
selected_dois:
  - "10.3389/fcell.2020.00363"
  - "10.1093/ecco-jcc/jjaa229"
```

### `oa_id`

Dans l'en-tête d'une page *membre*, vous pouvez aussi renseigner `oa_id` avec l'identifiant OpenAlex de la personne.
Pour trouver l'ID correspondant, cherchez sur [OpenAlex](https://openalex.org/) puis utilisez l'identifiant dans l'adresse de la page *Author*.
Par exemple, pour [https://openalex.org/authors/a5048124649](https://openalex.org/authors/a5048124649) : 

```yaml
oa_is: a5048124649
```

## Cas pratiques

### Modifier le texte d'une page

1. **Ouvrer [le bon fichier](#quels-fichiers-modifier)** avec un éditeur Markdown ([https://markdownviewer.org/](https://markdownviewer.org/) par exemple).
1. **Modifier le contenu** en utilisant la [syntaxe Markdown](#syntaxe-markdown-pour-le-contenu).
2. Enregistrer et **remplacer le fichier** sur DIGEST.

### Ajouter un nouveau membre

1. Préparer un **identifiant**, par exemple `prenom.nom`
    - Le plus simple est d'utiliser le nom utilisé pour son email.
1. Préparer une **image carrée**, de taille ~600x600 et la placer dans `static/images/people/`
    - Utiliser l'identifiant pour le nom de l'image, par exemple `prenom.nom.png`
1. Créer un **nouveau fichier** `content/people/prenom.nom.md`
    - Ou copier un fichier existant de votre équipe.
    - Si le nouveau membre a déjà publié, [chercher son ID OpenAlex](#publications) et remplir `oa_id`
    - S'assurer que `image:` pointe bien vers l'image préparée plus haut.
1. Idem for `content/people/prenom.nom.en.md`
   - À partir d'une copie de `content/people/prenom.nom.md`
   - Dans l'en-tête, il y a juste le champs `position` à traduire
1. (Optionnel) Envoyer [les templates](#templates) au nouveau membre pour qu'il/elle remplisse et vous renvoie le contenu de la page.

### Changer la photo d'un membre

**Remplacer l'image dans `static/images/people/`.**

Attention seulement à ce que le nom de l'image ne change pas. 
Si vous devez changer le nom, par exemple, à cause d'un format différent, il faudra aussi mettre à jour le champ `image:` dans les pages `content/people/prenom.nom.md`/`content/people/prenom.nom.en.md`. 
Dans ce cas, ne pas oublier de supprimer la vieille photo.

### Changer l'image bannière d'une équipe/plateforme

**Remplacer le fichier `static/images/<EQID>/banner.jpg`**, où `<EQID>` est [l'ID de l'équipe/plateforme](#ids-équipes-plateformes).

### Changer le "logo" d'une équipe/plateforme

"Logo" utilisé dans les pages [Équipes](https://www.irsd.fr/equipes/) ou [Plateformes](https://www.irsd.fr/platforms/)

**Remplacer le fichier `static/images/<EQID>/logo.svg`**, où `<EQID>` est [l'ID de l'équipe/plateforme](#ids-équipes-plateformes).

### Ajouter/enlever des publications

**Modifier le champ `selected_dois:`** dans l'en-tête du fichier:

- `content/eq1.md` pour une équipe (changer `eq1` en fonction du nom de l'équipe)
- `content/people/prenom.nom.md` pour un membre

Prévenir Jean que les publications doivent être mise à jour.

### Ajouter une image dans une page

1. Placer l'image dans le dossier `images/<EQID>` (avec `<EQID>` est [l'ID de l'équipe/plateforme](#ids-équipes-plateformes))
1. Dans le fichier de la page, par exemple `content/<EQID>.md`, insérer l'image avec :

```
{{< img "images/EQID/IMG.jpg" "80%" >}}
```

Le deuxième argument `80%` définit la taille d'affichage de l'image. 

Si vous voulez deux images côte-à-côte:

```
{{< img2 "images/EQID/IMG.jpg" "images/EQID/IMG2.jpg" "60%" >}}
```

Pour plus d'exemples, voir [`content/platform-organoid.md`](content/platform-organoid.md) ou [`content/eq4.md`](content/eq4.md).
