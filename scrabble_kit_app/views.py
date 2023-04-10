from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import *
from django.forms import inlineformset_factory
import itertools
import os


# original scrabble set view; presenting 27 pairs "letter - letter tiles amount"; displayed on scrabble-kit-app home url
def display_tiles_set(request):
    letters_dict = ScrabbleTiles.objects.all()
    return render(request, 'index.html', {'letters_dict': letters_dict})


# tiles amount view; presenting form in which user enters number of tiles that are kept in secret and from the board
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


# tiles view; presenting form in which user enters the tiles that are kept in secret and from the board
def enter_user_scrabble_set(request, pk):
    scrabble_set_length = get_object_or_404(ScrabbleWordLength, pk=pk)
    user_field_value = getattr(scrabble_set_length, 'user_word_length')
    board_field_value = getattr(scrabble_set_length, 'board_tiles')
    ScrabbleSetFormSet = inlineformset_factory(ScrabbleWordLength, UserScrabbleSet, form=UserScrabbleSetForm,
                                               extra=user_field_value)
    ScrabbleBoardFormSet = inlineformset_factory(ScrabbleWordLength, BoardScrabbleSet, form=BoardScrabbleSetForm,
                                                 extra=board_field_value)
    if request.method == 'POST':
        user_formset = ScrabbleSetFormSet(request.POST or None, instance=scrabble_set_length)
        board_formset = ScrabbleBoardFormSet(request.POST or None, instance=scrabble_set_length)
        if user_formset.is_valid() and board_formset.is_valid():
            user_formset.save()
            board_formset.save()
            return redirect('display_user_scrabble_set', pk=scrabble_set_length.pk)
        else:
            messages.error(request, 'The form contains errors!')
    else:
        user_formset = ScrabbleSetFormSet(queryset=UserScrabbleSet.objects.none())
        board_formset = ScrabbleBoardFormSet(queryset=UserScrabbleSet.objects.none())
    return render(request, 'scrabble_set_length.html', {'scrabble_set_length': scrabble_set_length,
                                                        'user_formset': user_formset,
                                                        'board_formset': board_formset
                                                        })


# user tiles set and modified original scrabble set view; presenting tiles chosen by user and scrabble set minus user's tiles kept in secret
def display_user_scrabble_set(request, pk):
    set_length = get_object_or_404(ScrabbleWordLength, pk=pk)
    user_scrabble_tiles = UserScrabbleSet.objects.filter(user_tile_id=pk).values_list('user_tile', flat=True)
    board_tiles = BoardScrabbleSet.objects.filter(board_tile_id=pk).values_list('board_tile', flat=True)
    tiles_set = list(itertools.chain(user_scrabble_tiles, board_tiles))
    pre_letters_dict = ScrabbleTiles.objects.all().values_list('all_tiles_set', flat=True)
    for user_letter in user_scrabble_tiles:
        for index in range(len(pre_letters_dict)):
            for letter in pre_letters_dict[index]:
                if user_letter == letter:
                    pre_letters_dict[index][letter] -= 1
                    if pre_letters_dict[index][letter] < 0:
                        messages.error(request, 'The "{}" letter scrabble set limit is exceeded.'
                                                'Using original scrabble set for sure? Try again!'.format(user_letter))
                        return redirect('letters_amount')
    return render(request, 'user_scrabble_set_results.html', {'user_scrabble_tiles': user_scrabble_tiles,
                                                              'tiles_set': tiles_set,
                                                              'pre_letters_dict': pre_letters_dict,
                                                              'set_length': set_length
                                                              })


# searching results view; presenting all the words arranged of user tiles set ordering from longest one to shortest one
def display_words_list(request, pk):
    letters = []
    for i in range(65, 91):
        let = chr(i)
        letters.append(let)
    all_permuted_words_list = []
    permutation_user_tiles_set = UserScrabbleSet.objects.filter(user_tile_id=pk).values_list('user_tile', flat=True)
    permutation_board_tiles_set = BoardScrabbleSet.objects.filter(board_tile_id=pk).values_list('board_tile', flat=True)
    permutation_tiles_set = list(itertools.chain(permutation_user_tiles_set, permutation_board_tiles_set))
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
