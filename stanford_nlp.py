from bs4 import BeautifulSoup

qtypes = {"person":["who"], "place":["where"]}
persons = ["who"]
locations = ["what", "where"]

class Stanfordnlp:

    def __init__(self):
        super().__init__()
        self.q_story = []
        self.story = ""
    
    def make_lower(self, q_story):
        for x,y in q_story:
            self.q_story.append([x.lower(),y.lower()])

    def make_story(self, q_story):
        self.make_lower(q_story)        
        #print(q_story)
        for sentence in self.q_story:
            #print(sentence)
            integrated_sentence = ""
            if any(x in str(sentence[0].lower()) for x in persons):
                integrated_sentence = sentence[0].replace("who",sentence[1])
            elif any(x in str(sentence[0].lower()) for x in locations):
                if "is" in sentence[0]:
                    integrated_sentence = sentence[0].replace("where ","").replace("is ", "") +" is in "+ sentence[1]+ ". "
                elif "are" in sentence[0]:
                    integrated_sentence = sentence[0].replace("where ","").replace("are ", "") +" are in "+ sentence[1]+ ". "
                else:
                     integrated_sentence = sentence[0].replace("where","") +" in "+ sentence[1]+ ". "
            else:
                integrated_sentence = "Error."
            self.story+=str(integrated_sentence)
        print(self.story)

    def solve_anaphora(self, story):
        #http://nlp.stanford.edu:8080/corenlp/process
        #self.story = story
        #print(self.story)
        pass
    #print(story)
    

