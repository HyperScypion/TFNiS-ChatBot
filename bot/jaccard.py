

class Jaccard:

    def __init__(self):
        pass

    def _compute_index(first_text, second_text):

        power = 0
        for i in range(int(len(first_text)) - 2):
            for j in range(int(len(second_text)) - 2):
                if first_text[i:i+3] == second_text[j:j+3]:
                    power += 1

        return (power/((int(len(first_text)) - 2) +
                (int(len(second_text)) - 2) - power))
