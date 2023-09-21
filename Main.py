
#mapping of every type
#hashmap
import pokebase as pb
if __name__ == '__main__':
    sala = pb.pokemon('salamence')
    ground = pb.type_('ground')
    print(sala.height)
    print(ground.damage_relations.no_damage_to)
        