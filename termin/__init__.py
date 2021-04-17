#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .db import termins as db_termins


__author__ = 'Nurzhan Saktaganov'


language_en = 'en'
language_ru = 'ru'
language_kz = 'kz'


def translation(tuple, language):
    # tuple is reserved keyword
    mapping = {
        language_en: 0,
        language_ru: 1,
        language_kz: 2,
    }

    position = mapping.get(language, None)
    if position is None:
        return ''

    return tuple[position]

def termins_to_dict():
    return [{
        language_en: translation(t, language_en),
        language_ru: translation(t, language_ru),
        language_kz: translation(t, language_kz),
    } for t in db.termins]

termins = termins_to_dict()
