class WordsFinder:
    file_names = ()
    def __init__(self,*files):
        self.file_names = files
        print(self.file_names)
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name,'r',encoding='utf-8') as file:
                words = file.read()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(i,'')
                all_words[file_name] = words.lower().split()
        return all_words
    def find(self, search_word):
        result = {}
        for name, words in self.get_all_words().items():
            for i,word in enumerate(words):
                if search_word.lower() == word:
                    result[name] = i+1
                    break
        return result

    def count(self, search_word):
        result = {}
        for name, words in self.get_all_words().items():
            word_count = 0
            for word in words:
                if search_word.lower() == word:
                    word_count +=1
                result[name] = word_count
        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('The'))
print(finder1.count('the'))