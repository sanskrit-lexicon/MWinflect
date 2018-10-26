# -*- coding: utf-8 -*-
""" stem_model.py 
    extract various inflection model information for substantives
    from lexnorm-all2.txt.
"""
import sys,re,codecs
from slp_cmp import slp_cmp
#sys.path.append('../../pysanskrit')
#from sandhi import sandhi_nR
#import decline_3stem
#from decline_util import declension_join

class Lexnorm(object):
 """
  The format of a line of lexnorm.txt is now 4 tab-delimited fields:
  lnum, key1, key2, lexinfo
  And, the lexinfo field has form of 1 or more colon-delimited fields, each
  of which has one of two forms:
  gender OR  gender#ending
 """
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.L,self.key1,self.key2,self.lexnorm) = line.split('\t')
  self.parsed = False

 def toString(self):
  s = '\t'.join([self.L,self.key1,self.key2,self.lexnorm])
  return s

class Model(object):
 d = {}
 def __init__(self,lexrec,modelname,stem,extra=None):
  self.lexrec = lexrec
  self.name = modelname
  self.stem = stem
  self.extra = extra
  key = self.name
  if key not in Model.d:
   Model.d[key] = []
  Model.d[key].append(self)

 def toString(self):
  if self.extra != None:
   s = '\t'.join([self.L,self.model,self.stem,self.extra])
  else:
   s = '\t'.join([self.L,self.model,self.stem])
  return s

def init_lexnorm(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Lexnorm(x) for x in f]
 print(len(recs),"read from",filein)
 return recs

def log_models(modelname,lexnormd,f):
 keys = sorted(lexnormd.keys())
 for key in keys:
  out = '%05d %s %s' %(lexnormd[key],key,modelname)
  f.write(out +'\n')

def model_ind(recs,flog):
 d = {}
 for rec in recs:
  if rec.lexnorm != 'ind':
   continue
  rec.parsed = True
  model = 'ind'
  stem = rec.key2
  rec.model = Model(rec,model,stem)
  if rec.lexnorm not in d:
   d[rec.lexnorm] = 0
  d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_ind',d,flog)

def model_m_a(recs,flog):
 endchar = 'a'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m']
  lexparts = rec.lexnorm.split(':')
  if not lexparts == knownparts:
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'm_a'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_m_a',d,flog)

def model_n_a(recs,flog):
 endchar = 'a'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['n']
  lexparts = rec.lexnorm.split(':')
  if not lexparts == knownparts:
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'n_a'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_n_a',d,flog)

def model_f_A(recs,flog):
 endchar = 'A'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f','f#A']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_A'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_A',d,flog)

def model_f_I(recs,flog):
 endchar = 'I'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f','f#I']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_I'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_I',d,flog)

def model_f_U(recs,flog):
 endchar = 'U'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f','f#U']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_U'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_U',d,flog)

def model_m_i(recs,flog):
 endchar = 'i'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'm_i'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_m_i',d,flog)

def model_f_i(recs,flog):
 endchar = 'i'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_i'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_i',d,flog)

def model_n_i(recs,flog):
 endchar = 'i'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['n']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'n_i'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_n_i',d,flog)

def model_m_u(recs,flog):
 endchar = 'u'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'm_u'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_m_u',d,flog)

def model_f_u(recs,flog):
 endchar = 'u'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['f']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'f_u'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_f_u',d,flog)

def model_n_u(recs,flog):
 endchar = 'u'
 d = {}
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['n']
  lexparts = rec.lexnorm.split(':')
  if set(lexparts) != set(knownparts):
   continue
  rec.parsed = True
  for part in lexparts:
   mstem = stem
   model = 'n_u'
   rec.model = Model(rec,model,mstem)
   if rec.lexnorm not in d:
    d[rec.lexnorm] = 0
   d[rec.lexnorm] = d[rec.lexnorm]+1
 log_models('model_n_u',d,flog)

def model_mfn_a(recs,flog):
 endchar = 'a'
 nparsed = 0
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  if rec.parsed:
   # this record has been previously parsed
   continue
  knownparts = ['m','f','n']
  lexparts = rec.lexnorm.split(':')
  if not lexparts == knownparts:
   continue
  rec.parsed = True
  nparsed = nparsed + 1
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_a, n_a
   elif part in ['f']:
    mstem = stem[0:-1] + 'A'  # deva -> devA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   else:
    print('mfn_a Internal error',part)
    exit(1)
   rec.model = Model(rec,model,mstem)
 print(nparsed,"records parsed in model_mfn_a")

def model_mfn_a1(recs,flog):
 endchar = 'a'
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  lexparts = rec.lexnorm.split(':')
  knownparts = ['m','f','n','f#A','f#I','f#akA','f#ikA',
                'f#enI','f#apI','f#apyA', 'f#sI',
                'f#iknI','f#ArI','f#AvI','f#enikA','f#vI',
                'f#padI','f#i','f#u','f#IkA', 'f#tyA','f#yanI',
                'f#iRI','f#inI','f#inikA','f#arI','f#rI',
                'f#sOrI','f#U', 'f#stI',
                'ind#am','ind']
  if not set(lexparts).issubset(set(knownparts)):
   continue
  if lexparts == ['ind']:
   # these are handled in model_ind
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)   #m_a, n_a
   elif part in ['f','f#A']:
    mstem = stem[0:-1] + 'A'  # deva -> devA
    mpart = 'f'
    model = '%s_%s' %(mpart,'A')
   elif part in ['f#I']:
    mstem = stem[0:-1] + 'I'  # akeSa -> akeSI
    mpart = 'f'
    model = '%s_%s' %(mpart,'I')
   elif part in ['f#akA','f#ikA']:
    newend = part[2:]
    if stem.endswith(('aka','ika')):
     mstem = stem[0:-3] + newend  #  replace final aka/ika with akA or ikA
     mpart = 'f'
     model = '%s_%s' %(mpart,'A')
    else:
     mstem = stem[0:-1] + newend # replace final a with akA or ikA
     print('mfn_a warning:',rec.key1,rec.lexnorm,mstem)
     mpart = 'f'
     model = '%s_%s' %(mpart,'A')
   elif part in ['f#enI']:
    ending = part[2:]
    assert stem.endswith('eta')
    mstem = stem[0:-3] + ending
    model = 'f_I'
   elif part in ['f#apI','f#apyA']:
    ending = part[2:]
    assert stem.endswith('apya')
    mstem = ending
    model = 'f_%s' %ending[-1]
   elif part in ['f#sI']:
    ending = part[2:]
    assert stem == 'apasya'
    mstem = stem[0:-3] + ending
    model = 'f_I'
   elif part in ['f#iknI']:
    ending = part[2:]
    assert stem in ['asita','palita']
    mstem = stem[0:-3] + ending # replace 'ita' with 'iknI'
    model = 'f_I'
   elif part in ['f#ArI']:
    ending = part[2:]
    assert stem == 'Arya'
    mstem = ending
    model = 'f_I'
   elif part in ['f#AvI']:
    ending = part[2:]
    assert stem == 'Avya'
    mstem = ending
    model = 'f_I'
   elif part in ['f#enikA']:
    ending = part[2:]
    assert stem == 'etaka'
    mstem = ending
    model = 'f_A'
   elif part in ['f#vI']:
    ending = part[2:]
    assert stem == 'Ekalavya'
    mstem = stem[0:-3] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#padI']:
    ending = part[2:]
    assert stem in ['kumBa-pAda','dru-pAda']
    mstem = stem[0:-4] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#i']:
    ending = part[2:]
    mstem = stem[0:-1] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#u']:
    ending = part[2:]
    mstem = stem[0:-1] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#U']:
    assert stem == 'svana'
    ending = part[2:]
    mstem = stem[0:-1] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#IkA']:
    assert stem == 'KuqqAka'
    ending = part[2:]
    mstem = stem[0:-3] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#tyA']:
    assert stem in ['cEkayata','bElvayata']
    ending = part[2:]
    mstem = stem[0:-2] + ending
    model = 'f_%s' % ending[-1]
   elif part in ['f#yanI']:
    assert stem in ['brADnAyanya']
    ending = part[2:]
    mstem = stem[0:-5] + ending # replace yanya with yanI
    model = 'f_%s' % ending[-1]
   elif part in ['f#iRI']:
    assert stem in ['Barita','rohita','Sukla-harita','harita']
    ending = part[2:]
    mstem = stem[0:-3] + ending # replace ita with iRI
    model = 'f_%s' % ending[-1]
   elif part in ['f#inI']:
    # what about compounds ending with lohita ?
    assert stem in ['lohita']
    ending = part[2:]
    mstem = stem[0:-3] + ending # replace ita with inI
    model = 'f_%s' % ending[-1]
   elif part in ['f#inikA']:
    # what about compounds ending with lohita ?
    assert stem in ['lohitaka']
    ending = part[2:]
    mstem = stem[0:-5] + ending # replace itaka with inikA
    model = 'f_%s' % ending[-1]
   elif part in ['f#arI']:
    assert stem in ['vi-BAva']
    ending = part[2:]
    mstem = stem[0:-1] + ending # replace final 'a' with arI
    model = 'f_%s' % ending[-1]
   elif part in ['f#rI']:
    assert stem in ['vEdUrya']
    ending = part[2:]
    mstem = stem[0:-3] + ending # replace final 'rya' with rI
    model = 'f_%s' % ending[-1]
   elif part in ['f#sOrI']:
    assert stem in ['sOrya']
    ending = part[2:]
    mstem = ending 
    model = 'f_%s' % ending[-1]
   elif part in ['f#stI']:
    assert stem in ['Agastya']
    ending = part[2:]
    mstem = stem[0:-4] + ending # replace final 'stya' with stI
    model = 'f_%s' % ending[-1]
   elif part in ['ind#am']:
    assert stem in ['nada','muKa','sAkzika']
    ending = part[4:]  # am
    mstem = stem[0:-1] + ending # replace final 'a' with 'am'
    model = 'ind'
   elif part in ['ind']:
    if stem not in ['ka','tIra','tUla','paSca']:
     print 'mfn_a  unexpected "ind"',stem
    mstem = stem
    model = 'ind'
   else:
    print('mfn_a Internal error',part)
    exit(1)
   rec.model = Model(rec,model,mstem)

def model_mfn_i(recs,flog):
 endchar = 'i'
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  lexparts = rec.lexnorm.split(':')
  knownparts = ['m','f','n','f#I',
                'f#i', # redundant. Could replace with 'f'
                'f#is','f#tnI','f#yA','f#A','f#ikA','ind','f#tinI']
  if not set(lexparts).issubset(set(knownparts)):
   continue
  if lexparts == ['ind']:
   # these are handled in model_ind
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)  
   elif part in ['f#I']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'I'
    mpart = 'f_%s' %ending
   elif part in ['f#i']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'i'  (same as 'f')
    mpart = 'f_%s' %ending
   elif part in ['f#is']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'is'
    mpart = 'f_%s' %ending
   elif part in ['f#A']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'A'
    mpart = 'f_%s' %ending
   elif part in ['f#ikA']:
    ending = part[2:]
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'ikA'
    mpart = 'f_%s' %ending[-1]
   elif part in ['f#tnI']:
    ending = part[2:]
    assert stem.endswith('pati')
    mstem = stem[0:-2] + ending  # replace ending 'ti' with 'tnI'
    mpart = 'f_%s' %ending[-1]
   elif part in ['f#tinI']:
    ending = part[2:]
    assert stem == 'prati-prati'
    mstem = stem[0:-2] + ending  # replace ending 'ti' with 'tinI'
    mpart = 'f_%s' %ending[-1]
   elif part in ['ind']:
    assert stem in ['vazaw-kfti']
    mstem = stem
    mpart = 'ind'
   elif part in ['f#yA']:
    ending = part[2:]
    # question this in dEva-yajYi. WOuld give dEva-yajYyA Right? Yes acc. to pwg
    mstem = stem[0:-1] + ending  # replace ending 'i' with 'yA'
    mpart = 'f_%s' %ending[-1]
   else:
    print('mfn_i internal ERROR',part)
    exit(1)
   rec.model = Model(rec,model,mstem)

def model_mfn_u(recs,flog):
 endchar = 'u'
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  lexparts = rec.lexnorm.split(':')
  knownparts = ['m','f','n','f#U','f#u','f#vI',
                'f#pUrvI','f#I','f#us','f#Us','ind']
  if not set(lexparts).issubset(set(knownparts)):
   continue
  if lexparts == ['ind']:
   # these are handled in model_ind
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar)  
   elif part in ['f#U']:
    mstem = stem[0:-1] + 'U'  # replace ending 'u' with 'U'
    mpart = 'f'
    model = '%s_%s' %(mpart,'U')
   elif part in ['f#u']:
    mstem = stem
    mpart = 'f'
    model = '%s_%s' %(mpart,'u')
   elif part in ['f#vI']:
    mstem = stem[0:-1] + 'vI'  # replace final 'u' with 'vI'
    model = 'f_I'
   elif part in ['f#pUrvI']:
    assert stem == 'puru'
    ending = part[2:]
    mstem = ending
    model = 'f_%s' %ending[-1]
   elif part in ['f#I']:
    assert stem == 'SASabindu'
    ending = part[2:]
    mstem = stem[0:-1]+ending  # replace final 'u' with 'I'
    model = 'f_%s' %ending[-1]
   elif part in ['f#us']:
    assert stem in ['an-uru','kawu','cAru','tanu']
    ending = part[2:]
    mstem = stem[0:-1]+ending  # replace final 'u' with 'us'
    model = 'f_us'  # how to decline? 10-10-2018
   elif part in ['f#Us']:
    assert stem in ['asita-jYu','kamaRqalu','kaSeru','guggulu','guNgu',
                   'jatu','tanu']
    ending = part[2:]
    mstem = stem[0:-1]+ending  # replace final 'u' with 'Us'
    model = 'f_Us'  # how to decline? 10-10-2018
   elif part in ['ind']:
    assert stem in ['yuvAku']
    mstem = stem
    model = 'ind'
   else:
    print('mfn_u. Internal error',part)
    exit(1)
   rec.model = Model(rec,model,mstem)

def model_f_AIU(recs,flog):
 endchars = ['A','I','U']
 for rec in recs:
  stem = rec.key2
  endchar = stem[-1]
  if not endchar in endchars:
   continue
  lexparts = rec.lexnorm.split(':')
  if lexparts != ['f']:
   continue
  rec.parsed = True
  mstem = stem
  mpart = 'f'
  model = '%s_%s' %(mpart,endchar)  
  rec.model = Model(rec,model,mstem)

def model_mfn_in(recs,flog):
 ending = 'in'
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(ending):
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(['m','f','n','f#inI','f#iRI'])):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)  
   elif part == 'f':
    # must decide stem using sandhi
    stemparts = stem.split('-')
    lastpart = stemparts[-1]
    firstparts = stemparts[0:-1]  # empty list if no '-' in stem
    firstpart = '-'.join(firstparts)
    lastpart1 = lastpart + 'I'
    lastpart2a = sandhi_nR(lastpart1)
    # lastpart2 is empty if no change
    if lastpart2a == None:
     lastpart2 = lastpart1
    else:
     lastpart2 = lastpart2a
    # lastpart2 used in new stem
    if firstpart == '':
     mstem = lastpart2
    else:
     mstem = firstpart + '-' + lastpart2
    #if lastpart2a != None:  # debugging
    # print('chk:',stem,"->",mstem)
    # model is f_in_I  (which is same as f_I)
    model = 'f_in_I'
    #rec.model = Model(rec,model,mstem)
   elif part in ['f#inI','f#iRI']:
    ending1 = part[2:] # inI or iRI
    mstem = stem[0:-2] + ending1  # replace ending 'in' 
    mpart = 'f'
    model = 'f_in_I' # '%s_%s' %(mpart,'I')
   else:
    print('model_in Internal error',part)
    exit(1)
   rec.model = Model(rec,model,mstem)

endings_Iyas = ('Iyas', 'jyAyas','Sreyas','preyas','BUyas')

def model_Iyas(recs,flog):
 """ comparative adjectives in Iyas """

 ending = 'Iyas'
 for rec in recs:
  stem = rec.key2
  found = False
  if not stem.endswith(endings_Iyas):
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(['m','f','n'])):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)  
   elif part == 'f':
    # feminine stem add 'I' to weak stem.
    # the weak stem is just stem
    mstem = stem + 'I'
    model = 'f_Iyas_I'
   rec.model = Model(rec,model,mstem)

def model_vat(recs,flog):
 # key2 ends with '-vat'
 ending = 'vat'
 ending1 = '-' + ending
 knownparts = ['m','f','n','f#atI','ind','f#antI','f#atnI']
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(ending1):
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  if lexparts == ['ind']:
   # these are handled in model_ind
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)    
   elif part == 'f':
    # add 'I' to stem
    mstem = stem + 'I'
    model = 'f_I'  # normal feminine ending in 'I'
    rec.model = Model(rec,model,mstem)
   elif part == 'f#atI':
    mstem = stem + 'I'
    model = 'f_I'  # normal feminine ending in 'I'
    rec.model = Model(rec,model,mstem)
   elif part == 'f#antI':
    mstem = stem[0:-2]+'antI'  # replace ending 'at' with 'antI'
    model = 'f_I'  # normal feminine ending in 'I'
    rec.model = Model(rec,model,mstem)
   elif part == 'f#atnI':
    assert stem in ['antar-vat']
    mstem = stem[0:-2]+'atnI'  # replace ending 'at' with 'atnI'
    model = 'f_I'  # normal feminine ending in 'I'
    rec.model = Model(rec,model,mstem)
   elif part in ['ind']:
    if stem not in ['harza-vat']:
     print 'mfn_a  unexpected "ind"',stem
    mstem = stem
    model = 'ind'
   else:
    print('mfn_vat Internal error',part)
    exit(1)
   rec.model = Model(rec,model,mstem)

def model_mat(recs,flog):
 # key2 ends with '-mat'
 ending = 'mat'
 ending1 = '-' + ending
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(ending1):
   continue
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(['m','f','n'])):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)    
   elif part == 'f':
    # add 'I' to stem
    mstem = stem + 'I'
    model = 'f_I'  # normal feminine ending in 'I'
    rec.model = Model(rec,model,mstem)
   rec.model = Model(rec,model,mstem)

def model_an(recs,flog):
 # key2 ends with 'an'
 ending = 'an'
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(ending):
   continue
  # For adjectives ending in 'an', the feminine stem is formed by adding
  # 'I' to the weak stem.  We recognize such 'adjectives' by
  # lexnorm == 'm:f:n'
  # Otherwise, the feminine is declined like a masculine ending in 'an'.
  # In fact, the only example of this feminine is sIman (Deshpande, Kale)
  # and we restrict to the (5) words of MW ending in sIman
  lexparts = rec.lexnorm.split(':')
  knownparts =['m','f','n','f#GnI','f#mnI','f#jYI','f#arI','f#varI',
               'f#rzRI','f#SIrzRI','f#zRI', 'f#DnI', 'f#jA', 'f#haRI',
               'f#hnI','f#mRI','ind','f#yUnI','f#yuvatI','f#yuvati']
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,ending)    
   elif part == 'f':
    if stem.endswith('sIman'):
     #Use f_an model, which is like m_an
     mstem = stem
     model = '%s_%s' %(part,ending)    
    else:
     # add 'I' to **weak** stem
     (s,m,w) = decline_3stem.stems_an(stem)
     # in my version of strong, middle, weak, we actually add 'nI' to weak
     mstem = declension_join(w,'nI')
     # Correct one issue with declension join: It changes m-nI to M-ni
     mstem = re.sub(r'M([nR])I$',r'm\1I',mstem)
     model = 'f_an_I'  # normal feminine ending in 'I'
   elif part == 'f#GnI':
    assert stem.endswith('han')
    mstem = stem[0:-3] + 'GnI'
    model = 'f_an_I'
   elif part == 'f#haRI':
    assert stem.endswith('han')
    mstem = stem[0:-1] + 'RI' # replace final 'n' with 'RI'
    model = 'f_an_I'
   elif part == 'f#hnI':
    assert stem.endswith('han')
    mstem = stem[0:-3] + 'hnI'
    model = 'f_an_I'
   elif part == 'f#mnI':
    assert stem.endswith('man')
    mstem = stem[0:-3] + 'mnI'
    model = 'f_an_I'
   elif part == 'f#jYI':
    assert stem.endswith('rAjan')
    mstem = stem[0:-3] + 'jYI'
    model = 'f_an_I'
   elif part == 'f#jA':
    assert stem.endswith('rAjan')
    mstem = stem[0:-2] + 'A'  # replace final 'an' with 'A'
    model = 'f_A'  # count as normal f_A model
   elif part in ['f#arI','f#varI']:
    assert stem.endswith('van')
    mstem = stem[0:-2] + 'arI' # replace final 'an' with 'arI'
    model = 'f_an_I'
   elif part in ['f#rzRI','f#SIrzRI','f#zRI']:
    assert stem.endswith('SIrzan')
    mstem = stem[0:-2] + 'RI'  # replace final 'an' with 'RI'
   elif part == 'f#DnI':
    assert stem.endswith('Dan')
    mstem = stem[0:-2] + 'nI' # replace final 'an' with 'nI'
    model = 'f_an_I'
   elif part == 'f#mRI':
    assert stem.endswith('zAman')
    mstem = stem[0:-3] + 'mRI'
    model = 'f_an_I'
   elif part == 'ind':
    if stem not in ('pari-jman','tman'):
     print('skipping',rec.key1,rec.lexnorm)
     continue
    mstem = stem
    model = 'ind'
   elif part in ['f#yUnI','f#yuvatI','f#yuvati']:
    assert stem == 'yuvan'
    mstem = part
    model = 'f_I'  
   else:
    print('model_an internal ERROR',part)
    exit(1)
   rec.model = Model(rec,model,mstem)

def model_pron(recs,flog):
 for rec in recs:
  m = re.search(r'^LEXID=pron,STEM=(.*)$',rec.lexnorm)
  if not m:
   continue
  stem = m.group(1)
  # one exception
  # for L=40112, hw = 'ena', stem is given as 'idam,etad' in lexnorma-all2.txt
  # we change this to 'idam'
  if stem == 'idam,etad':
   stem = 'idam'
   print('change pronoun stem from "idam,etad" to "idam"')
  if stem in ['asmad','yuzmad']:
   # These have no gender.  Assume gender = 'm' for convenience
   lexparts = ['m']  
  else:
   lexparts = ['m','n','f']
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,'pron')  
   else:
    print('model_pron internal ERROR')
    exit(1)
   rec.model = Model(rec,model,mstem)

def model_card(recs,flog):
 for rec in recs:
  m = re.search(r'^LEXID=card,STEM=(.*)$',rec.lexnorm)
  if not m:
   continue
  stem = m.group(1)
  if stem in ['eka','dvi','tri','catur']:
   lexparts = ['m','n','f']
  elif stem.endswith('i'):
   lexparts = ['f']
  elif stem.endswith('t'):
   lexparts = ['f']
  elif stem in ['Sata','sahasra']:
   lexparts = ['m','n']  # Deshpande only neuter
  else:
   # These have no gender.  Assume gender = 'm' for convenience
   lexparts = ['m']  
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,'card')  
   else:
    print('model_card internal ERROR')
    exit(1)
   rec.model = Model(rec,model,mstem)

def model_mfn_f(recs,flog):
 endchar = 'f'
 for rec in recs:
  stem = rec.key2
  if not stem.endswith(endchar):
   continue
  knownparts = ['m','f','n','f#trI','f#attrI','f#zwrI','f#rI','f#wrI',
            'f#yantrI','f#sanutrI','f#A','f#metA','f#I','f#f']
  lexparts = rec.lexnorm.split(':')
  if not set(lexparts).issubset(set(knownparts)):
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_%s' %(part,endchar) 
   elif part in ['f#trI','f#attrI','f#zwrI','f#rI','f#wrI','f#yantrI','f#sanutrI','f#I']:
    # remove final 'f' and replace with 'rI'
    mstem = stem[0:-1] + 'rI'
    model = 'f_I'
   elif part == 'f#I':
    assert stem in ['varDayitf']
    # Not sure. Assume replace final 'f' with 'rI'
    mstem = stem[0:-1] + 'rI'
    model = 'f_I'
   elif part == 'f#A':
    assert stem in ['manotf','su-ketf']
    # replace final 'f' with 'A'
    mstem = stem[0:-1] + 'A'
    model = 'f_A'
   elif part == 'f#metA':
    assert stem in ['metf']
    # replace final 'f' with 'A'
    mstem = stem[0:-1] + 'A'
    model = 'f_A'
   elif part == 'f#f':
    if stem not in ['saptasvasf']:
     print('model_mfn_f ERROR "f#f"',stem,rec.lexnorm)
    assert stem in ['sapta-svasf']
    # Not sure. assume no change
    mstem = stem
    model = 'f_f'
   else:
    print('model_mfn_f internal ERROR',stem,part)
    exit(1)
   rec.model = Model(rec,model,mstem)

known_1stems_list = [
 # palatal final from Deshpande
 'vAc','samrAj','viS','fc','tvac','Suc''vaRij','BiSaj','ftvij',
   'parivrAj','diS',
 # cerebral from Kale
 'gaR', # su-gaR from Kale.
 
 'parAR','prAR', # mw.txt
 # dental final from Deshpande
 'marut','sarit','jagat', 'BUBft', 'vidyut',
 'suhfd','Apad','sampad','parizad','viyat','kzuD',
 # dental final from Antoine
 'udBid','samiD',
 # ending in 'D' from mw headwords
 'agniD','agnID','kruD','ruD','vfD','buD','yuD','sriD','baD','bAD',
 'vIruD','iziD','ziD','spfD','pfkzuD','viD','mfD','sAD','guD','SuruD',
 'fD','spfD','srid','zamiD',
 # ending in 'd' from mw headwords
 'vid','pad','sad','zad','pAd','Bid','rud','kakud','kAkud','mud','SArad','nud',
 'samad','cCid','cCad','Cad','Cid','hfd','mfd','dad',
 # labial final from Antoine
 'kakuB',
 # r final
 'gir','dvAr','pur','Dur',
 # other r final from mw.txt
 'aNgir','jur','sPur','aptur','mur','svar','stir','dir','kir','ASir',
 'CidrAntar','jUr','tUr','dur','wur','Sar','yantur',
 'vaDar','vanDur','zwir','sabar',
 # ahar (a day) -- this is irregular
 'gur','tur',
 # l final - from mw
 'anekAl','SIl','hal',
 # cerebral final from Antoine
 'vfz','dviz', # prAvfz
 # cerebral z-final from mw
 'juz','tviz','iz','ruz','ukz','pfkz','muz','miz','susUz',
 'pruz','Sriz','akz','tfz','uz','kfz','viz','puz','kavaz',
 'Dfz','takz','rakz','camriz','cikIrz','tfz','diDakz','diDikz',
 'Sliz','Suz','pipakz','pipaWiz','makz','mUz','BAz','riz','roz','rez',
 'rohiz','rOhiz','prez','pluz','vivikz',
 # S final from mw.txt
 'spfS','dfS','IS','diS','naS','niS','qAS','LAS',
 'paS','piS','prAS','arRaS','yakzeS','liS','pAS','spaS',
 'zpaS','vriS','dAS','DaneS',
 # s-final from Deshpande
 'candramas', 'veDas','payas','uras',
 'sumanas','yaSas','havis','Ayus',
 'manas','cetas','uzas','tamas','vayas','tapas','cakzus','Danus',
 'jyotis','havis',
 # s-final from Antoine
 'tejas','Siras','sadas',
 # probable s-final 1-stems affixes from mw . These end in 'vas'
  'javas','dASvas','Savas','Sravas','Cravas','yavas','avas','Ayavas',
  'fBvas','cyavas','javas','juvas','tavas',
  'duvas','Dvas','ravas','tavas','Baktivas','sravas','BUvas',
  'Sikvas','savas','prasavas','sAhvas','pIvas','vas',
  'Sevas','sravas','avas','havas','hftsvas',
 # additional s-final 1-stem affixes from mw - don't end in 'vas'
  'cCandas','Candas','apas','vAsas','srotas','anDas','okas','ojas',
  'meDas','rajas','rakzas','rahas','retas',
 # h final from Antoine
 'maDulih','upAnah','kamaduh',
 
]
known_1stems = set(known_1stems_list)

def model_1stem(recs,flog):
 for rec in recs:
  stem = rec.key2
  # logic to determine whether stem ends in a consonant
  # and is declined with 1 stem.
  found = False
  if stem in known_1stems:
   found = True
  elif '-' in stem:
   m = re.search(r'^.*-([^-]*)$',stem)
   if m:
    # require that stem ends with '-X' where X is a known 1-stem noun
    if m.group(1) in known_1stems:
     found = True
  if not found:
   # other tests
   if stem.endswith(('k','K','g','G')):
    found = True
   elif stem.endswith('ac'):
    if stem not in ['ud-ac','dakziRA-pratyac','deva-dryac']:
     # these three are like 'aYc' direction adjectives, not 1-stem
     found = True
   elif stem.endswith('c') and not stem.endswith('Yc'):
    # exclude direction adjectives
    found = True
   elif stem.endswith(('C','j','J')):
    found = True
   elif stem.endswith(('w','W','q','Q')):
    found = True
   elif re.search(r'[^a]t$',stem):
    # must exclude stems ending in 'at', as some are pr. active participles
    found = True  
   elif stem.endswith(('T','d','D')):
    # things like 'yuzmad' will be excluded by lexnorm test below
    found = True
   elif stem.endswith(('p','P','b','B')):
    found = True
   elif stem.endswith(('is','us')):
    found = True
   elif stem.endswith('kas'):  
    # 45. Okas, and aNkas
    found = True
   elif stem.endswith(('kas','Kas','gas','Gas')):  
    # 45. Okas, and aNkas
    # 13. gas  (various)
    # 1.  Kas (sadmamaKas)
    # 3   Gas
    found = True
   elif stem.endswith(('cas','Cas','jas','Jas')):
    # cas:  93 (varcas, vacas, vyacas, etc.)
    # jas:  66 (pAjas, 'Ojas', etc.)
    found = True
   elif stem.endswith(('was','Was','qas','Qas','Ras')):
    # qas:   1 (heqas)
    # Ras:  24 (arRas, draviRas, etc.)
    found = True
   elif stem.endswith(('tas','Tas','das','Das','nas')):
    # tas:  12 (cetas, Srotas, etc.)
    # Tas:   6 (praTas, pATas)
    # das:  33 (vedas, medas, etc.)
    # Das:  63 (rADas, UDas, etc.)
    # nas:  43  (nas (nose), enas, etc.)
    found = True
   elif stem.endswith(('pas','Pas','bas','Bas','mas')):
    # pas:  25 (vepas, varpas,Apas, etc.)
    # Pas:   5 (SePas, rePas, varPas)
    # bas:   0 
    # Bas:  42 (amBas, naBas, raBas, etc.)
    # mas:   4 (candramas, namas)
    found = True
   # yas - excluding comparatives in Iyas
   elif stem.endswith(endings_Iyas):
    found = False
   elif stem.endswith('yas'):
    #   (gAyas,vasyas, hAyas, DAyas, etc.)
    found = True
    #print('check ..yas stem1',stem)
   elif stem.endswith('ras'):
    # 101  (saras, aNgiras, haras, jaras, taras, etc.
    found = True
   elif stem.endswith('las'):
    #   3  (las, calas)
    found = True
   elif stem.endswith('zas'):
    #   67  (cakzas, vakzas, dakzas, etc.
    found = True
   elif stem.endswith('Sas'):
    #   39  (Sas, peSas, etc.)
    found = True
   elif stem.endswith('sas'):
    #   17  (apsas, daMsas
    found = True
   elif stem.endswith('has'):
    #   62  (aMhas, raMhas, barhas, etc.)
    found = True
   elif stem.endswith('h'):
    found = True
  if not found:
   # record not recognized as a 1-stem noun
   continue
  lexparts = rec.lexnorm.split(':')
  knownparts = ['m','f','n','ind',
                'f#A','f#padI','f#I','f#AcI','f#AdI','f#AtI','f#AntI',
                'ind#Sam',
                'f#ryOhI','f#BArOhI','f#viSvOhI','f#SAlyUhI']
  if not set(lexparts).issubset(set(knownparts)):
   # we don't know how to handle the extra lex information yet
   print("model_1stem skipping:",stem,rec.lexnorm)
   continue
  if lexparts == ['ind']:
   # handled in model_ind
   continue
  rec.parsed = True
  for part in lexparts:
   if part in ['m','n','f']:
    # stem is unchanged
    mstem = stem
    model = '%s_1stem' %part
   elif part == 'ind':
    mstem = stem
    model = 'ind'
   elif part == 'f#A':
    assert stem in ['an-apa-sPur']
    mstem = stem + 'A'
    model = 'f_A'
   elif part == 'f#padI':
    assert stem.endswith('pad')
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'f#AdI':
    assert stem == 'Sata-pAd'
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'f#AtI':
    assert stem == 'ni-drAt'
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'f#AntI':
    assert stem == 'ni-drAt'
    mstem = 'ni-drAntI'
    model = 'f_I'
   elif part == 'f#I':
    assert stem.endswith(('pad','dfS','mah'))
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'f#AcI':
    assert stem in ['devAc','satrAc']
    mstem = stem + 'I'
    model = 'f_I'
   elif part == 'ind#Sam':
    assert stem == 'vi-pAS'
    mstem = stem + 'am'
    model = 'ind'
   elif part == 'f#ryOhI':
    assert stem == 'turya-vah'
    mstem = 'turyOhI'
    model = 'f_I'
   elif part == 'f#BArOhI':
    assert stem == 'BAra-vah'
    mstem = 'BArOhI'
    model = 'f_I'
   elif part == 'f#viSvOhI':
    assert stem == 'viSva-vah'
    mstem = 'viSvOhI'
    model = 'f_I'
   elif part == 'f#SAlyUhI':
    assert stem == 'SAli-vah'
    mstem = 'SAlyUhI'
    model = 'f_I'
   else:
    print('model_1stem internal ERROR')
    exit(1)
   rec.model = Model(rec,model,mstem)

def lexnorm_todo(recs,flog):
 """ not yet parsed """
 fileout = "temp_lexnorm_todo.txt"
 f = codecs.open(fileout,"w","utf-8")
 nout =0 
 for rec in recs:
  if rec.parsed:
   continue
  out = rec.toString()
  f.write(out + '\n')
  nout = nout + 1
 f.close()
 print(nout,fileout)

def model_stem_string(mrecs):
 """ model is list of Model instances, all of which
   have same model-name and stem
 """
 outarr = []
 mrec = mrecs[0]
 name = mrec.name  # model name
 outarr.append(name)
 outarr.append(mrec.stem)
 # get all the L-numbers
 Larr = [(mrec.lexrec.L,mrec.lexrec.key1) for mrec in mrecs]
 Larr = sorted(Larr,key = lambda x : float(x[0]))  # in L order
 Larr1 = ['%s,%s'%mrec for mrec in Larr]
 Larrstr = ':'.join(Larr1)
 outarr.append(Larrstr)
 out = '\t'.join(outarr)
 return out

def adjust_case(x):
 """ change uppercase letters X to x1  
 """
 def f(m):
  # A -> a1,  U -> u1, etc.
  u = m.group(0)
  v = u.lower()
  return v+'1'
 y = re.sub(r'[A-Z]',f,x)
 return y

def write_model_instances(modelname,instances):
 fileout = "%s.txt" % modelname
 # change uppercase letters since windows file system is case insensitive
 fileout = adjust_case(fileout)
 f = codecs.open(fileout,"w","utf-8")
 # instances is array of Model records
 # group by stem
 e = {}
 for mrec in instances:
  k = mrec.stem
  if k not in e:
   e[k] = []
  e[k].append(mrec)
 stems = e.keys()  # all stems for this model
 stems = sorted(stems, cmp=slp_cmp)
 nout = 0
 ntot = 0
 for stem in stems:
  mrecs = e[stem]  
  ntot = ntot + len(mrecs)
  # each item in mrecs is a Model instance
  # All items in mrecs has same value for (a)(model) name and (b) stem
  out = model_stem_string(mrecs)
  nout = nout + 1
  f.write(out + '\n')
 f.close()
 print(nout,"written to",fileout," (%s)"%ntot)

def write_models():
 d = Model.d
 models = d.keys()
 for model in models:
  write_model_instances(model,d[model])

def lexnorm_todo(recs,flog):
 fileout = 'temp_lexnorm_todo.txt'
 f = codecs.open(fileout,"w","utf-8")
 nout = 0
 for rec in recs:
  if rec.parsed:
   continue
  # print unparsed record
  nout = nout + 1
  out = rec.toString()
  f.write(out + '\n')
 f.close()
 print(nout,"written to",fileout)

if __name__ == "__main__":
 filein = sys.argv[1] # lexnorm-all2
 flog = codecs.open('stem_model_log.txt',"w","utf-8")
 recs = init_lexnorm(filein)
 model_ind(recs,flog)
 model_m_a(recs,flog)
 model_n_a(recs,flog)
 model_f_A(recs,flog)
 model_f_I(recs,flog)
 model_f_U(recs,flog)
 model_m_i(recs,flog)
 model_f_i(recs,flog)
 model_n_i(recs,flog)

 model_m_u(recs,flog)
 model_f_u(recs,flog)
 #model_n_u(recs,flog)
 #model_mfn_a(recs,flog)
 #model_mfn_a1(recs,flog)
 #model_mfn_u(recs,flog)
 #model_mfn_i(recs,flog)
 #model_f_AIU(recs,flog)
 #model_mfn_in(recs,flog)
 #model_mfn_f(recs,flog)
 #model_pron(recs,flog)
 #model_card(recs,flog)
 #model_vat(recs,flog)  #  -vat
 #model_mat(recs,flog)  #  -mat
 #model_an(recs,flog)
 #model_Iyas(recs,flog)
 #model_1stem(recs,flog)
 write_models()
 lexnorm_todo(recs,flog)
 exit(1)
 vas_1stems = [
 ]
 # 'vi-vikvas'
 # redups endings
 # probable reduplicated perfect active participle in 'vas'
 vas_redups = ['cakfvas','jaGnivas','vidvas','papivas',
               'biBIvas','upeyivas','Iyivas','udeyivas','pareyivas',
               'cikitvas','jakzivas','jaganvas','jagmivas',
               'jaGanvas','jajYivas','jAgfvas','tasTivas',
               'pIpivas','SiSrivas','SuSruvas','vavftvas',
               'sAsahvas','suzupvas',
              ]
 # Another type of participle. How declined?
 vas_others = ['okivas','Kidvas','caKvas','jUjuvas','pIvas','mIQvas',
               'SaMsivas',
               'prozivas', 'rarivas', 'saScivas','darSivas',
               'sedivas',
              ]
