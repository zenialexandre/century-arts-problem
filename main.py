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

    search_for_polygon_critical_point(art_gallery_dict)

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

def search_for_polygon_critical_point(art_gallery_dict) -> None:
    for _, art_gallery_dict_points_array in art_gallery_dict.items():
       print(execute_gift_wrapping_algorithm(art_gallery_dict_points_array))

def execute_gift_wrapping_algorithm(art_gallery_dict_points_array) -> str:
    leftmost_point_array = min(art_gallery_dict_points_array, key=lambda point: point[1])
    on_hull_point_array = leftmost_point_array
    orientation = False
    hull_array = []
    next_potential_point_array = []

    while (True):
        hull_array.append(on_hull_point_array)
        next_potential_point_array = art_gallery_dict_points_array[0]

        for point_on_iteration_array in art_gallery_dict_points_array:
            orientation = get_orientation(
                on_hull_point_array,
                next_potential_point_array,
                point_on_iteration_array
            )

            if (next_potential_point_array == on_hull_point_array or orientation == True):
                next_potential_point_array = point_on_iteration_array

        on_hull_point_array = next_potential_point_array

        if (next_potential_point_array == hull_array[0]):
            return 'No'
        else:
            return 'Yes'

def get_orientation(
        on_hull_point_array,
        next_potential_point_array,
        point_array
) -> bool:
    vectorial_product = get_vectorial_product_calculated(
        on_hull_point_array,
        next_potential_point_array,
        point_array
    )
    return get_is_counter_clock_wise(vectorial_product)

def get_vectorial_product_calculated(
        on_hull_point_array,
        next_potential_point_array,
        point_on_iteration_array
) -> float:
    return (next_potential_point_array[0] - on_hull_point_array[0]) * (point_on_iteration_array[1] - on_hull_point_array[1]) - \
        (next_potential_point_array[1] - on_hull_point_array[1]) * (point_on_iteration_array[0] - on_hull_point_array[0])

def get_is_counter_clock_wise(vectorial_product) -> bool:
    if (vectorial_product < 0.000001):
        return True
    elif (vectorial_product > 0.000001):
        return False

initialize_program()
