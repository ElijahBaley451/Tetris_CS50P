# class which stores colors used by game in dict


class Colors:
    @classmethod
    def get_color(cls):
        return {
            0: (26, 31, 40),  # grey
            1: (232, 18, 18),  # red
            2: (31, 64, 216),  # blue
            3: (47, 230, 23),  # green
            4: (237, 234, 4),  # yellow
            5: (226, 116, 17),  # orange
            6: (166, 0, 247),  # purple
            7: (21, 204, 209),  # cyan
        }
