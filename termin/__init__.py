#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .db_termins import termins as db_termins
from .db_sources import sources as db_sources


__author__ = 'Nurzhan Saktaganov'


translation_source = 'source'
language_en = 'en'
language_ru = 'ru'
language_kz = 'kz'

tupple_mapping = {
    translation_source: 0,
    language_en:        1,
    language_ru:        2,
    language_kz:        3,
}

def source(tuple):
    position = tupple_mapping.get(translation_source, None)
    if position is None:
        return None
    return tuple[position]

def translation(tuple, language):
    position = tupple_mapping.get(language, None)
    if position is None:
        return None
    return tuple[position]

def termins_to_dict():
    return [{
        translation_source: source(t),
        language_en: translation(t, language_en),
        language_ru: translation(t, language_ru),
        language_kz: translation(t, language_kz),
    } for t in db_termins]

termins = termins_to_dict()
sources = db_sources
