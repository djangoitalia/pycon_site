from datetime import date
from django.utils.translation import ugettext_lazy as _

def highlight(request):
    """
    Aggiunge il messaggio da mostrare in tutte le pagine
    """
    deadline = date(year = 2009, month = 4, day = 13)
    t = deadline - date.today()

    if t.days > 0:
        msg = _("Mancano solo *%(days)d giorni* alla fine dell'Early Bird.")
        msg = (msg % {'days': t.days}).replace('*', '<strong>', 1).replace('*', '</strong>')
    elif t.days == 0:
        msg = _("L'Early Bird finisce oggi!")
    else:
        msg = None
        
    if msg:
        msg = '<a href="/2009/registrazione/">' + msg + '</a>'
    return { 'HIGHLIGHT': msg }