from Adafruit_IO import Client, Feed, RequestError

# --- Configuration ---
# Replace with your actual Adafruit IO username and key
ADAFRUIT_IO_USERNAME = 'YOUR_USERNAME'
ADAFRUIT_IO_KEY = 'YOUR_AIO_KEY'

# Create an instance of the REST client
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# --- Usage Example ---
try:
    # Get a feed (create it if it doesn't exist)
    feed_name = 'test-feed'
    try:
        data_feed = aio.feeds(feed_name)
    except RequestError:
        feed = Feed(name=feed_name)
        data_feed = aio.create_feed(feed)

    # Send data to the feed
    print(f"Sending data to {feed_name}...")
    aio.send_data(data_feed.key, 42)
    print("Data sent successfully.")

    # Retrieve the latest data from the feed
    latest = aio.receive(data_feed.key)
    print(f"Latest value from {feed_name}: {latest.value}")

except Exception as e:
    print(f"An error occurred: {e}")
