var box = document.getElementById("scrabble_set");

function scrabble_set() {
    const letters = [];
    for (let i = 65; i < 92; i++) {
        let letter = String.fromCharCode(i);
        letters.push(letter);
    }
    letters.pop("[");
    letters.push("_");
    const lettersAmount = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2];
    const lettersWithAmount = Object.assign({}, ...letters.map((n, index) =>
                            ({[n]: lettersAmount[index]})));
    box.innerHTML += JSON.stringify(lettersWithAmount);
   }








//def create_letters_list():
//    word_lenght = int(input('Enter number of letters you need: '))
//    letters_list = []
//    new_scrabble_set = scrabble_set().copy()
//    for j in range(word_lenght):
//        letter = input('Enter your %d. letter: ' % (j + 1)).upper()
//        letters_list.append(letter)
//        new_scrabble_set[letter] -= 1
//        print(new_scrabble_set)
//        if new_scrabble_set[letter] == 0:
//            new_scrabble_set.pop(letter)
//            print('The limit of this letter is over!')
//            print('Your letters list is:', letters_list)
//            continue
//        print('Your letters list is:', letters_list)
//    return letters_list