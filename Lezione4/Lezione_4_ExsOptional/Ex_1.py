
class Voti:
    def __init__(self,name):
        self.name = name
    def calc_score(self, name: str, score: list[int], )->list:
        for num in range(18, 30):
            score.append(num)
            for num in score: 
                media = sum(num)/len(score)
                if media >= 60 and name:
                    print(f"Il nome dello Studente è {name}. \nLa sua media è: {media}. \n{name} ha superato l'esame")


v:Voti = Voti("Marco")


v.calc_score("Marco", [18,22,25,22])