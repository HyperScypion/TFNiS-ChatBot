class Jaccard:

    def __init__(self):
        pass

    def _compute_index(self, first_text, second_text):

        if len(first_text) <= 2:
            return 1
        power = 0
        for i in range(int(len(first_text)) - 2):
            for j in range(int(len(second_text)) - 2):
                if first_text[i:i + 3] == second_text[j:j + 3]:
                    power += 1

        if ((int(len(first_text)) - 2) +
                         (int(len(second_text)) - 2) - power) == 0:
            return 0
        else:
            return (power / ((int(len(first_text)) - 2) +
                         (int(len(second_text)) - 2) - power))
