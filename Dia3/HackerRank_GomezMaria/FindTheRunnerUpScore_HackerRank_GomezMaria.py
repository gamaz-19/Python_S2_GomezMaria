######################################################
####### Find The Runner-Up Score! - HackerRank #######
######################################################

if __name__ == '__main__':
    n = int(input())
    mat = map(int, input().split())
    
    # Convertimos el map object a una lista
    scores = list(mat)
    
    # Encontramos el valor máximo
    max_score = max(scores)
    
    # Filtramos todas las puntuaciones máximas
    filtered_scores = [score for score in scores if score != max_score]
    
    # Si no quedan elementos después de filtrar, no hay subcampeón
    if not filtered_scores:
        print("No hay subcampeón")
    else:
        # El subcampeón es el máximo de las puntuaciones restantes
        runner_up = max(filtered_scores)
        print(runner_up)


# Developed by: Maria Alejandra Gomez Archila - ID.1005234916