import json
from azure.storage.queue import QueueClient

AZURE_STORAGE_CONNECTION_STRING = ""

QUEUE_NAME = "subtopic-queue"
subtopic_ids = [
    "7AF986BE-8F14-4500-BA48-1A879EB70B33",
    "D18E7CBC-1A51-454E-9722-90AA7D098009",
    "3ABFFE0D-6E14-4C02-BF4B-6194FDFDE270",
    "B50734FA-0FE3-4FDB-9D44-85C92F6641F9",
    "925D7283-59DE-487F-96D9-EF40C7833209",
    "07ED0862-6CBA-4028-8D6C-50D98648DE18",
    "68ADCF44-7C29-4535-9FE1-605E4026BF7F",
    "B3FDF0CF-93AC-44A1-9EE4-B4390DD7EF9B",
    "57ADD943-1963-4A56-8258-8BE53C41ADA7",
    "8A11F9A8-39D6-442B-A4B2-59AA1C74B3BA",
]
queue = QueueClient.from_connection_string(
    AZURE_STORAGE_CONNECTION_STRING,
    QUEUE_NAME
)

for sid in subtopic_ids:
    message = {"subtopic_id": sid}
    queue.send_message(json.dumps(message))
    print(f"Queued: {sid}")

print(f"\n✅ {len(subtopic_ids)} subtopics pushed to {QUEUE_NAME}")