# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.api.v2010.account.incoming_phone_number.local import LocalList
from twilio.rest.api.v2010.account.incoming_phone_number.mobile import MobileList
from twilio.rest.api.v2010.account.incoming_phone_number.toll_free import TollFreeList
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class IncomingPhoneNumberList(ListResource):

    def __init__(self, version, owner_account_sid):
        """
        Initialize the IncomingPhoneNumberList
        
        :param Version version: Version that contains the resource
        :param owner_account_sid: A 34 character string that uniquely identifies this resource.
        
        :returns: IncomingPhoneNumberList
        :rtype: IncomingPhoneNumberList
        """
        super(IncomingPhoneNumberList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'owner_account_sid': owner_account_sid,
        }
        self._uri = '/Accounts/{owner_account_sid}/IncomingPhoneNumbers.json'.format(**self._kwargs)
        
        # Components
        self._local = None
        self._mobile = None
        self._toll_free = None

    def stream(self, beta=values.unset, friendly_name=values.unset,
               phone_number=values.unset, limit=None, page_size=None, **kwargs):
        """
        Streams IncomingPhoneNumberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param bool beta: Include new phone numbers
        :param str friendly_name: Filter by friendly name
        :param str phone_number: Filter by incoming phone number
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
            'Beta': beta,
            'FriendlyName': friendly_name,
            'PhoneNumber': phone_number,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            IncomingPhoneNumberInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, limit=None, page_size=None, **kwargs):
        """
        Reads IncomingPhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param bool beta: Include new phone numbers
        :param str friendly_name: Filter by friendly name
        :param str phone_number: Filter by incoming phone number
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
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        """
        Retrieve a single page of IncomingPhoneNumberInstance records from the API.
        Request is executed immediately
        
        :param bool beta: Include new phone numbers
        :param str friendly_name: Filter by friendly name
        :param str phone_number: Filter by incoming phone number
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of IncomingPhoneNumberInstance
        :rtype: Page
        """
        params = values.of({
            'Beta': beta,
            'FriendlyName': friendly_name,
            'PhoneNumber': phone_number,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            IncomingPhoneNumberInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, api_version=values.unset, friendly_name=values.unset,
               sms_application_sid=values.unset, sms_fallback_method=values.unset,
               sms_fallback_url=values.unset, sms_method=values.unset,
               sms_url=values.unset, status_callback=values.unset,
               status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset,
               phone_number=values.unset, area_code=values.unset):
        """
        Create a new IncomingPhoneNumberInstance
        
        :param str api_version: The Twilio Rest API version to use
        :param str friendly_name: A human readable description of this resource
        :param str sms_application_sid: Unique string that identifies the application
        :param str sms_fallback_method: HTTP method used with sms fallback url
        :param str sms_fallback_url: URL Twilio will request if an error occurs in executing TwiML
        :param str sms_method: HTTP method to use with sms url
        :param str sms_url: URL Twilio will request when receiving an SMS
        :param str status_callback: URL Twilio will use to pass status parameters
        :param str status_callback_method: HTTP method twilio will use with status callback
        :param str voice_application_sid: The unique sid of the application to handle this number
        :param bool voice_caller_id_lookup: Look up the caller's caller-ID
        :param str voice_fallback_method: HTTP method used with fallback_url
        :param str voice_fallback_url: URL Twilio will request when an error occurs in TwiML
        :param str voice_method: HTTP method used with the voice url
        :param str voice_url: URL Twilio will request when receiving a call
        :param str phone_number: The phone number
        :param str area_code: The desired area code for the new number
        
        :returns: Newly created IncomingPhoneNumberInstance
        :rtype: IncomingPhoneNumberInstance
        """
        data = values.of({
            'PhoneNumber': phone_number,
            'AreaCode': area_code,
            'ApiVersion': api_version,
            'FriendlyName': friendly_name,
            'SmsApplicationSid': sms_application_sid,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceApplicationSid': voice_application_sid,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
        })
        
        return self._version.create(
            IncomingPhoneNumberInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def local(self):
        """
        Access the local
        
        :returns: LocalList
        :rtype: LocalList
        """
        if self._local is None:
            self._local = LocalList(self._version, **self._kwargs)
        return self._local

    @property
    def mobile(self):
        """
        Access the mobile
        
        :returns: MobileList
        :rtype: MobileList
        """
        if self._mobile is None:
            self._mobile = MobileList(self._version, **self._kwargs)
        return self._mobile

    @property
    def toll_free(self):
        """
        Access the toll_free
        
        :returns: TollFreeList
        :rtype: TollFreeList
        """
        if self._toll_free is None:
            self._toll_free = TollFreeList(self._version, **self._kwargs)
        return self._toll_free

    def get(self, sid):
        """
        Constructs a IncomingPhoneNumberContext
        
        :param sid: Fetch by unique incoming-phone-number Sid
        
        :returns: IncomingPhoneNumberContext
        :rtype: IncomingPhoneNumberContext
        """
        return IncomingPhoneNumberContext(self._version, sid=sid, **self._kwargs)

    def __call__(self, sid):
        """
        Constructs a IncomingPhoneNumberContext
        
        :param sid: Fetch by unique incoming-phone-number Sid
        
        :returns: IncomingPhoneNumberContext
        :rtype: IncomingPhoneNumberContext
        """
        return IncomingPhoneNumberContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IncomingPhoneNumberList>'


class IncomingPhoneNumberContext(InstanceContext):

    def __init__(self, version, owner_account_sid, sid):
        """
        Initialize the IncomingPhoneNumberContext
        
        :param Version version
        :param owner_account_sid: The owner_account_sid
        :param sid: Fetch by unique incoming-phone-number Sid
        
        :returns: IncomingPhoneNumberContext
        :rtype: IncomingPhoneNumberContext
        """
        super(IncomingPhoneNumberContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'owner_account_sid': owner_account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{owner_account_sid}/IncomingPhoneNumbers/{sid}.json'.format(**self._kwargs)

    def update(self, account_sid=values.unset, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset):
        """
        Update the IncomingPhoneNumberInstance
        
        :param str account_sid: The new owner of the phone number
        :param str api_version: The Twilio REST API version to use
        :param str friendly_name: A human readable description of this resource
        :param str sms_application_sid: Unique string that identifies the application
        :param str sms_fallback_method: HTTP method used with sms fallback url
        :param str sms_fallback_url: URL Twilio will request if an error occurs in executing TwiML
        :param str sms_method: HTTP method to use with sms url
        :param str sms_url: URL Twilio will request when receiving an SMS
        :param str status_callback: URL Twilio will use to pass status parameters
        :param str status_callback_method: HTTP method twilio will use with status callback
        :param str voice_application_sid: The unique sid of the application to handle this number
        :param bool voice_caller_id_lookup: Look up the caller's caller-ID
        :param str voice_fallback_method: HTTP method used with fallback_url
        :param str voice_fallback_url: URL Twilio will request when an error occurs in TwiML
        :param str voice_method: HTTP method used with the voice url
        :param str voice_url: URL Twilio will request when receiving a call
        
        :returns: Updated IncomingPhoneNumberInstance
        :rtype: IncomingPhoneNumberInstance
        """
        data = values.of({
            'AccountSid': account_sid,
            'ApiVersion': api_version,
            'FriendlyName': friendly_name,
            'SmsApplicationSid': sms_application_sid,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceApplicationSid': voice_application_sid,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
        })
        
        return self._version.update(
            IncomingPhoneNumberInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def fetch(self):
        """
        Fetch a IncomingPhoneNumberInstance
        
        :returns: Fetched IncomingPhoneNumberInstance
        :rtype: IncomingPhoneNumberInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            IncomingPhoneNumberInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        """
        Deletes the IncomingPhoneNumberInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.IncomingPhoneNumberContext {}>'.format(context)


class IncomingPhoneNumberInstance(InstanceResource):

    def __init__(self, version, payload, owner_account_sid, sid=None):
        """
        Initialize the IncomingPhoneNumberInstance
        
        :returns: IncomingPhoneNumberInstance
        :rtype: IncomingPhoneNumberInstance
        """
        super(IncomingPhoneNumberInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'address_requirements': payload['address_requirements'],
            'api_version': payload['api_version'],
            'beta': payload['beta'],
            'capabilities': payload['capabilities'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'phone_number': payload['phone_number'],
            'sid': payload['sid'],
            'sms_application_sid': payload['sms_application_sid'],
            'sms_fallback_method': payload['sms_fallback_method'],
            'sms_fallback_url': payload['sms_fallback_url'],
            'sms_method': payload['sms_method'],
            'sms_url': payload['sms_url'],
            'status_callback': payload['status_callback'],
            'status_callback_method': payload['status_callback_method'],
            'uri': payload['uri'],
            'voice_application_sid': payload['voice_application_sid'],
            'voice_caller_id_lookup': payload['voice_caller_id_lookup'],
            'voice_fallback_method': payload['voice_fallback_method'],
            'voice_fallback_url': payload['voice_fallback_url'],
            'voice_method': payload['voice_method'],
            'voice_url': payload['voice_url'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'owner_account_sid': owner_account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: IncomingPhoneNumberContext for this IncomingPhoneNumberInstance
        :rtype: IncomingPhoneNumberContext
        """
        if self._instance_context is None:
            self._instance_context = IncomingPhoneNumberContext(
                self._version,
                self._kwargs['owner_account_sid'],
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The unique sid that identifies this account
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def address_requirements(self):
        """
        :returns: Indicates if the customer requires an address
        :rtype: incoming_phone_number.address_requirement
        """
        return self._properties['address_requirements']

    @property
    def api_version(self):
        """
        :returns: The Twilio REST API version to use
        :rtype: str
        """
        return self._properties['api_version']

    @property
    def beta(self):
        """
        :returns: Indicates if the phone number is a beta number
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def capabilities(self):
        """
        :returns: Indicate if a phone can receive calls or messages
        :rtype: str
        """
        return self._properties['capabilities']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resouce
        :rtype: str
        """
        return self._properties['friendly_name']

    @property
    def phone_number(self):
        """
        :returns: The incoming phone number
        :rtype: str
        """
        return self._properties['phone_number']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this resource
        :rtype: str
        """
        return self._properties['sid']

    @property
    def sms_application_sid(self):
        """
        :returns: Unique string that identifies the application
        :rtype: str
        """
        return self._properties['sms_application_sid']

    @property
    def sms_fallback_method(self):
        """
        :returns: HTTP method used with sms fallback url
        :rtype: str
        """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """
        :returns: URL Twilio will request if an error occurs in executing TwiML
        :rtype: str
        """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """
        :returns: HTTP method to use with sms url
        :rtype: str
        """
        return self._properties['sms_method']

    @property
    def sms_url(self):
        """
        :returns: URL Twilio will request when receiving an SMS
        :rtype: str
        """
        return self._properties['sms_url']

    @property
    def status_callback(self):
        """
        :returns: URL Twilio will use to pass status parameters
        :rtype: str
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: HTTP method twilio will use with status callback
        :rtype: str
        """
        return self._properties['status_callback_method']

    @property
    def uri(self):
        """
        :returns: The URI for this resource
        :rtype: str
        """
        return self._properties['uri']

    @property
    def voice_application_sid(self):
        """
        :returns: The unique sid of the application to handle this number
        :rtype: str
        """
        return self._properties['voice_application_sid']

    @property
    def voice_caller_id_lookup(self):
        """
        :returns: Look up the caller's caller-ID
        :rtype: bool
        """
        return self._properties['voice_caller_id_lookup']

    @property
    def voice_fallback_method(self):
        """
        :returns: HTTP method used with fallback_url
        :rtype: str
        """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """
        :returns: URL Twilio will request when an error occurs in TwiML
        :rtype: str
        """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """
        :returns: HTTP method used with the voice url
        :rtype: str
        """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """
        :returns: URL Twilio will request when receiving a call
        :rtype: str
        """
        return self._properties['voice_url']

    def update(self, account_sid=values.unset, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset):
        """
        Update the IncomingPhoneNumberInstance
        
        :param str account_sid: The new owner of the phone number
        :param str api_version: The Twilio REST API version to use
        :param str friendly_name: A human readable description of this resource
        :param str sms_application_sid: Unique string that identifies the application
        :param str sms_fallback_method: HTTP method used with sms fallback url
        :param str sms_fallback_url: URL Twilio will request if an error occurs in executing TwiML
        :param str sms_method: HTTP method to use with sms url
        :param str sms_url: URL Twilio will request when receiving an SMS
        :param str status_callback: URL Twilio will use to pass status parameters
        :param str status_callback_method: HTTP method twilio will use with status callback
        :param str voice_application_sid: The unique sid of the application to handle this number
        :param bool voice_caller_id_lookup: Look up the caller's caller-ID
        :param str voice_fallback_method: HTTP method used with fallback_url
        :param str voice_fallback_url: URL Twilio will request when an error occurs in TwiML
        :param str voice_method: HTTP method used with the voice url
        :param str voice_url: URL Twilio will request when receiving a call
        
        :returns: Updated IncomingPhoneNumberInstance
        :rtype: IncomingPhoneNumberInstance
        """
        return self._context.update(
            account_sid=account_sid,
            api_version=api_version,
            friendly_name=friendly_name,
            sms_application_sid=sms_application_sid,
            sms_fallback_method=sms_fallback_method,
            sms_fallback_url=sms_fallback_url,
            sms_method=sms_method,
            sms_url=sms_url,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            voice_application_sid=voice_application_sid,
            voice_caller_id_lookup=voice_caller_id_lookup,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
        )

    def fetch(self):
        """
        Fetch a IncomingPhoneNumberInstance
        
        :returns: Fetched IncomingPhoneNumberInstance
        :rtype: IncomingPhoneNumberInstance
        """
        return self._context.fetch()

    def delete(self):
        """
        Deletes the IncomingPhoneNumberInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._context.delete()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.IncomingPhoneNumberInstance {}>'.format(context)
