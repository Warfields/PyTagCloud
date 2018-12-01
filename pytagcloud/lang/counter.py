# -*- coding: utf-8 -*-
import re
from pytagcloud.lang.stopwords import StopWords
from operator import itemgetter

def get_tag_counts(text):
    """
    Search tags in a given text. The language detection is based on stop lists.
    This implementation is inspired by https://github.com/jdf/cue.language. Thanks Jonathan Feinberg.
    """

    # words = map(lambda x:x.lower(), re.findall(r'\w+', text, re.UNICODE))
    # the line above doesn't work on python 3.5

    s = StopWords()
    s.load_language(s.guess(map(lambda x:x.lower(), re.findall(r'\w+', text, re.UNICODE))))

    counted = {}

    for word in map(lambda x:x.lower(), re.findall(r'\w+', text, re.UNICODE)):
        if not s.is_stop_word(word) and len(word) > 1:
            if word in counted: #no has_key() method on python 3, use in instead
                counted[word] += 1
            else:
                counted[word] = 1

    return sorted(counted.items(), key=itemgetter(1), reverse=True)
