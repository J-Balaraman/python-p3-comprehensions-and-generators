#!/usr/bin/env python3

def return_evens(num_list):
    even_num_list = [n for n in num_list if (n % 2) == 0]
    return even_num_list

def make_exclamation(sentence_list):
    exclamtion_list = [f"{sentence_list[n]}!" for n in range(len(sentence_list)) if n != ""]
    return exclamtion_list