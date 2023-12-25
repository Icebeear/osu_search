from django import template

register = template.Library()

@register.filter(name="format_time")
def format_time(seconds: int) -> str:
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"


@register.simple_tag
def set_color(star_rate: int) -> str:
    color_ranges = {
        (1, 2): "#6EFF79",
        (2, 3): "#4FC0FF",
        (3, 4): "#F8DA5E",
        (4, 5): "#FF7F68",
        (5, 6): "#FF4E6F",
        (6, 7): "#A653B0",
        (7, 8): "#3B38B2"
    }

    for key, value in color_ranges.items():
        if key[0] <= star_rate < key[1]:
            return value

    return "#000000"  

    
@register.simple_tag
def set_color_map(map_type: str) -> str:
    colors = {
        "ranked": "#393053",
        "approved": "#6867AC",
        "loved": "#A267AC",
        "graveyard": "#323232",
    }

    return colors[map_type]
    

@register.simple_tag
def format_dif(star: str) -> str:
    return f"{star:.2f}"


@register.simple_tag
def format_labels(val: int) -> str:
    if val < 1000:
        return val
    elif val > 1000000:
        return f"{val // 1000000}m"
    else:
        return f"{val // 1000}k"


@register.simple_tag
def bpm_round(val: str) -> int:
    return int(val)


@register.simple_tag
def get_diff_id(link: str) -> str:
    return link.split("/")[-1]


@register.simple_tag
def title_resize(title: str) -> str:
    if len(title) > 30:
        return title[:27] + "..."
    else:
        return title 