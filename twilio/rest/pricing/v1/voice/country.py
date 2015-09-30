# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class CountryList(ListResource):

    def __init__(self, version):
        """
        Initialize the CountryList
        
        :param Version version: Version that contains the resource
        
        :returns: CountryList
        :rtype: CountryList
        """
        super(CountryList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = '/Voice/Countries'.format(**self._kwargs)

    def stream(self, limit=None, page_size=None, **kwargs):
        """
        Streams CountryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            CountryInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        """
        Reads CountryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        """
        Retrieve a single page of CountryInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of CountryInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            CountryInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def get(self, iso_country):
        """
        Constructs a CountryContext
        
        :param iso_country: The iso_country
        
        :returns: CountryContext
        :rtype: CountryContext
        """
        return CountryContext(self._version, iso_country=iso_country, **self._kwargs)

    def __call__(self, iso_country):
        """
        Constructs a CountryContext
        
        :param iso_country: The iso_country
        
        :returns: CountryContext
        :rtype: CountryContext
        """
        return CountryContext(self._version, iso_country=iso_country, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.CountryList>'


class CountryContext(InstanceContext):

    def __init__(self, version, iso_country):
        """
        Initialize the CountryContext
        
        :param Version version
        :param iso_country: The iso_country
        
        :returns: CountryContext
        :rtype: CountryContext
        """
        super(CountryContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'iso_country': iso_country,
        }
        self._uri = '/Voice/Countries/{iso_country}'.format(**self._kwargs)

    def fetch(self):
        """
        Fetch a CountryInstance
        
        :returns: Fetched CountryInstance
        :rtype: CountryInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            CountryInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Pricing.V1.CountryContext {}>'.format(context)


class CountryInstance(InstanceResource):

    def __init__(self, version, payload, iso_country=None):
        """
        Initialize the CountryInstance
        
        :returns: CountryInstance
        :rtype: CountryInstance
        """
        super(CountryInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'country': payload['country'],
            'iso_country': payload['iso_country'],
            'url': payload['url'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'iso_country': iso_country or self._properties['iso_country'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: CountryContext for this CountryInstance
        :rtype: CountryContext
        """
        if self._instance_context is None:
            self._instance_context = CountryContext(
                self._version,
                self._kwargs['iso_country'],
            )
        return self._instance_context

    @property
    def country(self):
        """
        :returns: The country
        :rtype: str
        """
        return self._properties['country']

    @property
    def iso_country(self):
        """
        :returns: The iso_country
        :rtype: str
        """
        return self._properties['iso_country']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: str
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a CountryInstance
        
        :returns: Fetched CountryInstance
        :rtype: CountryInstance
        """
        return self._context.fetch()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Pricing.V1.CountryInstance {}>'.format(context)
