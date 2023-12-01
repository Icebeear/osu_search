from django import template

register = template.Library()

@register.filter(name="format_time")
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"

@register.simple_tag
def set_color(star):
    if 1 <= star < 2:
        return "#6EFF79"
    elif 2 <= star < 3:
        return "#4FC0FF"
    elif 3 <= star < 4:
        return "#F8DA5E"
    elif 4 <= star < 5:
        return "#FF7F68"
    elif 5 <= star < 6:
        return "#FF4E6F"
    elif 6 <= star < 7:
        return "#A653B0"
    elif 7 <= star < 8:
        return "#3B38B2"
    else:
        return "#000000"
    
@register.simple_tag
def set_color_map(map_type):
    colors = {
        "ranked": "#393053",
        "approved": "#6867AC",
        "loved": "#A267AC",
        "graveyard": "#323232",
    }

    return colors[map_type]
    
@register.simple_tag
def format_dif(star):
    return f"{star:.2f}"

@register.simple_tag
def format_labels(val):
    if val < 1000:
        return val
    elif val > 1000000:
        return f"{val // 1000000}m"
    else:
        return f"{val // 1000}k"

@register.simple_tag
def bpm_round(val):
    return int(val)

@register.simple_tag
def get_diff_id(link):
    return link.split("/")[-1]

@register.simple_tag
def title_resize(title):
    if len(title) > 30:
        return title[:27] + "..."
    else:
        return title 