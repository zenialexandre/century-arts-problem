def initialize_program() -> None:
    corner_points_number = int(input())

    while (
        corner_points_number > 0 \
        and corner_points_number >= 3 \
        and corner_points_number <= 50
    ):
        art_gallery_dict = {}

        for corner_points_number_row in range(corner_points_number):
            populate_art_gallery(art_gallery_dict, corner_points_number_row)

        corner_points_number = int(input())

    print(art_gallery_dict)

def populate_art_gallery(art_gallery_dict, corner_points_number_row) -> dict:
    art_gallery_dict_key = f'art_{corner_points_number_row}'
    x_coordinate = int(input())
    y_coordinate = int(input())

    while (
        (x_coordinate >= 0 and x_coordinate <= 1000) \
        and (y_coordinate >= 0 and y_coordinate <= 1000)
    ):
        art_gallery_dict[art_gallery_dict_key] = [x_coordinate, y_coordinate]
        break

    return art_gallery_dict

initialize_program()
