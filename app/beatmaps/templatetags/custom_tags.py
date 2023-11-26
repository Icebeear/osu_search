from django import template

register = template.Library()

@register.filter(name="format_time")
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"

@register.simple_tag
def set_color(star):
    if star >= 1 and star < 2:
        return "#6EFF79"
    elif star >= 2 and star < 3:
        return "#4FC0FF"
    elif star >= 3 and star < 4:
        return "#F8DA5E"
    elif star >= 4 and star < 5:
        return "#FF7F68"
    elif star >= 5 and star < 6:
        return "#FF4E6F"
    elif star >= 6 and star < 7:
        return "#A653B0"
    elif star >= 7 and star < 8:
        return "#3B38B2"
    else:
        return "#000000"
    
@register.simple_tag
def format_dif(star):
    return round(star, 2)


@register.simple_tag
def format_labels(val):
    return f"{val // 1000}k"