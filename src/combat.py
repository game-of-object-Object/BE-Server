from flask import Blueprint, request, jsonify
import jwt
import os
from . import db
from .models import Users, Room, Npc, Merchant, Item

combat = Blueprint('combat', __name__)
JWT_SECRET = os.environ.get("SECRET")
@combat.route('/', methods=['POST'])
def execute_combat_command():

    userId = jwt.decode(request.headers['token'], JWT_SECRET)['user_id']
    user = db.session.query(Users).filter_by(id = userId).first()
    command = None
    command = request.get_json()["command"]

    current_room = db.session.query(Room).filter_by(title = user.current_room).first()
    print('\n\n', current_room.NPCs, '\n\n')

    if current_room.NPCs == '':
        return 'nothing to fite here, so fite me irl'
        
    else:
        current_enemy = db.session.query(Npc).filter_by(name = current_room.NPCs).first()

        if command == 'attack':
            # Take user's attack and subtract monster's hp by that amount
            current_enemy.HP -= user.attack
            # Take monster's attack and subtract user's hp by that amount
            user.HP -= current_enemy.attack

            if current_enemy.HP <= 0:
                current_room.NPCs = None # Check if this kills mob

            db.session.commit()
            # Return interface
            cerealuser = {
                "id": int(user.id),
                "username": str(user.username),
                "character_name": str(user.character_name),
                "character_type": str(user.character_type),
                "portrait": str(user.portrait),
                "HP": int(user.HP),
                "MP": int(user.MP),
                "attack": int(user.attack),
                "gold": int(user.gold),
                "encounter_cd": int(user.encounter_cd),
                "current_room": str(user.current_room)
            }
            cerealmob = {
                "id": current_enemy.id,
                "name": current_enemy.name,
                "description": current_enemy.description,
                "items": current_enemy.items,
                "gold": current_enemy.gold,
                "HP": current_enemy.HP,
                "isHostile": current_enemy.isHostile,
                "attack": current_enemy.attack
            }
            cerealroom = {
                "id": current_room.id,
                "title": current_room.title,
                "description": current_room.description,
                "floor": current_room.floor,
                "items": current_room.items,
                "NPCs": current_room.NPCs,
                "north": current_room.north,
                "east": current_room.east,
                "south": current_room.south,
                "west": current_room.west
            }
            controls = {
                "user": cerealuser,
                "mob": cerealmob,
                "room": cerealroom
            }
            return controls

        elif command == 'run':
            # If monster type is special, cannot run
            # Otherwise, there is a chance that mob will disappear
            current_room.NPCs = None
            db.session.commit()

            cerealuser = {
                "id": int(user.id),
                "username": str(user.username),
                "character_name": str(user.character_name),
                "character_type": str(user.character_type),
                "portrait": str(user.portrait),
                "HP": int(user.HP),
                "MP": int(user.MP),
                "attack": int(user.attack),
                "gold": int(user.gold),
                "encounter_cd": int(user.encounter_cd),
                "current_room": str(user.current_room)
            }
            # cerealmob = {
            #     "id": current_enemy.id,
            #     "name": current_enemy.name,
            #     "description": current_enemy.description,
            #     "items": current_enemy.items,
            #     "gold": current_enemy.gold,
            #     "HP": current_enemy.HP,
            #     "isHostile": current_enemy.isHostile,
            #     "attack": current_enemy.attack
            # }
            cerealroom = {
                "id": current_room.id,
                "title": current_room.title,
                "description": current_room.description,
                "floor": current_room.floor,
                "items": current_room.items,
                "NPCs": current_room.NPCs,
                "north": current_room.north,
                "east": current_room.east,
                "south": current_room.south,
                "west": current_room.west
            }
            controls = {
                "user": cerealuser,
                # "mob": cerealmob,
                "room": cerealroom
            }
            return controls