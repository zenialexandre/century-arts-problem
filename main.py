def initialize_program() -> None:
    arts_counter = 0
    art_gallery_dict = {}
    corner_points_number = int(input())

    while (
        corner_points_number > 0 \
        and corner_points_number >= 3 \
        and corner_points_number <= 50
    ):
        arts_counter = arts_counter + 1

        for _ in range(corner_points_number):
            populate_art_gallery(art_gallery_dict, arts_counter)

        corner_points_number = int(input())

    validateConvexPolygons(art_gallery_dict)

def populate_art_gallery(art_gallery_dict, arts_counter) -> None:
    art_gallery_dict_key = f'art_{arts_counter}'
    x_coordinate = int(input())
    y_coordinate = int(input())

    if (art_gallery_dict_key not in art_gallery_dict):
        art_gallery_dict[art_gallery_dict_key] = []

    while (
        (x_coordinate >= 0 and x_coordinate <= 1000) \
        and (y_coordinate >= 0 and y_coordinate <= 1000)
    ):
        art_gallery_dict[art_gallery_dict_key].append([x_coordinate, y_coordinate])
        break

def validateConvexPolygons(art_gallery_dict) -> None:
    print('\n')
    vectorial_product = 0

    for _, art_gallery_dict_points_array in art_gallery_dict.items():
        vectorial_product = get_vectorial_product_calculated(art_gallery_dict_points_array)

        if (vectorial_product > 0.000001):
            print('No\n')
        elif (vectorial_product < 0.000001):
            print('Yes\n')

def get_vectorial_product_calculated(art_gallery_dict_points_array) -> float:
    vector_first_second_points = [
        art_gallery_dict_points_array[1][0] - art_gallery_dict_points_array[0][0],
        art_gallery_dict_points_array[1][1] - art_gallery_dict_points_array[0][1]
    ]

    vector_first_third_points = [
        art_gallery_dict_points_array[2][0] - art_gallery_dict_points_array[0][0],
        art_gallery_dict_points_array[2][1] - art_gallery_dict_points_array[0][1]
    ]

    return abs(
        vector_first_second_points[0] * vector_first_third_points[1] \
            - vector_first_second_points[1] * vector_first_third_points[0]
    )

initialize_program()
