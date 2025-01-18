import random 

words = [
    {"fr": "le", "en": "the"},
    {"fr": "être", "en": "to be"},
    {"fr": "avoir", "en": "to have"},
    {"fr": "je", "en": "I"},
    {"fr": "de", "en": "of, from"},
    {"fr": "ne", "en": "not (in negation)"},
    {"fr": "pas", "en": "not (in negation)"},
    {"fr": "un", "en": "a, one"},
    {"fr": "pour", "en": "for"},
    {"fr": "dans", "en": "in"},
    {"fr": "qui", "en": "who"},
    {"fr": "que", "en": "that, what"},
    {"fr": "avec", "en": "with"},
    {"fr": "sur", "en": "on"},
    {"fr": "se", "en": "oneself (reflexive)"},
    {"fr": "vous", "en": "you (formal/plural)"},
    {"fr": "elle", "en": "she"},
    {"fr": "il", "en": "he"},
    {"fr": "nous", "en": "we"},
    {"fr": "en", "en": "in, by, of (depending on context)"},
    {"fr": "ce", "en": "this, it"},
    {"fr": "mais", "en": "but"},
    {"fr": "dire", "en": "to say"},
    {"fr": "avoir", "en": "to have"},
    {"fr": "faire", "en": "to do, to make"},
    {"fr": "aller", "en": "to go"},
    {"fr": "voir", "en": "to see"},
    {"fr": "savoir", "en": "to know (facts, information)"},
    {"fr": "pouvoir", "en": "can, to be able to"},
    {"fr": "vouloir", "en": "to want"},
    {"fr": "venir", "en": "to come"},
    {"fr": "prendre", "en": "to take"},
    {"fr": "bien", "en": "good, well"},
    {"fr": "moi", "en": "me"},
    {"fr": "toi", "en": "you (informal singular)"},
    {"fr": "ici", "en": "here"},
    {"fr": "là", "en": "there"},
    {"fr": "lui", "en": "him, her (indirect object)"},
    {"fr": "nous", "en": "us"},
    {"fr": "eux", "en": "them (masc.)"},
    {"fr": "elles", "en": "them (fem.)"},
    {"fr": "tout", "en": "all, everything"},
    {"fr": "rien", "en": "nothing"},
    {"fr": "quelque", "en": "some, a few"},
    {"fr": "tout", "en": "all, everything"},
    {"fr": "plus", "en": "more"},
    {"fr": "moins", "en": "less"},
    {"fr": "autre", "en": "other"},
    {"fr": "premier", "en": "first"},
    {"fr": "dernier", "en": "last"},
    {"fr": "nouveau", "en": "new"},
    {"fr": "ancien", "en": "old (things, objects)"},
    {"fr": "jour", "en": "day"},
    {"fr": "temps", "en": "time, weather"},
    {"fr": "homme", "en": "man"},
    {"fr": "femme", "en": "woman"},
    {"fr": "enfant", "en": "child"},
    {"fr": "ami", "en": "friend"},
    {"fr": "travail", "en": "work"},
    {"fr": "école", "en": "school"},
    {"fr": "maison", "en": "house"},
    {"fr": "ville", "en": "city"},
    {"fr": "pays", "en": "country"},
    {"fr": "voiture", "en": "car"},
    {"fr": "porte", "en": "door"},
    {"fr": "fenêtre", "en": "window"},
    {"fr": "table", "en": "table"},
    {"fr": "chaise", "en": "chair"},
    {"fr": "livre", "en": "book"},
    {"fr": "stylo", "en": "pen"},
    {"fr": "chose", "en": "thing"},
    {"fr": "idée", "en": "idea"},
    {"fr": "beau", "en": "beautiful, handsome"},
    {"fr": "grand", "en": "big, tall"},
    {"fr": "petit", "en": "small, short"},
    {"fr": "long", "en": "long"},
    {"fr": "court", "en": "short (length)"},
    {"fr": "lourd", "en": "heavy"},
    {"fr": "léger", "en": "light (weight)"},
    {"fr": "facile", "en": "easy"},
    {"fr": "difficile", "en": "difficult"},
    {"fr": "content", "en": "happy, content"},
    {"fr": "triste", "en": "sad"},
    {"fr": "intéressant", "en": "interesting"},
    {"fr": "important", "en": "important"},
    {"fr": "joli", "en": "pretty"},
    {"fr": "intelligent", "en": "intelligent"},
    {"fr": "fort", "en": "strong"},
    {"fr": "faible", "en": "weak"},
    {"fr": "sérieux", "en": "serious"},
    {"fr": "amusant", "en": "funny"},
    {"fr": "vrai", "en": "true"},
    {"fr": "faux", "en": "false"},
    {"fr": "beaucoup", "en": "a lot, much"},
    {"fr": "quelques", "en": "a few"},
    {"fr": "tous", "en": "all"},
    {"fr": "aucun", "en": "none, no"},
    {"fr": "toujours", "en": "always"},
    {"fr": "jamais", "en": "never"},
    {"fr": "souvent", "en": "often"},
    {"fr": "parfois", "en": "sometimes"},
    {"fr": "maintenant", "en": "now"},
    {"fr": "demain", "en": "tomorrow"},
    {"fr": "hier", "en": "yesterday"},
    {"fr": "avant", "en": "before"},
    {"fr": "après", "en": "after"}
]

def quiz_user(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"What is the English translation of '{word['fr']}'")
        user_answer=input("Your answer: ").strip().lower()
        correct_answer=word['en'].lower()

        if user_answer == correct_answer:
            print("Correct!!\n")
            score+=1
        else:
            print(f"Wrong! The correct answer is '{word['en']}'.\n")

def main():
    print("Welcome to the language learning flashcards app!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__=="__main__":
    main()