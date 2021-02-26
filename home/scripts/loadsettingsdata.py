from django.core.management import call_command


def run():
    call_command('loaddata', 'settings.json')
    
