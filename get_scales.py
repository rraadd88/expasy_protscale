from rohan.global_imports import *
lines=open('urls.txt','r').readlines()
methodn2url={s.split(': ')[1]:s.split(': ')[2].replace('\n','') for s in lines}
to_dict(methodn2url,'methodn2url.yml')

methodn2url=read_dict('methodn2url.yml')
from rohan.dandage.io_files import read_url
keys=['Author(s):</B> ',
    'Reference:</B> ',
     'Ala: ',
     'Arg: ',
     'Asn: ',
     'Asp: ',
     'Cys: ',
     'Gln: ',
     'Glu: ',
     'Gly: ',
     'His: ',
     'Ile: ',
     'Leu: ',
     'Lys: ',
     'Met: ',
     'Phe: ',
     'Pro: ',
     'Ser: ',
     'Thr: ',
     'Trp: ',
     'Tyr: ',
     'Val: ',]
from Bio.SeqUtils import IUPACData
def get_protscale(url,test=False):
    if test:
        print(url)
    text=read_url(url)
    lines=text.split('sib_body')[1].split('\\n\\n')
    lines=[s for s in lines for k in keys if k in s]
    d1={}
    for k,s in zip(keys,lines):
        d1[replacemany(k,[':</B> ',': '])]=s.split(k)[1]
    ks=['Author(s)', 'Reference']
    d2={'scale':{IUPACData.protein_letters_3to1[k]:float(d1[k]) for k in d1 if not k in ks}}
    for k in ks:
        d2[k]=d1[k]
    return d2

methodn2scale={k: get_protscale(methodn2url[k])  for k in methodn2url}
methodn2scale['Stickiness']={
'Author(s)':'Emmanuel D. Levy, Subhajyoti De, and Sarah A. Teichmann',
'Reference':'Cellular crowding imposes global constraints on the chemistry and evolution of proteomes (2012)',
'scale':{'A': 0.0062,
'C': 1.0372,
'D': -0.7485,
'E': -0.7893,
'F': 1.2727,
'G': -0.1771,
'H': 0.1204,
'I': 1.1109,
'K': -1.1806,
'L': 0.9138,
'M': 1.0124,
'N': -0.2693,
'P': -0.1799,
'Q': -0.4114,
'R': -0.0876,
'S': 0.1376,
'T': 0.1031,
'V': 0.7599,
'W': 0.7925,
'Y': 0.8806,}
}
to_dict(methodn2scale,'methodn2scale.yml')
