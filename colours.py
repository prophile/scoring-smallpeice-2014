def calculate_score(data):
    gold, silver = data.get('gold', 0), data.get('silver', 0)
    moved = data.get('moved', False)
    token_score = 2*(gold + silver) // (2 if gold and silver else 1)
    return token_score + int(moved)

def calculate_scores(scores):
    return {tla: calculate_score(data)
             for tla, data in scores.iteritems()}

if __name__ == '__main__':
    import sys
    sys.path.append('libproton')
    import libproton
    libproton.main(calculate_scores)

