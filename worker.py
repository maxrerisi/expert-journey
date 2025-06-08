import requests
import os, time


def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # # Example usage
    # # app_url = "http://192.168.2.215:1234/data"  # Replace with your app's URL
    # app_url = "http://127.0.0.1:1234/data"

    # payload = {"value": str(socket.gethostname())}
    # response = send_post_request(app_url, payload)
    # print(f"Response: {response}")
    os.system("git clone https://github.com/maxrerisi/expert-journey")
    t = time.time()
    os.system("cd expert-journey")
    os.system(f"touch data/{t}")
    os.system(f"git add .")
    os.system('git commit -m "committing"')
    os.system("git push")
