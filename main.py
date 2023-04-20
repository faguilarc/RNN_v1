import re
import string
import random as rm
import pandas as pd
import tensorflow as tf


def custom_standardization(input_string):
    """ transforms words into lowercase and deletes punctuations """

    stripped_spanish = tf.strings.lower(input_string)

    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'á', 'a')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'ä', 'a')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'Á', 'a')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'Ä', 'a')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'é', 'e')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'ë', 'e')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'É', 'e')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'Ë', 'e')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'í', 'i')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'ï', 'i')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'Í', 'i')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'Ï', 'i')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'ó', 'o')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'ö', 'o')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'Ó', 'o')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'Ö', 'o')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'ú', 'u')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'ü', 'u')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'Ú', 'u')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'Ü', 'u')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                ',', ' ')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                ';', ' ')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'entre', 'entre ')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'e /', ' entre ')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'e/', ' entre ')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                '#', ' num ')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'apt.', 'apt. ')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                'apartamento', 'apartamento ')
    stripped_spanish = tf.strings.regex_replace(stripped_spanish,
                                                '/', 'entre ')
    output = tf.strings.regex_replace(
        stripped_spanish, '[%s]' % re.escape(string.punctuation), '')

    return output


def custom_standardization_v2(input_string):
    # Transforma toda la cadena a minúsculas
    lower_str = input_string.lower()

    # Reemplaza los caracteres y vocales especiales por espacios
    char_spvow_off_str = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lower_str)

    # Quita cualquier caracter que no sea número o letra por espacio
    clear_str = re.sub('[^0-9a-zA-Z]+', ' ', char_spvow_off_str)

    return clear_str





def generate_address():
    street_types = ['Calle', 'Avenida', 'Carrera', 'Transversal']
    place_types = ['Parque', 'Plaza', 'Centro Comercial', 'Hospital']
    localities = ['Habana Vieja', 'Centro Habana', 'Vedado', 'Miramar']
    municipalities = ['La Habana', 'Artemisa', 'Mayabeque']
    provinces = ['Pinar del Río', 'Artemisa', 'La Habana']

    street_type = rm.choice(street_types)
    distance = str(rm.randint(1, 100)) + " km"
    place_type = rm.choice(place_types)
    locality = rm.choice(localities)
    municipality = rm.choice(municipalities)
    province = rm.choice(provinces)

    address_components = [('Calle', street_type), ('Distancia', distance), ('Lugar de interés', place_type),
                          ('Reparto o localidad', locality), ('Municipio', municipality), ('Provincia', province)]
    rm.shuffle(address_components)

    return address_components


def save_to_excel():
    data = []
    for i in range(1, 11):
        address_components = generate_address()
        for component in address_components:
            data.append([i, component[0], component[1]])

    df = pd.DataFrame(data, columns=['Sentence', 'Word', 'Tag'])
    df.to_excel('addresses.xlsx')


from random import randrange, choice
from spellchecker import SpellChecker
from fuzzywuzzy import fuzz

spell = SpellChecker(language='es')


def generate_spelling_errors(text):
    words = text.split()
    for i in range(len(words)):
        word = words[i]
        apply_value = randrange(100)
        if apply_value > 65:
            rand = randrange(100)
            if rand < 25:
                # Duplicate character
                char_index = randrange(len(word))
                words[i] = word[:char_index] + word[char_index] + word[char_index:]
            elif rand < 50:
                # Omit character
                char_index = randrange(len(word))
                words[i] = word[:char_index] + word[char_index + 1:]
            elif rand < 75:
                # Misspelling
                if word.lower() in spell:
                    suggestions = list(spell.candidates(word.lower()))
                    if len(suggestions) > 0:
                        new_word = choice(suggestions)
                        if fuzz.ratio(word.lower(), new_word) < 75:
                            words[i] = new_word
            else:
                # Replace similar character
                char_index = randrange(len(word))
                similar_chars = {'a': 'e', 'e': 'a', 'i': 'l', 'l': 'i', 'o': 'u', 'u': 'o','a':'@','0':'@'}
                if word[char_index].lower() in similar_chars:
                    new_char = similar_chars[word[char_index].lower()]
                    words[i] = word[:char_index] + new_char + word[char_index + 1:]

    return ' '.join(words)


def generate_write_error(word):
    """ This function randomly generates a write error given a word entered by parameter,
        the types of errors established,(with their range) were:

        -Omission of characters(0-20)
        -Spelling mistake(20-45)
        -Addition of other characters(45-50)
        -character duplication(50-60)
      ** if the value is -1, the word is returned in its original state

    :param word: string that will be subjected to the error generation process

    :return: string with write error
    """
    error_value = rm.randint(-2, 60)
    wrong_word = ''
    if word != '' or word != ' ':
        # Character Omission
        if error_value in range(0, 20):
            o_index = rm.randint(len(word))
            i = 0
            for char in word:
                if i == o_index:
                    wrong_word = word[:i] + '' + word[i + 1:]
                i += 1
        # Spelling Mistakes
        elif error_value in range(20, 45):
            pass
        # Addition of other characters
        elif error_value in range(45, 50):
            char_list = string.printable
            random_char = rm.randint(len(char_list))
            r_index = rm.randint(len(word))
            char_added = char_list[random_char]
            i = 0
            for char in word:
                if i == r_index:
                    wrong_word = word[:i] + '' + char_added + '' + word[i:]
                i += 1
        # Character duplication
        elif error_value in range(50, 60):
            r_index = rm.randint(len(word))
            i = 0
            for char in word:
                if i == r_index:
                    wrong_word = word[:i] + '' + char + '' + word[i:]
                i += 1
    return wrong_word


tesxt = "Busco la manera de generar errores de ortografia"

print(generate_spelling_errors(tesxt))
print(generate_write_error("Busco"))