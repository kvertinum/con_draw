import typing


def add_str(source_list: typing.List[str], pos: typing.Tuple[int], string: str):
    x, y = pos
    temp_list = source_list.copy()

    source_ind = y - 1
    line = temp_list[source_ind]

    stard_ind = x - 1
    line_start = line[:stard_ind]

    end_ind = len(string) + x - 1
    line_end = line[end_ind:]

    temp_list[source_ind] = line_start + string + line_end

    return temp_list
