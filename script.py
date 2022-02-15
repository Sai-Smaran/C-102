import cv2
import time
import random
import dropbox

start_time = time.time()

def take_picture():
	num = random.randint(0, 100)
	camObj = cv2.VideoCapture(0,cv2.CAP_DSHOW)

	result = True

	while (result):
		_, frame = camObj.read()
		img_name = "Picture"+str(num)+".jpg"

		cv2.imwrite(img_name, frame)
		start_time = time.time()
		result = False

	print("Picture taken")
	camObj.release()
	cv2.destroyAllWindows()
	return img_name


def upload_image(img_name):
	access_token = "gn0zun32O1cAAAAAAAAAAXXHAutKNkiZWRK9U46-lPINstuioPFsdXQeWX9BP9ob"
	file = img_name
	file_from = file
	file_to = "/Image"+(file)

	dbx = dropbox.Dropbox(access_token)

	with open(file_from, "rb") as f:
		dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
		print("File uploaded")


def main():
	while (True):
		
		# Yeah, you need to wait a day for this thing to take a photo and upload it
		if ((time.time()-start_time) >= 86400):
			name = take_picture()
			upload_image(name)


if __name__ == "__main__":
	main()