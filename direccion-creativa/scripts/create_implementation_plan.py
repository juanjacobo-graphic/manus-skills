'''
Este script genera un plan de implementación básico para un concepto creativo.
'''
import sys

def create_implementation_plan(concept_name):
    print(f"--- Plan de Implementación para el Concepto: {concept_name} ---")
    print("\n**Fase 1: Pre-producción**")
    print("- [ ] Definir equipo y roles")
    print("- [ ] Casting de actores/talentos")
    print("- [ ] Scouting de locaciones")
    print("- [ ] Storyboard y plan de rodaje")

    print("\n**Fase 2: Producción**")
    print("- [ ] Rodaje día 1")
    print("- [ ] Rodaje día 2")

    print("\n**Fase 3: Post-producción**")
    print("- [ ] Edición de video")
    print("- [ ] Diseño de sonido y música")
    print("- [ ] Corrección de color")
    print("- [ ] Entrega final")
    print("-----------------------------------------------------")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        create_implementation_plan(' '.join(sys.argv[1:]))
    else:
        print("Uso: python create_implementation_plan.py '<nombre_del_concepto>'")
