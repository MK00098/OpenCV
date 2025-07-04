import opencv_gray

# 이미지 불러오기
img = opencv_gray.imread('test.jpg')

# 이미지가 정상적으로 불러와졌는지 확인
if img is None:
    print("이미지를 불러올 수 없습니다. 경로를 확인하세요.")
else:
    # 창에 이미지 띄우기
    opencv_gray.imshow('My Image', img)
    opencv_gray.waitKey(0)
    opencv_gray.destroyAllWindows()