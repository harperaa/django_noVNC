from django.shortcuts import render
from django.conf import settings
def run_vnc(request):
    '''
        Call the VNC proxy for remote control
    '''
    # template = loader.get_template('vnc_auto.html')

    # token = token  # Used to determine the different access machine
    view_only = request.GET.get('view_only', 'false') # False can control the or true can only view
    #token = request.GET.get('token')
    token = 'abc'
    # The proxy server IP and port, this usually use school server LAN IP (127.0.0.1, 6080 is the default port)
    client = request.environ['REMOTE_ADDR']
    host = request.get_host().split(':')[0]
    print "VNC Connection Request: " + client + " => " + host
    
    port = settings.VNC_PROXY_PORT

    # context = Context({'token':token, 'host':host, 'port': port, 'view_only':view_only})
    context_dict = {'token':token, 'host': host, 'port': port, 'view_only': view_only}

    return render(request, 'vnc_auto.html', context_dict)
    #return render(request, 'vnc.html')
