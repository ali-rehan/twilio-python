# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class WorkspaceTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-08-01T22:10:40Z",
                "date_updated": "2016-08-01T22:10:40Z",
                "default_activity_name": "Offline",
                "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "event_callback_url": "",
                "events_filter": null,
                "friendly_name": "new",
                "links": {
                    "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                    "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                    "real_time_statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RealTimeStatistics",
                    "cumulative_statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CumulativeStatistics",
                    "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                    "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                    "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                    "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows",
                    "task_channels": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels",
                    "events": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events"
                },
                "multi_task_enabled": false,
                "prioritize_queue_order": "FIFO",
                "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "timeout_activity_name": "Offline",
                "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-08-01T22:10:40Z",
                "date_updated": "2016-08-01T22:10:40Z",
                "default_activity_name": "Offline",
                "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "event_callback_url": "",
                "events_filter": null,
                "friendly_name": "new",
                "links": {
                    "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                    "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                    "real_time_statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RealTimeStatistics",
                    "cumulative_statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CumulativeStatistics",
                    "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                    "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                    "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                    "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows",
                    "task_channels": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels",
                    "events": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events"
                },
                "multi_task_enabled": false,
                "prioritize_queue_order": "FIFO",
                "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "timeout_activity_name": "Offline",
                "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=50&Page=0",
                    "key": "workspaces",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=50&Page=0"
                },
                "workspaces": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2016-08-01T22:10:40Z",
                        "date_updated": "2016-08-01T22:10:40Z",
                        "default_activity_name": "Offline",
                        "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "event_callback_url": "",
                        "events_filter": null,
                        "friendly_name": "new",
                        "links": {
                            "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                            "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                            "real_time_statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RealTimeStatistics",
                            "cumulative_statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CumulativeStatistics",
                            "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                            "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                            "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                            "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows",
                            "task_channels": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels",
                            "events": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events"
                        },
                        "multi_task_enabled": false,
                        "prioritize_queue_order": "FIFO",
                        "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "timeout_activity_name": "Offline",
                        "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=50&Page=0",
                    "key": "workspaces",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces?PageSize=50&Page=0"
                },
                "workspaces": []
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces.create(friendly_name="friendly_name")

        values = {
            'FriendlyName': "friendly_name",
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://taskrouter.twilio.com/v1/Workspaces',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-08-01T22:10:40Z",
                "date_updated": "2016-08-01T22:10:40Z",
                "default_activity_name": "Offline",
                "default_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "event_callback_url": "",
                "events_filter": null,
                "friendly_name": "new",
                "links": {
                    "activities": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Activities",
                    "statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics",
                    "real_time_statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RealTimeStatistics",
                    "cumulative_statistics": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CumulativeStatistics",
                    "task_queues": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues",
                    "tasks": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tasks",
                    "workers": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers",
                    "workflows": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workflows",
                    "task_channels": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels",
                    "events": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events"
                },
                "multi_task_enabled": false,
                "prioritize_queue_order": "FIFO",
                "sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "timeout_activity_name": "Offline",
                "timeout_activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces.create(friendly_name="friendly_name")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)
