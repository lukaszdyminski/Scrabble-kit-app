from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import *
from django.forms import inlineformset_factory
import itertools
import os


# Create your views here.


def display_tiles_set(request):
    letters_dict = ScrabbleTiles.objects.all()
    return render(request, 'index.html', {'letters_dict': letters_dict})


def enter_letters_amount(request):
    if request.method == 'POST':
        letters_amount = ScrabbleWordLengthForm(request.POST or None)
        if letters_amount.is_valid():
            amount = letters_amount.save(commit=False)
            amount.save()
            return redirect('enter_user_scrabble_set', amount.pk)
        else:
            messages.error(request, 'The form contains errors!')
    else:
        letters_amount = ScrabbleWordLengthForm()
    return render(request, 'letters_amount.html', {'letters_amount': letters_amount})


def enter_user_scrabble_set(request, pk):
    scrabble_set_length = get_object_or_404(ScrabbleWordLength, pk=pk)
    field_value = getattr(scrabble_set_length, 'word_length')
    ScrabbleSetFormSet = inlineformset_factory(ScrabbleWordLength, ScrabbleSet, form=ScrabbleSetForm, extra=field_value)
    if request.method == 'POST':
        formset = ScrabbleSetFormSet(request.POST or None)
        if formset.is_valid():
            for form in formset:
                instance = form.save(commit=False)
                instance.tile_id = scrabble_set_length
                instance.save()
            return redirect('display_user_scrabble_set', pk=scrabble_set_length.pk)
    else:
        formset = ScrabbleSetFormSet(queryset=ScrabbleSet.objects.none())
    return render(request, 'scrabble_set_length.html', {'scrabble_set_length': scrabble_set_length,
                                                        'formset': formset})


def display_user_scrabble_set(request, pk):
    set_length = get_object_or_404(ScrabbleWordLength, pk=pk)
    user_scrabble_set = list(ScrabbleSet.objects.filter(tile_id=pk))
    pre_letters_dict = ScrabbleTiles.objects.all().values_list('all_tiles_set', flat=True)
    user_scrabble_tiles = ScrabbleSet.objects.filter(tile_id=pk).values_list('tile', flat=True)
    for user_letter in user_scrabble_tiles:
        for index in range(len(pre_letters_dict)):
            for letter in pre_letters_dict[index]:
                if user_letter == letter:
                    pre_letters_dict[index][letter] -= 1
                    if pre_letters_dict[index][letter] < 0:
                        messages.error(request, 'The "{}" letter scrabble set limit is exceeded.'
                                                'Using original scrabble set for sure? Try again!'.format(user_letter))
                        return redirect('letters_amount')
    return render(request, 'user_scrabble_set_results.html', {'user_scrabble_set': user_scrabble_set,
                                                              'pre_letters_dict': pre_letters_dict,
                                                              'set_length': set_length,
                                                              'user_scrabble_tiles': user_scrabble_tiles})


def display_words_list(request, pk):
    letters = []
    for i in range(65, 91):
        let = chr(i)
        letters.append(let)
    all_permuted_words_list = []
    permutation_tiles_set = ScrabbleSet.objects.filter(tile_id=pk).values_list('tile', flat=True)
    tile_set_length = len(permutation_tiles_set)
    if request.method == 'GET':
        if '-' in permutation_tiles_set:
            pre_permutation_list = (list(itertools.product(*permutation_tiles_set, letters)))
            non_space_list = [list(tup) for tup in pre_permutation_list]
            [lst.remove('-') for lst in non_space_list]
            for phrase in non_space_list:
                blank_tile_set_length = len(phrase)
                while blank_tile_set_length > 0:
                    all_permuted_words_blank = list(itertools.permutations(phrase, blank_tile_set_length))
                    blank_tile_set_length -= 1
                    for tile in all_permuted_words_blank:
                        word = ''.join(tile)
                        all_permuted_words_list.append(word)
        else:
            while tile_set_length > 0:
                all_permuted_words = list(itertools.permutations(permutation_tiles_set, tile_set_length))
                tile_set_length -= 1
                for tile in all_permuted_words:
                    word = ''.join(tile)
                    all_permuted_words_list.append(word)
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'static/Collins Scrabble Words (2019).txt')
    with open(file_path, 'r') as f:
        lines = list(f)
        list_of_words = []
        for line in lines:
            line = ''.join(line)
            new_line = line.replace('\n', '')
            list_of_words.append(new_line)
        common_words = []
        for word1 in all_permuted_words_list:
            for word2 in list_of_words:
                if word1 == word2:
                    if word2 in common_words:
                        continue
                    common_words.append(word2)
                    sorted_common_words = sorted(common_words, key=len, reverse=True)
    return render(request, 'final_words_list.html', {'sorted_common_words': sorted_common_words,
                                                     'permutation_tiles_set': permutation_tiles_set})
