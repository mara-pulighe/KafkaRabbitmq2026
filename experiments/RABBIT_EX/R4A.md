# R4A – Non-Durable Queue

## Objective

Verify the behaviour of RabbitMQ when persistence mechanisms are disabled.

## Procedure

1. Create a non-durable queue.
2. Publish one or more messages.
3. Verify that the messages are stored in the queue.
4. Restart the RabbitMQ broker.
5. Inspect the queue after the restart.

## Related Concepts

- Volatile Storage
- Message Loss
- Broker Restart
- Reliability

## Reference Files

- `producer.py`
- `consumer.py` 