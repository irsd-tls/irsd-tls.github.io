# OpenAlex pour extraire les publications

https://github.com/J535D165/pyalex

## Install OpenAlex

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install pyalex pyyaml
```

## Get publication info for all articles from the IRSD authors

```sh
source venv/bin/activate

python3 update_publications.py

cp pubs.json ../data/
```

# Plus trop utilisés

## Création de pages à partir de la table

```sh
python3 update_people_pages.py
```

## Table avec information des membres

- `people.csv`

# TODO

- ajouter 
    - position alumni fr/en
    - selected DOIs?
    - sous-équipe
