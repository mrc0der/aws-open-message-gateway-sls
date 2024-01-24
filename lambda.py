import os
import requests
import json


def send_slack_message(message, channel):
    """
    Sends a Slack message to the default channel using the Slack API.
    """
    slack_webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not slack_webhook_url:
        raise ValueError("SLACK_WEBHOOK_URL environment variable not set.")

    payload = {
        "text": message,
        "channel": channel
    }
    response = requests.post(slack_webhook_url, json=payload)
    response.raise_for_status()


def send_discord_message(message):
    """
    Sends a Discord message to the default channel using the Discord API.
    """
    discord_webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not discord_webhook_url:
        raise ValueError("DISCORD_WEBHOOK_URL environment variable not set.")

    payload = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(discord_webhook_url, json=payload, headers=headers)
    response.raise_for_status()


def send_ms_teams_message(message):
    """
    Sends a Microsoft Teams message to the default channel using the Microsoft Teams API.
    """
    ms_teams_webhook_url = os.environ.get("MS_TEAMS_WEBHOOK_URL")
    if not ms_teams_webhook_url:
        raise ValueError("MS_TEAMS_WEBHOOK_URL environment variable not set.")

    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": "Notification Engine",
        "themeColor": "0072C6",
        "title": "Notification",
        "text": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(ms_teams_webhook_url, json=payload, headers=headers)
    response.raise_for_status()

def send_message(message, channel, destination="slack"):
    """
    Sends a message to a channel on the specified destination platform.
    """
    if destination == "slack":
        send_slack_message(message, channel)
    elif destination == "discord":
        send_discord_message(message)
    elif destination == "ms_teams":
        send_ms_teams_message(message)
    else:
        raise ValueError("Invalid destination. Valid values are 'slack', 'discord', or 'ms_teams'.")

def entrypoint(event, context):

    send_slack_message(event['message'],'Alerts', local_event['event_type'])

    return 200
