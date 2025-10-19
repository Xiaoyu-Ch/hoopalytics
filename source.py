
def calculateOne(coefficients: list[float],player_data:list[int])->float:
#only for one player
    temp=min(len(coefficients),len(player_data))
    score=0.0
    for i in range(temp):
        score=score+coefficients[i]*player_data[i]
    return score
def calculateAll(coefficients: list[float], all_player_data: list[list[int]]) -> list[float]:
    """
    Calculates the scores for a list of players
    """
    res=[]
    for data in all_player_data:
        res.append(calculateOne(coefficients,data))
    return res