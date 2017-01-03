import VectorMaps
from os import system


#Used instead of print() and input() for purposes of accessibility to screenreaders
def dual_print(string):
    system("title "+string)
    print(string + '\n')
    
def dual_input(string):
    system("title "+string)
    return input(string)
    
#Utility functions
    
def get_commands():
    command = dual_input('Please enter a command: ')
    return command
    
def validate_position(position, bound):
    if position not in range(bound):
        return False
    else:
        return True
        
    
#Commands that can be used in tile edit mode

def list_fields(tile): #Lists fields within a tile
    if tile.fields == []:
        dual_print('There are no fields in this tile.')
    else:
        dual_print('There are ' + str(len(tile.fields)) + ' fields. In order of addition: ')
        
        for f in tile.fields:
            dual_print(f.name + ',')
            
            
    return tile

def create_field(tile):
    field_name = str(dual_input('Enter a name for the new field: '))
    for f in tile.fields:
        if f.name == field_name:
            dual_print('Error: Field named ' + field_name + ' already exists in this tile. Exiting field creation.')
            return
    
    while True:
        try:
            anchor_x = dual_input('Enter the x-position of the field\'s anchor (upper left corner): ')
            anchor_x = int(anchor_x)
        except:
            dual_print('Error: ' + str(anchor_x) + ' is not a number.')
            continue
        else:
            if validate_position(anchor_x, tile.width):
                break
            else:
                dual_print('Error: ' + str(anchor_x) + ' is out of bounds.')
        
    while True:
        try:
            anchor_y = dual_input('Enter the y-position of the field\'s anchor (upper left corner): ')
            anchor_y = int(anchor_y)
        except:
            dual_print('Error: ' + str(anchor_y) + ' is not a number.')
            continue
        else:
            if validate_position(anchor_y, tile.height):
                break
            else:
                dual_print('Error: ' + str(anchor_y) + ' is out of bounds.')
                
    while True:
        try:
            field_width = dual_input('Enter the width of the field: ')
            field_width = int(field_width)
        except:
            dual_print('Error: ' + str(field_width) + ' is not a number.')
            continue
        else:
            if validate_position(field_width + anchor_x, tile.width):
                break
            else:
                dual_print('Error: the edge of the field is out of bounds.')
        
    while True:
        try:
            field_height = dual_input('Enter the height of the field: ')
            field_height = int(field_height)
        except:
            dual_print('Error: ' + str(field_height) + ' is not a number.')
            continue
        else:
            if validate_position(field_height + anchor_y, tile.height):
                break
            else:
                dual_print('Error: the edge of the field is out of bounds. Try shortening it.')
                
    while True:
        field_clips = dual_input('Can entities pass through this field? Y/n: ')
        if field_clips.lower() == 'y':
            field_clips = True
            break
        elif field_clips.lower() == 'n':
            field_clips = False
            break
        else:
            dual_print('Invalid input.')
            
    
    dual_print('Creating field...')
    tile.fields.append(VectorMaps.Field([field_width, field_height],[anchor_x, anchor_y], name=field_name, clipping=field_clips))
    dual_print('Done. Returning to tile edit mode.')
    return tile
    
    
def edit_field(tile):
    found = False
    
    field_name = str(dual_input('Enter the name of the field you wish to edit. '))
    for f in tile.fields:
        if f.name == field_name:
            dual_print('Now editing field "' + field_name + '" in tile ' + str(tile.pos) + '.')
            found = True
            active_field_index = tile.fields.index(f)
    
    if not found:
        dual_print('Field "' + field_name + '" was not found. Returning to tile edit mode.')
        return
        
    while 1:
        option = str(dual_input('Enter the name of the item you want to edit. Options are: \'anchorX\', \'anchorY\', \'width\', \'height\', and \'name\'. To exit, use \'save\' to save changes and exit or \'cancel\' to revert changes and exit.')).lower().strip()
        if option == 'anchorx':
            dual_print('The anchor\'s current coordinates are ' + str(tile.fields[active_field_index].anchor) + '.')
            try:
                new_x = int(dual_input('Enter the new value for the anchor\'s position on the X axis: '))
            except:
                dual_print('Error: Not a Number')
                continue
            else:
                if validate_position(new_x + tile.fields[active_field_index].dimensions[0], tile.width):
                    tile.fields[active_field_index].anchor[0] = new_x
                    dual_print('Done. The anchor\'s coordinates are now ' + str(tile.fields[active_field_index].anchor) + '.')
                else:
                    dual_print('Error: the edge of the field is now out of bounds. Cancelling action.')
                
        elif option == 'anchory':
            try:
                new_y = int(dual_input('Enter the new value for the anchor\'s position on the Y axis: '))
            except:
                dual_print('Error: Not a Number')
                continue
            else:
                if validate_position(new_y + tile.fields[active_field_index].dimensions[1], tile.height):
                    tile.fields[active_field_index].anchor[1] = new_y
                    dual_print('Done. The anchor\'s coordinates are now ' + str(tile.fields[active_field_index].anchor) + '.')
                else:
                    dual_print('Error: the edge of the field is now out of bounds. Cancelling action.')
                    
                    
        elif option == 'width':
            try:
                new_width = int(dual_input('Enter the new value for the field\'s width: '))
            except:
                dual_print('Error: Not a Number')
                continue
            else:
                if validate_position(new_width + tile.fields[active_field_index].anchor[0], tile.width):
                    tile.fields[active_field_index].dimensions[0] = new_width
                    dual_print('Done. The field\'s dimensions are now' + str(tile.fields[active_field_index].dimensions) + '.')
                else:
                    dual_print('Error: the edge of the field is now out of bounds. Cancelling action.')
                    
        elif option == 'height':
            try:
                new_height = int(dual_input('Enter the new value for the field\'s height: '))
            except:
                dual_print('Error: Not a Number')
                continue
            else:
                if validate_position(new_height + tile.fields[active_field_index].anchor[1], tile.height):
                    tile.fields[active_field_index].dimensions[1] = new_height
                    dual_print('Done. The field\'s dimensions are now' + str(tile.fields[active_field_index].dimensions) + '.')
                else:
                    dual_print('Error: the edge of the field is now out of bounds. Cancelling action.')

        elif option == 'clipping'
            field_clips = dual_input('Can entities pass through this field? Y/n: ')
            if field_clips.lower() == 'y':
                tile.fields[active_field_index].clipping = True
                dual_print('Clipping set to True')
                break
            elif field_clips.lower() == 'n':
                tile.fields[active_field_index].clipping = False
                dual_print('Clipping set to False')
                break
            else:
                dual_print('Invalid input. Cancelling action.')
        
        elif option == 'cancel':
            dual_print('Cancelling all changes. Exiting to tile edit mode.')
            return
            
        elif option == 'save':
            dual_print('Saving all changes. Exiting to tile edit mode. Note that to save to a file you must export.')
            return tile
        
        
    
def delete_field(tile):
    found = False
    
    field_name = str(dual_input('Enter the name of the field you wish to delete. '))
    for f in tile.fields:
        if f.name == field_name:
            dual_print('Deleting field...')
            found = True
            tile.fields.remove(f)
            dual_print('Tile deleted. Returning to tile edit mode.')
            return tile
    
    if not found:
        dual_print('Field "' + field_name + '" was not found. Returning to tile edit mode.')
        return
        
def view_field(tile):
    found = False
    
    field_name = str(dual_input('Enter the name of the field you wish to view. '))
    for f in tile.fields:
        if f.name == field_name:
            dual_print('Now viewing field "' + field_name + '" in tile ' + str(tile.pos) + '.')
            dual_print('anchor: ' + str(f.anchor) + '\ndimensions: ' + str(f.dimensions) + '\nclips: ' + str(f.clipping) )
            found = True
            return
    
    if not found:
        dual_print('Field "' + field_name + '" was not found. Returning to tile edit mode.')
        return

def parse_command(command, tile):
    command_dict = {'field' : {'list' : list_fields, 'new' : create_field, 'delete' : delete_field, 'edit' : edit_field, 'view' : view_field}}
    commands = command.split(' ')
    try:
        options = command_dict[commands[0]]
    except:
        dual_print('Error, invalid command.')
    else:
        try:
            if commands[1] in options:
                tile = options[commands[1]](tile)
                return tile
            else:
                dual_print('Error, invalid argument')
        except:
            dual_print('You need to provide an argument.')
            raise
        
            

def setup():
    MAP_NAME = dual_input('Please name the map: ')

    TILE_HEIGHT = int(dual_input('What should the height of each tile be?: '))
    TILE_WIDTH = int(dual_input('What should the width of each tile be?: '))
    MAP_HEIGHT = int(dual_input('How tall should the map be (in tiles)?: '))
    MAP_WIDTH = int(dual_input('How wide should the map be (in tiles)?: '))

    map = VectorMaps.Map(MAP_HEIGHT, MAP_WIDTH, name=MAP_NAME)
    
    dual_print('Map object created. Propagating...')
    map.propagate(tile_width=TILE_WIDTH, tile_height=TILE_HEIGHT)
    dual_print('Done. Now entering tile edit mode.')
    return map

def edit_tile(pos):
    print('Now editing tile' + str(pos) + '. Type \'help\' for a list of commands.')
    while 1:
        command = get_commands()
        parsed_data = parse_command(command, map.tiles[(pos[0], pos[1])])

        if type(parsed_data) == type(map.tiles[(pos[0], pos[1])]):
            map.tiles[(pos[0], pos[1])] = parsed_data

            
map = setup()
edit_tile((0,0))

