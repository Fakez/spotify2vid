from django import template
register = template.Library()

@register.simple_tag
def format_milliseconds_to_minute_format(time_in_ms):
    millis = int(time_in_ms)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    #hours=(millis/(1000*60*60))%24
    minutes = str(minutes)
    seconds = str(seconds)
    if len(seconds) == 1: seconds = f'0{seconds}'

    return f'{minutes}:{seconds}'

@register.simple_tag
def format_artists_to_string(artists):
    return ', '.join([ x['name'] for x in artists if x['name'] ])
