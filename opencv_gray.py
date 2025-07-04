import cv2

# 이미지 불러오기
img = cv2.imread('test.jpg')

# 이미지가 정상적으로 불러와졌는지 확인
if img is None:
    print("이미지를 불러올 수 없습니다. 경로 또는 파일명을 확인하세요.")
else:
    print("이미지 불러오기 성공!")

    # 흑백 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("흑백 이미지 크기:", gray.shape)

    # 이미지 띄우기
    cv2.imshow('Gray Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()