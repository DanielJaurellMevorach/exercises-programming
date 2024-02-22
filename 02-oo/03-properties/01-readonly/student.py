class MusicalNote:
    def __init__(self, name, pitch):
        self.__pitch = pitch
        self.__name = name
        
    @property    
    def pitch(self):
        return self.__pitch
    
    
    @property    
    def name(self):
        return self.__name