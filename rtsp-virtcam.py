import requests
import subprocess
import threading

# Define the RTSP URL of your camera
rtsp_url = "rtsp://your-camera-url"  # Replace with the actual RTSP URL of your camera

# Define the URL of the DerbyNet web application
derbynet_url = "http://localhost/derbynet/action.php"  # Replace with the actual URL

# Define FFmpeg command to capture RTSP feed and output to a pipe
ffmpeg_cmd = [
    "ffmpeg",
    "-rtsp_transport", "tcp",  # Use TCP for RTSP transport
    "-i", rtsp_url,
    "-vf", "format=yuv420p",  # Adjust video format if needed
    "-f", "mpegts", "-"  # Output to MPEG-TS format and send to stdout
]

# Function to capture RTSP feed and forward it to DerbyNet
def capture_and_forward():
    try:
        # Start FFmpeg process to capture RTSP feed
        ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**8)

        # Send the initial replay message to DerbyNet
        initial_message_params = {
            "action": "replay-message",
            "status": "-1",
            "finished-replay": "0"
        }
        response = requests.post(derbynet_url, data=initial_message_params)

        if response.status_code == 200:
            print("Connection established with DerbyNet")
        else:
            print("Failed to connect to DerbyNet. Status code:", response.status_code)

        # Continuously read and forward RTSP feed to DerbyNet
        while True:
            video_chunk = ffmpeg_process.stdout.read(4096)  # Adjust buffer size as needed
            if not video_chunk:
                break
            requests.post(derbynet_url, data=video_chunk, headers={'Content-Type': 'application/octet-stream'})

        # Close the FFmpeg process
        ffmpeg_process.terminate()
        ffmpeg_process.wait()
        
    except Exception as e:
        print("Error:", str(e))

# Create a thread to run the capture_and_forward function
capture_thread = threading.Thread(target=capture_and_forward)

# Start the thread to capture and forward the RTSP feed
capture_thread.start()

# You can continue to perform other tasks here if needed
# ...

# Wait for the capture thread to finish (you can remove this if running indefinitely)
capture_thread.join()
