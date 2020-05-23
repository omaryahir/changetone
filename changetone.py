import sys
import re 

class ToneConverter:

    SEQUENCE = (
        'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'        
    )
    ESP = {
        'C'  : 'Do' ,   
        'C#' : 'Do#',   
        'D'  : 'Re' ,   
        'D#' : 'Re#',   
        'E'  : 'Mi',
        'F'  : 'Fa' ,   
        'F#' : 'Fa#',   
        'G'  : 'Sol',   
        'G#' : 'Sol#',
        'A'  : 'La' ,   
        'A#' : 'La#',   
        'B'  : 'Si',    
    }

    def __init__(self, start, end, file_content, esp=False, nobrackets=False):
        self.start = self.valid_note(start)
        self.end = self.valid_note(end)
        self.file_content = file_content
        self.esp = esp 
        self.nobrackets = nobrackets

        self._calculate_diff_tones()
        self._process_file_content()

    def valid_note(self, tone):
        tone = tone.upper().strip()
        found = False 
        for note in self.ESP.items():
            if tone == note[1].upper():
                tone = note[0]
                found = True     
            elif tone == note[0].upper():
                found = True 
            if found:
                break 
        
        if not found: 
            raise ValueError('{} is not valid tone.'.format(tone))
        return tone 

    def _calculate_diff_tones(self):
        diff = 0
        count = False 
        finding = True
        while finding:            
            for note in self.SEQUENCE:
                if not count and self.start == note:
                    count = True 
                if count and self.end == note:
                    diff = diff + 1
                    finding = False 
                    count = False 
                    break 
                if count:
                    diff = diff + 1
        self.diff = diff 
        print('------\ndiff tones: {}\n------\n'.format(self.diff))


    def _tone_translated(self, tone):
        diff = 0
        count = False 
        converting = True 
        while converting:
            for note in self.SEQUENCE:
                if tone == note:
                    count = True 
                if count:
                    diff = diff + 1
                if diff == self.diff:
                    if esp:
                        note = self.ESP[note]
                    return note

    def _process_file_content(self):

        result = self.file_content 
        
        # Preparing the notes ...
        for note in self.SEQUENCE:
            pattern = '[\[]{}[\]]'.format(note)
            result = re.sub(pattern, '-{}-'.format(note), result, 0, re.IGNORECASE)

        # Changing the notes ...
        for note in self.SEQUENCE:
            qry = '-{}-'.format(note)
            replacement = self._tone_translated(note)
            if not self.nobrackets:
                replacement = '[{}]'.format(replacement)
            result = result.replace(qry, replacement)

        self.result = result 

    def get_result(self):
        return '{}\n'.format(self.result)

if __name__ == '__main__':

    # Ask the information 
    if len(sys.argv) >= 2:        
        file = str(sys.argv[1])
    else:
        raise ValueError('Name of file is missing')

    esp = 'esp' in sys.argv

    nobrackets = 'nobrackets' in sys.argv

    start_tone = input("\nStart Tone: ")
    end_tone = input("End Tone: ")

    f = open (file, 'r')
    file_content = f.read()

    toneConverter = ToneConverter(start_tone, end_tone, file_content, esp, nobrackets)
    result = toneConverter.get_result()
    print(result)