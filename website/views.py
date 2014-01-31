from django.shortcuts import render_to_response

# Vista inicial del sitio
def home(solicitud):
	return render_to_response('website/home.html')

