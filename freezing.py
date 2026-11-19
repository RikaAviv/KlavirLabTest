# Mouse freezing demo
# A tiny practice script for the Klavir Lab GitHub workshop.
# The speeds below are made up for practice, not real data.

# ---- Settings you can change ----
MOUSE_NAME = "Mouse 1"
SPEED_THRESHOLD = 1.0  # cm/s: slower than this counts as "frozen"

# Speed of the mouse (cm/s), one number for each second of video
speeds = [5.2, 4.8, 0.3, 0.2, 0.1, 6.1, 7.0, 0.6, 0.2,
          5.5, 4.9, 0.1, 0.3, 0.2, 0.2, 6.3, 5.8, 0.8, 4.4, 5.1]

# ---- Analysis ----
print(f"Freezing analysis for {MOUSE_NAME}")
print(f"Threshold: below {SPEED_THRESHOLD} cm/s counts as frozen\n")
print(f"Lilian the queen")

frozen_seconds = 0
for second, speed in enumerate(speeds):
    if speed < SPEED_THRESHOLD:
        state = "frozen"
        frozen_seconds += 1
    else:
        state = "moving"
    bar = "#" * round(speed)
    print(f"{second:2d}s  {speed:4.1f} cm/s  {bar:<8} {state}")

percent = 100 * frozen_seconds / len(speeds)
print(f"\n{MOUSE_NAME} was frozen for {frozen_seconds} of {len(speeds)} seconds ({percent:.0f}%).")
