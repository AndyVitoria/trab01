#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Função que substitui os caracteres especiais unicode que estão de forma explicita, pelas suas equivalencias
def corrige(elem):
    acent = {'á': '\\u00e1', 'à': '\\u00e0', 'â': '\\u00e2', 'ã': '\\u00e3', 'ä': '\\u00e4', 'Á': '\\u00c1',
             'À': '\\u00c0', 'Â': '\\u00c2', 'Ã': '\\u00c3', 'Ä': '\\u00c4', 'é': '\\u00e9', 'è': '\\u00e8',
             'ê': '\\u00ea', 'ê': '\\u00ea', 'É': '\\u00c9', 'È': '\\u00c8', 'Ê': '\\u00ca', 'Ë': '\\u00cb',
             'í': '\\u00ed', 'ì': '\\u00ec', 'î': '\\u00ee', 'ï': '\\u00ef', 'Í': '\\u00cd', 'Ì': '\\u00cc',
             'Î': '\\u00ce', 'Ï': '\\u00cf', 'ó': '\\u00f3', 'ò': '\\u00f2', 'ô': '\\u00f4', 'õ': '\\u00f5',
             'ö': '\\u00f6', 'Ó': '\\u00d3', 'Ò': '\\u00d2', 'Ô': '\\u00d4', 'Õ': '\\u00d5', 'Ö': '\\u00d6',
             'ú': '\\u00fa', 'ù': '\\u00f9', 'û': '\\u00fb', 'ü': '\\u00fc', 'Ú': '\\u00da', 'Ù': '\\u00d9',
             'Û': '\\u00db', 'ç': '\\u00e7', 'Ç': '\\u00c7', 'ñ': '\\u00f1', 'Ñ': '\\u00d1', '&': '\\u0026',}
    for key in dict.keys(acent):
        if acent[key] in elem:
            elem = elem.replace(acent[key], key)
    return remove(elem)

# Função que remove caracteres especiais nao conhecidos
def remove(elem):
    while '\\' in elem:
        i = 0
        while elem[i] != '\\':
            i += 1
        elem = elem[:i] + elem[i+6:]
    return elem.replace('  ', ' ').replace('http:', 'http:\\\\').replace('https:', 'https:\\\\')
