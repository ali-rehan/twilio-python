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


class StatisticsContext(InstanceContext):

    def __init__(self, version, workspace_sid, workflow_sid):
        """
        Initialize the StatisticsContext
        
        :param Version version
        :param workspace_sid: The workspace_sid
        :param workflow_sid: The workflow_sid
        
        :returns: StatisticsContext
        :rtype: StatisticsContext
        """
        super(StatisticsContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'workflow_sid': workflow_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/Statistics'.format(**self._kwargs)

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset):
        """
        Fetch a StatisticsInstance
        
        :param str minutes: The minutes
        :param datetime start_date: The start_date
        :param datetime end_date: The end_date
        
        :returns: Fetched StatisticsInstance
        :rtype: StatisticsInstance
        """
        params = values.of({
            'Minutes': minutes,
            'StartDate': start_date,
            'EndDate': end_date,
        })
        
        return self._version.fetch(
            StatisticsInstance,
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
        return '<Twilio.Taskrouter.V1.StatisticsContext {}>'.format(context)


class StatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, workflow_sid):
        """
        Initialize the StatisticsInstance
        
        :returns: StatisticsInstance
        :rtype: StatisticsInstance
        """
        super(StatisticsInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'cumulative': payload['cumulative'],
            'realtime': payload['realtime'],
            'workflow_sid': payload['workflow_sid'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'workflow_sid': workflow_sid,
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: StatisticsContext for this StatisticsInstance
        :rtype: StatisticsContext
        """
        if self._instance_context is None:
            self._instance_context = StatisticsContext(
                self._version,
                self._kwargs['workspace_sid'],
                self._kwargs['workflow_sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def cumulative(self):
        """
        :returns: The cumulative
        :rtype: str
        """
        return self._properties['cumulative']

    @property
    def realtime(self):
        """
        :returns: The realtime
        :rtype: str
        """
        return self._properties['realtime']

    @property
    def workflow_sid(self):
        """
        :returns: The workflow_sid
        :rtype: str
        """
        return self._properties['workflow_sid']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: str
        """
        return self._properties['workspace_sid']

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset):
        """
        Fetch a StatisticsInstance
        
        :param str minutes: The minutes
        :param datetime start_date: The start_date
        :param datetime end_date: The end_date
        
        :returns: Fetched StatisticsInstance
        :rtype: StatisticsInstance
        """
        return self._context.fetch(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.StatisticsInstance {}>'.format(context)
