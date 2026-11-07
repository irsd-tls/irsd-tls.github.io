import json
import os
import pyalex
import glob
# https://github.com/J535D165/pyalex
# from utils import Article
import yaml


def read_md_header(filename):
    '''Read the YAML header of a file and return it as a dict'''
    head_content = ''
    with open(filename, 'rt') as inf:
        head_sep_cpt = 0
        for line in inf:
            if line == '---\n':
                head_sep_cpt += 1
                continue
            if head_sep_cpt > 1:
                break
            head_content += line
    return (yaml.load(head_content, Loader=yaml.SafeLoader))


# read openalex api key
# api_key = None
# with open('OPENALEX_API_KEY', 'rt') as inf:
#     api_key = next(inf).rstrip()
# pyalex.config.api_key = api_key

# try to read cache
if not os.path.exists('cache.openalex.json'):
    init_f = open('cache.openalex.json', 'wt')
    init_f.write('{}')
    init_f.close()
with open('cache.openalex.json', 'rt') as cache_inf:
    cache = json.load(cache_inf)
    
# read all markdown files and save some information
# IRSD authors info: oa_id -> team, id
auth_info = {}
# all selected DOIs
sel_dois = set()
# DOIs to show on the team pages: DOI -> set of team IDs
team_sel_dois = {}

# first, read the team/platform pages
md_files = glob.glob('../content/*md')
for mdfn in md_files:
    md_info = read_md_header(mdfn)
    if 'selected_dois' not in md_info:
        continue
    for doi in md_info['selected_dois']:
        if doi == '':
            continue 
        doi = doi.lower()
        sel_dois.add(doi)
        if doi not in team_sel_dois:
            team_sel_dois[doi] = set()
        team_sel_dois[doi].add(md_info['team'])

# then the people pages
md_files = glob.glob('../content/people/*md')
for mdfn in md_files:
    md_info = read_md_header(mdfn)
    if 'oa_id' in md_info and md_info['oa_id'] != '':
        ainfo = {}
        ainfo['team'] = md_info['team']
        ainfo['id'] = mdfn.replace('../content/people/', '')
        if ainfo['id'].endswith('.en.md'):
            ainfo['id'] = ainfo['id'][:-6]
        else:
            ainfo['id'] = ainfo['id'][:-3]
        auth_info[md_info['oa_id'].lower()] = ainfo
    if 'selected_dois' in md_info:
        for doi in md_info['selected_dois']:
            if doi == '':
                continue 
            doi = doi.lower()
            sel_dois.add(doi)

print('{} authors with a OpenAlex ID.'.format(len(auth_info)))
print('{} selected DOIs found in pages.'.format(len(sel_dois)))

# do we need to extract the information about new articles?
new_dois = set()
for doi in sel_dois:
    if 'https://doi.org/' + doi not in cache:
        new_dois.add(doi)
new_dois = list(new_dois)
print('{} selected DOIs not in the cache.'.format(len(new_dois)))
if len(new_dois) > 0:
    print('Querying OpenAlex...')
    print(new_dois)
    while new_dois:
        cur_dois = []
        while new_dois and len(cur_dois) < 10:
            cur_dois.append(new_dois.pop())
        doi_works = pyalex.Works().filter_or(doi=cur_dois).get()
        for ww in doi_works:
            print(ww['doi'])
            cache[ww['doi']] = ww
        cur_dois = []
    # update cache
    with open('cache.openalex.json', 'wt') as cache_outf:
        json.dump(cache, cache_outf)

# make simpler json
excl_types = ['dataset', 'software', 'conference-abstract']
res = []
for doi in cache:
    if doi is None:
        continue
    nb_irsd_auhtors = 0
    work = cache[doi]
    swork = {}
    doi = doi.replace('https://doi.org/', '').lower()
    swork['doi'] = doi
    swork['title'] = work['title']
    # convert special formatting
    swork['title'] = swork['title'].replace('<i>', '*').replace('</i>', '*')
    swork['title'] = swork['title'].replace(' <sub>', '~').replace('</sub>', '~')
    swork['title'] = swork['title'].replace(' <scp>', '').replace('</scp>', '')
    # other informations
    swork['year'] = work['publication_year']
    swork['type'] = work['type']
    swork['journal'] = work['primary_location']['raw_source_name']
    if swork['journal'] is not None:
        swork['journal'] = swork['journal'].replace('&amp;', '&')
    # authors
    auths = []
    for oa_auth in work['authorships']:
        auth = {}
        auth['name'] = oa_auth['author']['display_name']
        oa_id = None
        if oa_auth['author']['id'] is not None:
            oa_id = oa_auth['author']['id'].split('/')[-1]
            oa_id = oa_id.lower()
        if oa_id in auth_info:
            auth['id'] = auth_info[oa_id]['id']
            auth['team'] = auth_info[oa_id]['team']
            nb_irsd_auhtors += 1
        auths.append(auth)
    swork['authors'] = auths
    # selected by a team?
    swork['sel_team'] = []
    if doi in team_sel_dois:
        for team in team_sel_dois[doi]:
            swork['sel_team'].append(team)
    # show selected DOIs, or recent publications or with high citations
    # with at least two IRSD members and after IRSD start
    if (doi in sel_dois or
        (nb_irsd_auhtors > 1 and
         swork['type'] not in excl_types and
         swork['journal'] and
         (swork['year'] > 2020 or
          (swork['year'] >= 2016 and
           work['citation_normalized_percentile'] is not None and
           work['citation_normalized_percentile']['value'] > .95)))):
        res.append(swork)

print('{} publications prepared.'.format(len(res)))

# sort by year
res_o = sorted(res, key=lambda k: -k['year'])

with open('pubs.json', 'wt') as pubs_outf:
    json.dump(res_o, pubs_outf, indent=2)
