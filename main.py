import math

def initialize_program() -> None:
    arts_counter:int = 0
    art_gallery_dict:dict = {}
    corner_points_number:int = int(input())

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

def populate_art_gallery(art_gallery_dict:dict, arts_counter:int) -> None:
    art_gallery_dict_key:str = f'art_{arts_counter}'
    x_coordinate:int = int(input())
    y_coordinate:int = int(input())

    if (art_gallery_dict_key not in art_gallery_dict):
        art_gallery_dict[art_gallery_dict_key] = []

    while (
        (x_coordinate >= 0 and x_coordinate <= 1000) \
        and (y_coordinate >= 0 and y_coordinate <= 1000)
    ):
        art_gallery_dict[art_gallery_dict_key].append([x_coordinate, y_coordinate])
        break

def search_for_polygon_critical_point(art_gallery_dict:dict) -> None:
    gift_wrapping_algorithm_result:bool = False

    for _, art_gallery_dict_points_array in art_gallery_dict.items():
        gift_wrapping_algorithm_result = execute_gift_wrapping_algorithm(art_gallery_dict_points_array)

        if (gift_wrapping_algorithm_result == True):
            # Does NOT have a critical point (Convex).
            print('No')
        elif (gift_wrapping_algorithm_result == False):
            # Have a critical point (Not Convex).
            print('Yes')

def execute_gift_wrapping_algorithm(art_gallery_dict_points_array:list[list[int]]) -> bool:
    lower_point_array:list[int] = min(art_gallery_dict_points_array, key=lambda point: point[1])
    on_hull_point_array:list[int] = lower_point_array
    angles_between_points_tuple:list[tuple[list[int], int]] = []
    point_counter_clock_wise_array:list[int] = []
    hull_array:list[int] = []
    next_potential_point_array:list[int] = []

    while (True):
        hull_array.append(on_hull_point_array)

        for point_on_iteration_array in art_gallery_dict_points_array:
            if (point_on_iteration_array not in hull_array):
                populate_angles_between_points(
                    on_hull_point_array,
                    point_on_iteration_array,
                    angles_between_points_tuple
                )

        point_counter_clock_wise_array = get_is_point_counter_clock_wise(
            point_on_iteration_array,
            angles_between_points_tuple
        )

        next_potential_point_array = point_counter_clock_wise_array
        on_hull_point_array = next_potential_point_array

        if (next_potential_point_array == lower_point_array):
            break

    if (len(hull_array) == len(art_gallery_dict_points_array)):
        return True
    elif (len(hull_array) < len(art_gallery_dict_points_array)):
        return False

def populate_angles_between_points(
    on_hull_point_array:list[int],
    point_on_iteration_array:list[int],
    angles_between_points_tuple:list[tuple[list[int], int]]
) -> None:
    opposite_side_value:int = abs(on_hull_point_array[1] - point_on_iteration_array[1])
    adjacent_side_value:int = abs(on_hull_point_array[0] - point_on_iteration_array[0])
    hypotenuse:int = abs(math.hypot(opposite_side_value, adjacent_side_value))
    sine_angle:int = math.degrees(abs(opposite_side_value / hypotenuse))

    angles_between_points_tuple.append(point_on_iteration_array, sine_angle)

def get_is_point_counter_clock_wise(
    point_on_iteration_array:list[int],
    angles_between_points_tuple:tuple[list[int], int]
) -> bool:
    return False

initialize_program()
