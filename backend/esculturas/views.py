# encoding:utf-8
from django.shortcuts import render, HttpResponse
import urllib2
import simplejson
from esculturas.models import Escultura

#url base de la api de esculturas
base_url = "http://resistenciarte.org/api/v1/node/"

#se conecta a la api de esculturas, transforma los datos, agrega las fotos 360 y devuelve el json
def get_data(request):
	
	esculturas = Escultura.objects.all()
	response = []
	callback_name = request.GET.get("callback", "callback")

	for e in esculturas:

		resp = urllib2.Request(base_url + e.id_api)
		opener = urllib2.build_opener()
		data = opener.open(resp)
		result = simplejson.load(data)

		autor_id = result.get('field_autor').get("und")[0].get('target_id')
		autor_id
		autor = urllib2.Request(base_url + autor_id)
		opener_autor = urllib2.build_opener()
		data_autor = opener_autor.open(autor)
		autor_dict = simplejson.load(data_autor)
		
		images = []
		for i in e.imagen_set.all():
			images.append(i.imagen.url)

		escultura = {
			'title': result.get('title'),
			'anio': result.get('field_ano').get("und")[0].get('value'),
			'ubicacion': result.get('field_ubicacion').get("und")[0].get('value'),
			'longitud': result.get('field_mapa').get("und")[0].get('lon'),
			'latitud': result.get('field_mapa').get("und")[0].get('lat'),
			'autor': autor_dict.get('title'),
			'fotos': images
		}



		response.append(escultura)

	return HttpResponse(callback_name+"("+simplejson.dumps(response)+");", content_type='application/json')
