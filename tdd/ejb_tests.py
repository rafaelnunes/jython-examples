# -*- coding: utf-8 -*-
'''
Created on May 05, 2012

@author: Rafael Nunes
'''
import unittest

from tdd.lookup_properties import  *
from java.util import Hashtable
from javax.naming import InitialContext, NoInitialContextException
from javax.persistence import TransactionRequiredException

class TestEJBLookup(unittest.TestCase):
    
    def setUp(self):
        self.ejb = self.lookup(EJB_JYTHON)
        
    def etest_sum(self):
        self.assertEqual(self.ejb.sum(1), 2)
        
    def test_transaction(self):
        self.assertRaises(TransactionRequiredException, self.ejb.transaction_sum(EJB_JYTHON))
        
    def lookup(self, ejbName):
        properties = Hashtable();
        properties.put(FACTORY_INITIAL_KEY, FACTORY_INITIAL_VALUE);
        properties.put(FACTORY_URLPKGS_KEY, FACTORY_URLPKGS_VALUE);
        properties.put(PROVIDER_URL_KEY, PROVIDER_URL_VALUE);
        
        mylookup = None
        try:
            context = InitialContext(properties);
            mylookup = context.lookup(ejbName)
        except NoInitialContextException, err:
            raise Exception("Error with EJB connection[localhost:1099]\n" + str(err))
        return mylookup
        