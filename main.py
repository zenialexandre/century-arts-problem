# Alexandre Zeni

from math import dist, degrees, asin

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
            print('No')
        elif (gift_wrapping_algorithm_result == False):
            print('Yes')

def execute_gift_wrapping_algorithm(art_gallery_dict_points_list: list[list[int]]) -> bool:
    lower_point_list: list[int] = get_lower_point_list(art_gallery_dict_points_list)
    on_hull_point_list: list[int] = lower_point_list
    angles_between_points_list: list[tuple[list[int], int]] = []
    point_counter_clock_wise_list: list[int] = []
    inverse_point_counter_clock_wise_list: list[int] = []
    on_convex_hull_list: list[int] = []
    next_potential_point_list: list[int] = []
    is_points_on_right_side_still_exists: bool = False
    is_next_point_on_same_x_coordinate: bool = False

    while (True):
        on_convex_hull_list.append(on_hull_point_list)
        angles_between_points_list.clear()

        is_points_on_right_side_still_exists = get_is_points_on_right_side_still_exists(
            art_gallery_dict_points_list,
            on_convex_hull_list,
            on_hull_point_list
        )

        populate_angles_between_points_process(
            art_gallery_dict_points_list,
            on_convex_hull_list,
            on_hull_point_list,
            angles_between_points_list,
            is_points_on_right_side_still_exists,
            is_next_point_on_same_x_coordinate
        )       

        if (on_hull_point_list == on_convex_hull_list[0]):
            inverse_point_counter_clock_wise_list = \
                get_inverse_counter_clock_wise_point(angles_between_points_list)

        if (inverse_point_counter_clock_wise_list == on_hull_point_list):
            break

        point_counter_clock_wise_list = get_counter_clock_wise_point(angles_between_points_list)
        next_potential_point_list = point_counter_clock_wise_list
        on_hull_point_list = next_potential_point_list

    return get_is_polygon_with_critical_point(art_gallery_dict_points_list, on_convex_hull_list)

def get_lower_point_list(art_gallery_dict_points_list: list[list[int]]) -> list[int]:
    return min(art_gallery_dict_points_list, key=lambda point: (point[1], point[0]))

def populate_angles_between_points_process(
    art_gallery_dict_points_list: list[list[int]],
    on_convex_hull_list: list[list[int]],
    on_hull_point_list: list[int],
    angles_between_points_list: list[tuple[list[int], int]],
    is_points_on_right_side_still_exists: bool,
    is_next_point_on_same_x_coordinate: bool
) -> None:
    for point_on_iteration_list in art_gallery_dict_points_list:
        if (point_on_iteration_list not in on_convex_hull_list):
            is_next_point_on_same_x_coordinate = get_is_next_point_on_same_x_coordinate(
                on_hull_point_list,
                point_on_iteration_list
            )

            if (
                is_points_on_right_side_still_exists == True \
                and point_on_iteration_list[0] > on_hull_point_list[0]
            ):
                populate_angles_between_points(
                    on_hull_point_list,
                    point_on_iteration_list,
                    angles_between_points_list
                )
            elif (
                is_points_on_right_side_still_exists == False \
                and is_next_point_on_same_x_coordinate == True
            ):
                populate_angles_between_points(
                    on_hull_point_list,
                    point_on_iteration_list,
                    angles_between_points_list
                )
                break
            else:
                populate_angles_between_points(
                    on_hull_point_list,
                    point_on_iteration_list,
                    angles_between_points_list
                )

def get_is_points_on_right_side_still_exists(
    art_gallery_dict_points_list: list[list[int]],
    on_convex_hull_list: list[list[int]],
    on_hull_point_list: list[int]
) -> bool:
    for point_on_iteration_list in art_gallery_dict_points_list:
        if (
            point_on_iteration_list not in on_convex_hull_list \
            and point_on_iteration_list[0] > on_hull_point_list[0]
        ):
            return True
    return False

def get_is_next_point_on_same_x_coordinate(
    on_hull_point_list: list[int],
    point_on_iteration_list: list[int]
) -> bool:
    return True if point_on_iteration_list[0] == on_hull_point_list[0] else False

def populate_angles_between_points(
    on_hull_point_list: list[int],
    point_on_iteration_list: list[int],
    angles_between_points_list: list[tuple[list[int], int]]
) -> None:
    opposite_cathetus: int = abs(point_on_iteration_list[1] - on_hull_point_list[1])
    hypotenuse: float = dist(on_hull_point_list, point_on_iteration_list)
    sine_of_alpha: float = opposite_cathetus / hypotenuse
    alpha_angle: float = degrees(asin(sine_of_alpha))

    angles_between_points_list.append((point_on_iteration_list, alpha_angle))

def get_counter_clock_wise_point(angles_between_points_list: list[tuple[list[int], int]]) -> bool:
    return min(angles_between_points_list, key=lambda my_tuple: my_tuple[1])[0]

def get_inverse_counter_clock_wise_point(angles_between_points_list: list[tuple[list[int], int]]) -> bool:
    return max(angles_between_points_list, key=lambda my_tuple: my_tuple[1])[0]

def get_is_polygon_with_critical_point(
    art_gallery_dict_points_list: list[list[int]],
    on_convex_hull_list: list[list[int]]
) -> bool:
    if (len(on_convex_hull_list) == len(art_gallery_dict_points_list)):
        return True
    elif (len(on_convex_hull_list) < len(art_gallery_dict_points_list)):
        return False

initialize_program()
