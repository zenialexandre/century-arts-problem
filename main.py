import math

def initialize_program() -> None:
    arts_counter: int = 0
    art_gallery_dict: dict = {}
    corner_points_number: int = int(input())

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

def populate_art_gallery(art_gallery_dict: dict, arts_counter: int) -> None:
    art_gallery_dict_key: str = f'art_{arts_counter}'
    x_coordinate: int = int(input())
    y_coordinate: int = int(input())

    if (art_gallery_dict_key not in art_gallery_dict):
        art_gallery_dict[art_gallery_dict_key] = []

    while (
        (x_coordinate >= 0 and x_coordinate <= 1000) \
        and (y_coordinate >= 0 and y_coordinate <= 1000)
    ):
        art_gallery_dict[art_gallery_dict_key].append([x_coordinate, y_coordinate])
        break

def search_for_polygon_critical_point(art_gallery_dict: dict) -> None:
    gift_wrapping_algorithm_result: bool = False

    for _, art_gallery_dict_points_list in art_gallery_dict.items():
        gift_wrapping_algorithm_result = execute_gift_wrapping_algorithm(art_gallery_dict_points_list)

        if (gift_wrapping_algorithm_result == True):
            # Does NOT have a critical point (Convex).
            print('No')
        elif (gift_wrapping_algorithm_result == False):
            # Have a critical point (Not Convex).
            print('Yes')

def execute_gift_wrapping_algorithm(art_gallery_dict_points_list: list[list[int]]) -> bool:
    lower_point_list: list[int] = get_lower_point_list(art_gallery_dict_points_list)
    on_hull_point_list: list[int] = lower_point_list
    angles_between_points_list: list[tuple[list[int], int]] = []
    point_counter_clock_wise_list: list[int] = []
    inverse_point_counter_clock_wise_list: list[int] = []
    on_convex_hull_list: list[int] = []
    next_potential_point_list: list[int] = []

    while (True):
        on_convex_hull_list.append(on_hull_point_list)
        angles_between_points_list.clear()

        for point_on_iteration_list in art_gallery_dict_points_list:
            if (point_on_iteration_list not in on_convex_hull_list):
                populate_angles_between_points(
                    on_hull_point_list,
                    point_on_iteration_list,
                    angles_between_points_list
                )

        if (on_hull_point_list == on_convex_hull_list[0]):
            inverse_point_counter_clock_wise_list = \
                get_inverse_counter_clock_wise_point(angles_between_points_list)

        if (inverse_point_counter_clock_wise_list == on_hull_point_list):
            break

        point_counter_clock_wise_list = get_counter_clock_wise_point(angles_between_points_list)
        next_potential_point_list = point_counter_clock_wise_list
        on_hull_point_list = next_potential_point_list

    if (len(on_convex_hull_list) == len(art_gallery_dict_points_list)):
        return True
    elif (len(on_convex_hull_list) < len(art_gallery_dict_points_list)):
        return False

def get_lower_point_list(art_gallery_dict_points_list: list[list[int]]) -> list[int]:
    return min(art_gallery_dict_points_list, key=lambda point: (point[1], point[0]))

def populate_angles_between_points(
    on_hull_point_list: list[int],
    point_on_iteration_list: list[int],
    angles_between_points_list: list[tuple[list[int], int]]
) -> None:
    opposite_cathetus: int = abs(point_on_iteration_list[1] - on_hull_point_list[1])
    hypotenuse: float = math.dist(on_hull_point_list, point_on_iteration_list)
    sine_of_alpha: float = opposite_cathetus / hypotenuse
    alpha_angle: float = math.degrees(math.asin(sine_of_alpha))

    angles_between_points_list.append((point_on_iteration_list, alpha_angle))

def get_counter_clock_wise_point(angles_between_points_list: list[tuple[list[int], int]]) -> bool:
    return min(angles_between_points_list, key=lambda my_tuple: my_tuple[1])[0]

def get_inverse_counter_clock_wise_point(angles_between_points_list: list[tuple[list[int], int]]) -> bool:
    return max(angles_between_points_list, key=lambda my_tuple: my_tuple[1])[0]

initialize_program()
