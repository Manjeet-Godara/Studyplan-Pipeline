import json
from azure.storage.queue import QueueClient

AZURE_STORAGE_CONNECTION_STRING = ""

QUEUE_NAME = "topic-queue"

topic_ids = [
"42CD583B-F225-4D90-9448-D51079F918D9",
]

queue = QueueClient.from_connection_string(
    AZURE_STORAGE_CONNECTION_STRING,
    QUEUE_NAME
)

for sid in topic_ids:
    message = {"topic_id": sid}
    queue.send_message(json.dumps(message))
    print(f"Queued: {sid}")

print(f"\n✅ {len(topic_ids)} subtopics pushed to {QUEUE_NAME}")