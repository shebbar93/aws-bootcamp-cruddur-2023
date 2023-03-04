from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder

class NotificationActivities:
  def run():
    # # Start a subsegment
    # subsegment = xray_recorder.begin_subsegment('notification_activities_subsegment')
    now = datetime.now(timezone.utc).astimezone()
    
    dict = {
      "now": now.isoformat()
    }
    # subsegment.put_metadata('key', dict, 'namespace')

    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'handle':  'Srinidhi hebbar',
      'message': 'Cloud is fun!',
      'created_at': (now - timedelta(days=2)).isoformat(),
      'expires_at': (now + timedelta(days=5)).isoformat(),
      'likes_count': 5,
      'replies_count': 1,
      'reposts_count': 0,
      'replies': [{
        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Worf',
        'message': 'This post has no honor!',
        'likes_count': 0,
        'replies_count': 0,
        'reposts_count': 0,
        'created_at': (now - timedelta(days=2)).isoformat()
      }],
    }]
    dict = {
      "now": now.isoformat(),
      "results": len(results)
    }
    # subsegment.put_metadata('key', dict, 'namespace')
    # xray_recorder.end_subsegment()
    return results