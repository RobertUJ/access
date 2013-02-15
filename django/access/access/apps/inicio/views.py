from django.shortcuts 			import render_to_response
from django.template  			import RequestContext
from django.core.mail 			import EmailMultiAlternatives 
from django.http				import HttpResponseRedirect
from access.apps.inicio.forms 	import ContactForm



def inicio(request):
	return render_to_response('inicio/home.html',context_instance=RequestContext(request))

def contact_view(request):
	info_send = False # Define si se envio la info o no se envio
	name   = ""
	email  = ""
	subject = ""
	content  = ""
	if request.method == "POST":
		objForm = ContactForm(request.POST)
		if objForm.is_valid():
			info_send  = True
			name    = objForm.cleaned_data['Name']
			email   = objForm.cleaned_data['Email']
			subject = objForm.cleaned_data['Subject']
			content = objForm.cleaned_data['Content']
			# Configuracion para envio de email por gmail
			to_admin = 'roberto@newemage.com'
			html_content = "Information received from <br>Name: [%s] <br> Email: [%s]  <br><br>***Message<br><br>%s"%(name,email,content)
			msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
			msg.send() #enviamos el correo
	else:
		objForm = ContactForm()
	ctx = {'form':objForm,'name':name,'email':email,'subject':subject,'content':content,'info_send':info_send}
	return render_to_response('forms/contact/contact.html',ctx,context_instance=RequestContext(request))	


