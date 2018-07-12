"""A set of utils to work with statistics"""

import numpy as np
import scipy as sp
import scipy.stats

def mean_confidence_interval(data, confidence=0.95, axis=None):
    if not axis:
        axis = 0
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a, axis=axis), scipy.stats.sem(a, axis=axis)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, h

###############################################################################
def mean_confidence_dd(dd, pt, xlen = None, cutok=False):

  if cutok:
    lengths = []
    for d in dd:
      lengths.append(len(d['ts']))
      for p in pt:
        lengths.append(len(d[p]))
    xlen = min(lengths)
    #print('fixing length size to {}'.format(xlen))
  else:
    if not xlen: xlen = len(dd[0]['ts'])

  mc = {}
  for p in pt:
    data = np.empty((xlen, len(dd)))
    for i, d in enumerate(dd):
      data[0:xlen, i] = d[p][0:xlen]
    m, h = mean_confidence_interval(data, axis=1)
    mc[p] = (m, h)
  mc['ts'] = dd[0]['ts']
  return mc