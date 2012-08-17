# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseNotFound
from java.util import Hashtable
from javax.naming import InitialContext
from javax.naming import CommunicationException
from django.conf import settings
import lookup_properties
    
def lookup(ejbName):
    properties = Hashtable();
    properties.put(lookup_properties.FACTORY_INITIAL_KEY, lookup_properties.FACTORY_INITIAL_VALUE);
    properties.put(lookup_properties.FACTORY_URLPKGS_KEY, lookup_properties.FACTORY_URLPKGS_VALUE);
    properties.put(lookup_properties.PROVIDER_URL_KEY, lookup_properties.PROVIDER_URL_VALUE);
    
    context = InitialContext(properties);
    mylookup = None
    try:
        mylookup = context.lookup(ejbName)
    except CommunicationException, err:
        raise Exception("Error with EJB connection[" + settings.SERVIDOR + ":1099]\n" + str(err))
    return mylookup


