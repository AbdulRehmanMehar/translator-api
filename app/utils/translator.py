from ..config.nltk import nltk
from ..config.dl_translate import mt, dlt

def list_languages(): 
    langs = mt.get_lang_code_map()
    inverted_langs = {v:k for k, v in langs.items()}

    return inverted_langs

def translate(text, source_language, target_language):
    if ('\n' in text):
        sents = nltk.tokenize.sent_tokenize(text, source_language)
        translated = " ".join(mt.translate(sents, source=source_language, target=target_language))
        return translated

    return mt.translate(text, source=source_language, target=target_language)

    

