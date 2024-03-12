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
    is_polygon_not_convex = ''

    for _, art_gallery_dict_points_array in art_gallery_dict.items():
       is_polygon_not_convex = execute_gift_wrapping_algorithm(art_gallery_dict_points_array)
       print(is_polygon_not_convex)

def execute_gift_wrapping_algorithm(art_gallery_dict_points_array) -> str:
    print(art_gallery_dict_points_array)
    leftmost_point_array = min(art_gallery_dict_points_array, key=lambda point: point[0])
    print('leftmost: ', leftmost_point_array)
    hull_array = []
    endpoint = []
    loop_counter = 1

    p = leftmost_point_array
    q = 0

    while (loop_counter > 0):
        hull_array.append(p)
        print('hull_array: ', hull_array)
        print('len: ', len(art_gallery_dict_points_array))

        endpoint = art_gallery_dict_points_array[0]

        q = (p + 1) % len(art_gallery_dict_points_array)

        for i in range(len(art_gallery_dict_points_array)):
            if (endpoint == p or ):
                q = i
        
        p = q

        if (p == 1):
            return 'Yes'

    return 'No'

def get_clockwise_orientation(
        first_point_array,
        second_point_array,
        third_point_array
) -> int:
    vectorial_product = get_vectorial_product_calculated(
        first_point_array,
        second_point_array,
        third_point_array
    )

    if (vectorial_product == 0):
        return 0
    elif (vectorial_product > 0):
        return 1
    else:
        return 2

def get_vectorial_product_calculated(
        first_point_array,
        second_point_array,
        third_point_array
) -> float:    
    return (second_point_array[1] - first_point_array[1]) * (third_point_array[0] - second_point_array[0]) - \
        (second_point_array[0] - first_point_array[0]) * (third_point_array[1] - second_point_array[1])

initialize_program()
