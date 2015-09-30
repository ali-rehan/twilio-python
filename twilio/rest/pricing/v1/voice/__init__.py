# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.pricing.v1.voice.country import CountryList
from twilio.rest.pricing.v1.voice.number import NumberContext


class VoiceList(ListResource):

    def __init__(self, version):
        """
        Initialize the VoiceList
        
        :param Version version: Version that contains the resource
        
        :returns: VoiceList
        :rtype: VoiceList
        """
        super(VoiceList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = 'None'.format(**self._kwargs)
        
        # Components
        self._numbers = None
        self._countries = None

    @property
    def numbers(self):
        """
        Access the numbers
        
        :returns: NumberContext
        :rtype: NumberContext
        """
        if self._numbers is None:
            self._numbers = NumberContext(self._version, **self._kwargs)
        return self._numbers

    @property
    def countries(self):
        """
        Access the countries
        
        :returns: CountryList
        :rtype: CountryList
        """
        if self._countries is None:
            self._countries = CountryList(self._version, **self._kwargs)
        return self._countries

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.VoiceList>'


class VoiceInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the VoiceInstance
        
        :returns: VoiceInstance
        :rtype: VoiceInstance
        """
        super(VoiceInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'name': payload['name'],
            'url': payload['url'],
            'links': payload['links'],
        }

    @property
    def name(self):
        """
        :returns: The name
        :rtype: str
        """
        return self._properties['name']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: str
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: str
        """
        return self._properties['links']

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.VoiceInstance>'
