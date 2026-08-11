import time
import random

def sliding_window(frames, window_size):
    with open("output.txt", "w") as f:
        f.write(f"Starting Sliding Window Protocol with window size: {window_size}\n")
        f.write(f"Data to send: {frames}\n\n")
        
        idx = 0
        while idx < len(frames):
            f.write(f"Sender: Sending window of frames from index {idx} to {min(idx+window_size-1, len(frames)-1)}\n")
            
            for i in range(idx, min(idx + window_size, len(frames))):
                f.write(f"--> Frame {i}: {frames[i]}\n")
            
            success = random.choice([True, True, False])
            if success:
                f.write(f"Receiver: ACK received for frames up to {min(idx + window_size - 1, len(frames) - 1)}\n\n")
                idx += window_size
            else:
                f.write(f"Receiver: NACK or Timeout occurred! Resending window starting at index {idx}\n\n")
            
            time.sleep(0.1)
        f.write("All frames transmitted successfully.\n")

with open("data_stream.txt", "r") as f:
    data = f.read()

sliding_window(list(data), 3)
