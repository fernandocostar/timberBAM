class ScoreManager:
    def __init__(self):
        open('recorde.txt', 'a')
        with open('recorde.txt', 'r+') as f:
            try:
                self.record = int(f.read())
            except:
                self.record = 0

    def get_recorde(self):
        return self.record

    def set_new_record(self, score):
        with open('recorde.txt', 'w') as f:
            f.write(str(score))
        self.record = score
