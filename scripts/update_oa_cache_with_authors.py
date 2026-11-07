import json
import os
import pyalex
# https://github.com/J535D165/pyalex
# from utils import Article
import glob
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
api_key = None
with open('OPENALEX_API_KEY', 'rt') as inf:
    api_key = next(inf).rstrip()
pyalex.config.api_key = api_key

# try to read cache
if not os.path.exists('cache.openalex.json'):
    init_f = open('cache.openalex.json', 'wt')
    init_f.write('{}')
    init_f.close()
with open('cache.openalex.json', 'rt') as cache_inf:
    cache = json.load(cache_inf)
print('{} articles in the cache.'.format(len(cache)))

# read all markdown files and save some information
# IRSD authors info: oa_id -> name
oa_auth = {}

# read the people pages
md_files = glob.glob('../content/people/*md')
for mdfn in md_files:
    md_info = read_md_header(mdfn)
    if 'oa_id' in md_info and md_info['oa_id'] != '':
        oa_auth[md_info['oa_id'].lower()] = md_info['title']

print('{} authors with a OpenAlex ID.'.format(len(oa_auth)))

print('Querying OpenAlex...')
# for each author, retrieve all publications
for oa_id in oa_auth:
    pager = pyalex.Works().filter(author={"id": oa_id}).paginate(per_page=200)
    auth_dois = []
    for page in pager:
        for ww in page:
            # is this DOI already in the cache?
            auth_dois.append(ww['doi'])
            if ww['doi'] in cache:
                continue
            cache[ww['doi']] = ww
    print('{}: {} dois'.format(oa_auth[oa_id], len(auth_dois)))

# update cache
with open('cache.openalex.json', 'wt') as cache_outf:
    json.dump(cache, cache_outf)

print('{} articles in the cache.'.format(len(cache)))
