# VERSION : v0.1

from sys import argv
from translations import MORSE_TO_NATURAL, NATURAL_TO_MORSE

class CodificationError(Exception):
    '''
    Description
    -----------
     Exception class to indicate an error produced by a misspell in the command line.
    '''
    pass

class WordNotFound(Exception):
    '''
    Description
    -----------
     Exception class to indicate an error produced by the word not being in one of the translation dictionaries.
    '''
    pass

def morse_to_natural(msg:str|list) -> list:
    '''
    Description
    -----------
     Translates morse code to natural language.

    Parameters
    ----------
     msg : str
        Message to translate.
    
    Returns
    -------
     translated_morse : list
        A list of the letters translated.
    '''
    translated_morse = []
    for word in msg:
        if word in MORSE_TO_NATURAL:
            translated_morse.append(MORSE_TO_NATURAL[word])
        else:
            raise WordNotFound
        
    return translated_morse

def natural_to_morse(msg:str|list) -> list:
    '''
    Description
    -----------
     Translates natural language to morse code.

    Parameters
    ----------
     msg : str
        Message to translate.
    
    Returns
    -------
     translated_text : list
        A list of the letters translated.
    '''
    translated_text = []
    for symbol in msg:
        if symbol in NATURAL_TO_MORSE:
            translated_text.append(NATURAL_TO_MORSE[symbol])
        else:
            raise WordNotFound
        
    return translated_text

def main() -> None:
    '''
    Description
    -----------
     Main function that manages wheter the program needs to translate from morse
     code to natural language or the other way around and possible misspellings.

    Returns
    -------
     None
    '''
    if len(argv[2:]) > 1:
        if argv[1] == '-m':
            result: list = morse_to_natural(argv[2:])
        
        elif argv[1] == '-n':
            result: list = natural_to_morse(argv[2:])
        
        else:
            raise CodificationError
    
    elif len(argv[2:]) == 1:
        argument = argv[2].split()

        if argv[1] == '-m':
            result: list = morse_to_natural(argument)
        
        elif argv[1] == '-n':
            result: list = natural_to_morse(argument)
        
        else:
            raise CodificationError

    else:
        raise CodificationError
    
    for translation in result:
        print(translation, end=' ')

if __name__ == '__main__':
    try:
        main()

    except CodificationError:
        print('\nERROR : You should indicate whether the message is in morse code or natural language in the command prompt (-m or -n).\n')
    
    except WordNotFound:
        print('\nERROR : Either one of the words you tried to translate was not found or the code-type speficier is incorrect.\n')