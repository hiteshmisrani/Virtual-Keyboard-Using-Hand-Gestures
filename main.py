import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep

cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)  # Height

# Initialize HandDetector
detector = HandDetector(detectionCon=1, maxHands=1)

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
]

finalText = ""
click_active = False

# New color scheme
KEY_COLOR = (50, 50, 50)  # Dark gray keys
HOVER_COLOR = (100, 100, 100)  # Light gray hover
CLICK_COLOR = (0, 175, 175)  # Teal click
PANEL_COLOR = (30, 30, 30)  # Dark panel
TEXT_COLOR = (255, 255, 255)  # White text


class Button:
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

    def draw(self, img, color=KEY_COLOR):
        x, y = self.pos
        w, h = self.size
        cv2.rectangle(img, self.pos, (x + w, y + h), color, cv2.FILLED)
        cv2.putText(img, self.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, TEXT_COLOR, 4)
        return img


# Initialize buttons
buttonList = []
for i, row in enumerate(keys):
    for j, key in enumerate(row):
        buttonList.append(Button([100 * j + 50, 100 * (i + 1)], key))

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    # Draw all buttons with new color
    for button in buttonList:
        button.draw(img)

    # Check for finger position and clicks
    if lmList:  # If hand is detected
        current_click = False

        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            # Check if fingertip (landmark 8) is over a button
            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                button.draw(img, HOVER_COLOR) # Change color on hover
                # Check distance between index and middle finger tips
                l, _, _ = detector.findDistance(8, 12, img, draw=False)

                if l < 30:  # If fingers are close (pinch gesture)
                    button.draw(img, CLICK_COLOR)
                    current_click = True

                    if not click_active:
                        finalText += button.text
                        print(f"Pressed: {button.text}")
                        click_active = True
                        sleep(0.15)

        if not current_click:
            click_active = False

    # Draw output panel with new design
    text_box_y = 450
    panel_length = 800
    cv2.rectangle(img, (50, text_box_y), (50 + panel_length, text_box_y + 80),
                  PANEL_COLOR, cv2.FILLED)
    cv2.rectangle(img, (50, text_box_y), (50 + panel_length, text_box_y + 80),
                  CLICK_COLOR, 2)  # Border with click color
    cv2.putText(img, finalText, (60, text_box_y + 60),
                cv2.FONT_HERSHEY_PLAIN, 4, TEXT_COLOR, 4)

    cv2.imshow("Virtual Keyboard", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        finalText = ""
    elif key == 8:  # Backspace key
        finalText = finalText[:-1]

cap.release()
cv2.destroyAllWindows()