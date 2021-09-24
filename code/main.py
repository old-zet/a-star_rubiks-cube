#! python3.8

from resolution_experimentale import *
from operateurs import *
from preconds_operateurs import *
import time

'''etat_initial = [ # etat initial très difficile pour l'algo
    ['O', 'O', 'G'],
    ['B', 'O', 'R'],
    ['R', 'Y', 'W'],
    ['B', 'O', 'R', 'B', 'Y', 'W', 'O', 'G', 'W', 'B', 'R', 'Y'],
    ['W', 'W', 'B', 'Y', 'B', 'W', 'B', 'Y', 'R', 'G', 'G', 'R'],
    ['Y', 'G', 'Y', 'G', 'W', 'G', 'Y', 'W', 'W', 'R', 'B', 'O'],
    ['B', 'Y', 'R'],
    ['O', 'R', 'O'],
    ['G', 'G', 'O']
]'''

# nombre de mouvements minimal absolu pour créer un mélange compliqué
# je l'ai résolu en 43 mouvements, sans connaître les opérateurs appliqués
etat_initial = copie_cube(etat_final)
etat_initial = vrotate2(etat_initial)
etat_initial = hrotate_inv2(etat_initial)
etat_initial = plateau_rot_bas(etat_initial)

print("État initial :")
etat_en_texte(etat_initial)

# interrupteur pour tests conditionnels plus simples à executer
test_etoile = False

start = time.time() # pour mésurer les tests

if (test_etoile): # si test_etoile = True
    chemin_final = []
    print('avancement_sol_cube initial ', avancement_sol_cube(etat_initial)) # test 1
    hybride(etat_initial, LIM, chemin_final)
else:
    res = recherche_profondeur_limitee(etat_initial, est_final, operateurs_disponibles, 5) # test 2
    #res = recherche_profondeur_mem(etat_initial, est_final, operateurs_disponibles, etat_en_texte, {}) # test 3
    #res = recherche_largeur(etat_initial, est_final, operateurs_disponibles)  # test 4
    #res = recherche_profondeur(etat_initial, est_final, operateurs_disponibles)  # test 5
    #res = recherche_profondeur_iterative(etat_initial, est_final, operateurs_disponibles)  # test 6
    #res = recherche_profondeur_random(etat_initial, est_final, operateurs_disponibles)  # test 7
    affiche_solution(etat_initial, res, etat_en_texte) # affichage du cube

end = time.time()
print(end - start)

#pos = get_case(etat_initial) # pour des tests de get_case
#res = get_mult_path(etat_initial, operateurs_disponibles, LIM, pos) # pour des tests de get_mult_path
#print(res)