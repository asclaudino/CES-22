class Revertor(object):
    def __init__(self, string):
        self.string = string
        self.revert = ''

    
    def revert_string(self):
        for i in range(len(self.string)):
            self.revert += self.string[len(self.string) - i - 1]
        return self.revert
    
def create_dictionary(list,dictionary) -> None:
    for i in range(len(list)):
        dictionary[i] = list[i]
    return dictionary


Lista_Original = ["Ariel", "Joao", "Maria", "Pedro"]
Lista_Revertida = []
for str in Lista_Original:
    Lista_Revertida.append(Revertor(str).revert_string())
    
print(create_dictionary(Lista_Original,{}))
print(create_dictionary(Lista_Revertida,{}))